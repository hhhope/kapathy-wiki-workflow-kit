## ADDED Requirements

### Requirement: Public report gate SHALL own the outer route for reader-facing output

The public report gate SHALL remain the outer route for reader-facing reports,
H5/share drafts, Feishu review drafts, public materials, and external-facing
visual packages even when specialized skills perform source, learning, visual,
image-generation, Feishu, or verification work.

#### Scenario: Reader-facing article asks for knowledge cards

- **WHEN** the user asks to turn an existing reader-facing article, H5, or
  share draft into knowledge cards, chapter visuals, or a one-page infographic
- **THEN** the system SHALL route through the public report gate first
- **AND** the public report gate SHALL preserve the Article Intent Contract,
  Judgment Ownership Gate, Visual Gate, and Publish Gate
- **AND** visual skills SHALL be treated as delegated production routes rather
  than replacements for the public report gate

#### Scenario: Specialized skill is needed during public output work

- **WHEN** a reader-facing output needs source learning, visual package design,
  per-image infographic scripting, image generation, Feishu writing, or final
  verification
- **THEN** the public report gate SHALL identify the subordinate skill route
- **AND** the subordinate skill SHALL NOT weaken the public report gate's
  review-ready, publish, sync, source-boundary, visual, or judgment-ownership
  blockers

#### Scenario: Visual asset is generated for a public draft

- **WHEN** a visual asset is generated for a reader-facing draft
- **THEN** the public report gate review SHALL record the visual's intended
  reader-facing role, local asset path or delivery boundary, and remaining
  visual QA risk before any review-ready, publish, or sync claim
