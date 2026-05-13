## Purpose

Define repo-local Agent Intent Routing so agent actions enter the correct parent
gate before editing repo-public or reader-facing artifacts.

## Requirements

### Requirement: Repository SHALL classify agent intent before acting

The repository SHALL require agents to classify user intent before executing
tasks that may write, rewrite, polish, prepare, or update artifacts.

#### Scenario: Request changes an artifact read outside the current chat

- **WHEN** a user request writes or changes an artifact that will be read
  outside the current chat or worklog
- **THEN** the agent SHALL route through the applicable parent gate before
  editing
- **AND** the agent SHALL preserve specialized gates for frontmatter, skill
  authoring, OpenSpec lifecycle, and learning capture

### Requirement: Repo-public artifacts SHALL route through public gate lightweight path

The repository SHALL route repo-public artifacts through the lightweight path of
`public-report-quality-gate`.

#### Scenario: User asks to write README

- **WHEN** the user asks to write, rewrite, polish, or update `README.md`
- **THEN** the agent SHALL classify the request as a repo-public artifact
- **AND** the agent SHALL route through `public-report-quality-gate`
  lightweight path before editing
- **AND** the agent SHALL scan artifact-specific README constraints before
  drafting

#### Scenario: User asks for a small repo-public documentation edit

- **WHEN** the user asks for a small edit to `README.md`, `docs/*`,
  `examples/*`, or a published template
- **THEN** the agent SHALL identify reader and job-to-be-done
- **AND** the agent SHALL scan relevant artifact-specific constraints
- **AND** the agent SHALL NOT require a `wiki/ops/*-report-gate-review.md`
  artifact unless the output is review-ready, published, synced, complex,
  reference-shaped, or drift-corrected

### Requirement: Agent intent routing SHALL not steal specialized gates

Agent Intent Routing SHALL select the correct parent gate without weakening
existing specialized workflow gates.

#### Scenario: External README is used as learning input

- **WHEN** the user provides an external GitHub or GitLab README and asks what
  can be reused, learned, or adapted
- **THEN** the agent SHALL route to `learning-capture` and the README learning
  module
- **AND** it SHALL NOT treat the source-learning step as a repo-public artifact
  edit

#### Scenario: Wiki frontmatter is edited

- **WHEN** the user asks to create or modify wiki frontmatter
- **THEN** the agent SHALL route to the wiki frontmatter taxonomy gate
- **AND** the public gate SHALL NOT replace the taxonomy checker requirement

#### Scenario: Internal wiki ops page becomes a Feishu article

- **WHEN** the user asks to turn an internal `wiki/ops` page into a Feishu
  article, H5, share draft, or reader-facing report
- **THEN** the agent SHALL route through the full public report gate
- **AND** it SHALL NOT use the lightweight repo-public path as a substitute for
  publish, sync, visual, source, or judgment gates

### Requirement: Agent intent routing SHALL include behavior replay evidence

Changes to agent intent routing SHALL include repo-visible replay evidence.

#### Scenario: Runtime route changes

- **WHEN** the repository adds or changes Agent Intent Routing behavior
- **THEN** the change SHALL include RED baseline, GREEN result, pressure
  scenarios, repo-visible trigger artifacts, and residual risk
- **AND** the evidence SHALL state the proof boundary
