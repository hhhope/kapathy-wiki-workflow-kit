---
canonical_object: report-wiki-product-plan
artifact_type: product-plan
related_objects:
- account-knowledge-base
- product-capability-and-graph-gap
- obsidian-wiki-reference-gap-review
- wiki-status-dashboard
derived_from:
- PROJECT.md
- wiki/ops/account-knowledge-base-workbench.md
- wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
- wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
---

# report-wiki product plan / 2026-05-09

## Product North Star

把散落在聊天、Feishu、会议、附件、报告草稿里的经验，变成可追溯、可复用、可验证、可发布的团队知识工作台。

更短的判断：

```text
not a folder
not a note dump
not a graph demo

but a report-wiki operating system:

source evidence
  -> structured knowledge
  -> agent-readable context
  -> reviewable output
  -> replayable behavior
```

## Target Users

| User | Primary Need | Product Promise |
|---|---|---|
| 决策者 / 负责人 | 快速知道当前材料、风险、缺口、下一步 | 给出可读状态和可审核结论 |
| 报告作者 | 从来源材料组织成汇报、H5、Feishu 审核稿 | 复用素材和结构，不反复重写 |
| Agent / Codex | 知道先读什么、什么能改、什么时候停 | 结构化上下文、OpenSpec 边界、回放证据 |
| 未来维护者 | 理解为什么这么分层、哪些决策已稳定 | ADR、ops trace、git history 可追踪 |

## Capability Map

```text
                 Report Wiki Product
                         |
   +----------+----------+----------+----------+----------+
   |          |          |          |          |          |
 Capture   Organize   Connect    Produce    Govern
   |          |          |          |          |
 inbox      sources    graph      reports    OpenSpec
 Feishu     domains    relation   Feishu     ADR
 meeting    timeline   routing    H5         replay
 chat       ops        status     review     archive
```

### Capability Definitions

| Capability | What It Does | Current State | Planning Priority |
|---|---|---|---|
| Capture | 接收 Feishu、会议、附件、chat、外部参考 | 基本可用，有 `sources` / `ops` / learning capture | P0 maintain |
| Organize | 把来源分到 source / domain / timeline / report / ops | 基本可用，但 account domain taxonomy 还薄 | P1 strengthen |
| Connect | 建立页面身份、关系、图谱、状态 | 有 covered-layer extractor，缺 whole-wiki product graph | P1 build |
| Produce | 生成汇报、审核稿、H5、一图流资产 | 已有报告门禁和 Feishu 图片边界 | P0 maintain |
| Govern | 管 OpenSpec、ADR、skill、replay、archive review | 强于普通 wiki，但状态面不足 | P1 status |

## Product Architecture

```text
Layer 0: Upstream Inputs
  chat / Feishu / meeting notes / docs / images / external repos
        |
        v
Layer 1: Evidence Store
  wiki/sources + inbox records + ops traces
        |
        v
Layer 2: Knowledge Structure
  domains + timeline + reports + examples
        |
        v
Layer 3: Agent-Readable Runtime
  naming -> frontmatter -> graph -> relation -> scoring -> routing
        |
        v
Layer 4: Delivery Surface
  review draft / Feishu text sync / H5 / visual assets
        |
        v
Layer 5: Governance
  OpenSpec / ADR / behavior replay / archive review / git history
```

The product should optimize the handoff between layers, not only the content inside one layer.

## Current Maturity

```text
L1 Memory             [########--]  source and ops records exist
L2 Structured Wiki    [#######---]  clear repo layers, domain taxonomy still thin
L3 Governed Agent Use [########--]  OpenSpec/replay strong, status weak
L4 Product Graph      [###-------]  covered graph exists, whole-wiki graph missing
L5 Operating System   [####------]  workflows exist, dashboard/query not productized
```

## Main Gaps

| Gap | Why It Blocks Alignment | Desired Product Shape |
|---|---|---|
| No source manifest | Cannot compute what changed, what is stale, what was produced | `manifest` ledger for source -> pages |
| No wiki status dashboard | "还有什么任务" still requires manual reconstruction | one status page/command for pending/stale/unlinked |
| Weak process graph | Many ops/process files lack stable identity and relation | relation hygiene report with unresolved identity counts |
| No whole-wiki lint | Broken links, orphan pages, stale pages are invisible | lint report for link/frontmatter/status hygiene |
| No cheap query workflow | Agent still reads ad hoc instead of from stable retrieval path | query skill: index -> summary -> grep -> full page |
| No hot cache | New sessions must crawl too much context | compact recent-state page maintained after major writes |
| Claim provenance uneven | Report synthesis can blur source fact vs inference | extracted / inferred / ambiguous convention for selected pages |

## Evolution Path

```text
Phase A: Alignment Baseline
  goal: everyone agrees what the product is
  output:
    - product plan
    - capability map
    - gap list
    - next OpenSpec candidates

Phase B: Computable Status
  goal: answer "what changed / what is pending / what is stale"
  output:
    - source manifest
    - wiki status dashboard
    - OpenSpec completion/archive-review status view

Phase C: Relation Hygiene
  goal: make process files connect as product objects
  output:
    - identity coverage report
    - relation coverage report
    - unresolved process-file queue
    - whole-wiki lint baseline

Phase D: Usable Graph
  goal: graph becomes a navigation and reasoning surface
  output:
    - graph export
    - readable graph summary
    - hub / orphan / bridge views
    - graph-backed reading route

Phase E: Operating Loop
  goal: every major write updates the working state
  output:
    - hot cache
    - query workflow
    - status-driven next-task selection
    - repeatable archive/review handoff
```

## Roadmap

| Horizon | Theme | Scope | Exit Criteria |
|---|---|---|---|
| Now | Product alignment | This plan, capability map, graph gap framing | Planning page exists and is linked from ops index |
| Next | Wiki status + relation hygiene | manifest/status/lint for repo wiki | Can answer pending/stale/unlinked without manual reconstruction |
| Next+1 | Graph productization | graph export and readable graph report | Graph shows hubs, bridges, orphan/process gaps |
| Later | Query and hot cache | cheap retrieval path and recent-state cache | Agent starts from status/query instead of full crawl |
| Later | Cross-agent memory | controlled Codex/Claude history ingestion | Decisions stop being trapped in transcripts |

## First OpenSpec Candidate

Recommended first scoped change:

```text
add-wiki-status-and-relation-hygiene
```

Why this first:

- It directly answers "还有什么任务".
- It turns the graph complaint into measurable unresolved identity / relation counts.
- It creates a base for query, graph viewer, hot cache, and source manifest.
- It avoids jumping straight into graph UI before the underlying page identity is reliable.

Minimal first version:

```text
input:
  wiki/**/*.md
  openspec changes/specs

compute:
  page identity coverage
  relation coverage
  source/report/ops counts
  unresolved identity warnings
  active/completed OpenSpec state
  dirty task-related vs unrelated local state note

output:
  markdown status report
  JSON artifact for later automation
```

## Non-Goals

- Do not replace the current `sources/domains/timeline/reports/ops` taxonomy.
- Do not migrate the repo to Obsidian `[[wikilinks]]` by default.
- Do not claim graph-based semantic understanding before relation hygiene exists.
- Do not sync image-bearing Feishu documents as part of product planning.
- Do not treat external examples as accepted rules without local evidence.

## Alignment Statement

The next product step should make the current wiki state computable. Once status and relation hygiene exist, graph, query, hot cache, and cross-agent ingestion become incremental product surfaces rather than isolated automation experiments.
