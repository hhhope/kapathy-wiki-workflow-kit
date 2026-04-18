# kapathy-wiki-workflow-kit

[中文](README.md) | [English](README.en.md)

把飞书材料、会议纪要、汇报草稿和 agent 入口放进同一个可安装、可复用、可追踪的 Markdown 工作台。

[安装](#安装) · [快速开始](#快速开始) · [运行面](#运行面) · [文档](#文档) · [飞书来源说明](#飞书来源说明)

## 安装

如果你只想先把依赖装起来并确认命令可用，最小准备是：

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

如果你要使用飞书 / Lark 自动化能力，还需要额外完成：

```bash
lark-cli config init
lark-cli auth login --recommend
lark-cli auth status
```

## 快速开始

### 这是什么

这是一个给个人和项目组使用的工作流知识库模板：

- 用 [inbox/README.md](inbox/README.md) 接原始材料
- 用 [wiki/index.md](wiki/index.md) 导航长期知识、报告草稿和过程留痕
- 用 [openspec/](openspec/) 管仓库级 workflow 变更
- 用 [AGENTS.md](AGENTS.md) 和 [CLAUDE.md](CLAUDE.md) 把仓库规则暴露给不同 agent 运行面

它不是单纯的 wiki 样板，也不是只给某一个 AI 平台用的 prompt 仓库。

### 上手顺序

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

## 运行面

| 场景 | 入口 / 命令 | 说明 |
|---|---|---|
| Codex 仓库入口 | [AGENTS.md](AGENTS.md) | 仓库级默认规则、边界和路由 |
| Claude 仓库入口 | [CLAUDE.md](CLAUDE.md) | Claude 侧入口说明 |
| Cursor 适配说明 | [wiki/ai-chat-workflow-installer.md](wiki/ai-chat-workflow-installer.md) | 当前仓库把 Cursor 视为 adapter 目标 |
| 仓库级流程变更 | [openspec/](openspec/) | proposal / design / tasks / specs |
| 原始材料投递 | [inbox/README.md](inbox/README.md) | 先投递，再整理 |
| 知识导航 | [wiki/index.md](wiki/index.md) | domains / reports / timeline / sources / ops |
| 安装校验 | `python3 scripts/verify_wiki_workflow_kit.py` | 支持 `--without-obsidian` 等模式 |
| 飞书 / Lark 自动化 | `lark-cli` | 需要单独安装、配置和登录 |

### 常用命令

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

## 文档

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

## 飞书来源说明

你给的 Feishu 文章当前仍然无法从这个执行环境直接取回正文，所以 README 先按仓库现状组织。来源对齐状态记录在：

- [wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md](wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md)

这页负责记录：

- 原始 Feishu 链接
- 当前仓库已反映的内容
- 还没完成的正文同步点
