## ADDED Requirements

### Requirement: System SHALL provide a repo-local skill for weekly project-management handling
The repository SHALL provide a local skill that standardizes how weekly project-management requests are handled.

#### Scenario: User asks about project management
- **WHEN** the user asks for project-management handling, weekly progress organization, milestone drift review, or similar weekly PM work
- **THEN** the repository SHALL contain a skill that defines the trigger conditions and required output types

### Requirement: Skill SHALL define a fixed output contract
The skill SHALL require the agent to determine and produce the relevant weekly PM output types from the repository workflow.

#### Scenario: Agent handles weekly PM input
- **WHEN** weekly PM input is provided
- **THEN** the skill SHALL direct the agent to decide among source, html/source companion, intake, reminder, and Codex handoff candidate outputs
