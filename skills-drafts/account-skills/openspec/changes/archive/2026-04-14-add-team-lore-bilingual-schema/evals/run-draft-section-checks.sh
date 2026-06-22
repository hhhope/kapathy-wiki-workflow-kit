#!/usr/bin/env bash
set -euo pipefail

root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

check_sections() {
  local file="$1"
  shift
  for section in "$@"; do
    grep -q "^## ${section}$" "$file" || fail "$file missing section: ${section}"
  done
}

check_sections \
  "$root/drafts/wiki/index.md" \
  "Scope" "Aliases" "Applies When" "Not For" "Top Facts" "Watchpoints" "Load Next" "Notes"

check_sections \
  "$root/drafts/projects/account-skills/overview.md" \
  "Scope" "Aliases" "Applies When" "Not For" "Top Facts" "Watchpoints" "Load Next" "Notes"

check_sections \
  "$root/drafts/projects/account-team-efficiency/overview.md" \
  "Scope" "Aliases" "Applies When" "Not For" "Top Facts" "Watchpoints" "Load Next" "Notes"

check_sections \
  "$root/drafts/pitfalls/admin-scope-ui-backend-drift.md" \
  "Scope" "Aliases" "Top Checks" "Not For" "Watchpoints" "Load Next" "Notes"

check_sections \
  "$root/drafts/principles/explicit-team-selection-for-platform-admin.md" \
  "Aliases" "Applies When" "Not For" "Top Facts" "Watchpoints" "Load Next" "Notes"

echo "PASS: all draft pages expose the required retrieval-first sections"
