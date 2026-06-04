## ADDED Requirements

### Requirement: req-agent SHALL separate requirement readiness from detailed-design readiness

`req-agent` SHALL treat requirement review readiness and detailed-design
readiness as separate gates.

#### Scenario: Requirement skeleton is ready but design inputs are missing

- **WHEN** a requirements case passes domain model, domain coverage, and
  requirement delivery gates
- **AND** the current-state material package, business rule position table, or
  system boundary contract table is missing
- **THEN** the requirements checker SHALL keep the case `requirements_ready`
- **AND** it SHALL report detailed design as blocked
- **AND** `req-agent` SHALL NOT claim API, DDL, state-machine, or
  implementation-design readiness

#### Scenario: Product supplies or explicitly waives design inputs

- **WHEN** all detailed-design hard gates have approved material evidence or an
  explicit product waiver
- **THEN** the requirements checker SHALL report detailed design as passed
- **AND** `req-agent` MAY allow detailed design to start after the normal
  requirements/OpenSpec handoff boundary is satisfied

### Requirement: req-agent SHALL require three product-owned design input gates

Every normal `req-agent` requirements case SHALL carry reusable
detailed-design hard gates for current state, business rules, and system
boundaries.

#### Scenario: A new requirements case is created

- **WHEN** the requirements case package is built
- **THEN** it SHALL include `detailed_design_hard_gates`
- **AND** the gate IDs SHALL include `current_state_material_package`,
  `business_rule_position_table`, and `system_boundary_contract_table`
- **AND** the gates SHALL identify product or requirement proposer ownership

#### Scenario: req-agent reports a blocked design handoff

- **WHEN** detailed design is blocked by missing product-owned gate materials
- **THEN** `req-agent` SHALL ask for the missing materials from the product or
  requirement proposer
- **AND** it SHALL not infer current state, rule parameters, accounting
  treatment, or system integration boundaries from generic AGI assumptions

