## MODIFIED Requirements

### Requirement: AI material ingestion follows a staged workflow
The repository SHALL separate AI-assisted material handling into distinct stages so that source evidence, summaries, linked records, and drafts remain traceable and reviewable.

#### Scenario: New material enters the repository
- **WHEN** files are added under `inbox/` or otherwise handed to Codex as new source material
- **THEN** the workflow SHALL first register source lineage and classify the material
- **AND** it SHALL then apply the collaboration-defaults stage before the work is considered complete

#### Scenario: Collaboration defaults stage runs
- **WHEN** Codex is asked to process newly arrived materials without an explicitly narrowed workflow
- **THEN** the workflow SHALL require readable source summarization as the default completion bar
- **AND** it SHALL continue into linked ops extraction when the material includes operational follow-up signals
- **AND** it SHALL reserve clarification for output fork-points such as whether a visual artifact itself must be updated

#### Scenario: Material is revisited later
- **WHEN** Codex processes a material that has already been represented in the repository
- **THEN** the workflow SHALL prefer incremental update or skip behavior based on source lineage and completeness
- **AND** it SHALL avoid full reruns of unrelated materials
