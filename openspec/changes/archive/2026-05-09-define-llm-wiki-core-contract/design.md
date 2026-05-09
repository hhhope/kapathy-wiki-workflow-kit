## Context

The repository already has several strong layers:

- `wiki/` stores durable report knowledge, sources, reports, examples, and ops
  traces.
- OpenSpec owns scoped workflow changes and task progress.
- ADRs own stable decisions.
- Existing agent-readable wiki specs cover naming, frontmatter, graph
  extraction, relation analysis, scoring, runtime context, routing, context
  injection, and self-directed execution.
- Report delivery workflows cover Feishu text sync boundaries, H5/report drafts,
  visual assets, and behavior replay evidence.

The missing product-level contract is not another gate. It is a compact answer
to what the LLM Wiki exists to do before enhancements compete for priority.

## Decision

Define the repository's LLM Wiki core as:

> Durable compiled context for agents and humans.

The core loop is:

```text
Capture once -> Compile once -> Retrieve cheaply -> Apply safely
```

This means the repository should optimize for material entering once, becoming a
traceable wiki object with provenance and relations, being retrievable by future
agents without full recrawl, and being safely reused in reports, Feishu review
texts, H5/visual outputs, OpenSpec context, and runtime behavior evidence.

## Core Versus Enhancement

Core capabilities:

- Capture: source intake, source metadata, source manifest/delta direction.
- Compile: durable wiki pages, relations, links, provenance, lifecycle, and
  confidence boundaries.
- Retrieve: indexes, summaries, query routes, hot/current context, and agent
  reading routes.
- Apply: reports, Feishu review text, H5/visual outputs, OpenSpec context, and
  behavior replay evidence.

Enhancements:

- Agent self-service learning.
- Learning-to-output reuse maps.
- Learning-to-change suggestions or orchestration.
- Scorecard calibration by target state.
- Relation lint, graph hygiene, dashboards, and graph-backed planning.

The enhancements are valid backlog items, but they must not replace the core
north star.

## Reference Comparison

`Ar9av/obsidian-wiki` is useful because it demonstrates a tight LLM Wiki loop:
raw sources become compiled wiki pages; manifest/status/query/lint/hot-cache
style surfaces keep the compiled wiki fresh and usable.

This repository should not copy the full taxonomy or become an Obsidian clone.
The local product differs because its Apply layer is stronger: report drafts,
Feishu boundaries, H5/visual output, OpenSpec, ADRs, and behavior replay are
first-class delivery concerns.

The useful transfer is:

- Source manifest / delta status belongs to Capture.
- Provenance and lifecycle fields belong to Compile.
- Cheap query route and hot/current context belong to Retrieve.
- Output/replay/gate boundaries belong to Apply.

## First Artifact

Add `wiki/ops/llm-wiki-core-product-contract.md` as the repo-visible product
contract. It should include:

- North star.
- Core loop.
- Capability checklist.
- `obsidian-wiki` comparison reframed by loop stage.
- Current repo strengths.
- Core gaps.
- Enhancement backlog.
- Next OpenSpec candidates.

## Boundaries

This change is a product contract and alignment baseline. It does not implement
the backlog items it identifies.

Out of scope:

- Manifest generator.
- Query skill or CLI.
- Hot cache generator.
- Graph UI or whole-wiki graph export.
- Scorecard file changes.
- Learning-to-change queue implementation.
- Historical page migration or re-scoring.
- Feishu sync behavior.

## Follow-Up Ordering

Recommended backlog after this contract:

```text
P0 Core
  - source manifest / delta status
  - wiki status surface
  - cheap query route
  - hot/current context

P1 Enhancements
  - agent self-service learning intake
  - learning-to-output reuse map
  - scorecard calibration by target state
  - relation lint / graph hygiene

P2 Advanced Agent Work
  - learning-to-change orchestration
  - parallel OpenSpec queue
  - cross-agent history ingest
  - graph-backed planning
```
