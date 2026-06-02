# Tasks

- [x] 1. Add OpenSpec requirements for strict role instance and evidence anchor gates.
- [x] 2. Add failing checker tests for strict role/evidence behavior, including missing role evidence.
- [x] 3. Add failing draft-generation tests for strict readiness before draft creation.
- [x] 4. Implement checker strict mode, compatibility mode, and rich blockers.
- [x] 5. Update requirements case rendering for role instances and role refs.
- [x] 6. Update requirements analysis generation for role instances and candidate roles.
- [x] 7. Require strict readiness before OpenSpec draft generation.
- [x] 8. Migrate embedded-account-phase1 as the golden sample.
- [x] 9. Add golden sample regression tests.
- [x] 10. Run unit tests and OpenSpec validation.

  Evidence:
  - `python3 -m unittest tests.test_requirements_checker_gate tests.test_requirements_analysis_agent tests.test_req_agent_skills`: `Ran 34 tests in 1.471s`; `OK`.
  - `openspec validate strengthen-requirements-role-evidence-gate --strict`: `Change 'strengthen-requirements-role-evidence-gate' is valid`; PostHog telemetry flush reported DNS `EAI_AGAIN edge.openspec.dev` after validation.
  - `python3 -m scripts.check_requirements_case wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`: `status: requirements_ready`; `hard_gate_passed: true`; `strict: true`; `blockers: []`.
  - Compatibility probe `python3 -m unittest tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_legacy_case_shape_remains_readable_in_compatibility_mode`: `Ran 1 test in 0.033s`; `OK`.
- [x] 11. Update skill text and behavior evidence only if user-visible routing changes. N/A: no skill text or user-visible routing files changed.
