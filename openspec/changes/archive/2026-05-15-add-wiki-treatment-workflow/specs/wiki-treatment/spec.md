## ADDED Requirements

### Requirement: Repository SHALL plan bounded wiki treatment

The repository SHALL provide a treatment layer that turns approved low-risk
adjudication details into a dry-run treatment plan.

#### Scenario: A safe candidate has domain approval

- **WHEN** an adjudication detail is safe to apply
- **AND** the detail has no risk flags
- **AND** the candidate domain is explicitly approved
- **THEN** treatment SHALL include that detail as a treatment item.

#### Scenario: A safe candidate lacks approval

- **WHEN** an adjudication detail is safe to apply
- **AND** neither its domain nor its detail ref is approved
- **THEN** treatment SHALL skip that detail.

#### Scenario: A risky candidate is approved by domain

- **WHEN** an adjudication detail has risk flags
- **AND** its domain is explicitly approved
- **THEN** treatment SHALL skip that detail.

### Requirement: Treatment SHALL write only approved frontmatter with explicit apply

Treatment SHALL default to dry-run and SHALL mutate pages only when explicit
apply mode is requested.

#### Scenario: Treatment runs in dry-run mode

- **WHEN** treatment has approved items
- **AND** apply mode is not requested
- **THEN** treatment SHALL report planned items
- **AND** it SHALL NOT modify page files.

#### Scenario: Treatment runs in apply mode

- **WHEN** treatment has approved items
- **AND** apply mode is requested
- **THEN** treatment SHALL write only `candidate.suggested_frontmatter` fields
  to target page frontmatter
- **AND** it SHALL NOT write taxonomy config, relation fields, MOC pages, or
  OpenSpec state.

### Requirement: Treatment SHALL produce reviewable treatment records

The repository SHALL provide an explicit path for writing treatment records
under `wiki/ops/wiki-treatment-runs/`.

#### Scenario: User asks for a treatment record

- **WHEN** treatment is run with record writing enabled
- **THEN** the repository SHALL write a Markdown record under
  `wiki/ops/wiki-treatment-runs/`
- **AND** the record SHALL include planned/applied treatment items, skipped
  items, and proof boundaries.

#### Scenario: Later adjudication scans generated treatment records

- **WHEN** later adjudication scans covered wiki content
- **AND** files exist under `wiki/ops/wiki-treatment-runs/`
- **THEN** those generated treatment records SHALL NOT appear in
  `candidate_set`
- **AND** those generated treatment records SHALL NOT appear in
  `full_detail_set`.
