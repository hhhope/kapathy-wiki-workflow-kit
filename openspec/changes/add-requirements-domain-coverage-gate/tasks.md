# Tasks

- [ ] 1. Add OpenSpec spec deltas for domain coverage readiness.
- [ ] 2. Add RED checker tests showing a case with valid `domain_model`,
      roles, stories, and acceptance mappings is blocked when required
      subdomains/contexts have no coverage evidence.
- [ ] 3. Add RED checker tests for missing story `domain_refs`,
      `context_refs`, and `aggregate_refs`.
- [ ] 4. Add RED checker tests for missing acceptance coverage types:
      state change, handoff, failure path, and evidence.
- [ ] 5. Implement `domain_coverage_gate` in
      `scripts/check_requirements_case.py`.
- [ ] 6. Extend `scripts/requirements_case.py` rendering and machine package
      support for Domain Coverage.
- [ ] 7. Update `scripts/requirements_openspec_draft.py` so handoff drafts
      include coverage evidence and refuse coverage-blocked cases.
- [ ] 8. Update repo-local requirements worker skills only as needed:
      `req-agent`, `req-domain-analysis`, `req-scope`, `req-stories`,
      `req-acceptance`, and `req-handoff`.
- [ ] 9. Add or update golden sample evidence using
      `wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md`.
- [ ] 10. Run focused requirements tests and taxonomy validation.
- [ ] 11. Run OpenSpec validation for this change.
- [ ] 12. Record verification results and proof boundary in `tasks.md` or
      `evaluation.md`.

## Expected Verification

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate`
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_readiness_gate`
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_analysis_agent`
- `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml`
- `openspec validate add-requirements-domain-coverage-gate --strict`
