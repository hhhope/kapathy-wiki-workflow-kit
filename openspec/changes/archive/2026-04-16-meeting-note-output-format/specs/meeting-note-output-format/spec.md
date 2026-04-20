## ADDED Requirements

### Requirement: Meeting-note output SHALL use a fixed delivery structure
When the repository turns meeting material into a meeting-note output, the resulting note SHALL follow a fixed section structure rather than a generic summary-only format.

#### Scenario: Meeting note is generated from note material
- **WHEN** a meeting note is produced from note text, transcript, or combined material
- **THEN** the output SHALL include meeting metadata, core agenda, structured body sections, action items, and a closing summary

#### Scenario: Meeting note is used as an external deliverable
- **WHEN** the meeting-note output is synced to Feishu or another reader-facing document
- **THEN** the output SHALL remain directly readable without requiring the companion transcript page for basic understanding

### Requirement: Meeting-note output SHALL distinguish final decisions from rejected options
The meeting-note output SHALL explicitly show the selected path and any important options that were discussed but rejected.

#### Scenario: Multiple solution paths were discussed
- **WHEN** a meeting covered competing方案 or implementation paths
- **THEN** the note SHALL state the final selected approach
- **AND** it SHALL identify important rejected options and why they were rejected

### Requirement: Meeting-note output SHALL include a structured action-item block
The note SHALL capture follow-up work in a structured format that can be lifted into ops tracking without re-reading the entire narrative.

#### Scenario: Meeting contains concrete follow-up items
- **WHEN** owners, deadlines, or follow-up tasks are present in the meeting material
- **THEN** the note SHALL include a structured action-item section with content, owner, and time expectation when available

### Requirement: Transcript SHALL remain a supporting artifact
When both note text and transcript exist, the meeting note SHALL remain the main deliverable and the transcript SHALL remain supplementary evidence.

#### Scenario: Note text and transcript are both available
- **WHEN** the repository has both a meeting note source and a transcript source
- **THEN** the meeting note SHALL focus on decisions, risks, and actions
- **AND** the transcript SHALL focus on disputes, rationale, and raw discussion signals
