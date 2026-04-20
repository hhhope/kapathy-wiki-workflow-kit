## ADDED Requirements

### Requirement: Repository SHALL provide a readable timeline view for the active evolution chain

The repository SHALL expose a human-readable timeline view that makes the recent
evolution chain reviewable in time order.

#### Scenario: User needs to review chronology

- **WHEN** the user needs to understand how the recent wiki-governance work unfolded
- **THEN** the repository SHALL provide a readable timeline page
- **AND** that page SHALL be linked from wiki navigation

### Requirement: Repository SHALL provide a readable artifact-type grouping view

The repository SHALL expose a grouped reading surface for same-type documents so
artifact families can be compared directly.

#### Scenario: User needs to compare same-type documents

- **WHEN** the user needs to identify or compare documents by artifact type
- **THEN** the repository SHALL provide a grouped artifact-type reading page
- **AND** the page SHALL point to representative documents by type

### Requirement: Repository SHALL provide a readable relation view above structural graph artifacts

The repository SHALL expose a human-readable relation view that summarizes the
current object and relation layer without requiring direct JSON inspection.

#### Scenario: User needs to understand current object relations

- **WHEN** the user needs to understand which canonical objects matter and where
  unresolved reading pressure remains
- **THEN** the repository SHALL provide a readable relation page
- **AND** that page SHALL summarize current objects, layers, and reading pressure

### Requirement: Readable views SHALL stay scoped to reading-layer recovery

The repository SHALL treat this readable-view layer as a reading aid rather than
as a new runtime or command-design change.

#### Scenario: Readable views are added

- **WHEN** this capability is implemented
- **THEN** it SHALL not modify `openspec-explore`
- **AND** it SHALL not continue runtime, routing, injection, or autonomy work
