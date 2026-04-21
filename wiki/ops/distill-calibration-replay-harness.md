---
title: distill-calibration / replay-harness
canonical_object: agents-governance-drift-distill-calibration
artifact_type: replay-harness
---

# Distill Calibration Replay Harness

这页定义当前仓库用于 `distill` 校准争议的最小可执行 replay 合同。

用途只有一个：

当仓库想验证“这页 distill 是否把 still-open 的内容写成 already-settled”时，
用结构化 replay 记录去检查最小校准证据是否存在。

## 适用边界

适用于：

- distill 页把候选框架写得过像 stable decision
- factual recap 与 candidate governance model 混在一起
- calibration retro 已经指出问题，但还没有 executable proof

不适用于：

- 普通摘要文风优化
- 没有明确 calibration retro 的轻微措辞差异
- 需要语义判断“这个框架到底对不对”的争论

## 最小 Replay 字段

每次 replay 至少保留：

- `thread_label`
- `distill_page`
- `fact_recap_sections`
- `candidate_model_sections`
- `overclaim_markers`
- `downgraded_wording`
- `red_baseline`
- `green_result`
- `residual_risk`

## 可执行检查

仓库提供了一个最小可执行检查器：

- `scripts/distill_calibration_replay_check.py`

它做的不是语义理解，而是结构校验。

它会检查：

- 必填字段是否存在
- 列表字段是否非空且元素为字符串
- 5 个必需 pass-condition 是否显式存在且为 `true`

运行方式：

```bash
python3 scripts/distill_calibration_replay_check.py \
  scripts/examples/agents_governance_drift_distill_calibration_replay.json
```

这个脚本通过，只代表：

- replay 记录满足了最小校准合同

不代表：

- distill 页已经被自动修正
- 候选框架已经成为稳定 canonical
- rollout proof 已经成立

## 通过标准

一次 replay 只有同时满足下面这些，才算通过：

1. 明确区分了 fact recap 与 candidate model
2. 明确点出了 overclaim 词语或句型
3. 给出了更弱、更诚实的 wording 候选
4. 没把 replay pass 误说成治理共识

## 常见失败方式

- 只说“这页太强势”，但没指出具体 overclaim marker
- 只说“这是一套候选框架”，但没指出哪些段落已经越界
- 用更漂亮的二次总结替代了 calibration evidence
- 把 checker 通过当成框架正确性的证明

## 一句话判断

`这个 replay harness 不是用来证明 distill 正确，而是用来证明校准记录至少保住了“哪里说重了”。`
