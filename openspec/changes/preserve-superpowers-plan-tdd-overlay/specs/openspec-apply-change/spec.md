## ADDED Requirements

### Requirement: Derived OpenSpec changes SHALL preserve Superpowers plan overlays

The repository SHALL preserve an approved Superpowers design or writing-plan artifact as an implementation overlay when an OpenSpec change is derived from it.

The overlay preserves acceptance details, TDD strategy, module strategy, and
verification intent.

#### Scenario: OpenSpec change derives from Superpowers design and plan

- **WHEN** a Superpowers design or writing-plan artifact exists for the same
  implementation scope
- **AND** an OpenSpec change is created from it
- **THEN** the OpenSpec change SHALL reference the Superpowers source artifact
- **AND** it SHALL include an overlay mapping from key Superpowers acceptance
  and TDD details to OpenSpec tasks, spec scenarios, or verification evidence
- **AND** `tasks.md` SHALL remain the only progress and completion ledger.

#### Scenario: TDD details exist in the Superpowers plan

- **WHEN** the Superpowers plan defines RED/GREEN steps, failing evidence,
  checker fixtures, test commands, or TDD sequencing
- **THEN** the OpenSpec change SHALL preserve those details as mapped
  implementation or verification obligations
- **AND** it SHALL NOT collapse them into generic "run tests" or "verify"
  wording without citing the original TDD detail.

#### Scenario: Implementation resumes from an OpenSpec change with overlay

- **WHEN** implementation starts or resumes for a change with a mapped
  Superpowers overlay
- **THEN** the agent SHALL read `tasks.md` for progress state
- **AND** it SHALL read the mapped Superpowers overlay for acceptance and TDD
  tactics before editing implementation files
- **AND** it SHALL stop and re-anchor if the overlay and OpenSpec artifacts
  conflict.

#### Scenario: Completion is claimed for a derived OpenSpec change

- **WHEN** a derived OpenSpec change is claimed complete
- **THEN** completion evidence SHALL include OpenSpec validation and task
  status
- **AND** it SHALL include overlay conformance evidence for mapped acceptance
  and TDD details
- **AND** keyword presence, screenshot smoke, or generic validation SHALL NOT
  count as sufficient evidence when the mapped overlay requires structure-level
  or RED/GREEN verification.
