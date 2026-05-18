---
title: live-conversation-reanchor-gate / replay-harness
canonical_object: live-conversation-reanchor-gate
artifact_type: replay-harness
related_objects:
  - disagreement-management
validates:
  - live-conversation-reanchor-gate
language: zh-CN
audience: self
knowledge_level: working
domain: wiki
layer: ops
ops_area: agent-governance
status: active
updated_at: 2026-04-20
ai_generated: true
---

# live-conversation-reanchor-gate / replay-harness

这页定义 `live conversation re-anchor gate` 的最小可执行 replay 合同。

用途很窄：

- 证明 gate 不只停留在叙述性 RED/GREEN
- 用结构化 replay 记录去检查最小 gate 证据是否存在

## 最小 Replay 字段

- `thread_label`
- `original_requirement`
- `current_drift_chain`
- `trigger_signals`
- `stop_action`
- `reanchor_artifact`
- `unblock_condition`
- `red_baseline`
- `green_result`
- `residual_risk`

## 可执行检查

仓库现在提供：

- `scripts/reanchor_gate_replay_check.py`

运行方式：

```bash
python3 scripts/reanchor_gate_replay_check.py scripts/examples/live_conversation_reanchor_gate_replay.json
```

## 通过标准

检查器通过，只代表：

- re-anchor replay 记录满足最小结构合同
- gate 证据没有缺关键字段

不代表：

- drift 已被自动语义理解
- 所有 live conversation 都会被完美拦住
- rollout proof 已经成立

## 一句话判断

`这个 harness 证明 gate evidence 可执行可检查，不证明系统已经自动理解了所有偏移。`
