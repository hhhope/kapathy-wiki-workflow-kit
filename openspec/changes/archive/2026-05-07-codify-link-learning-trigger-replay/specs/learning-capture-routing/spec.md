## MODIFIED Requirements

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
- **AND** the system SHALL run the appropriate source-kind route before any
  durable wiki capture or promotion decision

#### Scenario: Runtime trigger is advertised in repo entrypoint

- **WHEN** repo `AGENTS.md` lists high-frequency runtime skill routes
- **THEN** it SHALL include the learning capture domain router for external
  source learning, reference, or adaptation material
- **AND** output routing SHALL remain a separate destination rule, not a
  substitute for the runtime trigger

## ADDED Requirements

### Requirement: Learning capture SHALL preserve link-trigger replay behavior

Learning capture SHALL make the expected behavior for the next provided link
replayable from repository artifacts rather than chat memory.

#### Scenario: Bare article link is provided inside a learning or governance thread

- **WHEN** the user provides a bare article, blog, paper, newsletter, or similar
  article link inside an active learning, governance, reusable-method, or
  method-calibration thread
- **THEN** the system SHALL route through `learning-capture`
- **AND** it SHALL classify the source as article-shaped before deep reading
- **AND** it SHALL run admission and score gates before durable wiki notes

#### Scenario: WeChat link is provided inside a learning or governance thread

- **WHEN** the user provides an `mp.weixin.qq.com` link inside an active
  learning, governance, reusable-method, or method-calibration thread
- **THEN** the system SHALL use the WeChat reader or an equivalent
  source-grounding path before scoring
- **AND** it SHALL preserve source metadata, access status, source class,
  grounding, score, local usefulness, and adoption boundary

#### Scenario: Repository link is provided as learning material

- **WHEN** the user provides a GitHub or GitLab repository or README link and
  asks what to learn, reuse, adapt, reject, or formalize
- **THEN** the system SHALL route through the repo/README learning module
- **AND** it SHALL score before deep reading the repository

#### Scenario: Link is only a raw fetch or lookup request

- **WHEN** the user asks only for raw article body extraction, fact lookup,
  latest-news context, or a short abstract with no local reuse or wiki intent
- **THEN** the system SHALL avoid learning capture by default
- **AND** it SHALL use the narrower task-specific path

#### Scenario: Bare link has no local reuse context

- **WHEN** the user provides a bare external source without active learning
  context, local reuse context, wiki intent, or method-calibration context
- **THEN** the system SHALL NOT create durable wiki notes by default
- **AND** it SHALL clarify intent or handle the source as an ordinary lookup or
  fetch request

#### Scenario: Learning link qualifies for durable capture

- **WHEN** the selected module's admission gate passes and the source reaches
  the durable deep-read threshold
- **THEN** the system SHALL update or create the lowest correct wiki artifact
- **AND** the response SHALL state the score, route, wiki target, and adoption
  boundary

#### Scenario: Learning link does not qualify for durable capture

- **WHEN** the source is low scoring, weakly anchored, inaccessible, or only
  generally interesting
- **THEN** the system SHALL record a skip reason or candidate status
- **AND** it SHALL NOT force durable topic linkage

#### Scenario: Learning takeaway is proposed for promotion

- **WHEN** a takeaway from a link replay is proposed for repo `AGENTS.md`, root
  `AGENTS.md`, OpenSpec `SHALL`, skill hard rules, or archive-ready claims
- **THEN** the system SHALL require the repository evidence-backed promotion
  gate or a scoped OpenSpec change
