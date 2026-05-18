---
canonical_object: wiki-runtime-context
artifact_type: method
layer: ops
domain: wiki
ops_area: wiki-runtime
formalizes:
- wiki-runtime-context
---

# wiki-runtime-context / method

这页定义当前仓库在演变型页面上的最小 runtime-context workflow。

目标不是做外部 retrieval 系统，也不是让 agent 自动路由，而是在 utilization
之后生成一个可直接阅读的 runtime context bundle，让 live agent 工作可以更低成本地拿到：

- first-pass preferred context
- supporting context with caution
- blocked context that should not anchor strong judgments
- repository-level caution notes

## 依赖顺序

runtime context 明确是 utilization 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis
5. semantic scoring
6. utilization layer

## 最小 runtime bundle 合同

runtime-context artifact 至少保留：

- `summary`
- `preferred_context`
- `supporting_context`
- `blocked_context`
- `runtime_caution`
- `runtime_notes`

### `summary`

至少包含：

- preferred / supporting / blocked counts
- whether caution is active

### `preferred_context`

优先阅读的 canonical object 候选，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`

### `supporting_context`

只能作为 supporting context 的对象，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`

### `blocked_context`

当前不应作为强锚点的对象，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`

### `runtime_caution`

至少保留：

- repository-wide unresolved pressure
- whether direct source inspection is still required

## 运行方式

直接基于 live utilization 运行：

```bash
python3 scripts/build_wiki_runtime_context.py
```

或基于已有 utilization artifact：

```bash
python3 scripts/build_wiki_runtime_context.py scripts/examples/agent_readable_wiki_utilization_sample.json
```

生成 sample artifact：

```bash
python3 scripts/build_wiki_runtime_context.py > scripts/examples/agent_readable_wiki_runtime_context_sample.json
```

## 当前 proof 边界

runtime-context layer 在 v1 只能证明：

- 仓库可以把现有 artifact 栈打包成一个 bounded runtime bundle
- preferred、supporting、blocked 仍然保持分离
- caution 不会被打平

它不能证明：

- retrieval 已完成
- agent 可以自动选完上下文就做最终判断
- runtime 路由已经自治
- unresolved 页面已经被理解

## 当前非目标

第一版不做这些事：

- 不做外部检索系统
- 不做 runtime auto-integration
- 不做 agent 自动取材执行
- 不做 blocked 对象自动晋升

## 一句话判断

`先把 runtime-ready context bundle 做出来，再谈自动检索和自动路由。`
