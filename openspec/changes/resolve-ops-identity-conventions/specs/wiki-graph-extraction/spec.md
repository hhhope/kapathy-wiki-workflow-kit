## ADDED Requirements

### Requirement: Wiki graph extraction SHALL support bounded ops filename identities

The graph extractor SHALL recognize selected `wiki/ops` filename conventions as
explicit identity signals when frontmatter is absent.

#### Scenario: Ops page uses a supported artifact suffix

- **WHEN** a page path matches a supported `wiki/ops` artifact suffix such as
  `-intake`, `-explore`, `-retro`, `-reminder`, or `-reanchor`
- **THEN** the extractor SHALL emit a node using the filename object segment as
  canonical object
- **AND** it SHALL use the suffix as artifact type

#### Scenario: Ops page uses a dated artifact suffix

- **WHEN** a page path matches a supported `wiki/ops` artifact suffix followed
  by `YYYY-MM-DD`
- **THEN** the extractor SHALL remove only the trailing date from the canonical
  object
- **AND** it SHALL preserve the suffix as artifact type

#### Scenario: Ops page does not match supported identity signals

- **WHEN** a covered `wiki/ops` page lacks frontmatter, a dedicated resolver, a
  fixed entry identity, or a supported filename convention
- **THEN** the extractor SHALL keep emitting an unresolved identity warning
- **AND** it SHALL NOT infer identity from arbitrary prose
