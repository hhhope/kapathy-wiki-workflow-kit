# Tasks

- [x] 1. Add OpenSpec spec deltas for reviewable requirements case output.
- [ ] 2. Add RED rendering tests showing the old compressed template lacks
      human-review JSON, taxonomy meanings, gate closure, and eval-plan output.
- [ ] 3. Implement reviewable rendering in `scripts/requirements_case.py`
      without changing machine case data.
- [ ] 4. Add a payment-transaction story fixture that demonstrates
      `review_judgment`, `taxonomy_refs`, `acceptance_functions`,
      `gate_closure`, and `eval_plan`.
- [ ] 5. Run focused requirements case tests.
- [ ] 6. Run the `agent-subscription-payment` requirements checker.
- [ ] 7. Run OpenSpec validation for this change.
- [ ] 8. Record RED/GREEN results, limitations, and proof boundary in
      `evaluation.md`.

## Expected Verification

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_case`
- `PYTHONPATH=. python3 scripts/check_requirements_case.py wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md --repo-root . --format markdown`
- `openspec validate improve-requirements-review-template --strict`
