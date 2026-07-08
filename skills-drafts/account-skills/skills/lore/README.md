# Lore / 团队知识 Wiki

> **[English](#english)** | **[中文](#中文)**

---

## English

### Overview

**Lore** is the persistent memory layer for agentic coding workflows.

It is designed to work **beside** OpenSpec, not compete with it:

- **OpenSpec** owns change lifecycle and task progress
- **Lore** owns project memory, pitfalls, principles, logs, and wiki upkeep
- **Graphify** can assist the same knowledge layer with code-topology evidence, but it does not replace Lore pages

Preferred host: **Obsidian + git**.  
Required baseline: plain markdown + git.

### Core split

| System | Owns |
|---|---|
| OpenSpec | explore / propose / apply / archive, `tasks.md` progress |
| Lore | wiki query / log / weekly synthesis / lint / reuse |
| Graphify | code graph, entry points, neighbors, bridge nodes, structural paths |

`tasks.md` is the only task-progress truth source.

### Process plane vs knowledge plane

- **OpenSpec** is the process plane
  - what the current change is
  - what is in scope
  - what tasks are pending or complete
- **Lore + Graphify** form the knowledge plane
  - Lore answers: what this problem means, which rule applies, which boundaries matter
  - Graphify answers: where this lives in code and how the relevant nodes connect

Graphify is not a second durable truth source. It is a structure-evidence layer inside the knowledge plane.

### Recommended structure

```text
wiki/
├── index.md
├── projects/
│   └── <project>/
│       ├── overview.md
│       └── domains/
├── pitfalls/
└── principles/
```

Project-local execution logs stay in the project repo `logs/`, not in the shared wiki repo.

### Core workflow

1. Read current OpenSpec change
2. Read `PROJECT.md`
3. Classify the question:
   - process
   - Lore
   - Graphify
   - mixed
4. For Lore or mixed questions, read `wiki/index.md`
5. Read only the most relevant project/domain/pitfall/principle pages
6. For mixed questions, consult Graphify after Lore has identified the scene
7. Execute with self-check
8. Record deviations in logs
9. Run weekly review to absorb logs into wiki pages
10. Run lore lint periodically

### Routing rule

- **Process question** → OpenSpec
- **Rule/boundary question** → Lore
- **Code structure question** → Graphify
- **Mixed question** → Lore first, Graphify second

Examples:

- "Which pitfall applies here?" → Lore
- "What file or node is the likely entry point?" → Graphify
- "This Lore rule, where does it land in code?" → Lore first, then Graphify

Weekly review is not just a prose summary. It should emit page updates plus a small metrics block:
- reviewed logs
- absorbed logs
- discarded logs
- `absorbed-to` completion rate
- absorption success rate
- dominant destination page types

### Hard rules

- ❌ Do not use Lore as the task-progress source
- ❌ Do not execute large work without an approved OpenSpec change
- ❌ Do not rely on raw logs as the main retrieval layer
- ❌ Do not promote team-wide knowledge from one project only
- ❌ Do not let wiki retrieval exceed the context budget without justification
- ❌ Do not treat Graphify adjacency as a substitute for durable Lore facts
- ❌ Do not collapse OpenSpec process tracking into the same retrieval layer as Lore or Graphify

### Command triggers

| Trigger | Action |
|---|---|
| project task | Health check + query wiki |
| `lore: {keyword}` | Search index and target pages |
| rule / boundary / pitfall question | Route through Lore pages first |
| mixed rule + code question | Route through Lore first, then Graphify |
| `weekly review` | Absorb logs into wiki pages |
| `code archaeology {path}` | Extract stable knowledge and unknowns |
| `lint lore` | Detect stale/orphan/conflicting wiki state |

### Graphify relationship

Use Graphify when the question depends on code topology:

- entry points
- function neighbors
- module clusters
- bridge nodes
- likely call paths

Do not use Graphify first when the real question is:

- which rule applies
- which pitfall fits
- what the stable boundary is
- what durable fact should be loaded first

### Validation assets

- `references/TDD-SPEC.md`
- `references/PRESSURE-TEST.md`
- `references/BASELINE-RESULTS.md`
- `references/SKILL-EVAL.md`
- `evals/evals.json`
- `evals/MANUAL-RESULTS.md`
- `evals/COMMAND-RESULTS.md`
- `evals/PRESSURE-RESULTS.md`
- `evals/LIVE-AGENT-RETRIEVAL.md`
- `evals/LIVE-WEEKLY-REVIEW.md`
- `evals/LIVE-INTEGRATION-RESULTS.md`
- `evals/KNOWLEDGE-PLANE-RESULTS.md`
- `evals/KNOWLEDGE-ROUTING-RESULTS.md`

---

## 中文

### 概述

**Lore** 是 agent 编码工作流里的持久记忆层。

它不是 OpenSpec 的替代品，而是与 OpenSpec 分层协作：

- **OpenSpec** 负责变更生命周期和任务进度
- **Lore** 负责项目记忆、坑点、原则、日志和 wiki 维护

推荐宿主：**Obsidian + git**。  
最低要求：纯 markdown + git 也能工作。

### 核心分工

| 系统 | 负责内容 |
|---|---|
| OpenSpec | explore / propose / apply / archive，`tasks.md` 进度 |
| Lore | wiki 检索 / log / 周回顾吸收 / lint / 复用 |

`tasks.md` 是唯一的任务进度真相源。

### 推荐结构

```text
wiki/
├── index.md
├── projects/
│   └── <project>/
│       ├── overview.md
│       └── domains/
├── pitfalls/
└── principles/
```

执行期的本地 `logs/` 仍留在项目仓库，不放进共享 wiki 仓库。

### 安装与迁移

当需求是初始化共享 wiki、迁移 flat `LORE.md`、或 bootstrap 共享 `team-lore` 仓库时，改用 `skills/lore-bootstrap/`。  
`lore` 只负责运行态的检索 / review / lint，不负责安装。

当前环境推荐把共享 wiki 放在 `/mnt/d/team-lore`。安装时要明确选择路径，不要静默回退到 `~/team-lore`。

### 核心流程

1. 先读当前 OpenSpec change
2. 读 `PROJECT.md`
3. 读 `wiki/index.md`
4. 只读最相关的项目 / domain / pitfall / principle 页面
5. 执行时做自检
6. 偏差先进入 log
7. 用 weekly review 把 log 吸收到 wiki 页面
8. 定期执行 lore lint

weekly review 不是自由总结，而是要给出页面更新和最小指标块：
- reviewed logs 数
- absorbed logs 数
- discarded logs 数
- `absorbed-to` 完整率
- absorption success rate
- 目标页面类型分布

### 硬规则

- ❌ 不要把 Lore 当成任务进度系统
- ❌ 大任务没有已批准的 OpenSpec change 就执行
- ❌ 不要把原始 logs 当成主检索层
- ❌ 单项目证据不足时不要晋升 team 级知识
- ❌ 不要无节制扩张启动上下文

### 意图入口

| 用户意图 / 命令形态 | 动作 |
|---|---|
| 项目任务 | 健康检查 + wiki 检索 |
| `lore: {keyword}` | 查 index 和目标页面 |
| `weekly review` | 把 logs 吸收进 wiki 页面 |
| `code archaeology {path}` | 提取稳定知识和未知项 |
| `lint lore` | 检查陈旧/孤儿/冲突页面 |

### 验证资产

- `references/TDD-SPEC.md`
- `references/PRESSURE-TEST.md`
- `references/BASELINE-RESULTS.md`
- `references/SKILL-EVAL.md`
- `evals/evals.json`
- `evals/MANUAL-RESULTS.md`
- `evals/COMMAND-RESULTS.md`
- `evals/PRESSURE-RESULTS.md`
- `evals/LIVE-AGENT-RETRIEVAL.md`
- `evals/LIVE-WEEKLY-REVIEW.md`
- `evals/LIVE-INTEGRATION-RESULTS.md`
