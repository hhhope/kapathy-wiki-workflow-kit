## ADDED Requirements

### Requirement: Wiki graph extraction SHALL support bounded ADR and example path identities

The graph extractor SHALL recognize repository-local ADR and example path
conventions as explicit identity signals when frontmatter is absent.

#### Scenario: Covered ADR page uses numbered ADR path shape

- **WHEN** a page path matches `wiki/adr/<number>-<canonical-object>.md`
- **THEN** the extractor SHALL emit a node with canonical object
  `<canonical-object>`
- **AND** it SHALL use artifact type `adr`

#### Scenario: Covered example page uses example path shape

- **WHEN** a page path matches `wiki/examples/<canonical-object>-example.md`
- **THEN** the extractor SHALL emit a node with canonical object
  `<canonical-object>`
- **AND** it SHALL use artifact type `example`

#### Scenario: Covered ops page lacks explicit identity

- **WHEN** a covered `wiki/ops` page lacks supported frontmatter or an explicit
  resolver
- **THEN** the extractor SHALL keep emitting an unresolved identity warning
- **AND** it SHALL NOT infer identity from arbitrary prose
