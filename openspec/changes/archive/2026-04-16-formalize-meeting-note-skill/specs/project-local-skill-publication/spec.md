## ADDED Requirements

### Requirement: Repository SHALL publish project-local skills only from `.codex/skills/`

When the repository claims that a project-local skill is available for future sessions, that skill SHALL exist under `.codex/skills/` rather than only under draft guidance paths.

#### Scenario: Workflow guidance exists only in draft form
- **WHEN** a workflow is documented only under `skills-drafts/`
- **THEN** the repository SHALL treat it as draft or staging content
- **AND** it SHALL NOT treat that content as a formally published project-local skill

#### Scenario: Project-local skill is formally published
- **WHEN** a project-local skill is intended to be available as a real local skill
- **THEN** the repository SHALL provide it under `.codex/skills/<skill-name>/SKILL.md`

### Requirement: Repository SHALL distinguish skills from manual agent role templates

The repository SHALL keep a clear boundary between project-local skills and manual agent role templates so workflow routing does not depend on the wrong mechanism.

#### Scenario: Contributor evaluates a repo-default workflow mechanism
- **WHEN** a contributor decides how to make a repo-default workflow reusable
- **THEN** project-local reusable workflow routing SHALL use the local skill mechanism
- **AND** manual agent role templates SHALL be treated as explicit role assets rather than automatic workflow publication
