## ADDED Requirements

### Requirement: Adjudication SHALL exclude generated review artifacts

Adjudication SHALL exclude repository-generated diagnosis and review-decision
records from its candidate input.

#### Scenario: Generated doctor and review-decision records exist

- **WHEN** adjudication scans covered wiki content
- **AND** files exist under `wiki/ops/wiki-doctor-runs/`
- **AND** files exist under `wiki/ops/wiki-review-decisions/`
- **THEN** those generated files SHALL NOT appear in `candidate_set`
- **AND** those generated files SHALL NOT appear in `full_detail_set`
- **AND** `summary.candidate_count` SHALL count only non-generated candidates.

#### Scenario: Ordinary ops pages still exist

- **WHEN** an ordinary covered page exists under `wiki/ops/`
- **THEN** adjudication SHALL keep that page eligible as a candidate.

