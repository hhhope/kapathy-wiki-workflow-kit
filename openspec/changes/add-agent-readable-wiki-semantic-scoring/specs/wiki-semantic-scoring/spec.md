## ADDED Requirements

### Requirement: Repository SHALL support bounded semantic scoring on top of relation analysis

The repository SHALL support a downstream semantic-scoring step that reads relation
analysis output and emits bounded semantic-strength signals for canonical objects.

#### Scenario: Relation-analysis artifact is available

- **WHEN** the repository has a relation-analysis artifact
- **THEN** the repository SHALL be able to score canonical objects using explicit bounded factors

### Requirement: Repository SHALL expose score factors, not just opaque totals

The repository SHALL preserve factor breakdown alongside semantic scores.

#### Scenario: Semantic score is generated

- **WHEN** a semantic-scoring artifact is produced
- **THEN** each scored object SHALL include visible factor breakdown or audit-friendly reasoning

### Requirement: Repository SHALL preserve proof boundaries for semantic scoring

The repository SHALL distinguish semantic scoring from retrieval proof, runtime proof,
or semantic understanding of unresolved pages.

#### Scenario: Semantic-scoring artifact is generated

- **WHEN** the repository produces semantic scores
- **THEN** it SHALL state that the scores are bounded repository-evidence signals only
