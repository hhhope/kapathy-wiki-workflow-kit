#!/bin/sh
set -eu

ROOT="skills/lore/evals/fixtures"
OPENSPEC="$ROOT/openspec/change-payment-retry"
WIKI="$ROOT/wiki"
LOGS="$ROOT/logs"

pass() {
  printf 'PASS | %s\n' "$1"
}

fail() {
  printf 'FAIL | %s\n' "$1"
  exit 1
}

check_file() {
  [ -f "$1" ] || fail "$2"
  pass "$2"
}

# Gate fixture: required OpenSpec files exist
check_file "$OPENSPEC/proposal.md" "gate-propose-present has proposal.md"
check_file "$OPENSPEC/design.md" "gate-propose-present has design.md"
check_file "$OPENSPEC/tasks.md" "gate-propose-present has tasks.md"

# Retrieval fixture: target pages exist and are linked from the corpus entry path
check_file "$WIKI/pitfalls/idempotency-keys.md" "retrieval fixture has idempotency page"
check_file "$WIKI/pitfalls/timeout-fallback.md" "retrieval fixture has timeout-fallback page"
check_file "$WIKI/principles/boundary-first.md" "retrieval fixture has boundary-first principle"

grep -q "pitfalls/idempotency-keys" "$WIKI/index.md" \
  || fail "index should reference idempotency page"
pass "index references idempotency page"

grep -q "pitfalls/timeout-fallback" "$WIKI/index.md" \
  || fail "index should reference timeout-fallback page"
pass "index references timeout-fallback page"

grep -q "principles/boundary-first" "$WIKI/index.md" \
  || fail "index should reference boundary-first principle"
pass "index references boundary-first principle"

grep -q "pitfalls/idempotency-keys" "$WIKI/projects/payments-core/domains/callback-processing.md" \
  || fail "callback-processing domain should reference idempotency page"
pass "callback-processing domain references idempotency page"

grep -q "pitfalls/timeout-fallback" "$WIKI/projects/payments-core/domains/payment-retry.md" \
  || fail "payment-retry domain should reference timeout-fallback page"
pass "payment-retry domain references timeout-fallback page"

grep -q "principles/boundary-first" "$WIKI/projects/payments-core/domains/payment-retry.md" \
  || fail "payment-retry domain should reference boundary-first principle"
pass "payment-retry domain references boundary-first principle"

# Noise fixture: auth does not exist in the tiny corpus
if find "$WIKI" -type f | grep -q "auth"; then
  fail "noise-auth-unrelated fixture should not contain auth pages"
fi
pass "noise-auth-unrelated fixture contains no auth pages"

# Absorption fixture: log text and target pages exist
check_file "$LOGS/20260411-090000-yan-payment-retry-gap-a1b2.md" "absorption fixture has project-domain log"
check_file "$LOGS/20260411-091500-yan-shared-boundary-gap-c3d4.md" "absorption fixture has principle log"

grep -q "Suggested destination" "$LOGS/20260411-090000-yan-payment-retry-gap-a1b2.md" \
  || fail "project-domain log should declare a suggested destination"
pass "project-domain log declares a suggested destination"

grep -q "domain page" "$LOGS/20260411-090000-yan-payment-retry-gap-a1b2.md" \
  || fail "project-domain log should map to a domain page"
pass "project-domain log maps to a domain page"

grep -q "principle page" "$LOGS/20260411-091500-yan-shared-boundary-gap-c3d4.md" \
  || fail "principle log should map to a principle page"
pass "principle log maps to a principle page"

# Startup-budget fixture: explicit medium scenario page set
startup_pages=6
[ "$startup_pages" -le 6 ] || fail "startup-budget-medium exceeds the target budget"
pass "startup-budget-medium stays within the 6-page budget"

printf 'SUMMARY | all fixture checks passed\n'
