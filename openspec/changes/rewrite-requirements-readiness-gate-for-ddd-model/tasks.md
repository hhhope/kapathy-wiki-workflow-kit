# Tasks

- [x] 1. Add OpenSpec requirements for DDD readiness gate.
- [x] 2. Add failing checker tests for taxonomy v2 domain-model readiness.
- [x] 3. Implement taxonomy v2 lookup and domain-model gate.
- [x] 4. Preserve legacy compatibility checks for old case shapes.
- [x] 5. Run focused requirements checker tests.
- [x] 6. Run DDD taxonomy validator and OpenSpec validation.
- [x] 7. Record verification results and proof boundary.

## Verification

- RED baseline:
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_readiness_gate` -> failed with three expected failures before implementation: complete DDD case blocked, missing `domain_model_gate`, and unknown role obligation not recognized.
- GREEN:
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_readiness_gate` -> passed, `Ran 3 tests`.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate` -> passed, `Ran 19 tests`.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy tests.test_requirements_checker tests.test_requirements_ddd_readiness_gate tests.test_requirements_checker_gate tests.test_requirements_case` -> passed, `Ran 36 tests`.
  - `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml` -> valid.
  - `openspec validate rewrite-requirements-readiness-gate-for-ddd-model --strict` -> valid.
    The command exited 0; the trailing PostHog DNS flush error is telemetry-only.

## Review Fix Evidence

- User review question: old `retail_customer`, `system_actor`, `product`, and
  similar legacy roles are no longer formal taxonomy v2 roles.
- RED:
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_readiness_gate.RequirementsDddReadinessGateTests.test_strict_ddd_case_rejects_legacy_actor_roles` -> failed because strict v2 accepted `system_actor`.
- GREEN:
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_readiness_gate.RequirementsDddReadinessGateTests.test_strict_ddd_case_rejects_legacy_actor_roles` -> passed.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_readiness_gate` -> passed, `Ran 4 tests`.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate` -> passed, `Ran 19 tests`.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy tests.test_requirements_checker tests.test_requirements_ddd_readiness_gate tests.test_requirements_checker_gate tests.test_requirements_case` -> passed, `Ran 37 tests`.
  - `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml` -> valid.
  - `openspec validate rewrite-requirements-readiness-gate-for-ddd-model --strict` -> valid.
    The command exited 0; the trailing PostHog DNS flush error is telemetry-only.

## Proof Boundary

This change proves the requirements checker can evaluate taxonomy v2 DDD
`domain_model` readiness and still keep explicit legacy compatibility checks.
In strict taxonomy v2 mode, role validation uses `role_archetypes`; legacy actor
roles are available only through compatibility mode.
It does not update `requirements_analysis_agent`, `req-agent`,
`req-domain-analysis`, or `req-scope` to generate the new DDD case shape.

Fresh boundary evidence:

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_analysis_agent` still fails with 7 old-model failures: legacy domain alias resolution remains `candidate_pending`, and draft creation is blocked by `requirements_not_ready`.
- That failure surface belongs to `upgrade-req-agent-domain-analysis-for-ddd-contexts`.
