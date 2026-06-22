# OpenSpec 产物速查（给 Agent）

## 与本工作流相关的生命周期

| 阶段 | 命令/动作 | 产物 | 交给谁 |
|------|-----------|------|--------|
| Explore | `/opsx:explore` | 对话；可选 `explore-notes.md` | 补充 brief §1 |
| Propose | `/opsx:propose` / `continue` | **`proposal.md`** + specs + design + tasks | 桥接 → writing-plans |
| **Implement** | **Superpowers TDD** | 代码、测试、`docs/superpowers/plans/*.md` 勾选 | **不用 `/opsx:apply`** |
| Archive | `/opsx:archive`（可选，完成后） | 合并 delta spec | 实现全部通过后 |

**动机与范围以 `proposal.md` 为准**（`## Why`、`## What Changes`、`## Capabilities` 等）。可选 `explore-notes.md` 仅作 explore 补充，没有也不阻塞桥接。

## 默认目录

```text
openspec/changes/<change-id>/
├── .openspec.yaml
├── proposal.md              ← 探索结论的主载体（你说的 proposal，不是 purpose）
├── design.md
├── tasks.md                 ← 规划里程碑，非实现进度真源
├── specs/<capability>/spec.md
├── explore-notes.md         ← 可选
└── planning-brief-for-superpowers.md   ← 桥接输出
```

## `tasks.md` 与 Superpowers 计划

| | OpenSpec `tasks.md` | Superpowers plan |
|--|---------------------|------------------|
| 阶段 | **规划对齐** spec | **实现执行** |
| 粒度 | 里程碑 | 2–5 分钟 TDD 步 |
| 勾选时机 | 可选，里程碑完成时 | **实现过程中持续勾选** |
| 真源（编码阶段） | 否 | **是** |

## `spec.md` delta 格式（易误解点）

- `## ADDED / MODIFIED / REMOVED Requirements`：相对主 spec 的增量。
- `### Requirement:` + `#### Scenario:`：writing-plans 须为每个 Scenario 安排测试或验证步骤。
- 实现时通过 **TDD** 满足 Scenario，不是通过 apply 命令。

## 可选 CLI

`openspec status --change <id> --json` 仅用于检查规划 artifact 是否齐全；**不**用于驱动实现。
