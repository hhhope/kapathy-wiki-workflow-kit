## Purpose

Define a minimal graph-extraction workflow that turns covered evolution-bearing pages
into a machine-readable graph artifact after naming and frontmatter structure exist.
## Requirements
### Requirement: Repository SHALL provide a minimal graph-extraction workflow for covered layers

The repository SHALL provide a repeatable workflow that extracts graph-shaped structure
from covered evolution-bearing layers.

#### Scenario: Extraction is run on covered layers

- **WHEN** the extraction workflow is run on `wiki/ops`, `wiki/adr`, `openspec/specs`, and `wiki/examples`
- **THEN** the repository SHALL emit a graph artifact from those covered layers

### Requirement: Repository SHALL emit node identity from naming and frontmatter contracts

The repository SHALL derive node identity from the stable naming model and frontmatter model.

#### Scenario: Covered-layer page is extracted

- **WHEN** a covered-layer page is extracted
- **THEN** the resulting node SHALL preserve page path, canonical object, artifact type, and source layer

### Requirement: Repository SHALL emit typed edges from the shared relation vocabulary

The repository SHALL extract typed edges only from the shared relation-field vocabulary defined by the repository.

#### Scenario: Covered-layer page contains relation fields

- **WHEN** a covered-layer page contains supported relation fields
- **THEN** the extraction workflow SHALL emit typed edges using those relation types

### Requirement: Repository SHALL keep extraction proof separate from graph-product claims

The repository SHALL treat extraction validation as structural proof, not as proof of full graph semantics or UI readiness.

#### Scenario: Extraction validation passes

- **WHEN** the extraction workflow emits valid graph output
- **THEN** the repository SHALL treat that result as structural extraction proof only

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

