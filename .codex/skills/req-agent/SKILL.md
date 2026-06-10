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
`requirement_delivery_gate`, `regulatory_gate`, and `detailed_design_gate`.

Regulatory readiness is part of requirement readiness:

- `regulatory_gate` triggers when the case includes `risk_compliance` or
  explicit regulation, compliance, identity, authorization, consent, personal
  information, SMS link, token, or similar regulated-action signals.
- Triggered cases must carry case-local regulatory obligations in
  `soft_evidence.regulatory_obligations`.
- Missing or unresolved regulatory obligations block `requirements_ready`.
- Do not treat regulatory obligations as generic design polish; they can change
  domain, scope, stories, acceptance, readiness, and blockers.

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
- `req-domain-analysis`: domain classification, regulatory obligations, and
  coverage obligations after intake and before scope.
- `req-scope`: roles, ownership, regulatory obligation ownership, boundaries,
  and unknowns after domain analysis.
- `req-stories`: user stories with role, want, and benefit.
- `req-acceptance`: observable acceptance functions, regulatory obligation
  mappings, and story mappings.
- `req-human-review`: human-readable review artifact, scenario/rule coverage,
  regulatory demand-fact coverage, gap classification, and machine-case
  synchronization before handoff.
- `req-handoff`: readiness gate and OpenSpec draft creation.

Boundaries:

- Do not ask the user to run Python as the normal path.
- Do not force unknown domains or roles into existing taxonomy IDs.
- Do not skip `req-human-review` before handoff when the user asks for a human
  readable requirements review or when a Human Review artifact exists.
- Do not let Human Review become a second source of truth: demand facts that
  change domain, scope, stories, acceptance, roles, readiness, or blockers must
  be synchronized into the requirements case.
- Do not mutate requirements taxonomy, wiki taxonomy, AGENTS, skills, or
  OpenSpec lifecycle state unless the active OpenSpec change explicitly scopes
  it.
- Do not create an OpenSpec draft until the hard readiness gate passes.
- Do not continue into implementation automatically after draft creation.
