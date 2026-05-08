## ADDED Requirements

### Requirement: Account Wiki public-draft repair SHALL happen locally before Feishu sync

The Account Wiki article set repair SHALL complete local draft, visual, and
gate-review evidence before any Feishu write or review-ready claim.

#### Scenario: Previous packet is frozen as failed

- **WHEN** the gate-review artifact records a failed reference-readback decision
- **THEN** the system SHALL treat the existing Feishu packet as a failed draft
- **AND** SHALL NOT polish, sync, or claim it review-ready without a new local
  repair decision

#### Scenario: Local repair is requested

- **WHEN** the user asks to repair the Account Wiki runtime and validation/cases
  drafts before release
- **THEN** the system SHALL update the local report pages first
- **AND** SHALL update the repo-visible gate-review artifact before any external
  sync

### Requirement: Runtime and validation pages SHALL contain concrete evidence jobs

The runtime and validation/cases pages SHALL carry distinct reader jobs instead
of repeating generic overview content.

#### Scenario: Runtime page is repaired

- **WHEN** the runtime page is updated
- **THEN** it SHALL explain a concrete material journey from input to source
  preservation, routing, asset creation, output gating, writeback, and closeout
- **AND** it SHALL preserve non-claim boundaries for automation and team
  consensus

#### Scenario: Validation/cases page is repaired

- **WHEN** the validation/cases page is updated
- **THEN** it SHALL include concrete evidence categories such as failed draft
  freeze, Feishu update/readback, behavior replay, skill RED/GREEN, and visual
  gate decisions
- **AND** it SHALL distinguish completed proof from manual replay, local draft
  proof, and missing final-publication proof

### Requirement: Account Wiki visuals SHALL preserve page-specific visual jobs

The local visual artifact SHALL include dedicated visuals for runtime and
validation/cases rather than only an overview poster.

#### Scenario: Runtime visual is added

- **WHEN** the visual artifact is repaired
- **THEN** it SHALL include a runtime visual that carries sequence or flow logic
  for source, route, asset, output, and writeback

#### Scenario: Validation/cases visual is added

- **WHEN** the visual artifact is repaired
- **THEN** it SHALL include a validation/cases visual that carries evidence,
  replay, gate decision, and boundary logic

### Requirement: Infographic skill repair SHALL be pressure-tested before reliance

Any semantic `infographic-onepager` skill change made for this repair SHALL
include local RED/GREEN evidence before it is treated as complete.

#### Scenario: Skill changes multi-page Account Wiki behavior

- **WHEN** the skill is changed to handle Account Wiki multi-page article sets
- **THEN** the change SHALL record a RED baseline against the old wording
- **AND** SHALL record a GREEN result showing separate overview, runtime,
  validation/cases, migration, and roadmap visual jobs are preserved when needed
