## Purpose

Define a minimal shared frontmatter model for evolution-bearing pages so agents can
read structural page identity and direct typed relations before graph automation.

## Requirements

### Requirement: Repository SHALL define a minimal frontmatter model for covered layers

The repository SHALL define a minimal shared frontmatter model for evolution-bearing
pages so agents can read structural page identity directly.

#### Scenario: New covered-layer page is created

- **WHEN** a new page is created in `wiki/ops`, `wiki/adr`, `openspec/specs`, or `wiki/examples`
- **THEN** the page SHALL follow the repository's minimal frontmatter model

### Requirement: Repository SHALL require structural identity fields for new covered-layer pages

The repository SHALL require a stable pair of identity fields for new covered-layer pages.

#### Scenario: New covered-layer page is added

- **WHEN** a new covered-layer page is added
- **THEN** the page SHALL include `canonical_object` and `artifact_type`

### Requirement: Repository SHALL define a stable relation-field vocabulary for covered layers

The repository SHALL use a stable set of relation fields so cross-page links can be
read structurally instead of only from prose.

#### Scenario: Covered-layer page needs to express direct relations

- **WHEN** a covered-layer page needs to express direct structural relations
- **THEN** the repository SHALL use the shared relation-field vocabulary instead of inventing ad hoc field names

### Requirement: Repository SHALL roll out the frontmatter model strongly for new pages and weakly for existing pages

The repository SHALL stop new structural drift without forcing immediate bulk migration.

#### Scenario: Existing covered-layer page predates the frontmatter model

- **WHEN** an existing page predates the frontmatter model
- **THEN** the repository MAY remain unchanged until the page is intentionally touched or migrated

#### Scenario: New covered-layer page is added after model adoption

- **WHEN** a new covered-layer page is added after model adoption
- **THEN** the repository SHALL require the frontmatter model for that page
