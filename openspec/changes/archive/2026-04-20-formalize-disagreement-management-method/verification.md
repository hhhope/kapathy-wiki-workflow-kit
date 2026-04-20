# Verification

## Structure

- `openspec validate formalize-disagreement-management-method`
- Result: `Change 'formalize-disagreement-management-method' is valid`

## GREEN

- `sed -n '1,220p' wiki/ops/disagreement-management-method.md`
  - Result confirmed the published method includes:
    - minimum raw material package
    - anti-compression states
    - positive naming threshold
    - downstream boundary
- `sed -n '1,220p' AGENTS.md`
  - Result confirmed the repo now has a `Disagreement Management Default` section
- `sed -n '1,220p' wiki/adr/0012-disagreement-management-before-conclusion-promotion.md`
  - Result confirmed the method is also recorded as a stable ADR-level decision
- `sed -n '1,220p' wiki/adr/index.md`
  - Result confirmed ADR-0012 is indexed

## Behavior Evidence

- Pressure scenario evidence is recorded in `evaluation.md` and the change design.
- The method was checked against two different disagreement types:
  - governance-shaped disagreement
  - method self-compression disagreement
- RED/GREEN evidence is based on the same disagreement inputs before and after the method was formalized.

## Limits

- This verification proves repo-visible publication and recorded behavior evidence.
- It does not prove multi-session rollout behavior or automatic triggering correctness.
