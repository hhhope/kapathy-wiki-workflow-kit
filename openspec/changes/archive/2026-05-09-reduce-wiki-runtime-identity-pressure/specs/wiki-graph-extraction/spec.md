## ADDED Requirements

### Requirement: Wiki graph extraction SHALL preserve explicit page identities

The graph extractor SHALL turn covered pages into graph nodes only when the page
identity is explicit in supported frontmatter or in a bounded repository-local
path convention.

#### Scenario: Covered page has frontmatter identity

- **WHEN** a covered page has `canonical_object` and `artifact_type`
  frontmatter
- **THEN** the extractor SHALL emit a node using those values

#### Scenario: Covered OpenSpec spec uses canonical path shape

- **WHEN** a page path matches `openspec/specs/<canonical-object>/spec.md`
- **THEN** the extractor SHALL emit a node with canonical object
  `<canonical-object>`
- **AND** it SHALL use artifact type `spec`
- **AND** it SHALL NOT require YAML frontmatter inside the OpenSpec spec file

#### Scenario: Covered page lacks explicit identity

- **WHEN** a covered page lacks supported identity signals
- **THEN** the extractor SHALL emit an unresolved identity warning
- **AND** it SHALL NOT infer identity from arbitrary prose
