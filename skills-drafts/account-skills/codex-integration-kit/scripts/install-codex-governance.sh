#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
TARGET_ROOT="${HOME}/.codex"
DRY_RUN=0
NO_PROMPT=0
SELECTED_COMPONENTS=()
AVAILABLE_COMPONENTS=(
  "global-base"
  "global-personal-example"
  "repo-template"
  "rules"
  "agents"
  "skills"
)

usage() {
  cat <<'EOF'
Install global AGENTS templates, repo AGENTS templates, and governance files into a Codex home directory.

Usage:
  ./scripts/install-codex-governance.sh
  ./scripts/install-codex-governance.sh --target ~/.codex
  ./scripts/install-codex-governance.sh --target ~/.codex --dry-run
  ./scripts/install-codex-governance.sh --install global-base,repo-template,rules,agents,skills --no-prompt

Options:
  --target <path>     Target Codex home. Defaults to ~/.codex.
  --install <csv>     Comma-separated components to install.
                      Components: global-base, global-personal-example,
                      repo-template, rules, agents, skills
  --no-prompt         Disable interactive selection. Requires --install.
  --dry-run           Print planned backup/copy operations without writing files.
  -h, --help          Show help.
EOF
}

component_target_path() {
  local component="$1"
  case "${component}" in
    global-base)
      printf "%s/AGENTS.md" "${TARGET_ROOT}"
      ;;
    global-personal-example)
      printf "%s/AGENTS.personal.example.md" "${TARGET_ROOT}"
      ;;
    repo-template)
      printf "%s/AGENTS.repo-template.md" "${TARGET_ROOT}"
      ;;
    *)
      printf "%s/%s" "${TARGET_ROOT}" "${component}"
      ;;
  esac
}

component_source_path() {
  local component="$1"
  case "${component}" in
    global-base)
      printf "%s/templates/global/AGENTS.base.md" "${SOURCE_ROOT}"
      ;;
    global-personal-example)
      printf "%s/templates/global/AGENTS.personal.example.md" "${SOURCE_ROOT}"
      ;;
    repo-template)
      printf "%s/templates/repo/AGENTS.repo-template.md" "${SOURCE_ROOT}"
      ;;
    *)
      printf "%s/%s" "${SOURCE_ROOT}" "${component}"
      ;;
  esac
}

is_valid_component() {
  local candidate="$1"
  local item
  for item in "${AVAILABLE_COMPONENTS[@]}"; do
    if [[ "${item}" == "${candidate}" ]]; then
      return 0
    fi
  done
  return 1
}

add_selected_component() {
  local candidate="$1"
  local item
  for item in "${SELECTED_COMPONENTS[@]}"; do
    if [[ "${item}" == "${candidate}" ]]; then
      return 0
    fi
  done
  SELECTED_COMPONENTS+=("${candidate}")
}

parse_install_csv() {
  local csv="$1"
  local part

  IFS=',' read -r -a parts <<< "${csv}"
  for part in "${parts[@]}"; do
    part="${part#"${part%%[![:space:]]*}"}"
    part="${part%"${part##*[![:space:]]}"}"
    if [[ -z "${part}" ]]; then
      continue
    fi
    if ! is_valid_component "${part}"; then
      echo "[install-codex-governance] unknown component: ${part}" >&2
      usage >&2
      exit 2
    fi
    add_selected_component "${part}"
  done
}

prompt_yes_no() {
  local prompt="$1"
  local default_answer="$2"
  local reply=""

  while true; do
    if [[ "${default_answer}" == "y" ]]; then
      read -r -p "${prompt} [Y/n] " reply || exit 1
      reply="${reply:-Y}"
    else
      read -r -p "${prompt} [y/N] " reply || exit 1
      reply="${reply:-N}"
    fi

    case "${reply}" in
      Y|y)
        return 0
        ;;
      N|n)
        return 1
        ;;
      *)
        echo "[install-codex-governance] please answer y or n" >&2
        ;;
    esac
  done
}

