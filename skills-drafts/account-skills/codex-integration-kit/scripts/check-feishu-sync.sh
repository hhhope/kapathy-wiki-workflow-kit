#!/usr/bin/env bash
set -euo pipefail

REPO="."
MODE="staged"
AGAINST_REF=""
FEISHU_SOURCE="codex-integration-kit/docs/feishu-codex-governance-share.md"

usage() {
  cat <<'EOF'
Check whether governance-surface changes in this repository also include the Feishu-facing source markdown.

Usage:
  ./codex-integration-kit/scripts/check-feishu-sync.sh --staged
  ./codex-integration-kit/scripts/check-feishu-sync.sh --against origin/main
  ./codex-integration-kit/scripts/check-feishu-sync.sh --repo /path/to/repo --staged

Options:
  --repo <path>     Repository root. Defaults to current directory.
  --staged          Check staged changes only. This is the default.
  --against <ref>   Check changes in <ref>...HEAD.
  -h, --help        Show help.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      REPO="$2"
      shift 2
      ;;
    --staged)
      MODE="staged"
      AGAINST_REF=""
      shift
      ;;
    --against)
      MODE="against"
      AGAINST_REF="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[check-feishu-sync] unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ ! -d "${REPO}/.git" ]]; then
  echo "[check-feishu-sync] repository not found: ${REPO}" >&2
  exit 2
fi

repo_rel_paths() {
  if [[ "${MODE}" == "staged" ]]; then
    git -C "${REPO}" diff --cached --name-only --diff-filter=ACMR
  else
    git -C "${REPO}" rev-parse --verify "${AGAINST_REF}" >/dev/null
    git -C "${REPO}" diff --name-only --diff-filter=ACMR "${AGAINST_REF}...HEAD"
  fi
}

is_governance_surface() {
  local path="$1"
  case "${path}" in
    codex-integration-kit/*|skills/*|PROJECT.md|AGENTS.md|.codex/hooks.json|openspec/changes/add-team-lore-bilingual-schema/*)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

mapfile -t changed_files < <(repo_rel_paths)

governance_files=()
feishu_changed=0

for path in "${changed_files[@]}"; do
  [[ -n "${path}" ]] || continue
  if [[ "${path}" == "${FEISHU_SOURCE}" ]]; then
    feishu_changed=1
  fi
  if is_governance_surface "${path}" && [[ "${path}" != "${FEISHU_SOURCE}" ]]; then
    governance_files+=("${path}")
  fi
done

if [[ "${#governance_files[@]}" -eq 0 ]]; then
  echo "Feishu sync gate passed: no governance-surface change detected."
  exit 0
fi

if [[ "${feishu_changed}" -eq 1 ]]; then
  echo "Feishu sync gate passed: governance changes include ${FEISHU_SOURCE}."
  exit 0
fi

echo "Feishu source update required: governance-surface changes detected without ${FEISHU_SOURCE}." >&2
echo "Changed governance files:" >&2
printf '  - %s\n' "${governance_files[@]}" >&2
echo "Add ${FEISHU_SOURCE} in the same work cycle, then rerun the gate." >&2
exit 1
