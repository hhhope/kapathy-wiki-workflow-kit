## Purpose

Define the stable ownership boundary between wiki runtime routing, trace eval,
apply preview, repair-route labels, and OpenSpec lifecycle.

## ADDED Requirements

### Requirement: Wiki runtime layers SHALL NOT substitute for each other

The repository SHALL keep wiki runtime routing, validation, preview, repair
labeling, and lifecycle ownership as separate responsibilities.

#### Scenario: Agent explains a wiki runtime repair question

- **WHEN** the user asks how wiki runtime repair should work
- **THEN** the agent SHALL distinguish `$wiki-react`, trace eval,
  `/wiki:apply`, repair-route labels, and OpenSpec
- **AND** it SHALL NOT treat one layer's output as proof that another layer's
  capability exists.

### Requirement: `$wiki-react` SHALL own explicit routing and decision traces

`$wiki-react` SHALL be treated as the explicit router and `decision_trace`
entrypoint for ambiguous or high-risk wiki runtime requests.

#### Scenario: High-risk wiki route is unclear

- **WHEN** a request may cross inspection, repair, queueing, governance, or
  OpenSpec lifecycle boundaries
- **THEN** `$wiki-react` SHALL produce a visible route and boundary decision
- **AND** it SHALL NOT be treated as a deterministic validator or repair
  executor.

### Requirement: Decision trace eval SHALL validate traces only

`eval_wiki_decision_trace.py` SHALL validate agent-produced traces against
explicit replay cases.

#### Scenario: Eval passes for a decision trace

- **WHEN** decision trace eval passes
- **THEN** the repository MAY treat the trace shape and boundary checks as
  validated
- **AND** it SHALL NOT infer that natural-language intent was classified by
  Python
- **AND** it SHALL NOT infer that repair execution or OpenSpec approval has
  occurred.

### Requirement: `/wiki:apply` SHALL remain a bounded preview surface

`/wiki:apply` SHALL summarize bounded self-directed execution or context
suggestions without directly mutating runtime assets.

#### Scenario: Apply output mentions candidate action

- **WHEN** `/wiki:apply` surfaces `execute_now`, `defer_for_followup`, or repair
  route guidance
- **THEN** the repository SHALL treat that output as preview or suggestion
- **AND** it SHALL NOT treat `/wiki:apply` as permission to edit scripts,
  skills, AGENTS, command behavior, or OpenSpec lifecycle state.

### Requirement: Repair-route labels SHALL NOT imply executable repair infrastructure

Repair-route labels SHALL identify diagnostic classes without implying that
every route has an executable implementation.

#### Scenario: Repair route is named in diagnostics or design

- **WHEN** a route such as `page-frontmatter-fix`, `taxonomy-config-fix`,
  `runtime-parser-fix`, or `readable-graph-fix` is named
- **THEN** the repository SHALL treat it as a route label or contract unless a
  separate implementation artifact proves executable support
- **AND** runtime, workflow, or command behavior changes SHALL still route
  through OpenSpec.
