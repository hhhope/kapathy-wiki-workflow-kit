---
canonical_object: wiki-runtime-auto-routing
artifact_type: method
formalizes:
- wiki-runtime-auto-routing
derived_from:
- wiki-runtime-context-source-integration
- wiki-runtime-context
---

# wiki-runtime-auto-routing / method

这页定义当前仓库在演变型页面上的最小 runtime auto-routing workflow。

目标不是做自动 prompt 注入，也不是让 agent 自治执行，而是在 runtime context source
integration 之后增加一层 repo-local 的 route staging，让 agent 明确知道：

- 哪些 source 应该 first-pass 打开
- 哪些 source 应该 second-pass 再看
- 哪些 blocked object 现在不应进入 first-pass routing

## 依赖顺序

runtime auto routing 明确是 runtime context source integration 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis
5. semantic scoring
6. utilization layer
7. runtime context
8. runtime context source integration

## 最小 runtime auto-routing 合同

runtime auto-routing artifact 至少保留：

- `summary`
- `open_first`
- `open_next`
- `do_not_open_first`
- `routing_notes`
- `proof_boundary_notes`

### `summary`

至少包含：

- open-first / open-next / blocked counts
- whether caution is active
- whether direct source inspection is still required

### `open_first`

first-pass 应打开的 source route，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`
- `route_sources`

### `open_next`

second-pass 可继续阅读的 source route，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`
- `route_sources`

### `do_not_open_first`

当前不应进入 first-pass route 的对象，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`

### `route_sources`

每个 routed source 至少保留：

- `page_path`
- `artifact_type`
- `source_layer`

## Version 1 Routing Model

第一版 routing 使用显式 banding：

- `preferred_sources` -> `open_first`
- `supporting_sources` -> `open_next`
- `blocked_objects` -> `do_not_open_first`

第一版不做这些事情：

- 不跨 band 重排对象
- 不覆盖 source integration 的 deterministic ordering
- 不把 blocked object 晋升进 routed sources

## 运行方式

直接基于 live source-integrated runtime 运行：

```bash
python3 scripts/derive_runtime_auto_routing.py
```

或基于已有 source-integration artifact：

```bash
python3 scripts/derive_runtime_auto_routing.py scripts/examples/agent_readable_wiki_runtime_context_source_integration_sample.json
```

生成 sample artifact：

```bash
python3 scripts/derive_runtime_auto_routing.py > scripts/examples/agent_readable_wiki_runtime_auto_routing_sample.json
```

## 当前 proof 边界

runtime auto routing 在 v1 只能证明：

- source-integrated runtime output 可以被整理成明确的 reading order
- preferred sources 可以进入 first-pass route
- supporting sources 可以进入 second-pass route
- blocked objects 仍然保持隔离

它不能证明：

- 外部 retrieval 已集成
- source 已自动注入 live context
- agent 可以跳过原始页面阅读
- runtime autonomy 已准备好

## 当前非目标

第一版不做这些事：

- 不接 Feishu 或其他外部系统
- 不做向量索引
- 不做自动 prompt/context 注入
- 不做 blocked 对象自动晋升

## 一句话判断

`先把 source-integrated runtime 变成明确的阅读顺序，再谈自动注入和自治执行。`
