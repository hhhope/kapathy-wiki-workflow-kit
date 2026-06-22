#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TMP_ROOT=$(mktemp -d /tmp/lore-e2e-XXXXXX)
CHANGE_DIR="$TMP_ROOT/change"
LOG_DIR="$TMP_ROOT/logs"

cleanup() {
  rm -rf "$TMP_ROOT"
}
trap cleanup EXIT

cp -R "$ROOT/fixtures/openspec/change-payment-retry" "$CHANGE_DIR"
cp -R "$ROOT/fixtures/logs" "$LOG_DIR"

printf '%s\n' "STEP | apply gate with full change docs"
APPLY_OK=$("$ROOT/openspec-fixture/apply.sh" "$CHANGE_DIR")
printf '%s\n' "$APPLY_OK"

printf '%s\n' "STEP | retrieval sample"
RETRIEVAL=$(python3 - <<'PY'
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('rpc', 'skills/lore/evals/run-pressure-checks.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
pages = mod.load_pages()
top = mod.score_query("How should repeated payment callbacks avoid duplicate ledger writes?", pages)
print("TOP | " + ", ".join(top))
if "pitfalls/idempotency-keys.md" not in top:
    raise SystemExit(1)
PY
)
printf '%s\n' "$RETRIEVAL"

printf '%s\n' "STEP | weekly review absorbs logs"
python3 - <<PY
from pathlib import Path

log_dir = Path("$LOG_DIR")
mapping = {
    "20260411-090000-yan-payment-retry-gap-a1b2.md": "projects/payments-core/domains/payment-retry.md",
    "20260411-091500-yan-shared-boundary-gap-c3d4.md": "principles/boundary-first.md",
}
for path in sorted(log_dir.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    text = text.replace("reviewed: false", "reviewed: true")
    dest = mapping[path.name]
    text = text.replace("absorbed-to:", f"absorbed-to: {dest}")
    text = text.replace("review-action:", "review-action: absorb")
    path.write_text(text, encoding="utf-8")
    print(f"ABSORB | {path.name} -> {dest}")
PY

printf '%s\n' "STEP | archive gate after review"
ARCHIVE_OK=$("$ROOT/openspec-fixture/archive.sh" "$LOG_DIR")
printf '%s\n' "$ARCHIVE_OK"

printf '%s\n' "SUMMARY | e2e fixture passed"
