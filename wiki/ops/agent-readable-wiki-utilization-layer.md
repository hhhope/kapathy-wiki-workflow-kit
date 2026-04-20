---
canonical_object: wiki-utilization-layer
artifact_type: method
formalizes:
- wiki-utilization-layer
---

# wiki-utilization-layer / method

这页定义当前仓库在演变型页面上的最小 agent-utilization workflow。

目标不是做 retrieval 系统，也不是做 runtime 自动路由，而是在 semantic scoring
之后增加一层可执行的 agent 使用指导，让 agent 可以低成本判断：

- 哪些 canonical object 现在值得优先读
- 哪些对象只能谨慎使用
- 哪些对象当前应被阻断，不该拿来做更强判断

## 依赖顺序

utilization layer 明确是 semantic scoring 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis
5. semantic scoring

## 最小利用输出合同

utilization artifact 至少保留：

- `summary`
- `repository_caution`
- `object_utilization`
- `utilization_notes`

### `summary`

至少包含：

- object count
- preferred / cautious / blocked counts

### `repository_caution`

至少保留：

- unresolved warning pressure
- whether repository-wide caution is active

### `object_utilization`

每个 canonical object 至少保留：

- `utilization_band`
- `reasons`
- `source_semantic_score`
- `usage_guidance`

### `utilization_notes`

显式保留 proof boundary，避免把利用指导误说成 retrieval readiness 或 runtime autonomy。

## Version 1 Banding Model

第一版 banding 使用显式 rule-based 规则：

- `preferred`
  - strong semantic score
  - cross-layer evidence is present
  - formalization depth is not thin
- `cautious`
  - object has some usable evidence
  - but repository pressure or object thinness still limits trust
- `blocked`
  - object is too thin or too local to support stronger agent use

## 运行方式

直接基于 live semantic scoring 运行：

```bash
python3 scripts/derive_wiki_utilization.py
```

或基于已有 semantic-scoring artifact：

```bash
python3 scripts/derive_wiki_utilization.py scripts/examples/agent_readable_wiki_semantic_scoring_sample.json
```

生成 sample artifact：

```bash
python3 scripts/derive_wiki_utilization.py > scripts/examples/agent_readable_wiki_utilization_sample.json
```

## 当前 proof 边界

utilization layer 在 v1 只能证明：

- 当前仓库里哪些 canonical object 更适合作为 agent 阅读候选
- 哪些对象需要谨慎使用
- 哪些对象现在还不该支撑更强判断

它不能证明：

- retrieval 已经准备好
- runtime 路由可以自动化
- unresolved 页面已经被理解
- agent 可以跳过直接 source inspection

## 当前非目标

第一版不做这些事：

- 不做 retrieval engine
- 不做 runtime automation
- 不做 autonomous page promotion
- 不做 unresolved page semantic expansion

## 一句话判断

`先把 agent 怎么用这些 artifact 讲清楚，再谈自动取材和自动路由。`
