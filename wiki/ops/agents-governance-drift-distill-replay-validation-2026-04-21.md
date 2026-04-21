---
title: agents-governance-drift-distill-calibration / replay-validation
canonical_object: agents-governance-drift-distill-calibration
artifact_type: replay-validation
derived_from:
  - wiki/ops/agents-governance-drift-distill-calibration-retro.md
  - wiki/ops/distill-calibration-replay-harness.md
validates:
  - disagreement-management-method
---

# agents-governance-drift-distill-calibration / replay-validation

这页记录对 `agents-governance-drift-distill-2026-04-21.md` 的第一轮
distill-calibration executable replay。

## 验证对象

- 待校准页面：
  [agents-governance-drift-distill-2026-04-21.md](/mnt/d/cloud/account-meeting-lore/wiki/ops/agents-governance-drift-distill-2026-04-21.md)
- 校准来源：
  [agents-governance-drift-distill-calibration-retro.md](/mnt/d/cloud/account-meeting-lore/wiki/ops/agents-governance-drift-distill-calibration-retro.md)

## RED 基线

在这轮 replay 之前：

- distill 页已经存在
- calibration retro 已经指出其 overclaim 问题
- 但仓库还没有 executable replay contract 去结构性检查这些证据是否齐全

所以：

- calibration 仍然主要依赖叙述性阅读

## GREEN 结果

本轮新增的 replay record：

- `scripts/examples/agents_governance_drift_distill_calibration_replay.json`

本轮运行命令：

```bash
python3 scripts/distill_calibration_replay_check.py \
  scripts/examples/agents_governance_drift_distill_calibration_replay.json
```

通过含义：

- fact recap 与 candidate model 已被结构化区分
- overclaim markers 已被显式列出
- weaker wording candidates 已被显式列出
- proof boundary 仍然明确停留在 structural replay

## Residual Risks

- 通过 replay checker 不代表 distill 页已经完成改写
- 通过 replay checker 不代表候选框架已经被仓库接受
- 这仍然是针对当前这条 distill dispute 的第一轮 bounded proof