collect_interactive_selection() {
  if prompt_yes_no "Install global baseline as AGENTS.md?" "y"; then
    add_selected_component "global-base"
  fi
  if prompt_yes_no "Install personal overlay example?" "n"; then
    add_selected_component "global-personal-example"
  fi
  if prompt_yes_no "Install repository AGENTS template?" "y"; then
    add_selected_component "repo-template"
  fi
  if prompt_yes_no "Install rules/?" "y"; then
    add_selected_component "rules"
  fi
  if prompt_yes_no "Install agents/?" "y"; then
    add_selected_component "agents"
  fi
  if prompt_yes_no "Install skills/?" "y"; then
    add_selected_component "skills"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      if [[ $# -lt 2 ]]; then
        echo "[install-codex-governance] missing value for --target" >&2
        exit 2
      fi
      TARGET_ROOT="$2"
      shift 2
      ;;
    --install)
      if [[ $# -lt 2 ]]; then
        echo "[install-codex-governance] missing value for --install" >&2
        exit 2
      fi
      parse_install_csv "$2"
      shift 2
      ;;
    --no-prompt)
      NO_PROMPT=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[install-codex-governance] unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ "${NO_PROMPT}" -eq 1 && "${#SELECTED_COMPONENTS[@]}" -eq 0 ]]; then
  echo "[install-codex-governance] --no-prompt requires --install" >&2
  exit 2
fi

if [[ "${#SELECTED_COMPONENTS[@]}" -eq 0 ]]; then
  if [[ "${NO_PROMPT}" -eq 1 ]]; then
    echo "[install-codex-governance] no components selected" >&2
    exit 2
  fi
  collect_interactive_selection
fi

if [[ "${#SELECTED_COMPONENTS[@]}" -eq 0 ]]; then
  echo "[install-codex-governance] no components selected; nothing to install"
  exit 0
fi

if [[ ! -d "${TARGET_ROOT}" ]]; then
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    echo "[install-codex-governance] target directory would be created: ${TARGET_ROOT}"
  else
    mkdir -p "${TARGET_ROOT}"
  fi
fi

if [[ -d "${TARGET_ROOT}" ]]; then
  TARGET_ROOT="$(cd "${TARGET_ROOT}" && pwd)"
else
  TARGET_PARENT="$(cd "$(dirname "${TARGET_ROOT}")" && pwd)"
  TARGET_ROOT="${TARGET_PARENT}/$(basename "${TARGET_ROOT}")"
fi
BACKUP_ROOT="${TARGET_ROOT}/.codex-governance-backup/$(date +%Y%m%d-%H%M%S)"

if [[ "${SOURCE_ROOT}" == "${TARGET_ROOT}" && "${DRY_RUN}" -eq 0 ]]; then
  cat >&2 <<EOF
[install-codex-governance] source and target are the same directory:
  ${SOURCE_ROOT}

This script installs the governance bundle into another Codex project.
Run from the target project with:
  bash ${SOURCE_ROOT}/scripts/install-codex-governance.sh

Or pass an explicit target:
  bash ${SOURCE_ROOT}/scripts/install-codex-governance.sh --target ~/.codex
EOF
  exit 2
fi

require_source_item() {
  local item="$1"
  if [[ ! -e "${SOURCE_ROOT}/${item}" ]]; then
    echo "[install-codex-governance] missing source item: ${SOURCE_ROOT}/${item}" >&2
    exit 1
  fi
}

plan_copy_path() {
  local source_path="$1"
  local target_path="$2"

  if [[ -e "${target_path}" ]]; then
    echo "[install-codex-governance] backup ${target_path} -> ${BACKUP_ROOT}/${target_path#${TARGET_ROOT}/}"
  fi
  echo "[install-codex-governance] copy ${source_path} -> ${target_path}"
}

copy_path() {
  local source_path="$1"
  local target_path="$2"
  local rel_path="${target_path#${TARGET_ROOT}/}"

  if [[ -e "${target_path}" ]]; then
    mkdir -p "$(dirname "${BACKUP_ROOT}/${rel_path}")"
    cp -a "${target_path}" "${BACKUP_ROOT}/${rel_path}"
    rm -rf "${target_path}"
  fi

  mkdir -p "$(dirname "${target_path}")"
  cp -a "${source_path}" "${target_path}"
}

plan_install_dir() {
  local dir_name="$1"
  while IFS= read -r -d '' source_path; do
    local rel_path="${source_path#${SOURCE_ROOT}/}"
    local target_path="${TARGET_ROOT}/${rel_path}"
    plan_copy_path "${source_path}" "${target_path}"
  done < <(find "${SOURCE_ROOT}/${dir_name}" -type f -print0 | sort -z)
}

copy_install_dir() {
  local dir_name="$1"
  while IFS= read -r -d '' source_path; do
    local rel_path="${source_path#${SOURCE_ROOT}/}"
    local target_path="${TARGET_ROOT}/${rel_path}"
    copy_path "${source_path}" "${target_path}"
  done < <(find "${SOURCE_ROOT}/${dir_name}" -type f -print0 | sort -z)
}

echo "[install-codex-governance] source=${SOURCE_ROOT}"
echo "[install-codex-governance] target=${TARGET_ROOT}"
echo "[install-codex-governance] components=${SELECTED_COMPONENTS[*]}"
if [[ "${DRY_RUN}" -eq 1 ]]; then
  echo "[install-codex-governance] mode=dry-run"
else
  echo "[install-codex-governance] backup-root=${BACKUP_ROOT}"
fi

for item in "${SELECTED_COMPONENTS[@]}"; do
  source_path="$(component_source_path "${item}")"
  target_path="$(component_target_path "${item}")"
  if [[ "${item}" == "rules" || "${item}" == "agents" || "${item}" == "skills" ]]; then
    require_source_item "${item}"
    plan_install_dir "${item}"
  else
    if [[ ! -e "${source_path}" ]]; then
      echo "[install-codex-governance] missing source item: ${source_path}" >&2
      exit 1
    fi
    plan_copy_path "${source_path}" "${target_path}"
  fi
done

if [[ "${DRY_RUN}" -eq 1 ]]; then
  echo "[install-codex-governance] dry-run complete"
  exit 0
fi

for item in "${SELECTED_COMPONENTS[@]}"; do
  source_path="$(component_source_path "${item}")"
  target_path="$(component_target_path "${item}")"
  if [[ "${item}" == "rules" || "${item}" == "agents" || "${item}" == "skills" ]]; then
    copy_install_dir "${item}"
  else
    copy_path "${source_path}" "${target_path}"
  fi
done

echo "[install-codex-governance] install complete"
echo "[install-codex-governance] next steps:"
echo "  1) review installed AGENTS templates in ${TARGET_ROOT}"
echo "  2) if you installed the personal example, merge only the parts you want into ${TARGET_ROOT}/AGENTS.md"
echo "  3) inspect ${TARGET_ROOT}/rules ${TARGET_ROOT}/agents ${TARGET_ROOT}/skills"
