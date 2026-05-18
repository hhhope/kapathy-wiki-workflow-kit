## Purpose

Define the standalone repo-local skill entry for inspecting wiki content
adjudication review packages.

## ADDED Requirements

### Requirement: Repository SHALL expose a content adjudication skill

The repository SHALL provide a repo-local `wiki-content-adjudication` skill for
direct inspection of adjudication review packages.

#### Scenario: User invokes the content adjudication skill

- **WHEN** the user invokes `$report-wiki-portfolio:wiki-content-adjudication`
- **THEN** the skill SHALL route to the existing content adjudication package
  builder
- **AND** it SHALL summarize full detail, review focus, taxonomy candidate,
  drift trace, and eval result sections.

### Requirement: Content adjudication skill SHALL remain review-only

The skill SHALL preserve existing wiki runtime boundaries.

#### Scenario: Adjudication output contains safe-looking candidates

- **WHEN** the skill displays adjudication output
- **THEN** it SHALL NOT write frontmatter
- **AND** it SHALL NOT mutate taxonomy
- **AND** it SHALL NOT write MOC pages
- **AND** it SHALL NOT mark OpenSpec tasks complete.
