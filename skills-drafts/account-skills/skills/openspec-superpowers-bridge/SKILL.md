---
name: openspec-superpowers-bridge
description: Bridges OpenSpec change artifacts (explore, proposal, delta specs, design, tasks) into a normalized planning-brief for superpowers:writing-plans. Use when implementation planning should start after proposal/design/specs/tasks exist, when writing-plans misreads delta specs or OpenSpec task granularity, or when the user mentions OpenSpec + Superpowers, opsx + writing-plan, or openspec-to-plan handoff. Run before superpowers:writing-plans, not during explore-only. Implementation follows Superpowers TDD (writing-plans → test-driven-development → executing-plans), not /opsx:apply or openspec-apply-change unless the user explicitly overrides.
---

# OpenSpec ↔ Superpowers 桥接

将 OpenSpec **规划产物**整理为 Superpowers **`writing-plans` 的唯一 OpenSpec 输入**。本工作流下**实现不由** `/opsx:apply` 或 `openspec-apply-change` 驱动。

**开场白（必须）：**「使用 openspec-superpowers-bridge，正在把 OpenSpec 变更整理成 Superpowers 计划输入。」

## 优先级（与仓库 AGENTS.md 对齐）

冲突时按顺序：

1. 目标仓库根 `AGENTS.md`
2. 活动中的 `openspec/changes/<id>/` 产物
3. 本 skill
4. Agent 默认

若 `AGENTS.md` 要求「Superpowers 产出须回写 OpenSpec」，则 brief / plan 中的持久结论须合并进 `proposal.md`、`design.md`、`tasks.md` 或 delta spec，勿保留平行权威文档。

## 分工边界

| 层 | 负责 | 不负责 |
|----|------|--------|
| **OpenSpec** | explore、proposal、delta specs、design、规划期 `tasks.md` | 本工作流下的逐步编码与 TDD 勾选 |
| **本桥接** | 生成 `planning-brief-for-superpowers.md` | 实现功能 |
| **Superpowers** | `writing-plans` → `test-driven-development` → `executing-plans` | 替代 OpenSpec 做需求探索 |

`tasks.md` 是**规划里程碑**（与 spec 对齐）。实现阶段进度真源为 **`docs/superpowers/plans/*.md` 内的 checkbox**（非 `tasks.md` 日常勾选）。

## 端到端流程

```text
/opsx:explore 或 explore-notes     →  可选 explore-notes.md
/opsx:propose / continue           →  proposal + specs + design + tasks
openspec-superpowers-bridge        →  planning-brief-for-superpowers.md
superpowers:writing-plans          →  docs/superpowers/plans/YYYY-MM-DD-*.md
test-driven-development + executing-plans  →  代码与测试
（可选）完成后 openspec-verify / archive  →  合并 spec；可选回写 tasks.md 里程碑
```

## 何时用 / 何时不用

| 用 | 不用 |
|----|------|
| proposal + design + tasks 已就绪，准备 writing-plans | 仅 explore，尚无 proposal |
| 用户选定 Superpowers TDD 实现路径 | 用户明确要求 `/opsx:apply` 或 `openspec-apply-change` |
| Agent 误读 delta spec 或任务粒度 | 只改 OpenSpec 文案、不写计划 |

## 工作流

### Step 0 — 定位变更目录

1. 确认 change 路径：`openspec/changes/<id>/` 或 `openspec/changes/archive/<dated>-<id>/`。
2. **必须**存在 `proposal.md`；缺 `design.md` / `tasks.md` 时停止，回到 OpenSpec propose/continue。

### Step 1 — 读取 explore 与 proposal

| 来源 | 作用 |
|------|------|
| `explore-notes.md` | 可选；写入 brief §1 |
| **`proposal.md`** | **主输入**（Why、What Changes、Capabilities、Impact） |

动机与范围**以 proposal 为准**，勿另建 `purpose.md`。

### Step 2 — 生成 planning brief

解析脚本路径（按优先级）：

1. 当前仓库 `skills/openspec-superpowers-bridge/scripts/build-planning-brief.py`
2. 与本 `SKILL.md` 同目录的 `scripts/build-planning-brief.py`（个人/项目 skill 安装）
3. 用户给出的 `account-skills` clone 绝对路径

```bash
python <script-path> openspec/changes/<change-dir>
# 可选：-o /path/to/planning-brief-for-superpowers.md
```

默认输出：`<change-dir>/planning-brief-for-superpowers.md`。读完全文，修正 §6 中 R*↔T* 映射。

### Step 3 — 门禁（再调用 writing-plans）

- [ ] brief §4 每个 **R*** 有 Scenario 或 excerpt
- [ ] brief §2 含 non-goals / acceptance boundary
- [ ] brief §5 已识别 OpenSpec **T***，准备在计划中分解
- [ ] 若仓库启用 `lore`，大改动满足 proposal/design/tasks 三门禁

### Step 4 — writing-plans

1. 阅读 [references/writing-plans-handoff.md](references/writing-plans-handoff.md)
2. 宣布使用 `superpowers:writing-plans`；**仅以 brief 为 OpenSpec 输入**（勿直接拼凑原始 `spec.md`）
3. 计划路径：`docs/superpowers/plans/YYYY-MM-DD-<feature>.md`

### Step 5 — Superpowers TDD 实现

按 writing-plans 文末 handoff **必须**接续：

1. `superpowers:test-driven-development`
2. `superpowers:executing-plans` 或 `superpowers:subagent-driven-development`

实现中：勾选**计划文件** checkbox；一个 OpenSpec **T*** 通常对应多个 TDD 微步与多次 commit。

### Step 6 — 收尾（可选）

- 测试与计划 checkbox 完成后：可选勾选 `tasks.md` 里程碑；可选 `openspec-verify-change` / archive
- 将 delta spec 合并入主 spec 后，删除或标注 brief 为历史产物

## Cursor 安装

详见 [README.md](README.md)。摘要：

- **个人：** junction/symlink 到 `~/.cursor/skills/openspec-superpowers-bridge`
- **项目：** `.cursor/skills/openspec-superpowers-bridge`
- **勿**写入 `~/.cursor/skills-cursor/`

## 参考

- [references/openspec-artifacts.md](references/openspec-artifacts.md) — 产物与 delta spec 速查
- [references/explore-notes-template.md](references/explore-notes-template.md) — explore 笔记模板
- [examples.md](examples.md) — 端到端示例

## 故障排查

| 症状 | 处理 |
|------|------|
| 提议用 apply 写代码 | 确认用户是否坚持；默认改回 Superpowers TDD 链 |
| writing-plans 漏需求 | brief §4 R*/S* 对照计划 self-review |
| 计划步骤过大 | 每个 OpenSpec T* 拆成 2–5 分钟 TDD 步 |
| 进度不知看哪 | 看 `docs/superpowers/plans/*.md`，非日常 `tasks.md` |
| 脚本找不到 | 使用 SKILL 同目录 `scripts/` 或 account-skills 绝对路径 |
