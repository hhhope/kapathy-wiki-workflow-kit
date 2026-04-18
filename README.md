# kapathy-wiki-workflow-kit

## 中文入口

把飞书材料、会议纪要、汇报草稿和 AI workflow 规则放进同一个可安装、可复用、可追踪的 Markdown 工作台。

### 这是什么

这是一个给个人和项目组使用的工作流知识库模板：

- 用 [inbox/README.md](inbox/README.md) 接原始材料
- 用 [wiki/index.md](wiki/index.md) 导航长期知识、报告草稿和过程留痕
- 用 [openspec/](openspec/) 管仓库级 workflow 变更
- 用 [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) 把仓库规则暴露给不同 agent 运行面

它不是单纯的 wiki 样板，也不是只给某一个 AI 平台用的 prompt 仓库。

### Quick Install

如果你只是想先把依赖装起来并确认命令可用，最小准备是：

```bash
npm install -g @fission-ai/openspec @larksuite/cli
python3 scripts/verify_wiki_workflow_kit.py --help
openspec --help
lark-cli --help
```

如果你要初始化一个新仓库来复用这套 kit：

```bash
python3 scripts/bootstrap_wiki_workflow_kit.py \
  --project-name "My Workflow Repo" \
  --target-dir /path/to/target \
  --owner your-name
```

### Getting Started

```bash
# 1. 看项目边界
sed -n '1,200p' PROJECT.md

# 2. 看 wiki 主导航
sed -n '1,200p' wiki/index.md

# 3. 看原始材料投递说明
sed -n '1,200p' inbox/README.md

# 4. 检查当前安装是否完整
python3 scripts/verify_wiki_workflow_kit.py

# 5. 如果要处理 inbox 文本材料
python3 -m scripts.inbox_intake --inbox inbox --sources wiki/sources --ops wiki/ops
```

### Runtime Quick Reference

| 场景 | 入口 / 命令 | 说明 |
|---|---|---|
| Codex 仓库入口 | [AGENTS.md](AGENTS.md) | 仓库级默认规则、边界和路由 |
| Claude 仓库入口 | [CLAUDE.md](CLAUDE.md) | Claude 侧入口说明 |
| 仓库级流程变更 | [openspec/](openspec/) | proposal / design / tasks / specs |
| 原始材料投递 | [inbox/README.md](inbox/README.md) | 先投递，再整理 |
| 知识导航 | [wiki/index.md](wiki/index.md) | domains / reports / timeline / sources / ops |
| 安装校验 | `python3 scripts/verify_wiki_workflow_kit.py` | 支持 `--without-obsidian` 等模式 |
| 飞书 / Lark 自动化 | `lark-cli` | 需要额外登录与配置 |

### CLI And Tooling

常用命令：

```bash
openspec list --json
openspec status --change <name> --json
openspec instructions apply --change <name> --json

lark-cli doctor
lark-cli auth --help
lark-cli docs --help
lark-cli calendar --help
```

说明：

- `python3`、`node` / `npm` 是基础依赖
- `openspec` 是 workflow-level 变更治理 CLI
- `lark-cli` 是飞书 / Lark 自动化 CLI，不装也能使用本仓库的大部分 wiki workflow
- Obsidian 是可选表层，不是仓库可用性的前提

### Documentation

| 文档 | 内容 |
|---|---|
| [PROJECT.md](PROJECT.md) | 项目身份、边界、source of truth |
| [wiki/index.md](wiki/index.md) | 知识导航总入口 |
| [wiki/ai-workflow.md](wiki/ai-workflow.md) | AI workflow 总览 |
| [wiki/ai-chat-workflow-installer.md](wiki/ai-chat-workflow-installer.md) | Codex / Cursor / Claude 安装模型 |
| [wiki/ops/index.md](wiki/ops/index.md) | intake、focus-thread、reminder、handoff |
| [wiki/reports/index.md](wiki/reports/index.md) | 面向受众的输出页 |
| [wiki/sources/index.md](wiki/sources/index.md) | 来源页与证据页 |
| [inbox/README.md](inbox/README.md) | 原始文件投递规则 |

