## ADDED Requirements

### Requirement: Skill-touching active changes SHALL include behavior-proof evaluation evidence

When an active change publishes or semantically edits project-local skills through `.codex/skills/`, the change SHALL include a dedicated `evaluation.md` artifact for behavior-proof evidence.

#### Scenario: Active change references formal skill publication
- **WHEN** an active change artifact references `.codex/skills/`
- **THEN** the change SHALL include `evaluation.md` in its own directory
- **AND** that file SHALL include baseline scenarios, before results, after results, and residual risks

### Requirement: Repository health-check SHALL fail when required skill evaluation evidence is missing

The repository SHALL expose missing skill behavior-proof evidence as a failing health-check result.

#### Scenario: Skill-touching change lacks evaluation evidence
- **WHEN** an active change references `.codex/skills/` but does not include a valid `evaluation.md`
- **THEN** the repo health-check SHALL report a failing `skill-evaluation-evidence` result
- **AND** it SHALL identify the offending change directory
