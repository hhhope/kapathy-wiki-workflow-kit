# Tasks

- [x] 1. Add OpenSpec spec coverage for the reusable req-agent regulatory gate.
- [x] 2. Add RED tests proving missing regulatory obligations block
      `requirements_ready` when triggered by `risk_compliance` or explicit
      regulatory signals.
- [x] 3. Add GREEN tests proving confirmed/waived obligations pass and
      non-regulatory cases remain unaffected.
- [x] 4. Implement `regulatory_gate` in the requirements checker.
- [x] 5. Update requirements case package defaults only if needed for new
      cases; avoid batch migration.
- [x] 6. Update `.codex/skills/req-agent/SKILL.md` and relevant worker skill
      guidance.
- [x] 7. Add behavior-asset evaluation evidence with RED/GREEN and prior-art
      dedupe.
- [x] 8. Run focused tests, behavior-asset checks, OpenSpec validation, and
      commit scoped artifacts.

## Verification

- RED checker tests:
  `PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_regulatory_gate_not_triggered_for_non_regulatory_case tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_risk_compliance_case_missing_regulatory_obligations_blocks_readiness tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_confirmed_regulatory_obligation_passes_gate`
  failed before implementation with missing `regulatory_gate` and
  `requirements_ready` instead of `blocked`.
- RED skill tests:
  `PYTHONPATH=. python3 -m unittest tests.test_req_agent_skills.ReqAgentSkillSurfaceTest.test_req_agent_surfaces_regulatory_gate tests.test_req_agent_skills.ReqAgentSkillSurfaceTest.test_workers_route_regulatory_obligations_through_lifecycle`
  failed before skill edits with 11 missing marker failures.
- Focused GREEN:
  `PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate tests.test_req_agent_skills`
  passed, `Ran 29 tests`.
- Wider requirements GREEN:
  `PYTHONPATH=. python3 -m unittest tests.test_requirements_case tests.test_requirements_checker tests.test_requirements_checker_gate tests.test_requirements_ddd_readiness_gate tests.test_requirements_domain_coverage_gate tests.test_requirements_openspec_draft tests.test_req_agent_skills`
  passed, `Ran 51 tests`.
- Taxonomy validation:
  `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml`
  reported valid.
- OpenSpec validation:
  `openspec validate add-req-agent-regulatory-gate --strict` passed. PostHog
  telemetry flush reported DNS `EAI_AGAIN edge.openspec.dev` after validation,
  but the command exited 0.
- Behavior asset checker:
  `python3 scripts/check_behavior_assets.py` still exits non-zero due existing
  `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md` evaluation
  debt. This change's `evaluation.md` no longer appears in the checker errors.
- Live Baofoo case replay:
  `PYTHONPATH=. python3 scripts/check_requirements_case.py wiki/ops/requirements-cases/2026-06-09-015054-baofu-multi-channel-legal-sms-verification.md --format markdown`
  now reports `Status: blocked`, `Regulatory gate passed: False`, and
  blocker `regulatory_obligations_missing`.
