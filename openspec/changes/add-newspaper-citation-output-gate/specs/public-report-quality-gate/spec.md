## ADDED Requirements

### Requirement: Public report gate SHALL require citation surfaces for newspaper outputs

The public report gate SHALL require a reader-visible citation surface for
newspaper-style H5/share packages and public newspaper drafts before
review-ready, publish, sync, or share claims.

#### Scenario: Newspaper has source map but no citation surface

- **WHEN** a newspaper-style H5, share package, or public newspaper draft has an
  internal source map, learning use map, or gate-review artifact
- **AND** the reader-facing output lacks a visible citation surface for
  load-bearing claims, figures, company examples, or visual panels
- **THEN** the Newspaper Citation Surface Gate SHALL fail
- **AND** the draft SHALL NOT be claimed review-ready, published, synced, or
  shared as final

#### Scenario: Citation surface records source strength

- **WHEN** a newspaper citation surface cites a source for a claim, number,
  company example, or visual panel
- **THEN** it SHALL identify the citation target and source class
- **AND** it SHALL include a boundary note when the cited source is secondary,
  practitioner, transcript mirror, candidate, paywalled without primary access,
  or otherwise too weak for a hard fact claim

#### Scenario: Existing newspaper replay

- **WHEN** the AI Agent Product Engineering Collaboration newspaper is evaluated
  for review-ready, publish, sync, or share status
- **THEN** the gate review SHALL cite the output artifact
  `wiki/reports/agentic-product-engineering-collaboration-newspaper.html`
- **AND** it SHALL cite the supporting source map
  `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`
- **AND** it SHALL verify that load-bearing newspaper panels have reader-visible
  citation routes or explicit boundary notes
