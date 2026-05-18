## Purpose

Define a controlled projection layer from explicit wiki graph/frontmatter
structure to Obsidian-visible MOC pages.

## ADDED Requirements

### Requirement: Repository SHALL derive MOC candidates from explicit graph structure

The repository SHALL derive domain, object, and relation MOC candidates from
explicit page frontmatter and graph extraction output.

#### Scenario: Graph summary runs

- **WHEN** graph summary is built from current graph artifacts
- **THEN** it SHALL include MOC candidates grouped by domain, canonical object,
  and relation type
- **AND** it SHALL NOT write `wiki/moc` files.

### Requirement: Status SHALL report MOC projection health without writing files

The repository SHALL compare MOC candidates against current `wiki/moc` files
and report missing or stale generated blocks.

#### Scenario: MOC pages are missing

- **WHEN** wiki status is built and candidate MOC pages do not exist
- **THEN** status SHALL report missing MOC projection entries
- **AND** status SHALL NOT create or modify the MOC pages.

### Requirement: Apply SHALL preview MOC projection changes without executing them

The repository SHALL provide a preview of MOC create, update, and noop actions.

#### Scenario: Apply preview is requested

- **WHEN** the MOC projection apply preview is built
- **THEN** it SHALL describe the planned file actions
- **AND** it SHALL NOT write MOC files.

### Requirement: MOC generation SHALL require explicit write mode

The repository SHALL keep MOC generation dry-run by default and require an
explicit apply flag before writing generated blocks.

#### Scenario: Generator runs without apply flag

- **WHEN** the MOC generator is invoked without `--apply`
- **THEN** it SHALL emit the plan
- **AND** it SHALL NOT write files.

#### Scenario: Generator runs with apply flag

- **WHEN** the MOC generator is invoked with `--apply`
- **THEN** it MAY create or update `wiki/moc/*.md`
- **AND** it SHALL preserve manual content outside generated blocks.

### Requirement: Decision trace eval SHALL guard projection routing boundaries

The repository SHALL include a replay case for Obsidian graph projection.

#### Scenario: Agent routes an Obsidian graph projection request

- **WHEN** a decision trace claims `obsidian_graph_projection`
- **THEN** eval SHALL require graph/status/apply-preview routing actions
- **AND** it SHALL reject actions that make status, graph, apply, react, or eval
  write MOC pages.
