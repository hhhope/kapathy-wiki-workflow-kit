# wiki-content-enrichment-preview Specification

## Purpose
TBD - created by archiving change add-wiki-content-enrichment-preview. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL preview content enrichment before projection

The repository SHALL provide a preview that suggests domain, canonical object,
artifact type, ops area, and relation candidates for covered `wiki/ops` and
`wiki/adr` pages.

#### Scenario: Covered page has missing frontmatter

- **WHEN** enrichment preview analyzes a `wiki/ops` or `wiki/adr` page with
  missing required fields
- **THEN** it SHALL suggest candidate frontmatter with evidence and confidence
- **AND** it SHALL NOT write the page.

### Requirement: Enrichment preview SHALL use bounded evidence

The enrichment preview SHALL only use path, title, body text, existing
frontmatter, taxonomy config, and existing canonical objects.

#### Scenario: Relation is not explicit

- **WHEN** a candidate relation lacks explicit textual, frontmatter, title, or
  existing-object evidence
- **THEN** the preview SHALL mark it as needing review or omit it
- **AND** it SHALL NOT infer hidden semantic relationships.

### Requirement: Status and apply SHALL expose enrichment as preview only

Status and apply surfaces SHALL expose enrichment gaps and candidates without
mutating pages.

#### Scenario: Enrichment candidates exist

- **WHEN** status or apply output includes enrichment information
- **THEN** it SHALL identify candidate actions as preview/review work
- **AND** it SHALL NOT directly edit frontmatter.

### Requirement: Decision trace eval SHALL guard enrichment write boundaries

The repository SHALL include replay coverage for `wiki_content_enrichment`.

#### Scenario: Agent routes a content enrichment request

- **WHEN** a decision trace claims `wiki_content_enrichment`
- **THEN** eval SHALL require static preview actions
- **AND** it SHALL reject direct frontmatter writes from the enrichment preview.

