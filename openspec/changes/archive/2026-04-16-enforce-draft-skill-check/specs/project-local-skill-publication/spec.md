## MODIFIED Requirements

### Requirement: Repository SHALL publish project-local skills only from `.codex/skills/`

When the repository claims that a project-local skill is available for future sessions, that skill SHALL exist under `.codex/skills/` rather than only under draft guidance paths.

#### Scenario: Workflow guidance exists only in draft form
- **WHEN** a workflow is documented only under `skills-drafts/`
- **THEN** the repository SHALL treat it as draft or staging content
- **AND** it SHALL NOT treat that content as a formally published project-local skill

#### Scenario: Draft skill remains after formal publication
- **WHEN** a formally published project-local skill exists under `.codex/skills/`
- **THEN** the corresponding workflow SHALL NOT continue to keep an active `SKILL.md` under `skills-drafts/`
- **AND** repository verification SHALL include an executable check that fails if such a draft `SKILL.md` exists
