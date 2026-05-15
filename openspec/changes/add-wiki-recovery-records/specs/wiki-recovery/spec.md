## ADDED Requirements

### Requirement: Repository SHALL produce wiki recovery packages

The repository SHALL provide a recovery layer that runs bounded post-treatment
or post-surgery checks and captures their results.

#### Scenario: Recovery checks run

- **WHEN** recovery is invoked
- **THEN** it SHALL run configured checks
- **AND** it SHALL preserve each command, exit code, pass/fail status, and parsed
  summary when available.

#### Scenario: A check exits nonzero

- **WHEN** a recovery check exits nonzero
- **THEN** recovery SHALL preserve that failure as a finding
- **AND** it SHALL still produce the recovery package
- **AND** it SHALL route the package to `blocked_by_recovery_findings`.

### Requirement: Recovery SHALL remain non-mutating by default

Recovery SHALL NOT apply treatment, apply surgery, write MOC pages, write status
files, mutate frontmatter, mutate taxonomy config, write relation fields, write
ADR decisions, or mutate OpenSpec state.

#### Scenario: User runs default recovery

- **WHEN** the recovery CLI runs without a record flag
- **THEN** it SHALL emit JSON to stdout
- **AND** it SHALL NOT write a recovery record.

#### Scenario: User asks for a recovery record

- **WHEN** recovery runs with record writing enabled
- **THEN** it SHALL write a Markdown record under `wiki/ops/wiki-recovery-runs/`
- **AND** the record SHALL include check results and proof boundaries.

#### Scenario: Later adjudication scans generated recovery records

- **WHEN** later adjudication scans covered wiki content
- **AND** files exist under `wiki/ops/wiki-recovery-runs/`
- **THEN** those generated recovery records SHALL NOT appear in `candidate_set`
- **AND** those generated recovery records SHALL NOT appear in `full_detail_set`.
