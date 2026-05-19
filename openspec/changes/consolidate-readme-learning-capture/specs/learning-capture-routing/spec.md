## MODIFIED Requirements

### Requirement: Learning capture SHALL route by evidence object

Learning capture SHALL separate user intent from the evidence object being
learned from.

#### Scenario: Article-shaped source is provided

- **WHEN** the learning source is an article, blog, paper, WeChat post, or
  article collection
- **THEN** the system SHALL route to the article learning module

#### Scenario: Repo-shaped source is provided

- **WHEN** the learning source is a GitHub/GitLab repository or README
- **THEN** the system SHALL route to the repo-readme learning module inside
  `learning-capture`
- **AND** the system SHALL NOT load a separate active
  `readme-learning-capture` skill as the runtime entry

#### Scenario: Example-shaped source is provided

- **WHEN** the learning source is primarily a writing, visual, output-shape,
  structure, or method example
- **THEN** the system SHALL route to the example-reference module

#### Scenario: Batch source intake is provided

- **WHEN** the user provides many external sources in one learning thread
- **THEN** the system SHALL triage and score before deep-reading individual
  sources
