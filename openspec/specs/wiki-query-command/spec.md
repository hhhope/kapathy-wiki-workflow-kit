# wiki-query-command Specification

## Purpose
TBD - created by archiving change add-wiki-query-command. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose a bounded wiki query skill

The repository SHALL provide a repo-local Codex skill named `wiki-query` that
turns a user task or focus text into a bounded wiki context packet.

#### Scenario: User asks for task-shaped wiki context

- **WHEN** the user invokes the repo's wiki query skill with a task or focus
- **THEN** the skill SHALL inspect status, route, context, and explicit text
  search evidence
- **AND** it SHALL summarize candidate `open_first`, `open_next`, and
  `do_not_anchor` context

### Requirement: Wiki query SHALL preserve explicit proof boundaries

The wiki query skill SHALL describe v1 query as bounded retrieval guidance, not
semantic search or autonomous execution.

#### Scenario: Query results are returned

- **WHEN** the wiki query skill returns candidate context
- **THEN** it SHALL include proof boundary or caution notes
- **AND** it SHALL NOT claim embeddings, hidden semantic ranking, graph UI, or
  automatic execution

### Requirement: Wiki query SHALL not mutate OpenSpec lifecycle state

The wiki query skill SHALL NOT create, modify, archive, or queue OpenSpec
changes by itself.

#### Scenario: Query completes

- **WHEN** the wiki query skill completes
- **THEN** it SHALL NOT open, modify, archive, or create OpenSpec changes
- **AND** it SHALL NOT mark OpenSpec tasks complete

### Requirement: README SHALL document wiki query

The README SHALL list `$wiki-query` with the repo-local wiki skill surface.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki skills are available
- **THEN** the README SHALL include `$wiki-query`
- **AND** it SHALL describe the skill as bounded task-shaped context
  retrieval
