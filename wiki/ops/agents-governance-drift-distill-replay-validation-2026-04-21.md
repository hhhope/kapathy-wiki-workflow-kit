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

## 当前版本复核

在 distill 页后续继续修改后，本轮又做了一次同合同复核。

当前新增但仍应视为 `candidate model` 而非已定结论的内容包括：

- `最终方案`
- `Enforcement 策略`
- `最小可防漂移起步集 = a + b + c + j`

这次复核后的判断没有翻转：

- distill 页仍然更适合作为 `candidate distill`
- 不宜单独作为 `stable decision` 或 `canonical governance framework`
- 继续校准时，仍应与 calibration retro 一起读取

## Residual Risks

- 通过 replay checker 不代表 distill 页已经完成改写
- 通过 replay checker 不代表候选框架已经被仓库接受
- 这仍然是针对当前这条 distill dispute 的第一轮 bounded proof
