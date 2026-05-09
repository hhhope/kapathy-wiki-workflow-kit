# wiki-query-command Specification

## Purpose
TBD - created by archiving change add-wiki-query-command. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose a bounded wiki query command

The repository SHALL provide a repo-local Codex command named `/wiki:query`
that turns a user task or focus text into a bounded wiki context packet.

#### Scenario: User asks for task-shaped wiki context

- **WHEN** the user invokes `/wiki:query` with a task or focus
- **THEN** the command SHALL inspect status, route, context, and explicit text
  search evidence
- **AND** it SHALL summarize candidate `open_first`, `open_next`, and
  `do_not_anchor` context

### Requirement: Wiki query SHALL preserve explicit proof boundaries

The wiki query command SHALL describe v1 query as bounded retrieval guidance,
not semantic search or autonomous execution.

#### Scenario: Query results are returned

- **WHEN** `/wiki:query` returns candidate context
- **THEN** it SHALL include proof boundary or caution notes
- **AND** it SHALL NOT claim embeddings, hidden semantic ranking, graph UI, or
  automatic execution

### Requirement: Wiki query SHALL not mutate OpenSpec lifecycle state

The wiki query command SHALL NOT create, modify, archive, or queue OpenSpec
changes by itself.

#### Scenario: Query completes

- **WHEN** `/wiki:query` completes
- **THEN** it SHALL NOT open, modify, archive, or create OpenSpec changes
- **AND** it SHALL NOT mark OpenSpec tasks complete

### Requirement: README SHALL document wiki query

The README SHALL list `/wiki:query` with the repo-local wiki command surface.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki commands are available
- **THEN** the README SHALL include `/wiki:query`
- **AND** it SHALL describe the command as bounded task-shaped context
  retrieval
