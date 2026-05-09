## ADDED Requirements

### Requirement: Remaining non-convention ops pages SHALL use explicit frontmatter identity

Covered `wiki/ops` pages that do not match supported path conventions SHALL use
explicit frontmatter when they need to participate in graph extraction.

#### Scenario: Chinese-titled ops page has explicit identity fields

- **WHEN** a Chinese-titled `wiki/ops` page includes `canonical_object` and
  `artifact_type`
- **THEN** the extractor SHALL use those fields for node identity
- **AND** it SHALL NOT require a Chinese filename resolver

#### Scenario: Chinese-titled ops page lacks explicit identity fields

- **WHEN** a Chinese-titled `wiki/ops` page lacks supported path conventions
  and lacks explicit identity fields
- **THEN** the extractor SHALL keep emitting an unresolved identity warning
