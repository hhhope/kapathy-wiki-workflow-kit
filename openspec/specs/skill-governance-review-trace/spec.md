# skill-governance-review-trace Specification

## Purpose
TBD - created by archiving change hermes-skill-governance-review. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL keep a traceable external agent-self-evolution review
The repository SHALL retain an OpenSpec review artifact that records the external sources, comparison dimensions, and conclusions when an outside agent-self-evolution model is used to benchmark this repository.

#### Scenario: User asks for a Hermes self-evolution comparison
- **WHEN** the user asks to review the Hermes article and its corresponding GitHub project and wants the result landed with traceability
- **THEN** the repository SHALL contain a review change that records the article, repository, and concrete governance conclusions

### Requirement: Review SHALL separate strengths, gaps, ADRs, and follow-up changes
The review SHALL explicitly distinguish what the repository already does well, what gaps remain, which decisions are ADRs, and which improvements require future changes.

#### Scenario: Review is inspected later
- **WHEN** a later contributor reads the review change
- **THEN** they SHALL be able to see current strengths, outstanding gaps, ADR-level decisions, and follow-up change candidates without inferring them from chat history

### Requirement: Review SHALL capture incremental-refresh governance gaps
The review SHALL explicitly record whether the repository distinguishes already-structured material from new raw material and whether the agent is expected to refresh incrementally instead of reprocessing everything.

#### Scenario: Repository is benchmarked against Hermes
- **WHEN** the review compares current behavior to Hermes-style experience reuse
- **THEN** it SHALL state whether the repository has a state-driven incremental refresh model and identify the gap if it does not

### Requirement: Review SHALL not silently expand into implementation
The review change SHALL document future governance work without directly modifying unrelated skill behavior as part of the benchmark exercise.

#### Scenario: Review leads to improvement ideas
- **WHEN** the review identifies useful governance improvements
- **THEN** those improvements SHALL be listed as follow-up changes rather than silently implemented inside the review change

