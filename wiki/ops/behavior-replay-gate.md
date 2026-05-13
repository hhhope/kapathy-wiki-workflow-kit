---
canonical_object: behavior-replay-gate
artifact_type: method
layer: ops
domain: none
ops_area: agent-governance
title: behavior-replay-gate / method
type: method
language: zh-CN
status: accepted
created_at: 2026-05-07
updated_at: 2026-05-07
related_objects:
  - learning-capture-routing
  - skill-evaluation-evidence
  - disagreement-management-method
  - live-conversation-reanchor-gate
derived_from:
  - openspec/changes/archive/2026-05-07-generalize-behavior-replay-gate/design.md
formalizes:
  - openspec/specs/behavior-replay-gate/spec.md
---

# behavior-replay-gate / method

## 目的

`Behavior Replay Gate` 解决的是“以后真的会触发吗”的问题。

它不是要求每篇学习笔记都写测试，也不是把所有 wiki 捕获都升级成
OpenSpec。它只管一种声明：我们说某个运行时行为以后会触发、停止、路由、
拒绝或持久化时，这个声明必须能从 repo 可见资产里被回放验证。

## 什么时候触发

| 场景 | 是否触发 | 原因 |
|---|---:|---|
| 修改 skill description，声称下次某类输入会自动触发 | 是 | 这是未来触发行为 |
| 修改 repo `AGENTS.md`，声称下次会先停下或先路由 | 是 | 这是运行时 stop / route 行为 |
| OpenSpec hard stop、archive gate、re-anchor gate 发生变化 | 是 | 这是未来停止条件 |
| 学习一篇文章，只产出候选观察 | 否 | 没有声明未来运行时行为 |
| 普通 wiki source summary | 否 | 只是来源记录 |
| 候选学习要晋升成 skill hard rule、AGENTS 规则或 spec `SHALL` | 是 | 开始声明未来行为 |

## 最小回放证据

| 字段 | 要回答的问题 |
|---|---|
| input / situation shape | 什么输入或局面会触发？ |
| trigger condition | 触发条件具体是什么？ |
| expected route / stop | 预期应该路由、停止、拒绝还是持久化？ |
| repo-visible artifact | 未来 agent 会读哪个 repo 文件得到这个行为？ |
| expected output / non-output | 应该输出什么，或者明确不输出什么？ |
| promotion boundary | 什么仍然不能晋升成规则？ |
| residual risk / proof boundary | 这次证据不能证明什么？ |

## 和已有 gate 的关系

- `skill-evaluation-evidence` 是 skill 语义修改的专用证据 gate。
- `local-skill-pressure-tests` 是 skill 的 RED / GREEN 压测格式。
- `Link Trigger Replay` 是学习链接触发行为的一个实例。
- disagreement replay 和 re-anchor replay 是分歧 / 漂移场景的专用 harness。

这些专用机制可以满足 `Behavior Replay Gate`，前提是保留最小回放证据和
proof boundary。反过来，`Behavior Replay Gate` 不替代这些专用机制。

## 边界

- 不要求每次学习都写自动化测试。
- 不要求每个 wiki 页面都有回放表。
- 不把候选学习直接升级成规则。
- 不声称一次文档级回放等于多轮真实会话 telemetry。

一句话：学习可以先沉淀，规则必须能回放。
