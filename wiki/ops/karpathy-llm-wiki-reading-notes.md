---
title: karpathy-llm-wiki / reading-notes
type: learning
canonical_object: karpathy-llm-wiki
artifact_type: reading-notes
language: zh-CN
audience: self
knowledge_level: working
domain: wiki
status: active
confidence: accepted
updated_at: 2026-05-08
ai_generated: true
derived_from:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
related_objects:
  - account-knowledge-base
  - harness-engineering-overview
notes_scope: Source-grounded learning from Karpathy's LLM Wiki gist. This page
  records the core wiki model and local transfer boundary; it does not invent a
  new implementation.
---

# Karpathy LLM Wiki / Reading Notes

## Source

| Field | Value |
|---|---|
| Title | LLM Wiki |
| URL | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Author / Publisher | Andrej Karpathy / GitHub Gist |
| Created At | 2026-04-04 |
| Accessed At | 2026-05-08 |
| Source Type | GitHub gist |
| Source Class | primary pattern source |
| Source Artifact Type | web-read source map |

## Core Claim

Wiki 的本质不是“资料夹”，也不是每次查询时临时检索 raw documents。

Karpathy 的核心模型是：

```text
raw sources
  -> LLM-maintained markdown wiki
  -> query / synthesis / new wiki pages
```

区别在于 compounding：知识不是每次从 raw documents 重新拼出来，而是被 LLM
持续编译进一个结构化、互相链接、可维护的 markdown 层里。

## Architecture

| Layer | Meaning | Local Translation |
|---|---|---|
| Raw sources | Immutable curated documents; source of truth | `wiki/sources`、外部链接、会议材料、飞书原文、附件 |
| Wiki | LLM-generated markdown pages: summaries, entities, concepts, comparisons, overview, synthesis | `wiki/ops`、`wiki/reports`、`wiki/examples` 等结构化页面 |
| Schema | Instructions telling the LLM structure, conventions, and workflows | repo instructions、skills、templates、gate-review contract |

## Operations

| Operation | Karpathy Model | Local Meaning |
|---|---|---|
| Ingest | Add one source; LLM summarizes and updates multiple existing pages plus index/log | 新文章或飞书材料进入时，不只写一页摘要，还要更新相关主题、索引和复用映射 |
| Query | Ask against the wiki; good answers can be filed back as pages | 分析、对比、结论不能只留在聊天里，值得保留时写回 wiki |
| Lint | Periodically check contradictions, stale claims, orphan pages, missing concepts, missing links | 周期性复查页面健康，不让 wiki 变成静态堆积 |
| Index / log | `index.md` is content-oriented; `log.md` is chronological | 本 repo 已有 index，但还缺一个清晰的 chronological wiki evolution log 模型 |

## Local Transfer

| Source Point | Local Usefulness | Boundary | Status |
|---|---|---|---|
| Wiki is a persistent compounding artifact | Replaces previous vague "工作环境 / harness" framing with a more precise knowledge-compilation model | Do not claim full auto-maintenance yet | accepted |
| Raw sources are immutable source of truth | Clarifies source pages versus generated wiki pages | Feishu/raw files may stay external, but references must remain traceable | accepted |
| LLM owns wiki maintenance, human owns sourcing and questions | Clarifies human/AI division | Current repo still uses human approval gates for public output | accepted |
| Ingest touches multiple pages | Explains why article learning should update index, topic page, gate-review, and output map | Avoid over-editing low-value sources | accepted |
| Query results can become pages | Supports preserving useful analysis instead of losing it in chat | Only durable insights should be written back | accepted |
| Periodic lint is core | Adds missing health-check narrative | Existing local validation is partial, not a full wiki lint loop | candidate |

## Correction To Current Draft

The prior Account Harness Wiki draft over-weighted the generic Harness
Engineering analogy. After reading this gist, the dominant claim should be:

> Account Harness Wiki is the persistent, compounding markdown layer between raw
> team sources and future questions/outputs.

Harness language can remain as a supporting analogy, but not as the essence.

## Output-Use Handoff

| Capability type | Learning point | Output use |
|---|---|---|
| `content` | Wiki is a persistent compounding artifact, not just retrieval or a folder | Opening definition and conclusion |
| `structure` | Explain raw sources -> wiki -> schema, then ingest/query/lint | Main article structure |
| `evidence` | Source traceability and log/index are proof mechanisms | Evidence section |
| `boundary` | Current local repo does not yet prove full LLM-owned maintenance | Non-claim section |
