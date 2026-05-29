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
TARGET_DIR=""
FORCE=0
VERIFY=0
MODE="repo"

usage() {
  printf '%s\n' "Usage: bash install.sh [target-repo] [--mode repo|codex-repo] [--force] [--verify]"
  printf '%s\n' ""
  printf '%s\n' "target-repo defaults to current directory."
  printf '%s\n' "--mode repo installs repo-local Codex skills plus scripts, taxonomy, tests, and OpenSpec docs."
  printf '%s\n' "--mode codex-repo is an explicit alias for repo-local Codex installation."
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

printf 'req-agent installed into %s\n' "$TARGET_DIR"
printf 'mode=%s\n' "$MODE"
printf 'installed=%s overwritten=%s skipped=%s\n' "$installed" "$overwritten" "$skipped"

if ! (cd "$TARGET_DIR" && python3 -c 'import yaml' >/dev/null 2>&1); then
  printf 'Warning: python3 cannot import yaml. Install PyYAML before running requirements checks.\n' >&2
fi

if [ "$VERIFY" -eq 1 ]; then
  (cd "$TARGET_DIR" && python3 -m unittest tests.test_req_agent_skills tests.test_requirements_analysis_agent)
  if command -v openspec >/dev/null 2>&1; then
    (cd "$TARGET_DIR" && openspec validate req-agent --strict)
  else
    printf 'openspec CLI not found; skipped OpenSpec validation.\n' >&2
  fi
fi
