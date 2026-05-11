## ADDED Requirements

### Requirement: Public report gate SHALL enforce reference-shaped article flow

The public report gate SHALL verify reference-shaped article flow when a
reader-facing draft uses a newspaper, article, or report reference for output
shape, preserving the reference's layout system rather than silently replacing
it with a card, dashboard, table, or prompt-script composition.

#### Scenario: Newspaper reference becomes a card wall

- **WHEN** the user asks for a reader-facing draft that references an existing
  newspaper or article-style report
- **AND** the draft renders prose-heavy company or topic analysis as repeated
  boxed cards, colored panels, comparison cells, or dashboard-like grids
- **THEN** the Article Flow Layout Gate SHALL fail
- **AND** the draft SHALL NOT be claimed review-ready until the content is
  converted into article flow with prose paragraphs and disciplined evidence
  callouts

#### Scenario: Visual prompt leaks into report body

- **WHEN** the requested final image route is image-model or Hybrid
- **AND** prompt text, visual-script instructions, or output-mode notes appear
  inside the reader-facing report body
- **THEN** the Article Flow Layout Gate SHALL fail
- **AND** the prompt or visual production route SHALL be moved to a separate
  asset brief or removed from the report body

#### Scenario: Gate review records layout replay

- **WHEN** a draft is repaired after layout drift against a newspaper/article
  reference
- **THEN** the gate-review artifact SHALL record the reference layout system,
  retained patterns, rejected card/table patterns, and replay result