### Feishu Source Note

你给的 Feishu 文章现在仍然无法从当前执行环境直接取回正文，所以 README 先按仓库现状组织。来源对齐状态记录在：

- [wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md](wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md)

这页负责记录：

- 原始 Feishu 链接
- 当前仓库已反映的内容
- 还没完成的正文同步点

---

## English Guide

### What This Is

This repository is a workflow kit for teams or individuals who want one Markdown workspace for:

- raw source intake in [inbox/README.md](inbox/README.md)
- durable knowledge and report assembly in [wiki/index.md](wiki/index.md)
- repository-level workflow governance in [openspec/](openspec/)
- agent-facing runtime entrypoints through [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md)

It is not just a passive wiki skeleton, and it is not a single-platform prompt repo.

### Quick Install

If you only want the minimum tooling installed first:

```bash
npm install -g @fission-ai/openspec @larksuite/cli
python3 scripts/verify_wiki_workflow_kit.py --help
openspec --help
lark-cli --help
```

If you want to initialize a new repository from this kit:

```bash
python3 scripts/bootstrap_wiki_workflow_kit.py \
  --project-name "My Workflow Repo" \
  --target-dir /path/to/target \
  --owner your-name
```

### Getting Started

```bash
# 1. Read repository boundaries
sed -n '1,200p' PROJECT.md

# 2. Open the wiki index
sed -n '1,200p' wiki/index.md

# 3. Review intake rules before dropping raw files
sed -n '1,200p' inbox/README.md

# 4. Verify the current install
python3 scripts/verify_wiki_workflow_kit.py

# 5. Process text material from inbox
python3 -m scripts.inbox_intake --inbox inbox --sources wiki/sources --ops wiki/ops
```

### Runtime Quick Reference

| Use Case | Entry / Command | Notes |
|---|---|---|
| Codex repo entry | [AGENTS.md](AGENTS.md) | repository-level rules and routing |
| Claude repo entry | [CLAUDE.md](CLAUDE.md) | Claude-facing startup file |
| Workflow change governance | [openspec/](openspec/) | proposal / design / tasks / specs |
| Raw source intake | [inbox/README.md](inbox/README.md) | drop first, refine later |
| Knowledge navigation | [wiki/index.md](wiki/index.md) | domains / reports / timeline / sources / ops |
| Installation verification | `python3 scripts/verify_wiki_workflow_kit.py` | supports optional-mode flags |
| Feishu / Lark automation | `lark-cli` | requires separate auth and setup |

### CLI And Tooling

Common commands:

```bash
openspec list --json
openspec status --change <name> --json
openspec instructions apply --change <name> --json

lark-cli doctor
lark-cli auth --help
lark-cli docs --help
lark-cli calendar --help
```

Notes:

- `python3` and `node` / `npm` are the base prerequisites
- `openspec` governs workflow-level changes
- `lark-cli` enables Feishu / Lark automation but is optional for core wiki usage
- Obsidian is an optional surface, not a hard requirement for the repository

### Documentation

| Document | What It Covers |
|---|---|
| [PROJECT.md](PROJECT.md) | repository identity, scope, and source of truth |
| [wiki/index.md](wiki/index.md) | top-level knowledge navigation |
| [wiki/ai-workflow.md](wiki/ai-workflow.md) | overall AI workflow model |
| [wiki/ai-chat-workflow-installer.md](wiki/ai-chat-workflow-installer.md) | Codex / Cursor / Claude installer model |
| [wiki/ops/index.md](wiki/ops/index.md) | intake, focus threads, reminders, handoff |
| [wiki/reports/index.md](wiki/reports/index.md) | audience-facing outputs |
| [wiki/sources/index.md](wiki/sources/index.md) | evidence and source pages |
| [inbox/README.md](inbox/README.md) | raw intake rules |

### Feishu Source Note

The referenced Feishu article is still unavailable from the current execution environment, so the README reflects the repository itself first. Source alignment is tracked in:

- [wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md](wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md)

That page records:

- the original source link
- what is already reflected in this repository
- what still needs a later sync pass
