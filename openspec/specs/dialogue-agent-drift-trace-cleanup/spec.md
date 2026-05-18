# dialogue-agent-drift-trace-cleanup Specification

## Purpose
Classify dialogue disagreement, agent drift, and re-anchor trace records as a
review-only surface before any write-capable wiki cleanup is approved.

## Requirements
### Requirement: Dialogue drift cleanup SHALL classify live-conversation calibration records separately

The repository SHALL provide a review-only classification for pages that record
dialogue disagreement, agent drift, or re-anchor traces so they are not mixed
with generic governance cleanup, learning notes, project intakes, or report
quality evidence.

#### Scenario: Page records rejected framing or user correction pressure
- **WHEN** a reviewed `wiki/ops` page explicitly records rejected framing,
  corrected framing, user correction pressure, or conversation-level
  disagreement
- **THEN** the review output SHALL classify it as `dialogue-disagreement`
- **AND** the review output SHALL include the evidence phrase or field used for
  that classification
- **AND** it SHALL NOT write wiki frontmatter or relation fields.

#### Scenario: Page records an agent route or workflow failure
- **WHEN** a reviewed `wiki/ops` page explicitly records that the agent followed
  the wrong route, output mode, workflow chain, or implementation boundary
- **THEN** the review output SHALL classify it as `agent-drift`
- **AND** it SHALL recommend either `defer-cleanup` or `openspec-candidate`
  rather than direct implementation.

#### Scenario: Page records a re-anchor gate or continuation stop
- **WHEN** a reviewed `wiki/ops` page explicitly records that continuation must
  stop and return to a confirmed requirement, route, or boundary
- **THEN** the review output SHALL classify it as `reanchor-trace`
- **AND** it SHALL preserve the proof boundary that re-anchor evidence is not an
  implementation approval.

### Requirement: Dialogue drift cleanup SHALL distinguish supporting examples from live incidents

The repository SHALL distinguish examples and replay harnesses that teach or
validate disagreement handling from records of actual live drift incidents.

#### Scenario: Page is a sample or replay harness
- **WHEN** a reviewed page is explicitly a sample, example, replay harness, or
  validation record for disagreement or re-anchor behavior
- **THEN** the review output SHALL classify it as `supporting-example`
- **AND** it SHALL NOT treat the page as a live drift incident.

### Requirement: Dialogue drift cleanup SHALL reject unrelated drift mentions

The repository SHALL avoid over-classifying pages as dialogue drift only because
they mention drift, disagreement, or framing.

#### Scenario: Page is project-management, learning, or report quality material
- **WHEN** a reviewed page is primarily a project-management intake, source
  learning note, reading note, report gate review, or public-output quality
  record
- **THEN** the review output SHALL classify it as `not-dialogue-drift`
- **AND** it SHALL route the page to the appropriate cleanup path instead of
  dialogue drift cleanup.

### Requirement: Dialogue drift cleanup SHALL remain review-only until separately approved

The classification SHALL remain a review surface unless a later implementation
workflow explicitly scopes write-capable behavior.

#### Scenario: Classification output is generated
- **WHEN** dialogue drift classification output is generated
- **THEN** it SHALL NOT mutate `wiki/config/frontmatter-taxonomy.yaml`
- **AND** it SHALL NOT write wiki frontmatter
- **AND** it SHALL NOT write relation fields
- **AND** it SHALL NOT modify ADRs, AGENTS, skills, or unrelated OpenSpec
  lifecycle state.
