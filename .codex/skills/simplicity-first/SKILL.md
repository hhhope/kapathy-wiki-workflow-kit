---
name: simplicity-first
description: Use when a solution is growing speculative abstractions, extra configuration, or future-proofing that the current task does not require.
---

# Simplicity First

## Overview

先做最小可验证解，不为未来需求提前设计。

## Use When

- 代码或规则开始为“以后可能会用”而膨胀
- 单次需求被包装成多层抽象
- 一个小改动正在长成框架

## Rules

- 只实现当前任务要求的能力
- 单次使用不要提前抽象
- 没有重复，不先做通用层
- 如果 200 行能变 50 行，先怀疑自己写复杂了

## Anti-Patterns

- 为一个函数先上 strategy / manager / config 层
- 把“灵活性”当成默认优点
- 用未来假设给当前复杂度找理由

## Self-Check

`这是不是在解决今天的问题，还是在幻想明天的问题？`
