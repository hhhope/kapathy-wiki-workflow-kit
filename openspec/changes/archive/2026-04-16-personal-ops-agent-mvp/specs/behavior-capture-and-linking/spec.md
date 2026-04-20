## ADDED Requirements

### Requirement: System SHALL capture personal operational inputs as intake records
The system SHALL support durable intake records for personal behaviors, files, notes, and events so new activity can enter the wiki in a structured form.

#### Scenario: New personal input is captured
- **WHEN** a new note, file, reminder source, or activity record enters the system
- **THEN** the system SHALL create or update an intake record with source path, type, audience, confidence, and related context

### Requirement: System SHALL relate captured inputs to existing operational context
The system SHALL link new intake records to relevant source pages, focus threads, and pending items when enough evidence exists.

#### Scenario: Captured input matches ongoing work
- **WHEN** an intake record aligns with an existing topic, source, or unresolved task
- **THEN** the system SHALL record the suggested relationship and preserve its confidence level

### Requirement: System SHALL preserve uncertain intake without pretending certainty
The system SHALL keep low-confidence intake records usable without forcing strong classification or hidden assumptions.

#### Scenario: Intake confidence is low
- **WHEN** the system cannot reliably determine the correct destination or relation for a captured input
- **THEN** the system SHALL still store the intake record and mark review-needed fields explicitly
