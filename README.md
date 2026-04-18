# kapathy-wiki-workflow-kit

## 中文说明

这是一个面向汇报知识、会议材料和 AI workflow 的 Markdown 工作台。仓库把上游材料、过程留痕、汇报草稿和稳定决策拆成可复用的层次，避免同一份材料反复复制。

### 适合谁用

- 需要把飞书文档、会议纪要、周报素材沉淀成长期可复用 wiki 的个人或项目组
- 需要把 Codex / Cursor / Claude 的仓库级 workflow 固化为可安装说明的团队
- 需要先手工整理材料、后续再补自动化的场景

### 快速开始

1. 阅读 [PROJECT.md](/mnt/d/github/kapathy-wiki-workflow-kit/PROJECT.md) 了解仓库边界和治理模型。
2. 阅读 [wiki/index.md](/mnt/d/github/kapathy-wiki-workflow-kit/wiki/index.md) 进入 wiki 主导航。
3. 如果要投递原始材料，先看 [inbox/README.md](/mnt/d/github/kapathy-wiki-workflow-kit/inbox/README.md)。
4. 如果要改仓库默认 workflow、入口规则或 skills，先在 `openspec/` 下开 change。
5. 跑 `python3 scripts/verify_wiki_workflow_kit.py` 检查当前仓库或 bootstrap 产物是否完整。

### 环境依赖

必需：

- `python3`
- `node` / `npm`

按需：

- `openspec` CLI：用于 change proposal、status、instructions、archive
- `lark-cli`：用于 Feishu / Lark 文档、日历、通讯录、消息等自动化
- Obsidian：把仓库作为 vault 浏览和维护

当前环境中的全局安装示例：

```bash
npm install -g @fission-ai/openspec @larksuite/cli
```

安装后可检查：

```bash
openspec --help
lark-cli --help
python3 scripts/verify_wiki_workflow_kit.py --help
```

如果要使用 Feishu / Lark 自动化，还需要完成 `lark-cli` 的登录和配置：

```bash
lark-cli auth --help
lark-cli doctor
```

### 运行面入口

Codex：

- 入口文件：`AGENTS.md`
- repo-local skills：`.codex/skills/`
- OpenSpec CLI 可直接在仓库内使用

Cursor：

- 当前仓库把 Cursor 视为 adapter 目标，而不是已经生成完整 `.cursor/rules/` 的原生安装物
- 使用时应先参考 `AGENTS.md`、`wiki/ai-chat-workflow-installer.md` 和相关 ADR

Claude：

- 入口文件：`CLAUDE.md`
- 与 Codex 共用 `wiki/`、`openspec/`、模板和大部分 workflow 资产

### 核心路径

- `PROJECT.md`：项目身份、边界和 source of truth
- `wiki/`：长期知识页、模板、示例和 workflow 指南
- `inbox/`：原始材料投递区
- `openspec/`：变更提案、设计、规格和任务
- `scripts/`：bootstrap、intake、verify 等脚本

### 推荐使用路径

1. 新材料先进入 `inbox/` 或 `wiki/sources/`
2. 再根据内容整理到 `wiki/domains/`、`wiki/reports/`、`wiki/timeline/`、`wiki/ops/`
3. 如果要改仓库默认行为、skills 或治理规则，先走 OpenSpec change
4. 如果要跨运行面安装，先看 [wiki/ai-chat-workflow-installer.md](/mnt/d/github/kapathy-wiki-workflow-kit/wiki/ai-chat-workflow-installer.md)

### 安装后验证

默认模式验证：

```bash
python3 scripts/verify_wiki_workflow_kit.py
```

如果目标仓库没有安装 Obsidian：

```bash
python3 scripts/verify_wiki_workflow_kit.py --without-obsidian
```

如果目标仓库没有安装 OpenSpec 或 examples，也可以用对应开关验证实际模式：

```bash
python3 scripts/verify_wiki_workflow_kit.py --without-openspec --without-examples
```

### Feishu 来源说明

