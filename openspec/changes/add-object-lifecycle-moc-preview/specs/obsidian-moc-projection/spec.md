# obsidian-moc-projection Specification Delta

## MODIFIED Requirements

### Requirement: Repository SHALL derive MOC candidates from explicit graph structure

The repository SHALL derive domain, object, and relation MOC candidates from
explicit page frontmatter and graph extraction output.

Object MOC previews SHALL group pages by explicit lifecycle signals from graph
node metadata and relation types rather than using process labels such as
`ops_area` as the primary navigation structure.

#### Scenario: Graph summary runs

- **WHEN** graph summary is built from current graph artifacts
- **THEN** it SHALL include MOC candidates grouped by domain, canonical object,
  and relation type
- **AND** it SHALL NOT write `wiki/moc` files.

#### Scenario: Object MOC preview is rendered

- **WHEN** an object MOC candidate has pages from multiple lifecycle stages
- **THEN** the object preview SHALL render stage headings for those pages
- **AND** it SHALL keep each page linked under its lifecycle section
- **AND** it SHALL NOT use `ops_area` values as the primary section headings.
