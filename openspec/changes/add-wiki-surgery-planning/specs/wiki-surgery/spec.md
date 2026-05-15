## ADDED Requirements

### Requirement: Repository SHALL produce plan-only wiki surgery packages

The repository SHALL provide a surgery planning layer for structural,
governance-sensitive, taxonomy, relation, OpenSpec, drift, ADR, and MOC work.

#### Scenario: Adjudication details contain surgery risks

- **WHEN** adjudication details contain `relation_weak_evidence`,
  `drift_risk`, `adr_risk`, `openspec_required`, or `taxonomy_candidate`
- **AND** adjudication eval has not failed
- **THEN** surgery planning SHALL include those details as surgery items
- **AND** it SHALL preserve the source detail refs, paths, risk flags, and
  reasons.

#### Scenario: Adjudication eval failed

- **WHEN** adjudication `eval_result.passed` is false
- **THEN** surgery planning SHALL mark the plan as blocked
- **AND** it SHALL NOT produce surgery items or MOC projection items.

#### Scenario: Adjudication details are safe treatment candidates

- **WHEN** adjudication details have no surgery risk
- **THEN** surgery planning SHALL NOT include them as surgery items.

### Requirement: Surgery planning SHALL include explicit MOC dry-run input

Surgery planning SHALL accept optional MOC projection dry-run input and classify
non-noop MOC entries as surgery items.

#### Scenario: MOC plan contains create, update, noop, and orphan entries

- **WHEN** a MOC plan is provided
- **THEN** surgery planning SHALL include `create`, `update`, and `orphan`
  entries as MOC surgery items
- **AND** it SHALL exclude `noop` entries.

### Requirement: Surgery planning SHALL remain non-writing

Surgery planning SHALL NOT mutate frontmatter, taxonomy config, relation fields,
MOC pages, ADR decisions, or OpenSpec state.

#### Scenario: User runs default surgery planning

- **WHEN** the surgery CLI runs without a record flag
- **THEN** it SHALL emit JSON to stdout
- **AND** it SHALL NOT write a surgery record.

#### Scenario: User asks for a surgery record

- **WHEN** the surgery CLI runs with record writing enabled
- **THEN** it SHALL write a Markdown record under `wiki/ops/wiki-surgery-runs/`
- **AND** the record SHALL preserve proof boundaries and next review actions.

#### Scenario: Later adjudication scans generated surgery records

- **WHEN** later adjudication scans covered wiki content
- **AND** files exist under `wiki/ops/wiki-surgery-runs/`
- **THEN** those generated surgery records SHALL NOT appear in `candidate_set`
- **AND** those generated surgery records SHALL NOT appear in `full_detail_set`.
