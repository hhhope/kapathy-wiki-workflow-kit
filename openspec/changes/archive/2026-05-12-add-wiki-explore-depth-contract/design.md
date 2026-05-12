## Context

Current wiki runtime surfaces have separate responsibilities:

- `wiki-query`: bounded retrieval from status, route, context, and explicit text
  search evidence.
- `openspec-explore`: an OpenSpec exploration stance for thinking before or
  during a change.
- `public-report-quality-gate`: reader-facing output quality gate.

None of these owns the specific behavior the user wants from `wiki:explore`:
when a wiki-backed topic is explored, the response should identify the current
object, open the relevant repo-visible evidence, show the evidence surface, and
judge whether the exploration is deep enough for the requested use.

## Decision

Create an independent `wiki-explore` skill.

`wiki-explore` is not a replacement for `wiki-query`. It may call or reference
`wiki-query` evidence, but it adds an exploration-depth contract and an
enoughness judgment.

## Trigger Model

Primary trigger:

- The user explicitly invokes `wiki:explore`.

Secondary trigger:

- The conversation is already in a wiki-backed exploration, source review,
  report repair, or governance replay context, and the user rejects the answer
  as shallow, incomplete, off-target, or "not enough".

Non-trigger:

- Ordinary one-off file lookup, status check, queue preview, or bounded context
  retrieval. Those remain `wiki-query`, `wiki-status`, `wiki-queue`, etc.

## Required Output Contract

Every `wiki-explore` answer should include:

- Current object: the exact wiki-backed topic/thread being explored.
- Opened evidence: concrete files, source groups, specs, or skills opened.
- Evidence surface: whether source map, public timeline, broad source pool,
  podcast/video pool, evidence matrix, gate review, output draft, and residual
  risk artifacts exist.
- Enoughness judgment: enough for what, not enough for what, and why.
- Next boundary: continue exploration, harden sources, open an OpenSpec change,
  repair a report, or stop.

## Public Source Depth

When the explored topic depends on public material, `wiki-explore` must
separate:

- primary sources;
- secondary/media sources;
- candidate leads;
- transcript or upstream-capture gaps;
- internal synthesis or gate-review evidence.

It must not convert "we have a source pool" into "this is public-ready".

## Reference Replay

The GREEN replay standard is the `agentic-product-engineering-collaboration`
thread:

- source map;
- 95-entry public timeline;
- 36-entry podcast/video discussion pool;
- article evidence matrix;
- report gate review;
- residual risks and publication blockers.

The important behavior is not the exact artifact count. The important behavior
is that the response shows the evidence surface and tells the user what the
current material is enough for.

## Boundaries

- `wiki-explore` does not create, modify, archive, or queue OpenSpec changes by
  itself.
- It does not mark tasks complete or execute queued work.
- It may recommend a new OpenSpec change when a behavior or default workflow
  should change.
- It does not claim semantic search, embeddings, or hidden source ranking.
