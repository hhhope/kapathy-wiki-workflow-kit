# OpenSpec Router Design

> Supports OpenSpec change: `add-openspec-router-governance`.
> This artifact starts as workflow-repair design and remains secondary to
> OpenSpec lifecycle state.

## Context

This repository uses OpenSpec as the lifecycle source of truth and also uses
Superpowers methods for brainstorming, planning, TDD, and execution discipline.
The current failure mode is that both are valid, but there is no explicit
pre-action router that decides which gate owns the next move.

The incident this design prevents:

```text
$superpowers:brainstorming
可以继续做
```

The agent read the brainstorming skill, but then treated the later approval as
permission to write OpenSpec artifacts and commit. That preserved some OpenSpec
discipline, but bypassed the Superpowers brainstorming gate.

## Design Goal

Add a small repo-local skill named `openspec-router` and bind it through
OpenSpec governance.

The router does not replace Superpowers, OpenSpec, or AGENTS.md:

- Superpowers owns method discipline: brainstorming, planning, TDD, execution,
  review, and written-spec review gates.
- OpenSpec owns authoritative lifecycle state: proposal, design, specs, tasks,
  verification, completion, and archive.
- AGENTS.md owns repo engineering discipline: health checks, git truth checks,
  validation, commit behavior, and repo-local hard stops.

## Approaches Considered

### Recommended: Small Router Skill + OpenSpec Governance

Add `openspec-router` as a compact pre-action gate and make AGENTS/OpenSpec
point to it.

Pros:

- Fixes the exact bypass pattern.
- Keeps OpenSpec as lifecycle truth source.
- Keeps Superpowers as method discipline.
- Leaves a replayable behavior contract.

Cons:

- Still depends on future agents loading the skill.

### Alternative: Add Only More AGENTS Text

Add a section to AGENTS.md without a dedicated skill.

Pros:

- Always visible in loaded repo instructions.

Cons:

- Adds more weight to an already large file.
- Does not give a focused trigger surface for mixed Superpowers/OpenSpec work.

### Alternative: Rely Only on Superpowers

Treat the Superpowers skill as sufficient.

Pros:

- No new repo-local behavior asset.

Cons:

- Already failed in the current incident.
- Does not clarify how Superpowers and OpenSpec interact in this repo.

## Router Flow

Before edits, implementation, verification, archive, or completion claims, the
router answers:

1. Intent: what is the user asking for now?
2. Gate: what class of action is allowed next?
3. Route line: what compact route should be visible to the user?

Intent values:

- `explore`
- `brainstorm`
- `propose`
- `implement`
- `verify`
- `archive`
- `repair-workflow`

Gate values:

- `read-only`
- `ask-or-present`
- `write-superpowers-spec`
- `write-openspec-change`
- `implement`
- `verify`
- `complete`

## Hard Rules

1. If `$superpowers:brainstorming` is active, OpenSpec is read-only until the
   Superpowers written design/spec review gate passes.
2. Short approvals such as `可以`, `继续`, `确认`, `做吧`, and `go` advance only
   the current gate.
3. Superpowers artifacts are secondary working material. Accepted lifecycle
   state must be copied into OpenSpec before implementation or archive claims.
4. OpenSpec remains the source of truth for large changes.
5. Implementation requires an active OpenSpec change with clear tasks unless
   the task is explicitly small and outside OpenSpec scope.

## Scenario Replay Requirements

Replay must cover:

- Brainstorming request.
- Short approval during design.
- Continue after design approval.
- Implementation request.
- Verification request.
- Archive request.
- The original incident.

The expected original-incident route is:

```text
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.
```

## Decision

Use the recommended approach: small router skill plus OpenSpec governance.
