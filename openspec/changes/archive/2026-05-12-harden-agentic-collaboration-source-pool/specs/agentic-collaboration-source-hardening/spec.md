## ADDED Requirements

### Requirement: Agentic collaboration source hardening SHALL separate source-lead count from publication readiness

The `agentic-product-engineering-collaboration` source-hardening pass SHALL
track source-lead volume separately from publication-grade evidence.

#### Scenario: Source pool reaches 300 leads

- **WHEN** the source pool is expanded toward 300 sources
- **THEN** the repository SHALL report the unique URL count
- **AND** it SHALL state that source leads are not the same as deeply read or
  publication-ready sources

### Requirement: Source hardening SHALL preserve source classes and use boundaries

New source leads SHALL retain enough classification to support later evidence
selection and prevent secondary or candidate leads from carrying hard claims.

#### Scenario: New source lead is added

- **WHEN** a new source lead is added to the source pool
- **THEN** it SHALL include a source class or status
- **AND** it SHALL include a short note about what the source can contribute
- **AND** secondary, candidate, media, index, and transcript-needed sources SHALL
  not be treated as final hard evidence

### Requirement: Source hardening SHALL update report evidence status

The repository SHALL update report evidence status when this source-hardening
pass changes the source pool count or evidence surface, without claiming
publication readiness by default.

#### Scenario: Source pool count changes

- **WHEN** the source pool reaches the target count
- **THEN** the article evidence matrix or gate review SHALL record the updated
  source count
- **AND** it SHALL preserve remaining blockers such as transcript capture,
  primary memo capture, visual QA, and user-owned local judgment
