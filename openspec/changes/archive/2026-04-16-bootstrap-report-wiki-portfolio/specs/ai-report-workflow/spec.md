## ADDED Requirements

### Requirement: Wiki SHALL distinguish AI-generated material from approved knowledge
The system SHALL label AI-generated summaries, link suggestions, and report drafts so they can be reviewed separately from accepted human conclusions.

#### Scenario: AI output is visible but not confused with final knowledge
- **WHEN** a page contains AI-generated assistance content
- **THEN** the page SHALL identify that content as AI-generated and preserve a place for human review status

### Requirement: AI workflow SHALL support progressive report assembly
The system SHALL support a workflow in which source pages and index pages can feed a draft report page without requiring contributors to rebuild context from scratch.

#### Scenario: Report draft is assembled from indexed knowledge
- **WHEN** a contributor prepares a periodic or audience-specific report
- **THEN** the wiki SHALL provide a report template and linked upstream pages that support draft assembly from existing sources and summaries

### Requirement: AI workflow SHALL remain optional for manual use
The initial wiki structure SHALL remain fully usable even if no AI automation or prompt execution is available.

#### Scenario: Manual report preparation still works
- **WHEN** a contributor uses the wiki without any AI tooling
- **THEN** the contributor SHALL still be able to record sources, maintain summaries, and prepare report drafts using the provided templates
