## REMOVED Requirements

### Requirement: Repository SHALL provide a dedicated skill for GitHub and GitLab README learning

The repository SHALL provide a dedicated repo-local skill for requests that use GitHub or GitLab repos or READMEs as learning inputs for repository workflow, skill, or template adaptation.

#### Scenario: User asks to learn from a GitHub or GitLab README

- **WHEN** the user provides a GitHub or GitLab repo or README and asks what is reusable, worth learning, or worth adapting
- **THEN** the system SHALL route the task through the dedicated README learning skill

## ADDED Requirements

### Requirement: Repo/README learning SHALL live under learning-capture

The repository SHALL expose repo/README learning through the `learning-capture`
runtime skill and its repo-readme module instead of a separate active README
learning skill.

#### Scenario: User asks to learn from a GitHub or GitLab README

- **WHEN** the user provides a GitHub or GitLab repo or README and asks what is
  reusable, worth learning, or worth adapting
- **THEN** the system SHALL route the task through `learning-capture`
- **AND** it SHALL use the repo-readme module for admission, score-first
  triage, adaptation boundaries, and output routing
- **AND** it SHALL NOT require or expose a dedicated active
  `readme-learning-capture` skill surface.
