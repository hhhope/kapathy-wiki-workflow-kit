## ADDED Requirements

### Requirement: System SHALL distinguish Codex-ready engineering tasks from general todos
The system SHALL support a separate record for development-oriented tasks that are ready to be handed off to Codex.

#### Scenario: Todo becomes an engineering handoff
- **WHEN** a pending item is identified as a development task with enough implementation context
- **THEN** the system SHALL allow it to be represented as a Codex handoff record instead of a generic reminder

### Requirement: Codex handoff SHALL preserve execution context
The system SHALL capture enough context for a Codex handoff record to be actionable.

#### Scenario: Codex handoff includes context
- **WHEN** a Codex handoff record is created
- **THEN** the record SHALL include objective, related links, current status, and an acceptance hint for the receiving execution flow

### Requirement: Codex handoff SHALL support collaboration tracking
The system SHALL preserve the collaboration state of a handed-off engineering task.

#### Scenario: User checks a dispatched task
- **WHEN** a Codex handoff has been created for an engineering item
- **THEN** the system SHALL allow the record to show whether it is draft, ready, dispatched, or completed
