# moc-temperature-reading-board Specification

## ADDED Requirements

### Requirement: Repository SHALL build relation feature packages before MOC admission

The repository SHALL derive bounded relation feature packages from explicit
wiki graph edges without claiming semantic value from Python-only scoring.

#### Scenario: Feature package is built from a graph edge

- **GIVEN** a graph edge with `source_page_path`, `relation_type`, and `target`
- **WHEN** relation feature packages are built
- **THEN** the package SHALL include source page, source object, relation type,
  target object, evidence refs, and structural features
- **AND** it SHALL NOT include a final MOC admission decision.

### Requirement: Repository SHALL gate relation MOC pages through temperature clue windows

The repository SHALL prevent raw relation types from becoming standalone MOC
pages unless an admission plan admits the relation from reviewed clue windows.
This narrows existing Obsidian MOC projection behavior: relation-type groups
MAY remain visible in graph summary, dry-run, and preview output as blocked or
review-needed admission state, but SHALL NOT be treated as generated relation
MOC page candidates unless admitted.

#### Scenario: Raw mechanical relation is blocked

- **GIVEN** graph edges with relation type `derived_from`
- **WHEN** MOC candidates are built without an admission plan
- **THEN** no `wiki/moc/relation-derived_from.md` candidate SHALL be produced.
- **AND** the relation type SHALL be represented as blocked or review-needed
  admission state in the temperature summary.

#### Scenario: Reviewed relation is admitted

- **GIVEN** a temperature clue board with an admitted relation type `validates`
- **WHEN** MOC candidates are built with the derived admission plan
- **THEN** `wiki/moc/relation-validates.md` SHALL be produced.

#### Scenario: Graph summary preserves relation groups without generating raw relation pages

- **GIVEN** graph summary includes relation-type MOC groups from explicit
  frontmatter edges
- **WHEN** no admission plan admits those relation types
- **THEN** dry-run or preview output SHALL expose those groups only as
  `blocked` or `needs_review` admission state
- **AND** it SHALL NOT produce generated `wiki/moc/relation-*.md` page
  candidates for those raw relation groups.

### Requirement: Medical-agent MOC preview SHALL remain read-only while surfacing admission state

The medical-agent MOC preview SHALL include temperature admission counts when
available and SHALL NOT write MOC pages or workflow records.

#### Scenario: MOC preview reports admission state

- **GIVEN** one active medical case
- **WHEN** the user asks for MOC preview surgery
- **THEN** the payload SHALL include MOC projection summary, surgery preview,
  and temperature admission summary
- **AND** no `wiki/moc` files SHALL be written.
