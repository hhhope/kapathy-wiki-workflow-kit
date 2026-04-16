## MODIFIED Requirements

### Requirement: Meeting-note output SHALL use a fixed delivery structure
When the repository turns meeting material into a meeting-note output, the resulting note SHALL follow a fixed section structure rather than a generic summary-only format.

#### Scenario: Meeting note is generated from note material
- **WHEN** a meeting note is produced from note text, transcript, or combined material
- **THEN** the output SHALL include meeting metadata, core agenda, structured body sections, action items, and a closing summary

#### Scenario: Meeting note workflow is published for future sessions
- **WHEN** the repository expects future sessions to follow the meeting-note workflow as a reusable local capability
- **THEN** the meeting-note workflow SHALL be formally published as a local skill under `.codex/skills/`
- **AND** draft-only guidance under `skills-drafts/` SHALL NOT be treated as sufficient publication

#### Scenario: Meeting note is used as an external deliverable
- **WHEN** the meeting-note output is synced to Feishu or another reader-facing document
- **THEN** the output SHALL remain directly readable without requiring the companion transcript page for basic understanding
