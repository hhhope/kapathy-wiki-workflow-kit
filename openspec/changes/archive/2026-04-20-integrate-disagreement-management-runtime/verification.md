# Verification

## Structure

- `openspec validate integrate-disagreement-management-runtime`
- Result: `Change 'integrate-disagreement-management-runtime' is valid`

## GREEN

- `sed -n '1,260p' wiki/ops/disagreement-management-method.md`
  - Result confirmed the method now includes runtime routing to `wiki/ops retro`
- `sed -n '1,220p' wiki/ops/sample-disagreement-retro.md`
  - Result confirmed the repo now has a minimal retro shape for disagreement routing
- `sed -n '1,260p' AGENTS.md`
  - Result confirmed archive review now explicitly checks disagreement preservation / promotion
- `sed -n '1,220p' wiki/ops/index.md`
  - Result confirmed the new retro sample is discoverable from the ops index

## Before / After Boundary

- Before:
  - disagreement method existed, but runtime retro routing was implicit
  - archive review did not explicitly ask about disagreement preservation or ADR promotion
- After:
  - disagreement-to-retro routing is explicit
  - archive review has an explicit disagreement check

## Limits

- This verifies repo-default runtime guidance only.
- It does not prove auto-trigger correctness or automated enforcement.
