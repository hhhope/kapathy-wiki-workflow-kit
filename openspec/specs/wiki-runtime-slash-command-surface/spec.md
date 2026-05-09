# wiki-runtime-slash-command-surface Specification

## Purpose
TBD - created by archiving change expose-wiki-runtime-slash-command-surface. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose the wiki runtime as repo-local slash commands

The repository SHALL provide repo-local Codex command files that expose the
existing LLM Wiki runtime layers through the `/wiki:*` namespace.

#### Scenario: User looks for wiki runtime commands

- **WHEN** the user wants to invoke the repo's LLM Wiki runtime capabilities
- **THEN** the repository SHALL provide command files for status, manifest,
  inbox, graph, scorecard, route, context, and apply surfaces
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
- **THEN** the README SHALL list status, manifest, inbox, graph, scorecard,
  route, context, and apply commands
- **AND** it SHALL keep `/wiki:status` as the existing status entrypoint
