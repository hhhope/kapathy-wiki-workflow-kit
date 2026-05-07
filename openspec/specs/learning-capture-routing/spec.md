# learning-capture-routing Specification

## Purpose
TBD - created by archiving change consolidate-learning-capture-routing. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL provide a learning capture domain router

The repository SHALL provide a repo-local skill that routes external-source
learning requests before material-specific learning workflows run.

#### Scenario: User asks to learn from an external source

- **WHEN** the user provides an external article, blog, paper, WeChat post,
  GitHub/GitLab repository, README, or concrete example and asks to learn,
  deep-read, score, write to wiki, extract useful practices, decide what to
  reuse, adapt, reject, or turn into an SOP
- **THEN** the system SHALL route the task through the learning capture domain
  router

#### Scenario: User provides a source inside an active learning thread

- **WHEN** the user provides an external article, blog, paper, WeChat post,
  GitHub/GitLab repository, README, or concrete example inside an active
  learning, governance, reusable-method, or method-calibration thread
- **THEN** the system SHALL treat the source as learning material even if the
  user does not repeat an explicit phrase such as "learn this"

#### Scenario: Runtime trigger is advertised in repo entrypoint

- **WHEN** repo `AGENTS.md` lists high-frequency runtime skill routes
- **THEN** it SHALL include the learning capture domain router for external
  source learning, reference, or adaptation material
- **AND** output routing SHALL remain a separate destination rule, not a
  substitute for the runtime trigger

### Requirement: Learning capture SHALL reject non-learning requests

The learning router SHALL not turn every external source into durable learning.

#### Scenario: User asks for a non-learning result

- **WHEN** the user asks for fact lookup, latest news, raw source fetching, a
  short abstract, or one-off digestion with no local reuse or wiki intent
- **THEN** the system SHALL avoid learning capture and use the narrower
  task-specific path

#### Scenario: User provides a bare source with no learning context

- **WHEN** the user provides a bare external source without an active learning
  thread, local reuse context, wiki intent, or method-calibration context
- **THEN** the system SHALL NOT assume durable learning capture by default

### Requirement: Learning capture SHALL route by evidence object

Learning capture SHALL separate user intent from the evidence object being
learned from.

#### Scenario: Article-shaped source is provided

- **WHEN** the learning source is an article, blog, paper, WeChat post, or
  article collection
- **THEN** the system SHALL route to the article learning module

#### Scenario: Repo-shaped source is provided

- **WHEN** the learning source is a GitHub/GitLab repository or README
- **THEN** the system SHALL route to the repo-readme learning module

#### Scenario: Example-shaped source is provided

- **WHEN** the learning source is primarily a writing, visual, output-shape,
  structure, or method example
- **THEN** the system SHALL route to the example-reference module

#### Scenario: Batch source intake is provided

- **WHEN** the user provides many external sources in one learning thread
- **THEN** the system SHALL triage and score before deep-reading individual
  sources

### Requirement: Learning capture SHALL preserve existing module gates

The domain router SHALL not weaken stricter module-specific evidence gates.

#### Scenario: Learning capture delegates to a module

- **WHEN** a module is selected by the learning router
- **THEN** the selected module SHALL preserve its existing source grounding,
  adaptation boundary, scoring, or promotion evidence requirements

### Requirement: Learning capture SHALL preserve topic anchoring boundaries

Learning capture SHALL distinguish explicit topic anchoring from weak semantic
association.

#### Scenario: User provides an explicit learning topic

- **WHEN** the user names a topic such as agent, harness, eval, README structure,
  or another existing wiki subject
- **THEN** the system SHALL check existing wiki topic anchors before creating a
  new durable learning page

#### Scenario: Topic is unclear or weakly matched

- **WHEN** no explicit topic or strong filename/title/index match exists
- **THEN** the system SHALL keep the source as a candidate for weekly review
- **AND** it SHALL NOT force a semantic link to an existing topic

### Requirement: Learning capture SHALL not promote unsupported learning

External-source learning SHALL remain candidate material until promotion
evidence exists.

#### Scenario: Learning takeaway is proposed as a behavior asset

- **WHEN** a learning takeaway is proposed for repo `AGENTS.md`, root
  `AGENTS.md`, OpenSpec `SHALL`, skill hard rules, or archive-ready claims
- **THEN** the promotion SHALL pass the repository evidence-backed gate or enter
  a scoped OpenSpec change

