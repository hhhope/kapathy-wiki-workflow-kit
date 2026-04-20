## MODIFIED Requirements

### Requirement: Repository SHALL provide a reusable replay harness for disagreement-management validation

When the repository validates disagreement-management behavior, it SHALL provide a reusable replay harness that keeps replay proof distinct from rollout proof.

#### Scenario: Executable replay record is validated
- **WHEN** the repository validates a structured disagreement replay record
- **THEN** the repository SHALL provide an executable checker for the replay record shape
- **AND** the checker SHALL fail when required replay fields or required pass-condition checks are missing

## ADDED Requirements

### Requirement: Executable replay proof SHALL stay structural and honest

When the repository provides an executable replay harness, it SHALL keep the proof boundary explicit and avoid pretending to semantically understand the underlying disagreement.

#### Scenario: Checker passes on a replay record
- **WHEN** the executable harness passes on a replay record
- **THEN** that pass SHALL mean the structured replay contract is satisfied
- **AND** it SHALL NOT claim that the disagreement itself has been semantically validated automatically
