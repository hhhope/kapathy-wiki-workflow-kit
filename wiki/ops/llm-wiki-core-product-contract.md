---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: llm-wiki-core-product-contract
artifact_type: product-contract
related_objects:
- report-wiki-product-plan
- obsidian-wiki-reference-gap-review
- product-capability-and-graph-gap
- learning-source-routing-gap
derived_from:
- PROJECT.md
- wiki/ops/report-wiki-product-plan-2026-05-09.md
- wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
- wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
- /home/yan/.gstack/projects/clearing-account-meeting-lore/yan-feat-refine-openspec-explore-trace-model-design-20260509-114904-llm-wiki-core-value.md
status: draft
---

# LLM Wiki core product contract

## North Star

LLM Wiki 的核心价值不是自动学习外部 repo，也不是自动开 change。

核心价值是：

```text
把分散、易丢、难复用的材料，编译成下一次 LLM 能直接使用的可信上下文。
```

短句：

```text
LLM Wiki = durable compiled context for agents and humans.
```

对用户的承诺：

```text
你不用每次重新解释背景。
你不用靠聊天记录找证据。
你不用担心 agent 把草稿、推断、结论、交付状态混在一起。

材料进入 wiki 后，下一次 agent 能知道：
- source 在哪
- 已经抽取了什么
- 哪些是事实，哪些是推断，哪些有争议
- 这些知识和哪些报告、决策、流程有关
- 当前该读什么，不该读什么
- 哪些输出能复用这些知识
```

## Core Loop

```text
┌──────────────┐
│ 1. Capture   │  收材料：Feishu / meeting / article / repo / image / chat
└──────┬───────┘
       v
┌──────────────┐
│ 2. Compile   │  编译：source -> wiki object -> relation -> provenance
└──────┬───────┘
       v
┌──────────────┐
│ 3. Retrieve  │  取用：index / summary / query / hot cache / routing
└──────┬───────┘
       v
┌──────────────┐
│ 4. Apply     │  应用：报告 / Feishu / H5 / decision / runtime behavior
└──────────────┘
```

判断句：

```text
Capture once. Compile once. Retrieve cheaply. Apply safely.
```

## Core Capability Checklist

```text
LLM Wiki Core
  |
  +-- Capture
  |     +-- source intake
  |     +-- source metadata
  |     +-- source manifest / delta
  |
  +-- Compile
  |     +-- durable wiki pages
  |     +-- relation / links
  |     +-- provenance: extracted / inferred / ambiguous
  |     +-- lifecycle / confidence
  |
  +-- Retrieve
  |     +-- index
  |     +-- summary frontmatter
  |     +-- cheap query path
  |     +-- hot cache
  |     +-- agent reading route
  |
  +-- Apply
        +-- report draft
        +-- Feishu review text
        +-- H5 / visual output
        +-- OpenSpec context
        +-- behavior replay evidence
```

## Core Versus Enhancement

学习能力是 LLM Wiki 上的增强能力，不是北极星。

```text
External source / repo / article
        |
        v
Agent reads and extracts reusable learning
        |
        v
LLM Wiki stores source, learning, relation, and boundary
        |
        v
Agent can later reuse it for output, planning, or change suggestions
```

增强能力包括：

```text
- agent self-service learning
- learning-to-output reuse map
- learning-to-change suggestions
- scorecard calibration
- relation lint / graph hygiene
- dashboard / status automation
- parallel OpenSpec queue
```

这些能力都重要，但都要服务于核心闭环。

## obsidian-wiki Comparison

`Ar9av/obsidian-wiki` 的价值不是 Obsidian UI，而是它保持了紧凑的 LLM Wiki
闭环：raw sources 进入 compiled wiki，再通过 manifest、status、query、
lint、hot cache 维持可用。

| Core Loop | obsidian-wiki | This repo now | Gap |
|---|---|---|---|
| Capture | raw sources, PDFs, images, histories | Feishu, meetings, reports, articles, repos | capture exists, but not ledged consistently |
| Compile | markdown wiki with sources, summary, provenance | wiki pages, ops traces, reports, ADRs | strong governance, uneven ordinary wiki provenance |
| Retrieve | index, frontmatter summary, query, hot cache | AGENTS routing, wiki index, grep/read | retrieval is agent-heavy and ad hoc |
| Apply | mainly wiki answers and graph exploration | reports, Feishu, H5, runtime behavior | local Apply layer is stronger |
| Status | manifest, delta, lint, insights | OpenSpec tasks plus scattered ops | no single wiki status surface |

结论：

```text
obsidian-wiki teaches us how to keep compiled knowledge fresh and queryable.

this repo adds a stronger Apply layer:
report delivery, Feishu boundaries, OpenSpec, ADR, replay.

therefore this repo should not copy obsidian-wiki.
it should become an LLM Wiki for report work.
```

## Current Repo Strengths

```text
Capture       medium
Compile       medium
Retrieve      weak to medium
Apply         strong
Governance    strong
Learning      medium
Orchestration weak
```

Interpretation:

```text
Delivery and governance are already unusually strong.
The missing core LLM Wiki value is not another gate.
The missing core is source freshness, compiled knowledge hygiene,
cheap retrieval, and current context.
```

## Core Gaps

| Gap | Core Loop | Why It Matters |
|---|---|---|
| Source manifest / delta status | Capture | Cannot know what changed, what is stale, or what was produced without manual reconstruction. |
| Compiled object provenance | Compile | Ordinary wiki claims can blur extracted fact, agent inference, ambiguity, and human conclusion. |
| Cheap query route | Retrieve | Future agents still over-read AGENTS, OpenSpec, ops pages, and full wiki pages. |
| Hot/current context | Retrieve | Session continuity depends on chat memory or recent git archaeology. |
| Wiki status surface | Retrieve / Apply | "还有什么任务" is still reconstructed rather than read from a stable status artifact. |

## Enhancement Backlog

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

Main correction:

```text
learning-to-change orchestration is P2, not the product north star.
```

## Next OpenSpec Candidates

Recommended ordering:

```text
1. add-source-manifest-and-wiki-status
   target: Capture / Retrieve
   why: makes source freshness and pending work visible

2. add-wiki-query-and-current-context
   target: Retrieve
   why: reduces repeated full-context crawling

3. add-compiled-object-provenance
   target: Compile
   why: separates extracted fact, inference, ambiguity, and conclusion

4. recalibrate-scorecards-by-target-state
   target: Apply enhancement
   why: prevents source admission, output quality, client proof, and runtime proof from mixing

5. add-relation-lint-and-graph-hygiene
   target: Compile / Retrieve enhancement
   why: makes process files and wiki relations visible before graph UI

6. add-learning-to-change-orchestration
   target: P2 advanced agent work
   why: useful after the core context layer can support reliable change suggestions
```

## Non-Goals

This contract does not implement:

```text
- manifest generator
- query skill
- hot cache generator
- graph UI
- scorecard edits
- learning-to-change queue
- historical page migration
- Feishu sync behavior
```

## Usage Rule

When future work says "继续做 LLM Wiki 产品化", start here.

Do not jump directly to graph, scorecard, Feishu, or change queue unless the
current OpenSpec explicitly selects that enhancement.
