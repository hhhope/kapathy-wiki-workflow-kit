## ADDED Requirements

### Requirement: Repository SHALL provide a project-level wiki ADR container
The repository SHALL provide a project-level ADR container under `wiki/adr/` for stable workflow and governance decisions that remain useful across multiple OpenSpec changes.

#### Scenario: Stable workflow decision is made
- **WHEN** a workflow or governance decision is expected to remain relevant beyond the current change
- **THEN** the decision SHALL be recorded in `wiki/adr/`

### Requirement: Change artifacts SHALL keep scope and checkpoint context
OpenSpec change artifacts SHALL continue to own change scope, tasks, and interruption checkpoints even after stable decisions move to the wiki ADR container.

#### Scenario: Workflow change is interrupted
- **WHEN** work on a workflow-level change is interrupted or leaves an unresolved branch
- **THEN** the active OpenSpec change SHALL keep a checkpoint or equivalent scope note
- **AND** the stable ADR SHALL remain in `wiki/adr/`

### Requirement: Repository SHALL separate ADRs from retros
The repository SHALL keep decision records separate from retros and event-layer notes.

#### Scenario: A later contributor reviews governance history
- **WHEN** the contributor needs to understand both what was decided and what failed before
- **THEN** they SHALL be able to distinguish ADR pages from retro or log pages without inferring the difference from chat history
