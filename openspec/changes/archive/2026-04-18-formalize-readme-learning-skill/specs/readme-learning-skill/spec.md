## ADDED Requirements

### Requirement: Repository SHALL provide a dedicated skill for GitHub and GitLab README learning

The repository SHALL provide a dedicated repo-local skill for requests that use GitHub or GitLab repos or READMEs as learning inputs for repository workflow, skill, or template adaptation.

#### Scenario: User asks to learn from a GitHub or GitLab README

- **WHEN** the user provides a GitHub or GitLab repo or README and asks what is reusable, worth learning, or worth adapting
- **THEN** the system SHALL route the task through the dedicated README learning skill

### Requirement: README learning SHALL preserve adaptation boundaries

The README learning workflow SHALL preserve the difference between the source and the repository rather than stopping at generic source summary.

#### Scenario: README learning result is produced

- **WHEN** the repository produces a durable result from GitHub or GitLab README learning
- **THEN** that result SHALL preserve at least:
  - source
  - what was reused
  - what was modified
  - what was rejected or not yet formalized
  - repo target

### Requirement: README learning SHALL reuse existing repository routing layers

The dedicated README learning skill SHALL route outputs into existing repository layers instead of inventing a separate storage model.

#### Scenario: README learning affects current repo workflow

- **WHEN** the README learning primarily affects workflow, governance, or operating behavior
- **THEN** the repository SHALL prefer `wiki/ops`

#### Scenario: README learning becomes a reusable output example

- **WHEN** the learning is primarily a validated output-shape example
- **THEN** the repository SHALL prefer `wiki/examples`

#### Scenario: README learning becomes a scoped repository change

- **WHEN** the learning becomes a repository-default workflow or implementation change
- **THEN** the repository SHALL route it into an `OpenSpec change`
