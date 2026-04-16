## ADDED Requirements

### Requirement: Repository SHALL expose a single health-check entry point for executable policy checks

When the repository has executable workflow-policy checks, it SHALL provide a stable repo-level entry point that runs them and reports named results.

#### Scenario: Repository health check runs on a clean repo
- **WHEN** the repo health-check entry runs against a repository with no policy violations
- **THEN** it SHALL report each included check as passing
- **AND** it SHALL exit successfully

#### Scenario: Repository health check finds a draft-skill violation
- **WHEN** the repo health-check entry runs against a repository containing `skills-drafts/**/SKILL.md`
- **THEN** it SHALL report the draft-skill policy check as failed
- **AND** it SHALL include the violating path in the output
- **AND** it SHALL exit with failure
