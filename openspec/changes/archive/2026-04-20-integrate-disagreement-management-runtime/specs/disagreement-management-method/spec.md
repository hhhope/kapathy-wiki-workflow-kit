## MODIFIED Requirements

### Requirement: Repository SHALL preserve disagreement as calibration material before promoting it into conclusion layers

When a repository-default workflow disagreement is still performing goal-calibration work, the repository SHALL preserve it as calibration material before promoting it into `ADR`, spec, skill, or other conclusion-oriented layers.

#### Scenario: Disagreement becomes repo-visible before stable decision
- **WHEN** a live disagreement is still doing calibration work
- **AND** it has enough shape to require durable repo-visible preservation
- **BUT** it is not yet stable enough for `ADR`, spec, or skill promotion
- **THEN** the repository SHALL prefer `wiki/ops retro`

## ADDED Requirements

### Requirement: Archive review SHALL check disagreement preservation and promotion

When an OpenSpec change reaches archive review, the repository SHALL check whether disagreement material was lost, should remain in method/retro form, or should already have been promoted to a stable decision layer.

#### Scenario: Archive review runs on a completed change
- **WHEN** archive review is performed on a completed change
- **THEN** the review SHALL check whether the change generated disagreement material that:
  - should remain in method or retro form
  - should be promoted to ADR
  - was flattened away without a durable record