你提供的 Feishu 文章目前在这个执行环境里拿不到正文，所以仓库先按现有 wiki、脚本和技能资产完成入口说明，并把对齐状态记录在来源页中：

- [wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md](/mnt/d/github/kapathy-wiki-workflow-kit/wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md)

这页会说明：

- 原始链接
- 仓库已反映的内容
- 仍待同步的正文点

## English Guide

This repository is a Markdown-first workspace for report knowledge, meeting material, and AI workflow guidance. It separates upstream evidence, operating traces, report drafts, and durable decisions so the same source material can be reused instead of copied repeatedly.

### Who This Is For

- Individuals or project teams turning Feishu docs, meeting notes, and reporting inputs into a reusable wiki
- Teams that want repository-level workflow guidance for Codex, Cursor, and Claude
- Workflows that start manual-first and add automation later

### Quick Start

1. Read [PROJECT.md](/mnt/d/github/kapathy-wiki-workflow-kit/PROJECT.md) for repository scope and governance.
2. Read [wiki/index.md](/mnt/d/github/kapathy-wiki-workflow-kit/wiki/index.md) for wiki navigation.
3. Read [inbox/README.md](/mnt/d/github/kapathy-wiki-workflow-kit/inbox/README.md) before dropping raw source material.
4. Create an OpenSpec change before editing default workflow rules, entry guidance, or repo-local skills.
5. Run `python3 scripts/verify_wiki_workflow_kit.py` to verify the current repository or a bootstrap output.

### Environment Setup

Required:

- `python3`
- `node` / `npm`

Optional:

- `openspec` CLI for change lifecycle workflows
- `lark-cli` for Feishu / Lark automation
- Obsidian for vault-style browsing and editing

Example global install:

```bash
npm install -g @fission-ai/openspec @larksuite/cli
```

Sanity checks:

```bash
openspec --help
lark-cli --help
python3 scripts/verify_wiki_workflow_kit.py --help
```

If you want Feishu / Lark automation, finish CLI auth and diagnostics:

```bash
lark-cli auth --help
lark-cli doctor
```

### Runtime Entry Points

Codex:

- entry file: `AGENTS.md`
- repo-local skills: `.codex/skills/`
- OpenSpec CLI is available directly in the repository

Cursor:

- this repository documents Cursor as an adapter target, not as a fully generated `.cursor/rules/` installation in this change
- use `AGENTS.md`, `wiki/ai-chat-workflow-installer.md`, and the related ADR pages as the current canonical source

Claude:

- entry file: `CLAUDE.md`
- shares `wiki/`, `openspec/`, templates, and most workflow assets with Codex-facing environments

### Core Paths

- `PROJECT.md`: repository identity, boundaries, and source of truth
- `wiki/`: durable knowledge pages, templates, examples, and workflow guidance
- `inbox/`: raw material drop zone
- `openspec/`: proposals, design docs, specs, and task tracking
- `scripts/`: bootstrap, intake, and verification tooling

### Recommended Flow

1. Start new material in `inbox/` or `wiki/sources/`
2. Link or refine it into `wiki/domains/`, `wiki/reports/`, `wiki/timeline/`, and `wiki/ops/`
3. Use an OpenSpec change before modifying repository-default workflow behavior
4. See [wiki/ai-chat-workflow-installer.md](/mnt/d/github/kapathy-wiki-workflow-kit/wiki/ai-chat-workflow-installer.md) for the canonical cross-runtime installer model

### Verification

Default verification:

```bash
python3 scripts/verify_wiki_workflow_kit.py
```

Without Obsidian:

```bash
python3 scripts/verify_wiki_workflow_kit.py --without-obsidian
```

Without OpenSpec or examples:

```bash
python3 scripts/verify_wiki_workflow_kit.py --without-openspec --without-examples
```

### Feishu Source Note

The Feishu article referenced for this repo cannot be fully fetched from the current execution environment, so the repository now documents the current onboarding flow from the repo itself and records source alignment separately:

- [wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md](/mnt/d/github/kapathy-wiki-workflow-kit/wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md)

That page records:

- the original link
- what is already reflected in the repository
- what still needs to be synced from the source article
