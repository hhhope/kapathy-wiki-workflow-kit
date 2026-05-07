# principle-skills-layer Specification

## Purpose
TBD - created by archiving change add-principle-skills-layer. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose a compact principle-skills layer for high-frequency agent mistakes

When the repository needs reusable guidance for cross-workflow agent mistakes, it SHALL provide a compact principle-skills layer separate from scene-specific workflow skills.

#### Scenario: Contributor looks for high-frequency behavior guidance
- **WHEN** a contributor needs guidance for common mistakes such as assuming,
  overbuilding, making adjacent edits, or claiming completion without checks
- **THEN** the repository SHALL provide a short principle layer
- **AND** that layer SHALL remain distinct from workflow-specific skills
- **AND** each principle-skill row exposed through repo guidance SHALL declare
  whether the skill is `repo-owned`, `root-candidate`, `root-owned-reference`,
  or `shared`

### Requirement: Repository SHALL publish the first principle-skills set through `.codex/skills/`

The repository SHALL formally publish the first principle-skills set through the same formal local-skill path used for workflow skills.

#### Scenario: Principle layer is published
- **WHEN** the repository publishes the principle-skills layer
- **THEN** it SHALL publish `clarify-before-acting`, `simplicity-first`,
  `surgical-changes`, and `verify-before-claiming` under `.codex/skills/`
- **AND** repo guidance SHALL point to the principle layer without replacing
  workflow routing
- **AND** publishing under repo `.codex/skills/` SHALL NOT by itself mean the
  behavior is repo-owned

