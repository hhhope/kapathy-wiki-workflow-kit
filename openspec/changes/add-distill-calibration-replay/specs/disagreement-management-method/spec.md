## ADDED Requirements

### Requirement: Repository SHALL provide an executable replay contract for distill-calibration disputes

When the repository needs to validate whether a `distill` page overstates the
current level of governance agreement, it SHALL provide a bounded executable
replay contract for the calibration record.

#### Scenario: Distill calibration replay record is validated

- **WHEN** the repository validates a structured distill-calibration replay
  record
- **THEN** it SHALL provide an executable checker for the record shape
- **AND** the checker SHALL fail when required fields or required pass
  conditions are missing

### Requirement: Distill calibration replay SHALL preserve fact/model separation

The distill-calibration replay record SHALL preserve the minimum evidence needed
to distinguish factual session recap from candidate governance modeling.

#### Scenario: Distill calibration replay record is captured

- **WHEN** the repository captures a distill-calibration replay record
- **THEN** it SHALL preserve at least:
  - the distill page under review
  - which sections are treated as fact recap
  - which sections are treated as candidate governance model
  - which phrases currently overclaim agreement
  - what downgraded wording would keep the result honest

### Requirement: Distill calibration replay proof SHALL stay structural and bounded

Executable replay proof for distill calibration SHALL stay structural and honest.

#### Scenario: Distill calibration checker passes

- **WHEN** the distill-calibration replay checker passes
- **THEN** the repository SHALL treat that pass as structural executable proof
  only
- **AND** it SHALL NOT claim governance consensus, semantic certainty, or full
  rollout proof
