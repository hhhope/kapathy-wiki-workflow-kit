# visual-agent-entry-route Specification

## Purpose
TBD - created by archiving change harden-visual-agent-entry-route. Update Purpose after archive.
## Requirements
### Requirement: Visual work SHALL expose visual-agent as the first route

Ordinary visual or drawing requests SHALL visibly enter through `visual-agent`
before routing to worker skills or executor tools.

#### Scenario: Ambiguous drawing request

- **WHEN** the user asks for 制图, 出图, 配图, 一图流, knowledge cards, section
  images, or visual polish
- **AND** the request does not explicitly choose SVG, H5/HTML, image-model, or
  hybrid output
- **THEN** the response SHALL expose `Using visual-agent`
- **AND** it SHALL ask the bounded mode fork or state strong content evidence
  before choosing a mode
- **AND** it SHALL NOT default to H5/HTML or SVG only because those routes are
  deterministic or easy to render

#### Scenario: User names a visual worker directly

- **WHEN** the user names `knowledge-article-visual`, `infographic-onepager`,
  `svg-flow-diagram`, `architecture-diagram`, `imagegen`, or another visual
  worker/executor
- **AND** the request is ordinary visual production rather than debug review of
  that worker
- **THEN** the response SHALL still expose `Using visual-agent`
- **AND** it SHALL describe the named worker as a child route after mode
  confirmation

#### Scenario: Prior H5/SVG dissatisfaction is present

- **WHEN** the user says prior visual output incorrectly became H5, HTML, SVG,
  browser screenshots, or deterministic cards
- **THEN** `visual-agent` SHALL treat image-model or hybrid output as the
  active route pressure until the user explicitly reselects deterministic
  SVG/H5 output

### Requirement: Visual-agent SHALL maintain a child-worker reference map

`visual-agent` SHALL list the child worker route for each supported visual
surface so future agents can load the controller first and then delegate the
narrow execution step.

#### Scenario: Reader-facing visual package

- **WHEN** the output is a reader-facing H5/share/report visual package
- **THEN** the route SHALL preserve `public-report-quality-gate` as the outer
  reader-facing gate
- **AND** the visual-production segment SHALL include `visual-agent` before
  article visual package, per-image script, or bitmap generation work

#### Scenario: Deterministic diagram

- **WHEN** the output is a flow or architecture diagram with strong
  deterministic evidence
- **THEN** the route MAY proceed from `visual-agent` to `svg-flow-diagram` or
  `architecture-diagram`
- **AND** the response SHALL state the evidence for that route

### Requirement: Visual-agent runtime card SHALL remain compact and scan-first

The visual-agent skill body SHALL keep only trigger, mode, route, and hard stop
rules needed at runtime. Detailed rationale, replay history, and proof evidence
SHALL live outside the runtime skill body.

#### Scenario: Agent loads visual-agent for a routine request

- **WHEN** a user asks for a visual deliverable
- **THEN** the agent SHALL be able to identify the mode fork and child route
  from the skill body without reading governance history
- **AND** evaluation evidence SHALL include a compactness check for the runtime
  skill body

### Requirement: Colloquial visual requests SHALL trigger visual-agent

Visual-agent SHALL trigger on the class of formal or colloquial requests to
make, draw, add, polish, convert, or generate a visual artifact, not only on a
fixed list of phrases.

#### Scenario: User uses casual visual wording

- **WHEN** the user says casual visual-deliverable wording such as "弄个图",
  "画一下", "整张图", "做成卡片", "配几张图", or "图像化一下"
- **AND** no output mode is explicit
- **THEN** the response SHALL expose `Using visual-agent`
- **AND** it SHALL ask the SVG / H5-HTML / image-model / hybrid mode fork unless
  strong content evidence selects a mode
- **AND** it SHALL NOT default to H5/HTML or SVG only because those routes are
  easier to render

### Requirement: Visual agent child workers SHALL be discoverable

This repository SHALL publish discoverable ordinary visual child workers for
repo-local `visual-agent` routes unless they are explicitly documented as
runtime/system tools or host-repo gates.

#### Scenario: Runtime loads visual-agent in this repository

- **WHEN** the runtime skill surface includes `.codex/skills/visual-agent`
- **THEN** ordinary visual workers named as bundled child routes SHALL exist
  under `.codex/skills/<worker>/SKILL.md`
- **AND** `imagegen` SHALL remain documented as a runtime/system image tool
- **AND** `public-report-quality-gate` SHALL remain documented as a host-repo
  parent gate rather than a visual worker

#### Scenario: Worker is not installed

- **WHEN** `visual-agent` would route to a worker that is not discoverable in
  the current runtime
- **THEN** the response SHALL keep ownership in `visual-agent`
- **AND** it SHALL mark the worker availability as blocked instead of claiming a
  child-worker route

### Requirement: Visual agent triggers SHALL not rely on fixed colloquial lists

The repo-local visual-agent trigger model SHALL classify visual-deliverable
intent by output role, transformation role, medium-selection role, or visual
repair role rather than relying on a fixed list of colloquial phrases.

#### Scenario: Casual visual wording appears

- **WHEN** the user uses casual or incomplete wording
- **AND** the intended deliverable is visual
- **THEN** `visual-agent` SHALL trigger from visual-deliverable intent
- **AND** it SHALL NOT require a fixed keyword to match

