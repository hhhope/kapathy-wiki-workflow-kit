#!/usr/bin/env bash
set -euo pipefail

SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
  SOURCE_DIR="$(cd "$(dirname "$SOURCE")" && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  case "$SOURCE" in
    /*) ;;
    *) SOURCE="$SOURCE_DIR/$SOURCE" ;;
  esac
done
SCRIPT_DIR="$(cd "$(dirname "$SOURCE")" && pwd)"
PAYLOAD_DIR="$SCRIPT_DIR/payload"
AGENTS_SNIPPET="$SCRIPT_DIR/AGENTS_SNIPPET.md"
TARGET_DIR=""
FORCE=0
VERIFY=0
MODE="repo"
UPDATE_AGENTS=0
PRINT_AGENTS_SNIPPET=0

usage() {
  printf '%s\n' "Usage: bash install.sh [target-repo] [--mode repo|codex-repo] [--update-agents] [--print-agents-snippet] [--force] [--verify]"
  printf '%s\n' ""
  printf '%s\n' "target-repo defaults to current directory."
  printf '%s\n' "--mode repo installs repo-local Codex skills plus scripts, taxonomy, tests, and OpenSpec docs."
  printf '%s\n' "--mode codex-repo is an explicit alias for repo-local Codex installation."
  printf '%s\n' "--update-agents appends or refreshes the req-agent routing block in AGENTS.md."
  printf '%s\n' "--print-agents-snippet prints the AGENTS.md routing snippet and exits."
  printf '%s\n' "--force overwrites different existing files."
  printf '%s\n' "--verify runs installed tests and OpenSpec validation when available."
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --force)
      FORCE=1
      ;;
    --verify)
      VERIFY=1
      ;;
    --update-agents)
      UPDATE_AGENTS=1
      ;;
    --print-agents-snippet)
      PRINT_AGENTS_SNIPPET=1
      ;;
    --mode)
      if [ "$#" -lt 2 ]; then
        printf '%s\n' "--mode requires a value: repo or codex-repo" >&2
        exit 2
      fi
      MODE="$2"
      shift
      ;;
    --mode=*)
      MODE="${1#--mode=}"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      if [ -n "$TARGET_DIR" ]; then
        printf 'Unexpected argument: %s\n' "$1" >&2
        usage >&2
        exit 2
      fi
      TARGET_DIR="$1"
      ;;
  esac
  shift
done

if [ "$PRINT_AGENTS_SNIPPET" -eq 1 ]; then
  if [ ! -f "$AGENTS_SNIPPET" ]; then
    printf 'AGENTS snippet is missing: %s\n' "$AGENTS_SNIPPET" >&2
    exit 2
  fi
  cat "$AGENTS_SNIPPET"
  exit 0
fi

case "$MODE" in
  repo|codex-repo)
    ;;
  *)
    printf 'Unsupported mode: %s\n' "$MODE" >&2
    usage >&2
    exit 2
    ;;
esac

if [ -z "$TARGET_DIR" ]; then
  TARGET_DIR="."
fi

if [ ! -d "$TARGET_DIR" ]; then
  printf 'Target repository does not exist: %s\n' "$TARGET_DIR" >&2
  exit 2
fi

TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

if [ ! -d "$PAYLOAD_DIR" ]; then
  printf 'Payload directory is missing: %s\n' "$PAYLOAD_DIR" >&2
  exit 2
fi

installed=0
skipped=0
overwritten=0
agents_status="not_requested"

copy_one() {
  local source="$1"
  local rel="${source#$PAYLOAD_DIR/}"
  local target="$TARGET_DIR/$rel"
  local mode="0644"

  case "$rel" in
    scripts/*.py)
      mode="0755"
      ;;
  esac

  if [ -e "$target" ]; then
    if cmp -s "$source" "$target"; then
      skipped=$((skipped + 1))
      return 0
    fi
    if [ "$FORCE" -ne 1 ]; then
      printf 'Refusing to overwrite different file: %s\n' "$target" >&2
      printf 'Re-run with --force to replace it intentionally.\n' >&2
      exit 3
    fi
    overwritten=$((overwritten + 1))
  else
    installed=$((installed + 1))
  fi

  install -D -m "$mode" "$source" "$target"
}

while IFS= read -r -d '' file; do
  copy_one "$file"
done < <(find "$PAYLOAD_DIR" -type f -print0 | sort -z)

update_agents_file() {
  local agents_file="$TARGET_DIR/AGENTS.md"
  local start_marker="<!-- req-agent-routing:start -->"
  local end_marker="<!-- req-agent-routing:end -->"
  local tmp_file

  if [ ! -f "$AGENTS_SNIPPET" ]; then
    printf 'AGENTS snippet is missing: %s\n' "$AGENTS_SNIPPET" >&2
    exit 2
  fi

  tmp_file="$(mktemp)"
  if [ -f "$agents_file" ]; then
    if grep -q "$start_marker" "$agents_file"; then
      if python3 - "$agents_file" "$AGENTS_SNIPPET" <<'PY'
from pathlib import Path
import sys

agents = Path(sys.argv[1]).read_text(encoding="utf-8")
snippet = Path(sys.argv[2]).read_text(encoding="utf-8")
start = "<!-- req-agent-routing:start -->"
end = "<!-- req-agent-routing:end -->"
if start not in agents or end not in agents:
    raise SystemExit(1)
block = start + agents.split(start, 1)[1].split(end, 1)[0] + end
raise SystemExit(0 if block.strip() == snippet.strip() else 1)
PY
      then
        agents_status="unchanged"
        rm -f "$tmp_file"
        return 0
      fi
      python3 - "$agents_file" "$AGENTS_SNIPPET" "$tmp_file" <<'PY'
from pathlib import Path
import sys

agents = Path(sys.argv[1])
snippet = Path(sys.argv[2]).read_text(encoding="utf-8").rstrip() + "\n"
target = Path(sys.argv[3])
text = agents.read_text(encoding="utf-8")
start = "<!-- req-agent-routing:start -->"
end = "<!-- req-agent-routing:end -->"
before, rest = text.split(start, 1)
_, after = rest.split(end, 1)
target.write_text(before + snippet + after, encoding="utf-8")
PY
      if cmp -s "$tmp_file" "$agents_file"; then
        agents_status="unchanged"
      else
        install -m 0644 "$tmp_file" "$agents_file"
        agents_status="updated"
      fi
    else
      {
        cat "$agents_file"
        printf '\n\n'
        cat "$AGENTS_SNIPPET"
      } > "$tmp_file"
      install -m 0644 "$tmp_file" "$agents_file"
      agents_status="appended"
    fi
  else
    install -D -m 0644 "$AGENTS_SNIPPET" "$agents_file"
    agents_status="created"
  fi
  rm -f "$tmp_file"
}

if [ "$UPDATE_AGENTS" -eq 1 ]; then
  update_agents_file
fi

printf 'req-agent installed into %s\n' "$TARGET_DIR"
printf 'mode=%s\n' "$MODE"
printf 'agents=%s\n' "$agents_status"
printf 'installed=%s overwritten=%s skipped=%s\n' "$installed" "$overwritten" "$skipped"

if ! (cd "$TARGET_DIR" && python3 -c 'import yaml' >/dev/null 2>&1); then
  printf 'Warning: python3 cannot import yaml. Install PyYAML before running requirements checks.\n' >&2
fi

if [ "$VERIFY" -eq 1 ]; then
  (cd "$TARGET_DIR" && python3 -m unittest \
    tests.test_req_agent_skills \
    tests.test_requirements_analysis_agent \
    tests.test_requirements_case \
    tests.test_requirements_checker \
    tests.test_requirements_checker_gate \
    tests.test_requirements_ddd_analysis_agent \
    tests.test_requirements_ddd_readiness_gate \
    tests.test_requirements_ddd_taxonomy \
    tests.test_requirements_domain_coverage_gate \
    tests.test_requirements_openspec_draft)
  if command -v openspec >/dev/null 2>&1; then
    (cd "$TARGET_DIR" && openspec validate req-agent --strict)
  else
    printf 'openspec CLI not found; skipped OpenSpec validation.\n' >&2
  fi
fi
