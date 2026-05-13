---
canonical_object: wiki-semantic-scoring
artifact_type: method
layer: ops
domain: none
ops_area: wiki-runtime
formalizes:
- wiki-semantic-scoring
---

# wiki-semantic-scoring / method

这页定义当前仓库在演变型页面上的最小 semantic-scoring workflow。

目标不是做 embeddings，也不是直接驱动 retrieval 或 runtime 行为，而是在
relation analysis 之上增加一层透明、可审计的对象强度分层，让 agent 可以低成本判断：

- 哪些 canonical object 已经形成较强的语义覆盖
- 哪些对象仍然只是结构存在、语义上偏薄
- 当前仓库的 unresolved 结构还在多大程度上限制更强语义理解

## 依赖顺序

semantic scoring 明确是 relation analysis 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis

## 覆盖范围

第一版 semantic scoring 只评分 relation analysis 已覆盖的 canonical object。

## 最小评分输出合同

semantic-scoring artifact 至少保留：

- `summary`
- `repository_context`
- `object_scores`
- `scoring_notes`

### `summary`

至少包含：

- scored object count
- score range
- strong / moderate / weak object counts

### `repository_context`

至少包含：

- unresolved warning pressure
- source relation-analysis summary

### `object_scores`

每个 canonical object 至少保留：

- `semantic_score`
- `score_band`
- `factor_breakdown`
- `coverage_snapshot`

### `scoring_notes`

显式保留 proof boundary，避免把评分误说成 retrieval proof 或语义真值。

## Version 1 Factor Model

第一版使用显式、可审计的 rule-based 因子，满分 `10`：

- `cross_layer_presence`: `0-3`
- `artifact_type_variety`: `0-2`
- `relation_presence`: `0-2`
- `formalization_depth`: `0-3`

这些分数只来自仓库内已 formalize 的结构证据，不来自 embeddings 或外部模型。

## 运行方式

直接基于 live relation analysis 运行：

```bash
python3 scripts/score_wiki_semantics.py
```

或基于已有 relation-analysis artifact：

```bash
python3 scripts/score_wiki_semantics.py scripts/examples/agent_readable_wiki_relation_analysis_sample.json
```

生成 sample artifact：

```bash
python3 scripts/score_wiki_semantics.py > scripts/examples/agent_readable_wiki_semantic_scoring_sample.json
```

## 当前 proof 边界

semantic scoring 在 v1 只能证明：

- canonical object 在仓库证据里的相对强弱
- 分数来自哪些明确结构因子
- unresolved 结构仍然在限制更强语义判断

它不能证明：

- unresolved 页面已经被理解
- score 等于 retrieval quality
- score 足以驱动 runtime routing
- 仓库已经具备语义图谱完备性

## 当前非目标

第一版不做这些事：

- 不做 embeddings
- 不做 LLM scoring
- 不做 retrieval integration
- 不做自动 rewrite 或 auto-promotion

## 一句话判断

`先把对象强弱的显式语义评分稳定下来，再谈 retrieval 和 agent 利用层。`
