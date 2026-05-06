## Design Boundary

Target layer: Root AGENTS.

Root `~/.codex/AGENTS.md` owns cross-repo safety floor and entrance routing. It
must not own repo-local archive detail, rule bodies, skill bodies, or wiki
method content.

This change governs root context so it reduces drift. It does not chase
single-file size reduction. A moved block counts as reduction only if it leaves
the default loaded path and becomes genuinely trigger-gated.

## Reused Governance

This change reuses the archived `decide-root-governance-alignment` model:

- Six principles: single source of truth, authority order, triggered assets,
  instruction budget, evidence before behavior change, candidate vs decided.
- Six-step process: declare layer, check source of truth, check authority,
  choose surface by semantic weight, record evidence, self-check.
- Pattern Catalog target: Root AGENTS.
- Self-Check four columns: structure, semantic, evidence, boundary.

No new pattern, checklist field, or rule category is introduced here.

## Progressive Context Strategy

### 1. Measure Loaded Context

Evaluation must distinguish:

- **default loaded context**: text read on the ordinary session path before a
  task-specific trigger fires
- **triggered loaded context**: text read only after a concrete work type,
  skill, rule, or verification need is identified
- **always-on hard-stop context**: text that must remain ambient because a miss
  would cause unsafe continuation

`AGENTS.md` line count is supporting evidence. It is not the success metric.

### 2. Reject Fake Progressive Disclosure

The following shape must fail:

```text
move Global Rule Routing from AGENTS.md to rule-routing.md
AND require non-trivial work to load rule-routing.md by default
```

Reason: default file size drops, but practical loaded context for the dominant
non-trivial path does not.

### 3. Consolidate Git and Execution Discipline

The current `Execution discipline` and `Git discipline` sections overlap on:

- dirty tree handling
- committing only task-related files
- resume checks
- push/claim truth-source checks

The consolidated section must preserve the behavioral stops while removing
duplicated wording.

### 4. Preserve Hard Stops

The compression must not weaken:

- pre-task health check
- active OpenSpec requirement for large work
- OpenSpec completion stop
- destructive git protection
- dirty tree preservation
- raw-data validation for new APIs or fields
- skill semantic edit gate
- long-step reporting

## Governance Growth Constraint

This change must not grow governance without paying for it. New governance text
must do at least one of the following:

- replace existing text
- shorten existing text
- move existing text off the default loaded path
- prove that it is an always-on hard stop

Adding a new checklist, support file, skill, or rule is not success by itself.

## Evidence Plan

`evaluation.md` records:

- baseline line/word/byte counts
- default loaded context before and after
- triggered loaded context before and after
- RED/GREEN result for fake progressive disclosure
- section mapping before and after
- Self-Check four-column result
- residual risks
