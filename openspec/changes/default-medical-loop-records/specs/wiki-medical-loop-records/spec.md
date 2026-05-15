## Purpose

Define durable default record behavior for the diagnosis and confirmation
stages of the LLM-WIKI medical loop.

## ADDED Requirements

### Requirement: wiki-doctor SHALL write diagnosis records by default

The repository SHALL treat `wiki-doctor` invocation as a diagnosis stage that
creates a complete repo-visible diagnosis record by default.

#### Scenario: User invokes wiki-doctor

- **WHEN** the user invokes `$report-wiki-portfolio:wiki-doctor`
- **THEN** the repository SHALL run the content adjudication package builder
- **AND** it SHALL write a complete Markdown diagnosis record under
  `wiki/ops/wiki-doctor-runs/`
- **AND** stdout SHALL include a compact summary and the diagnosis record path
- **AND** the written record SHALL NOT be truncated by stdout preview limits.

#### Scenario: User needs JSON-only doctor debugging

- **WHEN** the user or test invokes the doctor CLI with `--stdout-json-only`
- **THEN** the repository SHALL emit the JSON adjudication package to stdout
- **AND** it SHALL NOT write a diagnosis record.

### Requirement: wiki-confirm SHALL write confirmation records by default

The repository SHALL treat `wiki-confirm` invocation as a confirmation stage
that creates a complete repo-visible confirmation record by default.

#### Scenario: User invokes wiki-confirm

- **WHEN** the user invokes `$report-wiki-portfolio:wiki-confirm`
- **THEN** the repository SHALL run the review decision package builder
- **AND** it SHALL write a complete Markdown confirmation record under
  `wiki/ops/wiki-review-decisions/`
- **AND** stdout SHALL include a compact summary and the confirmation record path
- **AND** the written record SHALL NOT be truncated by stdout preview limits.

#### Scenario: User needs JSON-only confirm debugging

- **WHEN** the user or test invokes the confirm CLI with `--stdout-json-only`
- **THEN** the repository SHALL emit the JSON review decision package to stdout
- **AND** it SHALL NOT write a confirmation record.

### Requirement: Medical-loop records SHALL explain standards and advice

Diagnosis and confirmation records SHALL preserve enough evidence for later
treatment, surgery, recovery, and audit.

#### Scenario: Diagnosis record is written

- **WHEN** the doctor CLI writes a diagnosis record
- **THEN** the record SHALL include source, exam items, reference standards,
  diagnosis summary, abnormal findings, proof boundary, and recommended next
  stage sections
- **AND** it SHALL explain risk markers such as `agent_uncertain`,
  `relation_weak_evidence`, `openspec_required`, `drift_risk`, and `adr_risk`.

#### Scenario: Confirmation record is written

- **WHEN** the confirm CLI writes a confirmation record
- **THEN** the record SHALL include source, decision rules, confirmed buckets,
  abnormal findings, medical advice, and proof boundary sections
- **AND** it SHALL preserve the fixed buckets `accepted_candidates`,
  `rejected_candidates`, `deferred_items`, `treatment_candidates`,
  `surgery_candidates`, and `openspec_required`.

### Requirement: Medical-loop records SHALL preserve repair boundaries

Diagnosis and confirmation records SHALL be evidence and routing artifacts, not
repair approval.

#### Scenario: Record contains treatment or surgery candidates

- **WHEN** a generated record lists treatment, surgery, or OpenSpec-required
  candidates
- **THEN** it SHALL NOT write frontmatter, taxonomy config, relation fields,
  MOC files, ADRs, or OpenSpec lifecycle state
- **AND** it SHALL state that later explicit approval or planning is required
  before treatment or surgery.
