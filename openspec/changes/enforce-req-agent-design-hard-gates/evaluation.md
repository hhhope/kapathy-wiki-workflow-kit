# Evaluation

## Pressure Scenarios

### Positive Scenario

Input or situation shape: user provides market-level requirement material with
enough story and acceptance coverage, then asks whether the case can enter
detailed design.

Trigger condition: `requirements_ready` is true but the product-owned
current-state material package, business rule position table, or system
boundary contract table is missing.

Expected route: ordinary requirements work still routes through `req-agent`;
the case remains reviewable for requirements/OpenSpec handoff, while detailed
design is blocked by `detailed_design_gate`.

Repo-visible artifact: `.codex/skills/req-agent/SKILL.md`,
`scripts/check_requirements_case.py`, `scripts/requirements_case.py`, and this
OpenSpec change.

Expected output: response may say `requirements_ready`, but must also report
that API, DDL/schema, state-machine, rule-model, integration-contract, and
engineering-breakdown design are blocked until product provides or waives the
three required inputs.

Promotion or non-promotion boundary: this behavior is promoted into
`req-agent` and checker behavior; it does not promote any case-specific Agent
subscription rule value into the requirements taxonomy.

Proof boundary: tests prove the gate is surfaced and enforced structurally;
they do not prove product materials are business-correct.

### Negative / Should-Not-Trigger Scenario

Input or situation shape: user asks only to intake or review the requirements
skeleton, and does not ask for detailed design, API, DDL/schema, state-machine,
or implementation breakdown.

Trigger condition: requirements gates pass while detailed-design inputs are
missing.

Expected route: `req-agent` may continue requirements review or OpenSpec
handoff, but should-not-trigger detailed design or implementation design.

Repo-visible artifact: the requirements case and checker report carry
`detailed_design_gate`, while the OpenSpec draft remains a review artifact.

Expected output: allowed action is requirement review/handoff; blocked action is
detailed design.

Promotion or non-promotion boundary: the missing product materials do not
demote the requirement skeleton from `requirements_ready`.

Proof boundary: this prevents AGI inference of current state, rule parameters,
accounting treatment, and system boundaries; it does not validate final
detailed-design content.

## RED Baseline

Before this change, `.codex/skills/req-agent/SKILL.md` only required
`domain_model_gate`, `domain_coverage_gate`, and `requirement_delivery_gate`
before handoff. `scripts/check_requirements_case.py` returned no
`detailed_design_gate`, and `build_requirements_case_package` did not add
default `detailed_design_hard_gates`.

Expected failure before implementation:

- a checker test expecting `detailed_design_gate` fails because the key is
  absent
- a case package test expecting default design gates fails because the package
  contains no such gates
- a skill surface test expecting the reusable hard-gate wording fails because
  the skill does not mention it

## GREEN Result

Implemented with focused tests:

- `tests/test_requirements_case.py` checks new packages include the three
  default detailed-design hard gates.
- `tests/test_requirements_checker_gate.py` checks missing product materials
  keep `requirements_ready` while blocking `detailed_design_gate`, and provided
  materials pass the detailed-design gate.
- `tests/test_req_agent_skills.py` checks `req-agent` names
  `detailed_design_gate`, current-state material package, business rule
  position table, and system boundary contract table.

Verification run:

- `python3 -m unittest tests.test_requirements_case tests.test_requirements_checker_gate tests.test_requirements_checker tests.test_requirements_ddd_readiness_gate tests.test_requirements_domain_coverage_gate tests.test_req_agent_skills`
  passed, 44 tests.
- `openspec validate enforce-req-agent-design-hard-gates --strict` passed.
  OpenSpec emitted PostHog telemetry network flush errors after validation, but
  the command exited 0 and printed `Change 'enforce-req-agent-design-hard-gates'
  is valid`.
- Targeted behavior-asset evaluation check for this change passed with no
  entries.
- Full `python3 scripts/check_behavior_assets.py` still fails on unrelated
  pre-existing `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
  evaluation gaps; it no longer reports this change.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/changes/req-agent`
- `requirements/config/requirements-taxonomy.yaml`
- `.codex/skills/req-agent/SKILL.md`
- `scripts/check_requirements_case.py`
- `scripts/requirements_case.py`
- `wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md`

Owns:

- Reusable `req-agent` distinction between requirement readiness and
  detailed-design readiness.
- Structural checker field `detailed_design_gate`.
- Default product-owned hard gates for new requirements case packages.

References:

- `AGENTS.md` owns repo health checks, OpenSpec gates, git discipline, and
  behavior-asset evaluation.
- `requirements/config/requirements-taxonomy.yaml` owns DDD taxonomy and
  requirement readiness vocabulary.
- `openspec/changes/req-agent` owns the controller/worker split.

Rejects:

- Does not add new taxonomy IDs.
- Does not make missing detailed-design inputs fail `requirements_ready`.
- Does not promote Agent subscription-specific fee or settlement values into
  the generic workflow rule.
- Does not replace OpenSpec handoff or implementation gates.

## Residual Risks

- Existing case files will not be backfilled unless regenerated or explicitly
  updated.
- The checker can verify gate metadata and approval/material status, but it
  cannot validate the business correctness of provided product materials.
