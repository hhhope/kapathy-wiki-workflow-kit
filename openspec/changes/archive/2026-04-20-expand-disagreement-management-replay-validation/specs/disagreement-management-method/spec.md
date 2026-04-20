## MODIFIED Requirements

### Requirement: Repository SHALL preserve disagreement as calibration material before promoting it into conclusion layers

When a repository-default workflow disagreement is still performing goal-calibration work, the repository SHALL preserve it as calibration material before promoting it into `ADR`, spec, skill, or other conclusion-oriented layers.

#### Scenario: Replay validation checks a new disagreement shape
- **WHEN** the repository validates the disagreement-management method against another disagreement shape
- **THEN** that replay SHALL preserve the disagreement as calibration material first
- **AND** the replay evidence SHALL keep the method boundary explicit rather than collapsing into endpoint-only conclusions

## ADDED Requirements

### Requirement: Repository SHALL provide a reusable replay harness for disagreement-management validation

When the repository validates disagreement-management behavior, it SHALL provide a reusable replay harness that keeps replay proof distinct from rollout proof.

#### Scenario: Future contributor replays a disagreement thread
- **WHEN** a contributor validates the method on a disagreement thread
- **THEN** the repository SHALL provide a harness that captures at least:
  - disagreement shape
  - rejected framing
  - correction pressure
  - redirection moment
  - clarity state
  - protected target, if visible
  - RED baseline
  - GREEN result
  - residual risk

#### Scenario: Replay validation is recorded
- **WHEN** the repository records replay validation evidence
- **THEN** it SHALL state that replay / harness validation is stronger than narrative design-only reasoning
- **AND** it SHALL NOT claim rollout proof from replay evidence alone
