## ADDED Requirements

### Requirement: Superpowers-native execution SHALL remain uninterrupted

The repository SHALL execute from the approved Superpowers plan when a Superpowers design spec and writing-plan are active.

#### Scenario: Superpowers plan is active during implementation

- **WHEN** a user-approved Superpowers design spec and writing-plan exist
- **AND** implementation begins or resumes
- **THEN** the agent SHALL use the Superpowers plan as the implementation plan
- **AND** OpenSpec `tasks.md` SHALL NOT track Superpowers block progress
- **AND** OpenSpec `tasks.md` SHALL NOT replace the Superpowers plan with a
  second implementation plan.

### Requirement: OpenSpec tasks SHALL be check and archive lifecycle items

OpenSpec tasks SHALL stay limited to check, evidence, validation, and archive lifecycle items when the implementation is driven by a Superpowers plan.

#### Scenario: OpenSpec is used after Superpowers implementation

- **WHEN** all Superpowers plan blocks are complete
- **THEN** OpenSpec MAY be used to check acceptance, summarize evidence, run
  validation, and perform archive review
- **AND** OpenSpec tasks SHALL NOT introduce implementation steps such as RED,
  GREEN, file edits, or block execution.

### Requirement: Scope changes SHALL stop Superpowers implementation

The repository SHALL stop Superpowers plan execution when implementation discovers scope outside the approved plan or acceptance spec.

#### Scenario: Implementation discovers new scope

- **WHEN** a Superpowers plan block requires behavior, files, or acceptance
  criteria outside the approved plan
- **THEN** the agent SHALL stop implementation
- **AND** the agent SHALL update or create OpenSpec scope before continuing
- **AND** the agent SHALL NOT silently merge the new scope into the current
  Superpowers plan.

### Requirement: Completion evidence SHALL summarize Superpowers block evidence

Completion evidence SHALL summarize evidence from completed Superpowers blocks instead of replacing the Superpowers plan.

#### Scenario: OpenSpec check/archive follows Superpowers completion

- **WHEN** OpenSpec check/archive starts after Superpowers implementation
- **THEN** `evaluation.md` SHALL cite the source Superpowers spec and plan
- **AND** it SHALL summarize acceptance evidence from completed plan blocks
- **AND** keyword presence, screenshot smoke, or generic validation SHALL NOT
  count as sufficient evidence when the Superpowers Acceptance Spec requires
  structure-level, reader-path, behavior, RED/GREEN, or replay verification.
