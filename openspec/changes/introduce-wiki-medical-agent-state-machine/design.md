# Design: wiki medical agent state machine

## Core Model

`wiki-medical-agent` is the lifecycle controller. It is not a sixth stage.

```text
user request
  -> intent diagnosis
  -> active case resolver
  -> case state machine
  -> internal worker execution
  -> same case file update
  -> recovery / next_action
```

## Authority

The case file is the only authority. Stage records are evidence attachments.
`Confirmed Decisions` is the only executable decision surface.

## Normal Entry

Use:

```text
$report-wiki-portfolio:wiki-medical-agent <intent>
```

Old stage skills redirect ordinary use to the agent and only run in explicit
legacy/debug mode.

## State Rules

No confirmed decisions means no treatment apply. Treatment apply must run
recovery. Recovery findings become proposed decisions, blockers, or surgery
requirements; they do not auto-execute.

## Boundaries

The agent must not automatically write relations, taxonomy config, MOC pages,
ADRs, AGENTS, skills, or OpenSpec lifecycle state.
