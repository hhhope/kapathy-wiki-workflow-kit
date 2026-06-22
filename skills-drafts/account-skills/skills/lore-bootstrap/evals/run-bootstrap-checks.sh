#!/usr/bin/env bash
set -euo pipefail

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
script="$repo_root/skills/lore-bootstrap/scripts/bootstrap_lore_wiki.sh"

pass() {
  echo "PASS: $1"
}

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

assert_file() {
  [ -f "$1" ] || fail "missing file: $1"
}

assert_grep() {
  grep -q "$2" "$1" || fail "missing pattern '$2' in $1"
}

run_fresh_install() {
  local tmp_root
  tmp_root=$(mktemp -d /tmp/lore-bootstrap-fresh-XXXXXX)
  mkdir -p "$tmp_root/project" "$tmp_root/home/.codex" "$tmp_root/d"
  cat > "$tmp_root/project/PROJECT.md" <<'EOF'
---
project: account-skills
---
EOF

  LORE_BOOTSTRAP_DEFAULT_REPO="$tmp_root/d/team-lore" bash "$script" \
    --project-dir "$tmp_root/project" \
    --codex-home "$tmp_root/home/.codex" \
    --member yan >/tmp/lore-bootstrap-fresh.out

  assert_file "$tmp_root/d/team-lore/.git/HEAD"
  assert_file "$tmp_root/d/team-lore/wiki/index.md"
  assert_file "$tmp_root/d/team-lore/wiki/projects/account-skills/overview.md"
  assert_file "$tmp_root/d/team-lore/wiki/projects/account-skills/domains/entrypoint.md"
  assert_grep "$tmp_root/home/.codex/AGENTS.md" "team-lore: $tmp_root/d/team-lore/wiki"
  assert_grep /tmp/lore-bootstrap-fresh.out "INSTALL_TARGET_SOURCE: env-default"
  assert_grep /tmp/lore-bootstrap-fresh.out "WIKI_REPO: $tmp_root/d/team-lore"
  pass "fresh install"
}

run_existing_repo_bootstrap() {
  local tmp_root
  tmp_root=$(mktemp -d /tmp/lore-bootstrap-existing-XXXXXX)
  mkdir -p "$tmp_root/home/team-lore" "$tmp_root/home/.codex" "$tmp_root/project"
  git -c init.defaultBranch=main init "$tmp_root/home/team-lore" >/dev/null
  cat > "$tmp_root/project/PROJECT.md" <<'EOF'
---
project: payments-core
---
EOF

  bash "$script" \
    --project-dir "$tmp_root/project" \
    --wiki-repo "$tmp_root/home/team-lore" \
    --codex-home "$tmp_root/home/.codex" >/tmp/lore-bootstrap-existing.out

  assert_file "$tmp_root/home/team-lore/.git/HEAD"
  assert_file "$tmp_root/home/team-lore/wiki/projects/payments-core/overview.md"
  assert_file "$tmp_root/home/team-lore/templates/project-overview.md"
  pass "existing repo bootstrap"
}

run_legacy_migration() {
  local tmp_root
  tmp_root=$(mktemp -d /tmp/lore-bootstrap-migration-XXXXXX)
  mkdir -p "$tmp_root/project/logs" "$tmp_root/home/.codex"
  cat > "$tmp_root/project/PROJECT.md" <<'EOF'
---
project: settlements
---
EOF
  cat > "$tmp_root/project/LORE.md" <<'EOF'
[domain:: settlement]
- retries were missed during callback reconciliation
EOF
  cat > "$tmp_root/project/logs/sample.md" <<'EOF'
reviewed: false
EOF

  bash "$script" \
    --project-dir "$tmp_root/project" \
    --wiki-repo "$tmp_root/home/team-lore" \
    --codex-home "$tmp_root/home/.codex" \
    --legacy-lore "$tmp_root/project/LORE.md" >/tmp/lore-bootstrap-migration.out

  assert_file "$tmp_root/home/team-lore/wiki/projects/settlements/legacy/LORE-legacy.md"
  assert_file "$tmp_root/home/team-lore/wiki/projects/settlements/migration-notes.md"
  assert_file "$tmp_root/project/logs/sample.md"
  pass "legacy migration"
}

[ -f "$script" ] || fail "bootstrap script missing"

run_fresh_install
run_existing_repo_bootstrap
run_legacy_migration
