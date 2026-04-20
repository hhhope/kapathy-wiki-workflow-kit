---
canonical_object: wiki-self-directed-execution
artifact_type: method
formalizes:
- wiki-self-directed-execution
derived_from:
- wiki-context-injection
- wiki-runtime-auto-routing
---

# wiki-self-directed-execution / method

这页定义当前仓库在演变型页面上的最小 bounded self-directed execution workflow。

目标不是让 agent 无限自治执行，也不是放开任意副作用，而是在 automatic context
injection 之后增加一层 repo-local 的 execution-plan bundle，让 agent 明确知道：

- 哪些动作现在可以先执行
- 哪些动作应延后为 follow-up
- 哪些对象当前不应进入 first-pass execution

## 依赖顺序

bounded self-directed execution 明确是 automatic context injection 之后的下游层，依赖：

1. naming model
2. frontmatter model
3. graph extraction
4. relation analysis
5. semantic scoring
6. utilization layer
7. runtime context
8. runtime context source integration
9. runtime auto routing
10. context injection

## 最小 execution-plan 合同

bounded self-directed execution artifact 至少保留：

- `summary`
- `execute_now`
- `defer_for_followup`
- `do_not_execute`
- `execution_notes`
- `proof_boundary_notes`

### `summary`

至少包含：

- execute-now / deferred / blocked counts
- whether caution is active
- whether direct source inspection is still required

### `execute_now`

当前可以先执行的动作，至少保留：

- `canonical_object`
- `execution_guidance`
- `reasons`
- `action_type`
- `action_sources`

### `defer_for_followup`

后续再执行的动作，至少保留：

- `canonical_object`
- `execution_guidance`
- `reasons`
- `action_type`
- `action_sources`

### `do_not_execute`

当前不应进入 first-pass execution 的对象，至少保留：

- `canonical_object`
- `execution_guidance`
- `reasons`

### `action_sources`

每个 action source 至少保留：

- `page_path`
- `artifact_type`
- `source_layer`
- `title`

## Version 1 Execution Model

第一版 execution 使用显式 banding：

- `injected_first_pass` -> `execute_now`
- `secondary_context` -> `defer_for_followup`
- `excluded_objects` -> `do_not_execute`

第一版 action type 保持 bounded：

- `inspect_and_apply_context`
- `inspect_before_followup`
- `blocked_from_first_pass_execution`

## 运行方式

直接基于 live automatic context injection 运行：

```bash
python3 scripts/derive_self_directed_execution.py
```

或基于已有 context-injection artifact：

```bash
python3 scripts/derive_self_directed_execution.py scripts/examples/agent_readable_wiki_context_injection_sample.json
```

生成 sample artifact：

```bash
python3 scripts/derive_self_directed_execution.py > scripts/examples/agent_readable_wiki_self_directed_execution_sample.json
```

## 当前 proof 边界

bounded self-directed execution 在 v1 只能证明：

- injected-context output 可以被整理成明确的 execution plan
- first-pass injected context 可以进入 `execute_now`
- secondary context 可以进入 `defer_for_followup`
- blocked objects 仍然保持隔离

它不能证明：

- 外部 retrieval 已集成
- agent 可以无界执行副作用
- 完整 autonomy 已准备好
- unresolved 页面已经被理解

## 当前非目标

第一版不做这些事：

- 不接 Feishu 或其他外部系统
- 不做向量索引
- 不做无界 agent execution loop
- 不做 blocked 对象自动晋升

## 一句话判断

`先把 injected-context 变成 bounded execution-plan bundle，再谈完整 autonomy。`
