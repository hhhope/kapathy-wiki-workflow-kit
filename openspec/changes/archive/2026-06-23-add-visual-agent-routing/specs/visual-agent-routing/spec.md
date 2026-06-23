# visual-agent-routing Specification

## ADDED Requirements

### Requirement: Visual requests SHALL route through visual-agent

Ordinary non-debug user requests for drawing, visual production, visual routing, H5 visual pages, SVG diagrams, image-model output, or ambiguous visual mode selection SHALL use `visual-agent` as the user-facing controller.

#### Scenario: User asks for visual routing

- **WHEN** the user asks whether to use SVG, H5, image model, or another visual
  mode
- **THEN** the controller SHALL classify the content shape
- **AND** present or apply a mode route before production starts

#### Scenario: User names a worker directly

- **GIVEN** the user names an implementation worker such as
  `svg-flow-diagram`, `architecture-diagram`, `knowledge-article-visual`, or
  `infographic-onepager`
- **WHEN** the request is ordinary visual work rather than debug behavior
- **THEN** the controller SHALL confirm whether the named worker matches the
  content shape and user preference before execution

### Requirement: Visual mode choice SHALL be explicit or evidence-based

The controller SHALL choose SVG, H5/HTML, image-model, or hybrid mode only from explicit user preference or strong content evidence. If neither is present, it SHALL ask for a mode decision.

#### Scenario: Content strongly implies SVG

- **GIVEN** the source is a Mermaid sequence, fund-flow, process-flow, state, or
  architecture-like diagram request
- **WHEN** the user has not expressed a conflicting preference
- **THEN** the controller MAY choose an SVG route
- **AND** state the content evidence for that route

#### Scenario: Preference and content conflict

- **GIVEN** the user asks for image-model output
- **AND** the content requires exact Chinese labels, tables, or precise
  compliance text
- **WHEN** the controller detects the conflict
- **THEN** it SHALL present a tradeoff and offer a hybrid or deterministic text
  route before production

#### Scenario: Ambiguous visual request

- **WHEN** the user asks only for 制图, 出图, 配图, 一图流, visual polish, or a
  similar ambiguous visual task
- **THEN** the controller SHALL present a bounded mode fork for SVG, H5/HTML,
  image-model, and hybrid output unless the provided material strongly selects
  a mode

### Requirement: Visual-agent SHALL route to bounded workers

`visual-agent` SHALL route to specialized workers and tools without copying or overriding their detailed execution rules.

#### Scenario: Reader-facing report visual

- **GIVEN** the requested output is an H5, share page, Feishu-facing visual,
  article visual package, or reader-facing report artifact
- **WHEN** the controller routes the work
- **THEN** it SHALL preserve the public-report quality gate before worker
  execution

#### Scenario: Direct image generation

- **GIVEN** the selected route is image-model or hybrid output
- **WHEN** bitmap generation is needed
- **THEN** the controller SHALL treat image generation as an executor step
- **AND** keep source extraction, prompt/script boundaries, and verification
  outside the image model's ownership

### Requirement: Visual-agent responses SHALL expose state and evidence

Normal controller responses SHALL include intent, visual case, content shape, output mode, state, allowed action, blocked action when applicable, next action, and evidence.

#### Scenario: Route is ready

- **WHEN** the controller has enough evidence to route
- **THEN** it SHALL state the allowed worker or production path
- **AND** state the evidence used for the decision

#### Scenario: Route is blocked

- **WHEN** the controller lacks source material, user preference, or a safe mode
  choice needed for production
- **THEN** it SHALL state the blocked action
- **AND** ask only for the missing decision or material needed to proceed
