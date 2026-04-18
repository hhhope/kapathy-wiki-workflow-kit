## ADDED Requirements

### Requirement: Repository SHALL require explicit local pressure tests for semantic skill changes

When a semantic skill change requires `evaluation.md`, the evaluation SHALL include explicit local pressure-test evidence rather than only a descriptive before/after summary.

#### Scenario: Skill change includes evaluation evidence
- **WHEN** a semantic change touches `.codex/skills/*`
- **THEN** the evaluation SHALL include `Pressure Scenarios`
- **AND** the evaluation SHALL include `RED Baseline`
- **AND** the evaluation SHALL include `GREEN Result`
- **AND** the evaluation SHALL include `Residual Risks`

### Requirement: Repository SHALL not require multi-end rollout proof as the minimum skill gate

The minimum gate for semantic skill changes SHALL be local pressure testing, even if broader rollout proof is deferred.

#### Scenario: Change author cannot run multi-end validation
- **WHEN** the author can run local pressure scenarios but not broader rollout or multi-end tests
- **THEN** the local pressure-test evidence SHALL still count as the minimum completion gate
- **AND** any missing broader proof SHALL be recorded in residual risks
