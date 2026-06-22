#!/bin/sh
set -eu

ROOT="skills/lore/evals/fixtures"
TMP="/tmp/lore-live-integration.$$"
OPS="skills/lore/evals/openspec-fixture"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/full/change" "$TMP/missing/change" "$TMP/archive/logs"

cp "$ROOT/openspec/change-payment-retry/proposal.md" "$TMP/full/change/proposal.md"
cp "$ROOT/openspec/change-payment-retry/design.md" "$TMP/full/change/design.md"
cp "$ROOT/openspec/change-payment-retry/tasks.md" "$TMP/full/change/tasks.md"

cp "$ROOT/openspec/change-payment-retry/design.md" "$TMP/missing/change/design.md"
cp "$ROOT/openspec/change-payment-retry/tasks.md" "$TMP/missing/change/tasks.md"

cp "$ROOT/logs/20260411-090000-yan-payment-retry-gap-a1b2.md" "$TMP/archive/logs/"
cp "$ROOT/logs/20260411-091500-yan-shared-boundary-gap-c3d4.md" "$TMP/archive/logs/"

pass() {
  printf 'PASS | %s\n' "$1"
}

fail() {
  printf 'FAIL | %s\n' "$1"
  exit 1
}

# Apply gate: full change present
"$OPS/apply.sh" "$TMP/full/change" >/tmp/lore-apply-ok.out 2>/tmp/lore-apply-ok.err \
  || fail "apply gate should allow execution when proposal/design/tasks are present"
grep -q "ALLOW | apply gate satisfied" /tmp/lore-apply-ok.out \
  || fail "apply gate allow case should emit ALLOW"
pass "apply gate allows execution when proposal/design/tasks are present"

# Apply gate: missing proposal blocks
if "$OPS/apply.sh" "$TMP/missing/change" >/tmp/lore-apply-miss.out 2>/tmp/lore-apply-miss.err; then
  fail "apply gate should block execution when proposal.md is missing"
fi
grep -q "BLOCK | missing proposal.md" /tmp/lore-apply-miss.out \
  || fail "missing proposal scenario should emit BLOCK for proposal.md"
pass "apply gate blocks execution when proposal.md is missing"

# Archive gate: unreviewed logs block
if "$OPS/archive.sh" "$TMP/archive/logs" >/tmp/lore-archive-block.out 2>/tmp/lore-archive-block.err; then
  fail "archive gate should block when unreviewed logs exist"
fi
grep -q "BLOCK |" /tmp/lore-archive-block.out \
  || fail "archive gate block scenario should emit BLOCK"
pass "archive gate blocks when unreviewed logs exist"

# Archive gate: reviewed logs allow archive
sed -i 's/reviewed: false/reviewed: true/' "$TMP/archive/logs/"*.md
sed -i 's/review-action:/review-action: absorb/' "$TMP/archive/logs/"*.md
sed -i 's/absorbed-to:/absorbed-to: fixture-target/' "$TMP/archive/logs/"*.md
remaining=$(grep -rl "reviewed: false" "$TMP/archive/logs" | wc -l | tr -d ' ')
[ "$remaining" -eq 0 ] || fail "archive gate should clear after review markers are updated"
"$OPS/archive.sh" "$TMP/archive/logs" >/tmp/lore-archive-ok.out 2>/tmp/lore-archive-ok.err \
  || fail "archive gate should allow progression after logs are reviewed"
grep -q "ALLOW | archive gate satisfied" /tmp/lore-archive-ok.out \
  || fail "archive gate allow scenario should emit ALLOW"
pass "archive gate allows progression after logs are marked reviewed with destinations"

printf 'SUMMARY | all live integration checks passed\n'
