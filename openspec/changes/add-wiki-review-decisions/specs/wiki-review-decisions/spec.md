## Purpose

Define the review stage that turns `wiki-doctor` diagnosis output into a
repo-visible draft decision record without applying wiki repairs.

## ADDED Requirements

### Requirement: Repository SHALL generate draft wiki review decision records

The repository SHALL provide an explicit path for generating Markdown
`wiki-review-decisions` records under `wiki/ops/wiki-review-decisions/`.

#### Scenario: User asks to confirm or route doctor findings

- **WHEN** the user asks to turn doctor diagnosis into a review decision
- **THEN** the repository SHALL build or consume the adjudication review package
- **AND** it SHALL write a draft review-decision record when explicitly asked
- **AND** it SHALL preserve stdout JSON behavior for inspection.

### Requirement: Review decisions SHALL preserve write boundaries

Review-decision records SHALL classify findings for human confirmation without
approving or applying repairs.

#### Scenario: Review decision contains treatment candidates

- **WHEN** a record lists treatment candidates
- **THEN** it SHALL label them as candidates only
- **AND** it SHALL NOT write frontmatter, taxonomy config, relation fields, or
  MOC files.

#### Scenario: Review decision contains surgery candidates

- **WHEN** a record lists surgery candidates
- **THEN** it SHALL require later surgery planning or OpenSpec routing before
  structural writes
- **AND** it SHALL NOT execute batch repair.

### Requirement: Review decisions SHALL classify doctor details into bounded buckets

The repository SHALL classify review details into explicit draft buckets that
preserve source references.

#### Scenario: Adjudication package has review focus details

- **WHEN** the review-decision package is built
- **THEN** each bucket entry SHALL include a `detail_ref` and path when available
- **AND** the package SHALL include draft buckets for accepted candidates,
  rejected candidates, deferred items, treatment candidates, surgery candidates,
  and OpenSpec-required items.

### Requirement: Repository SHALL expose wiki-review-decisions as a repo-local skill

The repository SHALL publish a compact `.codex/skills/wiki-review-decisions`
skill for the review stage of the LLM-WIKI medical loop.

#### Scenario: User asks for a diagnosis confirmation sheet

- **WHEN** the user asks to confirm, triage, or route `wiki-doctor` findings
- **THEN** the `wiki-review-decisions` skill SHALL route to the review-decision
  CLI
- **AND** it SHALL preserve that the output is draft review routing, not repair
  approval.
