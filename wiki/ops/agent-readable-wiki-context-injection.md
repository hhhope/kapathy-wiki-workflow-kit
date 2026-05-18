---
canonical_object: wiki-context-injection
artifact_type: method
layer: ops
domain: wiki
ops_area: wiki-runtime
formalizes:
- wiki-context-injection
derived_from:
- wiki-runtime-auto-routing
- wiki-runtime-context-source-integration
---

# wiki-context-injection / method

这页定义当前仓库在演变型页面上的最小 automatic context-injection workflow。

目标不是做 agent 自治执行，也不是把上下文自动注入所有入口，而是在 runtime
auto routing 之后增加一层 repo-local 的 injected-context bundle，让 agent 可以直接消费：

- first-pass 应注入的上下文材料
- second-pass 仍然可读但不应抢占首轮位置的材料
- 当前必须排除在 first-pass 注入之外的对象

## 依赖顺序

automatic context injection 明确是 runtime auto routing 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis
5. semantic scoring
6. utilization layer
7. runtime context
8. runtime context source integration
9. runtime auto routing

## 最小 injected-context 合同

automatic context-injection artifact 至少保留：

- `summary`
- `injected_first_pass`
- `secondary_context`
- `excluded_objects`
- `injection_notes`
- `proof_boundary_notes`

### `summary`

至少包含：

- injected-first-pass / secondary / excluded counts
- whether caution is active
- whether direct source inspection is still required

### `injected_first_pass`

first-pass 注入材料，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`
- `injected_sources`

### `secondary_context`

second-pass 可保留的注入材料，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`
- `injected_sources`

### `excluded_objects`

当前不应进入 first-pass 注入的对象，至少保留：

- `canonical_object`
- `usage_guidance`
- `reasons`

### `injected_sources`

每个 injected source 至少保留：

- `page_path`
- `artifact_type`
- `source_layer`
- `title`
- `excerpt`

## Version 1 Injection Model

第一版 injection 使用显式 banding：

- `open_first` -> `injected_first_pass`
- `open_next` -> `secondary_context`
- `do_not_open_first` -> `excluded_objects`

第一版只注入有界 excerpt，不注入整页全文。

## Excerpt Policy

第一版 excerpt 必须保持 bounded：

- 保留标题
- 保留去掉 frontmatter 之后的正文前段
- 不依赖语义摘要或模型重写
- 不因为长页而注入整页全文

## 运行方式

直接基于 live runtime auto-routing 运行：

```bash
python3 scripts/build_runtime_context_injection.py
```

或基于已有 auto-routing artifact：

```bash
python3 scripts/build_runtime_context_injection.py scripts/examples/agent_readable_wiki_runtime_auto_routing_sample.json
```

生成 sample artifact：

```bash
python3 scripts/build_runtime_context_injection.py > scripts/examples/agent_readable_wiki_context_injection_sample.json
```

## 当前 proof 边界

automatic context injection 在 v1 只能证明：

- runtime auto-routing output 可以被整理成明确的 injected-context bundle
- first-pass route 可以变成 first-pass injected context
- second-pass route 可以保留为 secondary context
- excluded objects 仍然保持隔离

它不能证明：

- 外部 retrieval 已集成
- 所有入口都已自动注入
- agent 已经拥有自治执行能力
- unresolved 页面已经被理解

## 当前非目标

第一版不做这些事：

- 不接 Feishu 或其他外部系统
- 不做向量索引
- 不做 agent 自治执行
- 不做 blocked 对象自动晋升

## 一句话判断

`先把 reading route 变成 bounded injected-context bundle，再谈自治执行。`
