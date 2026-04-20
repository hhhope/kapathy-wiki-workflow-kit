---
canonical_object: wiki-runtime-context-source-integration
artifact_type: method
formalizes:
- wiki-runtime-context-source-integration
derived_from:
- wiki-runtime-context
- wiki-utilization-layer
---

# wiki-runtime-context-source-integration / method

这页定义当前仓库在演变型页面上的最小 runtime-context source-integration workflow。

目标不是做外部 retrieval，也不是把上下文自动注入每个 agent 入口，而是在 runtime
context 之后增加一层 repo-local 的 source resolution，让 agent 可以直接拿到下一步应读的具体页面路径。

## 依赖顺序

runtime context source integration 明确是 runtime context 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis
5. semantic scoring
6. utilization layer
7. runtime context

## 最小 source-integrated runtime 合同

source-integrated runtime artifact 至少保留：

- `summary`
- `preferred_sources`
- `supporting_sources`
- `blocked_objects`
- `source_resolution_notes`
- `proof_boundary_notes`

### `summary`

至少包含：

- preferred / supporting / blocked counts
- whether caution is active
- whether direct source inspection is still required

### `preferred_sources`

优先阅读对象的 source resolution 结果，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`
- `resolved_sources`

### `supporting_sources`

只能作为 supporting context 的 source resolution 结果，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`
- `resolved_sources`

### `blocked_objects`

当前不应进入 first-pass source selection 的对象，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`

### `resolved_sources`

每个 resolved source 至少保留：

- `page_path`
- `artifact_type`
- `source_layer`

## Version 1 Resolution Model

第一版只解析仓库内已 formalize 的 repo-visible sources：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

解析规则保持 deterministic，不做语义猜测。

### 排序规则

同一个 canonical object 的 source resolution 按固定顺序输出：

1. `method`
2. `adr`
3. `spec`
4. `runtime-rule`
5. `example`
6. `sample`
7. `runtime-validation`
8. `replay-harness`
9. `replay-validation`
10. 其他已识别 artifact type

第一版不为 `blocked_objects` 解析 first-pass reading targets。

## 运行方式

直接基于 live runtime context 运行：

```bash
python3 scripts/resolve_runtime_context_sources.py
```

或基于已有 runtime-context artifact：

```bash
python3 scripts/resolve_runtime_context_sources.py scripts/examples/agent_readable_wiki_runtime_context_sample.json
```

生成 sample artifact：

```bash
python3 scripts/resolve_runtime_context_sources.py > scripts/examples/agent_readable_wiki_runtime_context_source_integration_sample.json
```

## 当前 proof 边界

runtime context source integration 在 v1 只能证明：

- 当前 runtime context 可以被 repo-local source refs 补全
- preferred 和 supporting 对象可以稳定落到真实页面路径
- blocked 对象仍然保持隔离

它不能证明：

- 外部 source retrieval 已集成
- agent 会自动把这些 source 注入 live context
- unresolved 页面已经被理解
- runtime autonomy 已准备好

## 当前非目标

第一版不做这些事：

- 不接 Feishu 或其他外部系统
- 不做向量索引
- 不做自动 prompt/context 注入
- 不做 blocked 对象自动晋升

## 一句话判断

`先把 runtime context 解析成应读的 repo-local source refs，再谈外部 source integration。`
