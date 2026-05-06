## Design Boundary

Target layer: Root AGENTS.

Root `~/.codex/AGENTS.md` owns cross-repo safety floor and entrance routing. It
must not own repo-local archive detail, rule bodies, skill bodies, or wiki
method content.

This change governs root context so it reduces drift and improves agent
legibility. It does not chase single-file size reduction. A moved block counts
as reduction only if it leaves the default loaded path and becomes genuinely
trigger-gated.

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

### 1. Treat Root AGENTS as a Map, Not a Manual

The calibrated target is an agent-legible map:

- default context keeps hard stops, routing principles, and source-of-record
  pointers
- repo/wiki/OpenSpec/evaluation artifacts hold the detailed knowledge
- the next agent can tell where to read, how to verify, and when to stop
- interruption recovery depends on repo-visible artifacts, not chat memory

This follows the external harness-engineering signal that a large monolithic
`AGENTS.md` becomes stale, unverifiable, and attractive nuisance; the goal is
not less information, but better located and more inspectable information.

### 2. Measure Loaded Context

Evaluation must distinguish:

- **default loaded context**: text read on the ordinary session path before a
  task-specific trigger fires
- **triggered loaded context**: text read only after a concrete work type,
  skill, rule, or verification need is identified
- **always-on hard-stop context**: text that must remain ambient because a miss
  would cause unsafe continuation

`AGENTS.md` line count is supporting evidence. It is not the success metric.

### 3. Reject Fake Progressive Disclosure

The following shape must fail:

```text
move Global Rule Routing from AGENTS.md to rule-routing.md
AND require non-trivial work to load rule-routing.md by default
```

Reason: default file size drops, but practical loaded context for the dominant
non-trivial path does not.

### 4. Keep Harness Assumptions Reviewable

Harness rules encode assumptions about what the model cannot do unaided. Those
assumptions can go stale as models and tools improve. Therefore any retained
root instruction should be classed as one of:

- stable interface or source-of-record pointer
- always-on hard stop
- trigger-gated task detail
- candidate assumption requiring future review

### 5. Require Evidence-Backed Best Practices

An article-derived best practice is not actionable until it has one of these
evidence shapes:

- **external-doc evidence**: URL plus exact section/line reference and the
  narrow conclusion it supports
- **local demo / fixture evidence**: RED/GREEN scenario, input/output, and a
  command or manual replay record
- **git-like project evidence**: repository, commit or path, and the observable
  structure or behavior being compared

Without one of these, the practice remains a candidate observation. It must not
be promoted into root `AGENTS.md`, a spec `SHALL`, a skill hard rule, or an
archive-ready conclusion.

### 6. Consolidate Git and Execution Discipline

The current `Execution discipline` and `Git discipline` sections overlap on:

- dirty tree handling
- committing only task-related files
- resume checks
- push/claim truth-source checks

The consolidated section must preserve the behavioral stops while removing
duplicated wording.

### 7. Preserve Hard Stops

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

The default workflow pattern remains sequential: reframe target, record
evidence, then implement. Parallel agents, evaluator-optimizer loops, or
automation are out of scope unless a later measurable quality gap justifies
them.

## Evidence Plan

`evaluation.md` records:

- baseline line/word/byte counts
- default loaded context before and after
- triggered loaded context before and after
- RED/GREEN result for fake progressive disclosure
- agent-legibility check: source-of-record path, verification path, recovery
  artifact
- evidence-backed best-practice table
- section mapping before and after
- Self-Check four-column result
- residual risks
