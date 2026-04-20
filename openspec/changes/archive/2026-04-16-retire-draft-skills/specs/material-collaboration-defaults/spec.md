## MODIFIED Requirements

### Requirement: Material processing SHALL default to readable source outputs before stopping

When the user drops material into the repository and expects Codex to process it, the default completion bar SHALL include readable source output rather than placeholder-only intake.

#### Scenario: New materials are processed by default
- **WHEN** the repository receives meeting notes, transcripts, weekly materials, attachments, exported files, or preview-related source files
- **THEN** Codex SHALL create or update a readable `source` output with summary-level conclusions
- **AND** it SHALL continue into linked `ops` output when the material already carries action signals

#### Scenario: Material-processing workflow is published for future sessions
- **WHEN** the repository expects future sessions to reuse the material-processing defaults workflow
- **THEN** that workflow SHALL be formally published as a local skill under `.codex/skills/`
- **AND** draft-only guidance under `skills-drafts/` SHALL NOT be treated as sufficient publication
