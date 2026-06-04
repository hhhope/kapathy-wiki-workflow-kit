# Evaluation

## Pressure Scenarios

1. User provides market-level requirement material with enough story and
   acceptance coverage but no current-state/system/rule materials.
2. User asks whether the case can enter detailed design after
   `requirements_ready`.
3. User asks whether missing design materials should apply to all future
   `req-agent` cases, not just one case.

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

Pending implementation.

## Prior-Art / Common-Rule Dedupe

- `AGENTS.md` already owns repo health checks, OpenSpec gates, git discipline,
  and behavior-asset evaluation. This change does not restate those as generic
  rules.
- `requirements/config/requirements-taxonomy.yaml` owns domain/readiness
  vocabulary. This change does not add new taxonomy IDs.
- Existing `req-agent` OpenSpec change owns the normal controller and worker
  split. This change extends the readiness boundary only.
- Current case-specific hard gates in
  `wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md`
  are used as motivating evidence, not as the reusable rule source.

## Residual Risks

- Existing case files will not be backfilled unless regenerated or explicitly
  updated.
- The checker can verify gate metadata and approval/material status, but it
  cannot validate the business correctness of provided product materials.

