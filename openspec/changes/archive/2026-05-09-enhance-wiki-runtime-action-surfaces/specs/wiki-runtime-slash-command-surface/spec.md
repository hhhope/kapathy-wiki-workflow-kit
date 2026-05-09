## MODIFIED Requirements

### Requirement: Repository SHALL expose the wiki runtime as repo-local slash commands

The repository SHALL provide repo-local Codex command files that expose the
existing LLM Wiki runtime layers through the `/wiki:*` namespace.

#### Scenario: User looks for wiki runtime commands

- **WHEN** the user wants to invoke the repo's LLM Wiki runtime capabilities
- **THEN** the repository SHALL provide command files for status, manifest,
  inbox, query, graph, scorecard, route, context, apply, and queue surfaces
- **AND** each command SHALL use a `/wiki:*` invocation name

### Requirement: README SHALL document the wiki command surface

The README SHALL list the available repo-local `/wiki:*` command surface so
users can discover the runtime layers without reading implementation files.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki commands are available
- **THEN** the README SHALL list status, manifest, inbox, query, graph,
  scorecard, route, context, apply, and queue commands
- **AND** it SHALL keep `/wiki:status` as the existing status entrypoint

## ADDED Requirements

### Requirement: Wiki graph command SHALL provide an explainable object view

The `/wiki:graph` command SHALL expose a bounded object-level graph summary
derived from explicit graph extraction and relation-analysis artifacts.

#### Scenario: User inspects graph structure

- **WHEN** the user invokes `/wiki:graph`
- **THEN** the command SHALL run or read graph extraction and relation-analysis
  output
- **AND** it SHALL summarize canonical objects, source layers, artifact types,
  relation counts, representative pages, and unresolved warning pressure
- **AND** it SHALL describe the output as structural evidence, not semantic
  understanding

### Requirement: Wiki scorecard command SHALL provide actionable diagnostics

The `/wiki:scorecard` command SHALL turn semantic scoring and utilization output
into bounded diagnostics that indicate what to inspect next.

#### Scenario: User inspects scorecard diagnostics

- **WHEN** the user invokes `/wiki:scorecard`
- **THEN** the command SHALL summarize preferred, cautious, and blocked objects
- **AND** it SHALL include score bands, utilization reasons, next inspection
  actions, and proof-boundary notes
- **AND** it SHALL NOT claim embeddings, hidden semantic ranking, or retrieval
  proof

### Requirement: Repository SHALL expose a preview-only wiki queue command

The repository SHALL provide `/wiki:queue` as a preview-only queue view derived
from bounded self-directed execution output.

#### Scenario: User previews possible wiki work

- **WHEN** the user invokes `/wiki:queue`
- **THEN** the command SHALL group candidate work as ready, needs user
  decision, and blocked
- **AND** it SHALL include source paths and caution notes when available
- **AND** it SHALL NOT create, modify, archive, or queue OpenSpec changes
- **AND** it SHALL NOT execute queued work or mark tasks complete
