---
name: verify-before-claiming
description: Use when the agent is about to say something is fixed, complete, synced, or clean without a fresh command, test, or state check.
---

# Verify Before Claiming

## Overview

没验过，就不要说完成。结论要来自当前检查，不来自记忆。

## Use When

- 准备说“已修复”“已提交”“已同步”“worktree 干净”
- 中断之后要继续判断仓库或任务状态
- 结果依赖测试、命令输出或外部同步状态

## Rules

- 先检查，再下结论
- git 结论至少看当前 `status` 和最新 `log`
- 行为变更优先给出测试或命令验证
- 如果没法验证，就明确说没验证到哪一步

## Anti-Patterns

- 凭刚才的记忆说“已经提交了”
- 代码改完就默认功能正确
- 外部同步没重查就说“已经好了”

## Self-Check

`这句话是来自刚刚的验证结果，还是来自我的印象？`
