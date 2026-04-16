## ADDED Requirements

### Requirement: External sources SHALL be represented as local source pages
The system SHALL represent each tracked external report source as a local source page that records enough metadata to support discovery and reuse even when the full source body is not mirrored.

#### Scenario: Feishu source is recorded locally
- **WHEN** a Feishu document is selected as report evidence
- **THEN** the wiki SHALL provide a source page that records its link, summary context, ownership hint, status, and related knowledge targets

### Requirement: Source pages SHALL preserve evidence lineage
Source pages SHALL capture where the evidence came from and which report or topic pages depend on it.

#### Scenario: User traces a report claim back to evidence
- **WHEN** a report draft references a source-backed statement
- **THEN** the linked source page SHALL identify the external source reference and the related wiki pages that reuse it

### Requirement: Source ingestion SHALL degrade gracefully before automation exists
The source model SHALL remain usable when ingestion is manual and SHALL not depend on a live sync process to create valid source records.

#### Scenario: Manual ingestion produces a valid source page
- **WHEN** a contributor adds a source page without any automation
- **THEN** the page SHALL still conform to the source template and participate in wiki navigation
