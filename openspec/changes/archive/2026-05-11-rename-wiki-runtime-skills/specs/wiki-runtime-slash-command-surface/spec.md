## REMOVED Requirements

### Requirement: Repository SHALL expose the wiki runtime as repo-local slash commands

The repository SHALL provide repo-local Codex command files that expose the
existing LLM Wiki runtime layers through the `/wiki:*` namespace.

#### Scenario: User looks for wiki runtime commands

- **WHEN** the user wants to invoke the repo's LLM Wiki runtime capabilities
- **THEN** the repository SHALL provide command files for status, manifest,
  inbox, query, graph, scorecard, route, context, apply, and queue surfaces
- **AND** each command SHALL use a `/wiki:*` invocation name

### Requirement: Wiki runtime commands SHALL remain thin wrappers

The wiki runtime slash commands SHALL wrap existing scripts, generated
artifacts, and wiki/spec records rather than inventing new runtime semantics.

#### Scenario: Runtime command is invoked

- **WHEN** a `/wiki:*` runtime command is invoked
- **THEN** it SHALL identify the scripts or artifacts it uses
- **AND** it SHALL summarize the generated or inspected runtime output
- **AND** it SHALL preserve the proof boundary of the underlying runtime layer

### Requirement: Wiki runtime commands SHALL not mutate OpenSpec lifecycle state

Wiki runtime commands SHALL NOT create, modify, archive, or queue OpenSpec
changes by themselves.

#### Scenario: Command completes

- **WHEN** any wiki runtime command completes
- **THEN** it SHALL NOT open, modify, archive, or create OpenSpec changes
- **AND** it SHALL NOT mark tasks complete or execute a change queue

### Requirement: README SHALL document the wiki command surface

The README SHALL list the available repo-local `/wiki:*` command surface so
users can discover the runtime layers without reading implementation files.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki commands are available
- **THEN** the README SHALL list status, manifest, inbox, query, graph,
  scorecard, route, context, apply, and queue commands
- **AND** it SHALL keep `/wiki:status` as the existing status entrypoint

## ADDED Requirements

### Requirement: Repository SHALL expose the wiki runtime as named Codex skills

The repository SHALL provide installable user-scope Codex skills that expose the
existing LLM Wiki runtime layers through the `wiki-*` namespace.

#### Scenario: User looks for wiki runtime skills

- **WHEN** the user wants to invoke the repo's LLM Wiki runtime capabilities in
  current Codex
- **THEN** the repository SHALL provide skill source files for status, manifest,
  inbox, query, graph, scorecard, route, context, apply, and queue surfaces
- **AND** each skill SHALL use a `wiki-*` invocation name without the
  `report-wiki-portfolio:` repo namespace

### Requirement: Wiki runtime skills SHALL remain thin wrappers

The wiki runtime skills SHALL wrap existing scripts, generated artifacts, and
wiki/spec records rather than inventing new runtime semantics.

#### Scenario: Runtime skill is invoked

- **WHEN** a `wiki-*` runtime skill is invoked
- **THEN** it SHALL identify the scripts, artifacts, or command contract it uses
- **AND** it SHALL summarize the generated or inspected runtime output
- **AND** it SHALL preserve the proof boundary of the underlying runtime layer

### Requirement: Wiki runtime skills SHALL not mutate OpenSpec lifecycle state

Wiki runtime skills SHALL NOT create, modify, archive, or queue OpenSpec changes
by themselves.

#### Scenario: Skill completes

- **WHEN** any wiki runtime skill completes
- **THEN** it SHALL NOT open, modify, archive, or create OpenSpec changes
- **AND** it SHALL NOT mark tasks complete or execute a change queue

### Requirement: README SHALL document the wiki skill surface

The README SHALL list the available `$wiki-*` skill surface so users can
discover the runtime layers without relying on unsupported custom slash
commands.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki runtime skills are available
- **THEN** the README SHALL list status, manifest, inbox, query, graph,
  scorecard, route, context, apply, and queue skills
- **AND** it SHALL keep `$wiki-status` as the status entrypoint
