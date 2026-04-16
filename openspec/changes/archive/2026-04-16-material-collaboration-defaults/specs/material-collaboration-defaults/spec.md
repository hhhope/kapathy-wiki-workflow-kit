## ADDED Requirements

### Requirement: Material processing defaults to readable source output
When the repository receives new meeting notes, transcripts, reports, attachments, or exported source files, the system SHALL treat processing as incomplete until it has created or updated a readable `source` record rather than stopping at placeholder-only intake output.

#### Scenario: Meeting note is dropped for processing
- **WHEN** a user provides a meeting note or transcript and asks Codex to process it
- **THEN** the repository SHALL create or update a `source` page with a Chinese summary of the material
- **AND** the `source` page SHALL extract key conclusions, risks, or follow-up items when those are present in the material

#### Scenario: Attachment or exported file is dropped for processing
- **WHEN** a user provides a weekly report, attachment, spreadsheet, or exported source file and asks Codex to process it
- **THEN** the repository SHALL create or update a `source` page that preserves source lineage
- **AND** the page SHALL contain a readable summary instead of unresolved placeholder text as the default completion bar

### Requirement: Material processing continues into ops when action signals exist
The system SHALL continue from `source` into `intake` or `reminder` output when the material already contains concrete actions, owners, deadlines, blockers, or other operational follow-up signals.

#### Scenario: Material contains follow-up actions
- **WHEN** a processed material includes explicit next steps, owners, deadlines, or blockers
- **THEN** the repository SHALL create or update an `intake` record linked to the source
- **AND** the repository SHALL add reminder-oriented output when the follow-up signal is strong enough to require tracking

#### Scenario: Material is evidence only
- **WHEN** a processed material does not contain actionable operational follow-up
- **THEN** the repository SHALL stop at `source` output unless the user explicitly requests another layer

### Requirement: Material processing is incremental by default
The system SHALL use source lineage to distinguish previously processed materials from new materials and SHALL prefer incremental update or skip behavior over full reruns.

#### Scenario: Material was already processed
- **WHEN** a material matches an existing record by source lineage such as `source_path`
- **THEN** the repository SHALL update the existing record or skip regeneration based on completeness
- **AND** it SHALL NOT regenerate unrelated materials as part of the same processing run

#### Scenario: New material is richer than an earlier draft
- **WHEN** a later material provides richer context than an existing low-quality or placeholder draft
- **THEN** the repository SHALL update the existing record with the stronger summary and extracted conclusions

### Requirement: Clarification is limited to material output fork-points
The system SHALL avoid re-confirming the full workflow for ordinary material processing and SHALL ask the user only when a real output fork-point materially changes the scope or cost of the work.

#### Scenario: Visual artifact branch is ambiguous
- **WHEN** the material includes `html`, `h5`, or `preview` files and the request does not clearly state whether the visual file itself should be changed
- **THEN** the system SHALL ask whether to sync only wiki conclusions or also update the visual artifact

#### Scenario: Ordinary source summarization path is clear
- **WHEN** the user provides source materials and asks Codex to process them without additional branching constraints
- **THEN** the system SHALL proceed with source summarization and linked ops extraction without asking for the base workflow again
