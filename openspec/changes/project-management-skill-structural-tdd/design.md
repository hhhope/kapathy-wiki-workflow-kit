## Context

The current skill already encodes:

- preserve source pages
- update editable HTML previews when the user asks
- verify gantt row alignment after edits

But it does not yet state the stricter requirement:

- for structural visual pages, write or run a failing structural check first, then edit, then re-run it green

That gap matters because the recent HTML gantt fix was post-fix validation, not strict TDD.

## Goals / Non-Goals

**Goals:**

- Add an explicit structural-TDD rule for editable weekly visual files.
- Make the rule concrete enough to cover month columns, bar-cell counts, and row alignment.

**Non-Goals:**

- Add new scripts or automation.
- Rewrite the whole skill.

## Decisions

### Decision: Scope the rule to structural visual files

The new requirement applies when editing:

- html weekly previews
- gantt-like layouts
- h5 project views

It does not attempt to force the same method on ordinary markdown summaries.

### Decision: Require RED then GREEN in wording

The skill will explicitly state:

1. run or write a failing structural check first
2. edit the file
3. re-run the check green

This keeps the expectation aligned with TDD rather than post-fix spot checks.
