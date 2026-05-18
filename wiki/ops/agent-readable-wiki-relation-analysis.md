---
canonical_object: wiki-relation-analysis
artifact_type: method
layer: ops
domain: wiki
ops_area: wiki-runtime
formalizes:
- wiki-relation-analysis
---

# wiki-relation-analysis / method

这页定义当前仓库在演变型页面上的最小 relation-analysis workflow。

目标不是做语义理解，也不是直接驱动 runtime agent 行为，而是在 graph
extraction 之上增加一层稳定的结构分析，让 agent 可以低成本判断：

- 哪些 canonical object 已经形成跨层覆盖
- 哪些对象仍然偏弱或碎片化
- typed relation 是否已经在真实页面里出现
- unresolved 结构主要堆在哪些层

## 依赖顺序

relation analysis 明确是 graph extraction 之后的下游层，依赖：

1. `canonical object / artifact type` 命名模型
2. 最小 frontmatter 与 typed relation fields
3. graph extraction

## 覆盖范围

第一版 relation analysis 只分析 graph extraction 已覆盖的层：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

## 最小分析输出合同

分析 artifact 至少保留：

- `summary`
- `object_coverage`
- `artifact_type_distribution`
- `relation_type_distribution`
- `unresolved_warning_summary`
- `analysis_notes`

### `summary`

至少包含：

- analyzed node count
- analyzed edge count
- unresolved warning count
- canonical object count
- cross-layer object count

### `object_coverage`

每个 canonical object 至少保留：

- `node_count`
- `source_layers`
- `artifact_types`
- `relation_count`

### `artifact_type_distribution`

按 artifact type 聚合节点数量。

### `relation_type_distribution`

按 typed relation 聚合边数量。

### `unresolved_warning_summary`

至少按 layer 汇总 unresolved identity warning 数量。

### `analysis_notes`

显式保留 proof boundary，避免把结构分析误说成语义理解或 rollout proof。

## 运行方式

直接基于 live extractor 运行：

```bash
python3 scripts/analyze_wiki_relations.py
```

或基于已存在的 graph artifact：

```bash
python3 scripts/analyze_wiki_relations.py scripts/examples/agent_readable_wiki_graph_sample.json
```

生成 sample artifact：

```bash
python3 scripts/analyze_wiki_relations.py > scripts/examples/agent_readable_wiki_relation_analysis_sample.json
```

## 当前 proof 边界

relation analysis 在 v1 只提供结构层信号。

它可以证明：

- 哪些对象已跨层出现
- 哪些 typed relation 已经真实落地
- unresolved 结构主要堆在哪些层

它不能证明：

- unresolved 页面已经被语义理解
- object quality 已经等于 retrieval quality
- graph analysis 足以驱动 runtime routing
- 这已经是 rollout proof

## 当前非目标

第一版不做这些事：

- 不做 graph viewer
- 不做 embedding 或 semantic similarity scoring
- 不做自动 page rewrite
- 不把 unresolved warning 强行解释成已理解节点

## 一句话判断

`先把结构分析稳定下来，再谈语义图谱和 agent 利用层。`
