---
name: clarify-before-acting
description: Use when a request still has material ambiguity and the agent is about to silently pick one interpretation, scope, output shape, or boundary.
---

# Clarify Before Acting

## Overview

先把关键歧义摊开，再动手。不要替用户补决定性的前提。

## Use When

- 一个请求存在两个以上合理解释
- 输出形态、范围、对象或边界还没定
- 继续执行会把“猜测”变成真实改动

## Rules

- 列出关键假设，不要静默选择
- 能从本地上下文确认的先确认，再提问
- 真正会改变结果的歧义才问，不把整套流程重新问一遍
- 如果更简单或更安全的解释存在，要明确说出来

## Anti-Patterns

- 把模糊需求当成唯一明确需求
- 用户只说“整理一下”，却自己决定交付物形态
- 明明存在边界风险，还继续实现再回头解释

## Self-Check

`我现在是在执行已确认的要求，还是在把自己的猜测写进结果？`
