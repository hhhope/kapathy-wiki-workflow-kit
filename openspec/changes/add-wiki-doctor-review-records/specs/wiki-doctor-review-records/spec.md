## Purpose

Define explicit repo-visible `wiki-doctor` review records as diagnosis artifacts
that preserve adjudication review output without applying wiki structure changes.

## ADDED Requirements

### Requirement: Repository SHALL generate explicit wiki-doctor review records

The repository SHALL provide an explicit, non-default path for generating
Markdown `wiki-doctor` review records under `wiki/ops/wiki-doctor-runs/`.

#### Scenario: User requests a review record

- **WHEN** the user explicitly asks `wiki-doctor` to generate a diagnosis record
- **THEN** the repository SHALL build the adjudication package
- **AND** it SHALL write a Markdown review record under `wiki/ops/wiki-doctor-runs/`
- **AND** it SHALL preserve stdout diagnosis behavior for the package.

### Requirement: Review records SHALL preserve diagnosis boundaries

Review records SHALL be diagnosis evidence only and SHALL NOT approve or apply
structural wiki changes.

#### Scenario: Review record contains taxonomy candidates

- **WHEN** a review record includes taxonomy candidates
- **THEN** it SHALL label them as candidates only
- **AND** it SHALL NOT mutate `wiki/config/frontmatter-taxonomy.yaml`.

#### Scenario: Review record contains accepted or likely judgments

- **WHEN** a review record includes adjudication judgments
- **THEN** it SHALL NOT write page frontmatter
- **AND** it SHALL NOT write MOC pages
- **AND** it SHALL NOT mark OpenSpec tasks complete.

### Requirement: Default doctor diagnosis SHALL remain non-writing

The default adjudication CLI and `wiki-doctor` diagnosis path SHALL remain
review-only and non-writing unless review-record generation is explicitly
requested.

#### Scenario: User asks for ordinary doctor diagnosis

- **WHEN** the user asks for `wiki-doctor` diagnosis without asking for a record
- **THEN** the repository SHALL show or summarize the review package
- **AND** it SHALL NOT create files under `wiki/ops/wiki-doctor-runs/`.
