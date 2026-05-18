# wiki-content-adjudication-eval Specification

## Purpose
TBD - created by archiving change add-wiki-content-adjudication-eval. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL produce adjudication review packages

The repository SHALL provide a deterministic package that contains
`candidate_set`, `full_detail_set`, `agent_judgment_set`,
`taxonomy_candidate_set`, `review_focus_set`, `drift_trace_set`, and
`eval_result` for covered wiki content enrichment candidates.

#### Scenario: Candidate set contains reviewable pages

- **WHEN** adjudication runs over content enrichment candidates
- **THEN** every candidate SHALL have a corresponding full detail entry
- **AND** review focus entries SHALL reference full detail entries
- **AND** the package SHALL NOT write wiki frontmatter.

### Requirement: Adjudication SHALL preserve agent judgments and evidence

The adjudication package SHALL assign each candidate a judgment state and keep
evidence, rejected candidates, and risk flags.

#### Scenario: Candidate has uncertain or conflicting evidence

- **WHEN** a candidate has weak, missing, or conflicting evidence
- **THEN** adjudication SHALL mark it as `needs_user_confirmation` or `reject`
- **AND** it SHALL preserve the reason in the full detail entry.

### Requirement: Taxonomy candidates SHALL remain candidates

Unknown domain, ops area, or artifact type values SHALL be surfaced as taxonomy
candidates instead of silently mutating the taxonomy config.

#### Scenario: Candidate references an unknown taxonomy value

- **WHEN** adjudication sees a candidate value that is absent from the taxonomy
  YAML
- **THEN** it SHALL add the value to `taxonomy_candidate_set`
- **AND** it SHALL mark the page for user review.

### Requirement: Eval SHALL check judgment quality and missed risks

Adjudication eval SHALL fail when judgments lack evidence, miss required risks,
or claim safe application while unresolved risks remain.

#### Scenario: Risky candidate lacks required evidence

- **WHEN** a candidate has ADR, drift, taxonomy, or OpenSpec risk
- **THEN** eval SHALL require evidence and matching risk flags
- **AND** it SHALL report failures without writing pages.

### Requirement: Runtime surfaces SHALL expose adjudication as review only

Status, apply, and react surfaces SHALL expose adjudication health and routing
without directly writing frontmatter, mutating taxonomy, generating MOC pages,
or marking OpenSpec tasks complete.

#### Scenario: User asks for content judgment

- **WHEN** the request intent is `wiki_content_adjudication`
- **THEN** react/eval SHALL route to adjudication review/eval actions
- **AND** apply SHALL only show review package context.

