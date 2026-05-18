# wiki-doctor-skill Specification

## Purpose
TBD - created by archiving change rename-wiki-content-adjudication-skill-to-doctor. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose wiki-doctor

The repository SHALL provide a repo-local `wiki-doctor` skill for direct
inspection of content adjudication review packages.

#### Scenario: User invokes wiki-doctor

- **WHEN** the user invokes `$report-wiki-portfolio:wiki-doctor`
- **THEN** the skill SHALL route to the existing content adjudication package
  builder
- **AND** it SHALL summarize full detail, review focus, taxonomy candidate,
  drift trace, and eval result sections.

### Requirement: wiki-doctor SHALL remain review-only

The skill SHALL diagnose review-package risks without applying structural
changes.

#### Scenario: Review package contains accepted candidates

- **WHEN** `wiki-doctor` displays adjudication output
- **THEN** it SHALL NOT write frontmatter
- **AND** it SHALL NOT mutate taxonomy
- **AND** it SHALL NOT write MOC pages
- **AND** it SHALL NOT mark OpenSpec tasks complete.

