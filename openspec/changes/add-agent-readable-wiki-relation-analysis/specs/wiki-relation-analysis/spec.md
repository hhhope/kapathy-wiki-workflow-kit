## ADDED Requirements

### Requirement: Repository SHALL support relation analysis on top of extracted wiki graph structure

The repository SHALL support a downstream relation-analysis step that reads extracted
graph structure and summarizes it into reusable structural signals.

#### Scenario: Extracted graph is available

- **WHEN** the repository has an extracted wiki graph artifact
- **THEN** the repository SHALL be able to analyze object coverage, relation usage, and unresolved areas

### Requirement: Repository SHALL preserve proof boundaries for relation analysis

The repository SHALL distinguish structural relation analysis from semantic graph
understanding or rollout proof.

#### Scenario: Relation analysis artifact is produced

- **WHEN** a relation-analysis artifact is generated
- **THEN** the repository SHALL make clear that the result is structural analysis only
- **AND** it SHALL not claim unresolved pages are semantically understood

### Requirement: Repository SHALL expose unresolved structure in the analysis output

The repository SHALL preserve unresolved areas as first-class analysis output rather
than flattening them away.

#### Scenario: Extracted graph still contains unresolved identity warnings

- **WHEN** relation analysis runs on a graph with unresolved warnings
- **THEN** the analysis artifact SHALL summarize unresolved structure explicitly
