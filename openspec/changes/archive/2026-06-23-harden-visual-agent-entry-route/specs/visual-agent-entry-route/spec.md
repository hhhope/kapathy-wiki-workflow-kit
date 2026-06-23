# visual-agent-entry-route Specification

## ADDED Requirements

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
