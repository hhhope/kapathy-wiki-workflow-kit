# Design

## Model

Requirements readiness and detailed-design readiness are separate gates:

- `requirements_ready` means the requirement skeleton is reviewable: domain,
  coverage, roles, stories, acceptance, and traceability pass.
- `detailed_design_hard_gates` means product-owned design inputs are present or
  explicitly waived before API, DDL, state-machine, or implementation design.

The checker must not collapse these two gates. Missing detailed-design materials
should surface as a design readiness block while preserving the requirement
hard-gate status.

## Default Hard Gates

Every new requirements case package includes three default design hard gates:

1. `current_state_material_package`
2. `business_rule_position_table`
3. `system_boundary_contract_table`

Each gate records:

- `hard_gate: true`
- required product owner/source
- required material
- pass condition
- blocked design scope
- approval/material status

## Checker Behavior

The checker returns `detailed_design_gate` with:

- `passed`
- `mode`
- `required_gates`
- `blockers`

The existing `summary.hard_gate_passed` remains about requirement readiness.
The CLI markdown report prints detailed-design status after the existing
requirements gates.

## Skill Behavior

`req-agent` must report this distinction during readiness and handoff work:

- allowed: requirement review and OpenSpec handoff when requirement gates pass
- blocked: detailed design and implementation design until design hard gates
  pass or are explicitly waived with evidence

## Skill Evaluation

Because `.codex/skills/req-agent/SKILL.md` changes semantically, this change
includes evaluation evidence with:

- RED baseline
- GREEN result
- pressure scenarios
- prior-art/common-rule dedupe
- residual risks

