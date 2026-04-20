## ADDED Requirements

### Requirement: Repository SHALL support a bounded agent-utilization layer on top of semantic scoring

The repository SHALL support a downstream utilization step that reads semantic-scoring
output and emits bounded guidance for agent-side usage of canonical objects.

#### Scenario: Semantic-scoring artifact is available

- **WHEN** the repository has a semantic-scoring artifact
- **THEN** the repository SHALL be able to classify canonical objects into explicit utilization bands

### Requirement: Repository SHALL preserve utilization reasons, not only final bands

The repository SHALL preserve why an object is preferred, cautious, or blocked.

#### Scenario: Utilization artifact is generated

- **WHEN** utilization guidance is produced
- **THEN** each object SHALL include explicit reasons or factor-based justification

### Requirement: Repository SHALL preserve proof boundaries for utilization output

The repository SHALL distinguish utilization guidance from retrieval proof, runtime
autonomy, or semantic understanding of unresolved pages.

#### Scenario: Utilization artifact is generated

- **WHEN** the repository produces utilization guidance
- **THEN** it SHALL state that the output is bounded usage guidance only
