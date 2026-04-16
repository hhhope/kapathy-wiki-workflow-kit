---
name: surgical-changes
description: Use when the task is narrow but the edit is drifting into adjacent cleanup, style normalization, comment churn, or unrelated refactors.
---

# Surgical Changes

## Overview

只改和当前目标直接相关的内容。清理自己的副作用，不顺手改别人的地盘。

## Use When

- diff 正在扩散到相邻文件或无关区块
- 修一个点时顺手想“把这块也一起整理了”
- 现有代码不完美，但不是当前问题

## Rules

- 每一处改动都要能直接追溯到当前任务
- 只清理自己改动带来的 orphan 或副作用
- 发现旧问题可以指出，但不要顺手修
- 保持现有局部风格，除非当前任务明确要求改风格

## Anti-Patterns

- 修 bug 时顺手重排整个文件
- 改一个场景时把注释、命名、格式一起洗一遍
- 借当前任务偷带一个小重构

## Self-Check

`如果删掉这行改动，当前任务还成立吗？如果成立，它大概率不该在这个 diff 里。`
