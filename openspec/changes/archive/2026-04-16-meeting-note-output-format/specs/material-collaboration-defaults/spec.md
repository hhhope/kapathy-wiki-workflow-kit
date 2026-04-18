## MODIFIED Requirements

### Requirement: Material processing defaults to readable source output
When the repository receives new meeting notes, transcripts, reports, attachments, or exported source files, the system SHALL treat processing as incomplete until it has created or updated a readable `source` record rather than stopping at placeholder-only intake output.

#### Scenario: Meeting note is dropped for processing
- **WHEN** a user provides a meeting note or transcript and asks Codex to process it
- **THEN** the repository SHALL create or update a `source` page with a Chinese summary of the material
- **AND** for meeting-note outputs the page SHALL follow the repository's fixed meeting-note section structure rather than a generic summary-only layout

#### Scenario: Attachment or exported file is dropped for processing
- **WHEN** a user provides a weekly report, attachment, spreadsheet, or exported source file and asks Codex to process it
- **THEN** the repository SHALL create or update a `source` page that preserves source lineage
- **AND** the page SHALL contain a readable summary instead of unresolved placeholder text as the default completion bar
