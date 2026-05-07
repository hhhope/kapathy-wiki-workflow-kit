## MODIFIED Requirements

### Requirement: Repository SHALL provide a README learning skill

The repository SHALL provide a repo-local skill for GitHub/GitLab repository or
README learning requests that ask what should be reused, adapted, rejected, or
formalized locally.

#### Scenario: User asks to learn from a repository or README

- **WHEN** the user provides a GitHub/GitLab repository or README and asks to
  learn, compare approaches, extract reusable structure, score value, or decide
  what should be copied, adapted, rejected, or formalized
- **THEN** the system SHALL route the task through the repo/README learning
  module

### Requirement: Repo/README learning SHALL score before deep reading

Repo/README learning SHALL triage repository learning value before investing in
deep reading.

#### Scenario: Repo or README passes deep-reading threshold

- **WHEN** repo/README learning passes admission and scores 75 or higher
- **THEN** it MAY proceed to deep reading and durable wiki notes

#### Scenario: Repo or README is a brief candidate

- **WHEN** repo/README learning scores from 60 through 74
- **THEN** it SHALL remain a brief candidate note by default

#### Scenario: Repo or README is below candidate threshold

- **WHEN** repo/README learning scores below 60
- **THEN** it SHALL record source and skip reason only

### Requirement: Repo/README learning SHALL preserve adaptation boundary

Repo/README learning SHALL not stop at source summary or copy external
structure without local fit.

#### Scenario: Repo learning is extracted

- **WHEN** repo/README learning extracts a point for local use
- **THEN** it SHALL preserve source, reused, modified, rejected or not yet
  formalized, repo target, adoption boundary, and status
