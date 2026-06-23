# visual-agent-entry-route Specification

## ADDED Requirements

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
