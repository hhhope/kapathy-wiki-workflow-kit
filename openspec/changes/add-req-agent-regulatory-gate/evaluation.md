# Evaluation

## Behavior Change

`req-agent` now treats regulatory obligations as requirement-readiness facts
when a case is in `risk_compliance` or explicitly mentions regulation,
compliance, identity, authorization, consent, personal information, SMS links,
tokens, or similar regulated-action signals.

Missing or unresolved `soft_evidence.regulatory_obligations` now blocks
`requirements_ready`. This is intentionally stricter than
`detailed_design_gate`, which can block design while leaving a requirement
skeleton reviewable.

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| positive trigger: `risk_compliance` requirement has no `soft_evidence.regulatory_obligations` | Checker blocks `requirements_ready` with `regulatory_obligations_missing` | `tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_risk_compliance_case_missing_regulatory_obligations_blocks_readiness` |
| positive trigger: explicit legal/SMS/identity/compliance material routes through worker guidance | `req-agent` and worker skills name `regulatory_gate` and regulatory obligation routing | `tests.test_req_agent_skills.ReqAgentSkillSurfaceTest.test_req_agent_surfaces_regulatory_gate`; `test_workers_route_regulatory_obligations_through_lifecycle` |
| negative should-not-trigger: non-regulatory billing/account case | `regulatory_gate.mode=not_triggered` and readiness is not blocked by this gate | `tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_regulatory_gate_not_triggered_for_non_regulatory_case` |
| parent gate preserve: detailed-design hard gates still exist separately | Regulatory gate blocks requirement readiness only when triggered; `detailed_design_gate` remains the API/DDL/state-machine blocker | `tests.test_requirements_checker_gate` focused and full run |

## RED Baseline

Command:

```bash
PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_regulatory_gate_not_triggered_for_non_regulatory_case tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_risk_compliance_case_missing_regulatory_obligations_blocks_readiness tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_confirmed_regulatory_obligation_passes_gate
```

Result before implementation:

- `test_regulatory_gate_not_triggered_for_non_regulatory_case`: failed with
  `KeyError: 'regulatory_gate'`.
- `test_risk_compliance_case_missing_regulatory_obligations_blocks_readiness`:
  failed because status was `requirements_ready`, not `blocked`.
- `test_confirmed_regulatory_obligation_passes_gate`: failed with
  `KeyError: 'regulatory_gate'`.

Skill RED command:

```bash
PYTHONPATH=. python3 -m unittest tests.test_req_agent_skills.ReqAgentSkillSurfaceTest.test_req_agent_surfaces_regulatory_gate tests.test_req_agent_skills.ReqAgentSkillSurfaceTest.test_workers_route_regulatory_obligations_through_lifecycle
```

Result before skill edits:

- 11 marker failures across `req-agent`, `req-domain-analysis`, `req-scope`,
  `req-acceptance`, and `req-human-review`; the skills did not name
  `regulatory_gate` or regulatory obligation routing.

## GREEN Result

Focused checker command:

```bash
PYTHONPATH=. python3 -m unittest tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_regulatory_gate_not_triggered_for_non_regulatory_case tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_risk_compliance_case_missing_regulatory_obligations_blocks_readiness tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_confirmed_regulatory_obligation_passes_gate
```

Result: passed, `Ran 3 tests`.

Focused skill command:

```bash
PYTHONPATH=. python3 -m unittest tests.test_req_agent_skills
```

Result: passed, `Ran 6 tests`.

## Replay Evidence

### Replay: Non-regulatory requirement

- input or situation shape: DDD-shaped billing/account requirement with no `risk_compliance`
  and no explicit regulation/identity/consent/SMS-link signals.
- trigger condition: none.
- expected route: `regulatory_gate.mode=not_triggered`.
- repo-visible artifact a future agent should read: `scripts/check_requirements_case.py`, `tests/test_requirements_checker_gate.py`, and `.codex/skills/req-agent/SKILL.md`.
- expected output or non-output: requirements readiness is not blocked by the regulatory
  gate.
- promotion or non-promotion boundary: does not promote generic security best
  practices into every requirement; no obligation is required without trigger.
- proof boundary: proves the gate is not global for every payment case.

### Replay: Legal SMS / compliance requirement

- input or situation shape: legal representative SMS verification, compliance evidence,
  H5 link, token, identity binding, or personal information.
- trigger condition: `risk_compliance` or explicit regulatory terms.
- expected route: `req-domain-analysis` surfaces regulatory obligations,
  `req-scope` assigns owners, `req-acceptance` maps obligations to observable
  acceptance, and `req-human-review` verifies synchronization.
- repo-visible artifact a future agent should read: `scripts/check_requirements_case.py`,
  `.codex/skills/req-agent/SKILL.md`, worker skills, and this OpenSpec change.
- expected output or non-output: missing obligations block `requirements_ready`.
- promotion or non-promotion boundary: regulatory obligations stay case-local
  evidence objects; the change does not add a legal-rule library or new
  taxonomy domain.
- proof boundary: local checker and skill-surface tests prove the behavior;
  they do not prove future legal sufficiency of any particular obligation.

## Prior-Art / Common-Rule Dedupe

- Scanned: `AGENTS.md`, `PROJECT.md`, `openspec/specs`,
  `openspec/changes/enforce-req-agent-design-hard-gates`,
  `openspec/changes/req-agent`, `.codex/skills/req-agent`,
  `.codex/skills/req-domain-analysis`, `.codex/skills/req-scope`,
  `.codex/skills/req-acceptance`, `.codex/skills/req-human-review`,
  `requirements/config/requirements-taxonomy.yaml`, and
  `~/.codex/rules/common/security.md`.
- Owns: `regulatory_gate` readiness behavior, case-local
  `soft_evidence.regulatory_obligations`, and worker guidance for routing
  regulatory obligations through domain, scope, acceptance, and human review.
- References: existing `enforce-req-agent-design-hard-gates` owns detailed-design hard
  gates and intentionally keeps `requirements_ready` separate from design
  readiness. This change does not alter that distinction.
- References: existing `req-agent` owns the normal controller route and worker split. This
  change adds one gate to that route instead of creating a new user-facing
  skill.
- References: `requirements/config/requirements-taxonomy.yaml` owns domain vocabulary. This
  change does not add new taxonomy domains or owner roles.
- References: common security rules own generic API/auth/input/logging constraints. This
  change only ensures regulatory obligations are captured as requirement facts
  before handoff.
- Rejects: hard-coding law articles, adding a new legal taxonomy domain,
  changing all payment cases into regulatory cases, or treating OWASP/NIST/PBC
  examples as automatically sufficient legal proof.

## Residual Risks

- The trigger term scan is explicit and conservative; unusual regulatory
  wording may still need human review.
- The gate validates obligation structure, ownership, evidence anchors, and
  acceptance mappings. It does not validate legal correctness.
- Historical risk/compliance cases may become blocked if rechecked and missing
  obligations; this is intentional but may require case-by-case migration.
