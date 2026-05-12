## MODIFIED Requirements

### Requirement: Wiki graph skill SHALL provide an explainable object view

The wiki graph skill SHALL expose a bounded object-level graph summary derived
from explicit graph extraction and relation-analysis artifacts.

#### Scenario: User inspects graph structure

- **WHEN** the user invokes the repo's wiki graph skill
- **THEN** the skill SHALL run or read graph extraction and relation-analysis
  output
- **AND** it SHALL summarize canonical objects, source layers, artifact types,
  relation counts, representative pages, and unresolved warning pressure
- **AND** it SHALL describe the output as structural evidence, not semantic
  understanding

### Requirement: Wiki scorecard skill SHALL provide actionable diagnostics

The wiki scorecard skill SHALL turn semantic scoring and utilization output into
bounded diagnostics that indicate what to inspect next.

#### Scenario: User inspects scorecard diagnostics

- **WHEN** the user invokes the repo's wiki scorecard skill
- **THEN** the skill SHALL summarize preferred, cautious, and blocked objects
- **AND** it SHALL include score bands, utilization reasons, next inspection
  actions, and proof-boundary notes
- **AND** it SHALL NOT claim embeddings, hidden semantic ranking, or retrieval
  proof

### Requirement: Repository SHALL expose a preview-only wiki queue skill

The repository SHALL provide a wiki queue skill as a preview-only queue view
derived from bounded self-directed execution output.

#### Scenario: User previews possible wiki work

- **WHEN** the user invokes the repo's wiki queue skill
- **THEN** the skill SHALL group candidate work as ready, needs user decision,
  and blocked
- **AND** it SHALL include source paths and caution notes when source
  references are available, including for blocked items
- **AND** it SHALL NOT create, modify, archive, or queue OpenSpec changes
- **AND** it SHALL NOT execute queued work or mark tasks complete

### Requirement: Repository SHALL expose the wiki runtime as named Codex skills

The repository SHALL provide repo-local Codex skills that expose the existing
LLM Wiki runtime layers through the `wiki-*` skill family under `.codex/skills`.

#### Scenario: User looks for wiki runtime skills

- **WHEN** the user wants to invoke the repo's LLM Wiki runtime capabilities in
  current Codex
- **THEN** the repository SHALL provide skill source files under `.codex/skills`
  for status, manifest, inbox, query, graph, scorecard, route, context, apply,
  and queue surfaces
- **AND** the supported runtime path SHALL NOT require plugin marketplace
  loading or copying skills into user scope

### Requirement: README SHALL document the wiki skill surface

The README SHALL list the available repo-local wiki skill surface so users can
discover the runtime layers without relying on unsupported custom slash commands
or user-scope installation.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki runtime skills are available
- **THEN** the README SHALL list status, manifest, inbox, query, graph,
  scorecard, route, context, apply, and queue skills
- **AND** it SHALL keep `.codex/skills/wiki-status/SKILL.md` as the status
  source path
