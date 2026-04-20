# live-conversation-reanchor-gate-replay Specification

## ADDED Requirements

### Requirement: Repository SHALL provide an executable replay contract for re-anchor-gate validation

When the repository validates `live-conversation-reanchor-gate`, it SHALL provide an executable replay contract that can fail when the required gate evidence is missing.

#### Scenario: Replay record is validated
- **WHEN** a structured re-anchor replay record is validated
- **THEN** the repository SHALL provide an executable checker for the record shape
- **AND** the checker SHALL fail when required fields or required pass checks are missing

### Requirement: Replay record SHALL preserve re-anchor-specific evidence

The re-anchor replay record SHALL preserve the minimum evidence needed to reconstruct the gate behavior.

#### Scenario: Re-anchor replay record is captured
- **WHEN** the repository captures a re-anchor replay record
- **THEN** it SHALL preserve at least:
  - original requirement
  - current drift chain
  - trigger signals
  - stop action
  - repo-visible re-anchor artifact
  - unblock condition

### Requirement: Repository SHALL keep executable replay proof bounded

Executable replay proof for re-anchor-gate SHALL stay structural and bounded.

#### Scenario: Replay checker passes
- **WHEN** the re-anchor replay checker passes
- **THEN** the repository SHALL treat it as structural executable proof only
- **AND** it SHALL NOT claim semantic certainty or perfect automatic drift detection
