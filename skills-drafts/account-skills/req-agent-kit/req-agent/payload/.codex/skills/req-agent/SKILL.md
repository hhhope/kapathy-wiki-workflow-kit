---
name: req-agent
description: Use when the user asks to intake, clarify, check, gate, or hand off requirements work before development.
---

Use this skill as the single normal Codex-facing entry point for requirements
analysis and OpenSpec handoff readiness.

The agent must classify user intent, resolve or create the requirements case,
validate state, then route to one bounded worker or report the block.

Every normal response must show:

- Intent
- Case
- State
- Allowed Action
- Blocked Action, when blocked
- Next Action
- Evidence

Authority model:

- Requirements case data is the live workflow state.
- `requirements/config/requirements-taxonomy.yaml` owns requirement readiness
  vocabulary.
- `wiki/config/frontmatter-taxonomy.yaml` is wiki page identity only.
- Python scripts are internal evidence tools, not the normal user interface.

Internal tools:

- `scripts/build_requirements_analysis_agent.py`
- `scripts/check_requirements_case.py`
- `scripts/requirements_openspec_draft.py`

Readiness evidence must include `domain_model_gate`, `domain_coverage_gate`,
`requirement_delivery_gate`, and `detailed_design_gate`.

Requirement readiness and detailed-design readiness are separate:

- `requirements_ready` means the requirement skeleton is reviewable.
- `detailed_design_gate` blocks API, DDL/schema, state-machine, rule-model,
  integration-contract, and engineering-breakdown design until product provides
  or explicitly waives the current-state material package, business rule
  position table, and system boundary contract table.
- Required product input: current-state material package.
- Required product input: business rule position table.
- Required product input: system boundary contract table.
- Missing detailed-design materials must not be hidden by AGI assumptions about
  current state, rule parameters, accounting treatment, or system boundaries.
- Do not claim detailed design can start when `detailed_design_gate.passed` is
  false, even if the requirements hard gate passes.

Worker routing:

- `req-intake`: source material and case creation or append.
- `req-domain-analysis`: domain classification and coverage obligations after
  intake and before scope.
- `req-scope`: roles, ownership, boundaries, and unknowns after domain analysis.
- `req-stories`: user stories with role, want, and benefit.
- `req-acceptance`: observable acceptance functions and story mappings.
- `req-handoff`: readiness gate and OpenSpec draft creation.

Boundaries:

- Do not ask the user to run Python as the normal path.
- Do not force unknown domains or roles into existing taxonomy IDs.
- Do not mutate requirements taxonomy, wiki taxonomy, AGENTS, skills, or
  OpenSpec lifecycle state unless the active OpenSpec change explicitly scopes
  it.
- Do not create an OpenSpec draft until the hard readiness gate passes.
- Do not continue into implementation automatically after draft creation.
