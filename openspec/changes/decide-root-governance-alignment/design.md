## Context

Phase 0 explicitly deferred root dotfiles. That was the correct move for repo
acceptance, but it was also a deferral, not a permanent closure.

If the whole `agents-governance-drift` topic is to be closed, the repository
still needs to answer:

- should root dotfiles align to the repo mainline
- should they remain intentionally different
- if different, what is the principled split

## Goals / Non-Goals

**Goals**

- Resolve repo-vs-root governance alignment as a stable decision.
- Preserve a clear ownership split between repo policy and root defaults.
- Avoid leaving root drift as an unspoken tail.
- Define the SDD-first sequence for personal global `AGENTS.md`, skill
  skeleton, and replay-harness collaboration.

**Non-Goals**

- Do not merge repo and root guidance into one file.
- Do not redesign all personal/global tooling defaults.
- Do not reopen repo Phase 0.
- Do not publish a wiki method page or ADR before the design boundary is
  accepted.
- Do not edit `~/.codex/AGENTS.md`, `~/.claude/CLAUDE.md`, or any skill in this
  design step.

## Decisions To Resolve

### Decision: Alignment model

Selected model: hybrid split with explicit ownership.

The repo may record the relationship between repo governance and root dotfiles,
but it does not own the full content of personal global dotfiles. Root files may
align on shared safety boundaries while keeping personal or agent-specific
behavior separate.

Required alignment:

- root files must not contradict repo-owned boundaries when operating inside
  this repository
- root files should treat repo `AGENTS.md` and `PROJECT.md` as the source of
  repo-specific workflow semantics
- behavior-asset changes need evaluation before being treated as complete

Allowed divergence:

- personal global startup preferences
- agent-specific capability differences
- cross-repo defaults that are not specific to this repository
- local machine paths, provided they are not mistaken for repo policy

### Decision: Update burden

If alignment is required, define the minimum update set rather than a broad
rewrite.

For this change, the first update burden is SDD evidence only. Root dotfile
edits are deferred until this design has enough evaluation evidence to avoid
turning the global file into another accumulation surface.

### Decision: SDD-first before implementation

The current work must proceed in this order:

1. OpenSpec proposal/design/tasks/evaluation define the boundary.
2. Evaluation records the previous failure mode and the desired after state.
3. Only then may a later step edit root dotfiles, repo skills, or repo guidance.

This prevents a chat-level plan from becoming an immediate global behavior
change without a spec/design checkpoint.

### Decision: Three-layer collaboration model

The personal global collaboration model has three layers:

- `AGENTS.md` as an entry card: scope, hard stops, startup gates, git truth
  rules, and routing to deeper assets
- `SKILL.md` as compact behavior contracts: trigger-only descriptions, hard
  rules, anti-triggers, and pointers to references
- replay harness as evidence: RED/GREEN behavior records and proof boundaries,
  not hooks, runtime gates, or automatic enforcement

### Decision: Wiki landing remains gated

Do not land this design directly as a wiki method page. Wiki remains available
for trace or retro material when the conversation needs durable recovery, but
method or ADR promotion requires a stable decision after this OpenSpec design
is accepted.

The immediate durable surface is this active change. If later review finds that
the live correction itself must be preserved beyond the change artifacts, add a
targeted `wiki/ops retro` rather than promoting the design straight to ADR.

## Evaluation Plan

- RED baseline: the agent jumps from chat design into implementation, or treats
  wiki publication as the default landing zone before SDD.
- GREEN result: the agent records SDD boundaries first, keeps wiki landing
  gated, and defers root dotfile edits.
- Residual risk: the accepted design still needs later pressure testing before
  changing behavior assets.
