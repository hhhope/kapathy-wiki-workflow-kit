## ADDED Requirements

### Requirement: Repository SHALL provide executable validation for the readable-view bundle

The repository SHALL provide a bounded executable validation contract for the
first-pass readable-view bundle.

#### Scenario: Readable-view bundle is validated

- **WHEN** the repository validates the current readable-view bundle
- **THEN** it SHALL be able to check that the required pages exist
- **AND** it SHALL be able to check that the expected index entry points exist

### Requirement: Readable-view executable validation SHALL preserve proof boundaries

The repository SHALL distinguish structural reading-bundle validation from
semantic proof of reading quality.

#### Scenario: Validation checker passes

- **WHEN** the readable-view validation checker passes
- **THEN** the repository SHALL treat that as structural proof only
- **AND** it SHALL not claim semantic certainty or future rollout proof
