# Tasks

- [x] 1. Add requirements domain model OpenSpec spec.
- [x] 2. Update requirements taxonomy with payment skeleton domains and aliases.
- [x] 3. Record compatibility mapping for `account`, `clearing`, and `settlement`.
- [x] 4. Verify requirements checker accepts the updated taxonomy.
- [x] 5. Validate OpenSpec change.

## Verification

- `python3 -c "import yaml; data=yaml.safe_load(open('requirements/config/requirements-taxonomy.yaml')); print(len(data['domains'])); print([d['id'] for d in data['domains']])"` -> loaded 11 domains including the payment skeleton.
- `python3 scripts/check_requirements_case.py --help` -> failed because direct script execution cannot import `scripts`.
- `PYTHONPATH=. python3 scripts/check_requirements_case.py --help` -> passed.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate tests.test_requirements_analysis_agent` -> 31 tests passed.
- Minimal strict requirements case using `billing_revenue` -> `requirements_ready`, `hard_gate_passed=True`, no blockers.
- `openspec validate define-requirements-domain-standards-and-payment-skeleton --strict` -> valid.

## Proof Boundary

This change proves the OpenSpec standard and first payment-domain taxonomy
skeleton are repo-visible and accepted by the current requirements checker.
It does not implement or prove the future `req-domain-analysis` skill behavior.
