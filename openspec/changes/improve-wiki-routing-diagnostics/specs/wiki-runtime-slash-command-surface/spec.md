## Purpose

Clarify the user-facing wiki command routing loop and repair boundaries.

## ADDED Requirements

### Requirement: Wiki status SHALL be the default health entry point

The command documentation SHALL route general wiki health questions to
`/wiki:status`.

#### Scenario: User asks whether the wiki is healthy

- **WHEN** the user asks for wiki health, current status, or what needs
  attention
- **THEN** command documentation SHALL identify `/wiki:status` as the default
  health entry
- **AND** the status summary SHALL include inbox, OpenSpec, identity, relation,
  domain taxonomy, and graph parse health

### Requirement: Wiki graph SHALL remain structural drilldown

The command documentation SHALL keep `/wiki:graph` scoped to structural graph
inspection.

#### Scenario: User asks why an object is disconnected

- **WHEN** the user asks why a page, object, layer, artifact, or relation is
  not connected
- **THEN** command documentation SHALL route to `/wiki:graph`
- **AND** it SHALL state that raw graph extraction keeps `openspec/specs`
  nodes
- **AND** it SHALL state that readable summaries collapse spec details by
  default

### Requirement: Wiki apply SHALL summarize repair routes without executing them

The command documentation SHALL make `/wiki:apply` a repair-plan surface, not a
runtime mutation command.

#### Scenario: Diagnostic output suggests a repair

- **WHEN** status or graph diagnostics identify a repair route
- **THEN** `/wiki:apply` documentation SHALL describe repair routes including
  `page-frontmatter-fix`, `taxonomy-config-fix`, `runtime-parser-fix`, and
  `readable-graph-fix`
- **AND** it SHALL state whether implementation requires OpenSpec
- **AND** it SHALL NOT directly edit runtime files, scripts, rules, skills,
  AGENTS, command behavior, or OpenSpec lifecycle state

