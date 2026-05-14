## Purpose

Define a bounded ReAct decision-trace layer for repo-local wiki runtime skills
and a deterministic eval harness for replaying agent-produced traces.

## ADDED Requirements

### Requirement: Wiki runtime SHALL produce bounded decision traces for high-risk routes

High-risk wiki routes SHALL use a compact decision trace before suggesting or
performing bounded wiki work.

#### Scenario: Agent handles a high-risk wiki request

- **WHEN** the request involves wiki apply, frontmatter repair, article
  learning, exploratory scoring, relation exploration, or promotion to a
  behavior asset
- **THEN** the agent SHALL identify intent, evidence object, risk level, actions,
  observation class, decision, and boundary
- **AND** the trace SHALL distinguish static facts from exploratory judgments.

### Requirement: Decision trace eval SHALL validate traces without classifying intent

The eval harness SHALL validate agent-produced traces against explicit cases
without using Python to infer the intent from natural language.

#### Scenario: Eval case allows multiple intents

- **WHEN** a case lists multiple allowed intents
- **THEN** the trace SHALL pass when its `intent` is one of those allowed values
- **AND** required actions and boundary checks still SHALL pass.

### Requirement: Exploratory wiki scoring SHALL remain candidate judgment

Article weight, temperature, source confidence, and relation strength SHALL be
treated as exploratory judgments unless a later OpenSpec change stabilizes their
semantics.

#### Scenario: Article temperature is evaluated

- **WHEN** the input asks for article weight, temperature, or relation strength
- **THEN** the trace SHALL route through exploratory judgment or scorecard
  context
- **AND** it SHALL NOT hard-gate, auto-promote, mutate taxonomy, or repair
  frontmatter by default.

### Requirement: Scorecard SHALL remain an observation source

The wiki scorecard SHALL provide observation context, not behavior correctness
judgment.

#### Scenario: Eval checks scorecard-backed routing

- **WHEN** a trace reads scorecard context
- **THEN** the eval harness MAY require that action
- **AND** it SHALL judge the trace boundary, not the scorecard object score.
