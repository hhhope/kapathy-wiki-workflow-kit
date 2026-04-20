## ADDED Requirements

### Requirement: System SHALL preserve a weekly PM source record
When weekly project-management material is ingested for Nirvana, the system SHALL create a source page that keeps the original file lineage and a Chinese summary of the weekly content.

#### Scenario: Weekly report is placed in inbox
- **WHEN** the Nirvana weekly report is provided through `inbox/nirvana/`
- **THEN** the repository SHALL create a source page that points back to the inbox file and summarizes the weekly PM facts

### Requirement: System SHALL create ops records from weekly PM material
The repository SHALL create an intake page and a reminder page from the same weekly PM material so that the weekly loop produces actionable follow-up structure.

#### Scenario: Weekly PM material is processed
- **WHEN** the agent processes the Nirvana weekly report
- **THEN** it SHALL produce an intake summary and a reminder record with next actions and current risks
