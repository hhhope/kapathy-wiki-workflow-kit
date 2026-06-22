# Codex Integration Kit

面向 Codex 新项目首次接入的可复用规范包。

## 解决什么问题

新项目第一次接 Codex 时，最常见的问题是：`AGENTS.md`、长期规则、子代理角色提示词、场景化 skill 全混在一起，或者每个仓库都从零重写一套，最后规则重复、边界不清、也不好复用。

这套 kit 现在提供“全局基线 + repo 门禁 + rules/agents/skills”的完整分层，并把职责拆成六层：

| 层级 | 路径 | 作用 |
|-------|------|---------|
| 全局基线模板 | `templates/global/` | 可安装到 `~/.codex/AGENTS.md` 的通用基线，以及可选个人增强示例 |
| 项目门禁模板 | `AGENTS.md` / `templates/repo/` | 仓库根 `AGENTS.md` 模板，负责项目启动顺序、上下文恢复顺序、rules/agents/skills 入口索引 |
| 常驻规则 | `rules/` | Git 流程、安全底线、测试要求、Python 后端规则、Vue 前端规则 |
| Agent 角色模板 | `agents/` | planner、code-reviewer、security-reviewer、python-reviewer 的职责边界和输出格式 |
| Skill 速查卡 | `skills/` | DB migration、Jira 需求提取这类“已知道要做什么后直接查约束和字段”的 cheatsheet |
| 对话式安装 Skill | `skills/governance-install/` | 让用户直接通过对话安装到 Codex 或 Cursor，而不是先切到 shell |
| 安装脚本 | `scripts/install-codex-governance.sh` | 一键装到 `~/.codex`，支持备份和 dry-run |
| 分享稿源文件 | `docs/feishu-codex-governance-share.md` | 可直接发飞书的说明文档 |

## 当前内置 Git 命名规范

- 分支名：`<type>/<intent-slug>`
- 允许的分支类型：`feat`、`fix`、`refactor`、`chore`、`docs`、`test`
- commit message：`<type>: <short summary>`
- 允许的 commit 类型：`feat`、`fix`、`refactor`、`docs`、`test`、`chore`
- slug 用短英文、小写、连字符，不用空格、中文、`final`、`test`、`new` 这类低信息词
- 有 REQ 或 ticket 时，优先让 branch slug 反映需求意图

示例：

- `feat/multitenant-sql`
- `fix/dashboard-refresh-state`
- `docs/codex-governance-install`
- `feat: add global AGENTS templates`
- `fix: preserve selected team scope after refresh`
- `docs: clarify codex installation modes`

## Install

### Chat-First Install

如果用户是在对话里直接说“帮我安装”，优先走对话式安装，而不是先把人打回 shell：

- `帮我把这套规范装到 Codex`
- `给当前项目装 Cursor 规则`
- `先预览最小版，再安装`
- `给我装团队版，不要个人增强`

对应 skill：

- `skills/governance-install/SKILL.md`

对话式安装的目标：

- Codex：直接安装到 `~/.codex`
- Cursor：直接生成项目内 `.cursor/` 配置文件
- 支持 `dry-run` 和 `apply`
- 支持 `minimal` 和 `team` 两种范围
- 如果同时涉及共享 Lore Wiki，保持对话式安装，不把用户打回 shell；wiki 位置要显式确认，当前环境推荐 `/mnt/d/team-lore`
- 如果用户要产出或更新飞书分享稿、知识总览页、治理说明文档，优先使用 `skills/feishu-doc-writing/SKILL.md`
- 如果用户还要求对真实飞书文档执行创建、读取、搜索、更新，必须同时配合 `lark-doc`；前者管内容结构，后者管 CLI 写入/读取
- 如果文档还需要一张高信息密度总结图，优先让 `feishu-doc-writing` 决定结构，再按图的类型配 `xiaohongshu-retro-grid-content` 或 `lark-whiteboard`

### Shell Install

默认进入交互式安装，会依次询问是否安装：

- 全局基线 `~/.codex/AGENTS.md`
- 个人增强示例 `~/.codex/AGENTS.personal.example.md`
- repo 模板 `~/.codex/AGENTS.repo-template.md`
- `rules/`、`agents/`、`skills/`

```bash
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh
```

只预览，不实际写文件：

```bash
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh --dry-run
```

安装到指定 Codex home：

```bash
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh --target /path/to/.codex
```

无提示安装指定组件：

```bash
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh \
  --no-prompt \
  --install global-base,repo-template,rules,agents,skills
```

## 安装行为

- `templates/global/AGENTS.base.md` 可安装到目标 Codex home 的 `AGENTS.md`。
- `templates/global/AGENTS.personal.example.md` 可安装到目标 Codex home 的 `AGENTS.personal.example.md`。
- repo 模板会安装到目标 Codex home 的 `AGENTS.repo-template.md`。
- `rules/`、`agents/`、`skills/` 会逐文件复制到目标 Codex home。
- 目标路径下如果已有同名文件，会先备份到 `.codex-governance-backup/<timestamp>/`。
- `~/.codex/rules` 和 `~/.codex/skills` 里其他无关文件会保留，不会整目录清空。

## Cursor 直接安装产物

如果目标平台是 Cursor，推荐直接生成这些文件，而不是只给用户口头说明：

- `templates/cursor/.cursor/rules/codex-governance.mdc`
- `templates/cursor/.cursor/mcp.json`
- `templates/cursor/.cursorrules.example`

## 安装后怎么用

推荐顺序：

1. 先安装 `~/.codex/AGENTS.md`，作为全局基线。
2. 如果你需要更强个人纪律，再从 `~/.codex/AGENTS.personal.example.md` 里挑选条目合并进全局文件。
3. 检查安装后的 `rules/`、`agents/`、`skills/`。
4. 新项目接入时，把 repo 模板放到项目根目录作为 `AGENTS.md` 起点。
5. 拿一个小任务试跑，验证这些门禁和速查卡是不是真的能提升工作流。

## 当前仓库的 Feishu 同步门槛

这个仓库已经加了 repo-local 的 Feishu 同步校验，不影响全局 `~/.codex`。

- 校验脚本：`codex-integration-kit/scripts/check-feishu-sync.sh`
- 可选 hook：`.githooks/pre-commit`
- 启用方式：

```bash
git config core.hooksPath .githooks
```

推荐在提交前跑一次：

```bash
bash codex-integration-kit/scripts/check-feishu-sync.sh --staged
```

门槛含义：

- 如果 staged 改动命中了治理工作面，例如 `codex-integration-kit/**`、`skills/**`、`PROJECT.md`、`AGENTS.md`、`.codex/hooks.json`
- 但没有同时包含 `codex-integration-kit/docs/feishu-codex-governance-share.md`
- 校验会失败，阻止把这次工作当成 complete

## 推荐落地方式

- 个人使用：安装 `global-base`，按需参考 `global-personal-example`
- 团队共享：安装 `global-base + repo-template + rules + skills`
- 新项目 bootstrap：先装全局，再把 repo 模板复制进新仓库根目录

## 迁移决策

安装这个 kit 之前，先判断你是在做 `install`、`migration`、`adaptation`，还是只想拿它做治理参考：

- `mirror`：内容已经适配你的本地治理，可以原样安装
- `adapt`：核心方法可用，但命名、路径、触发条件、权限边界需要改成你的本地约束
- `wrapper`：只需要其中一小段方法时，写一张更窄的本地 skill 包一层，不要把整套外部语义直接暴露出去
- `reject`：如果和现有治理、目录结构、团队流程冲突，就不要导入

对 `skills/` 尤其要谨慎：

- kit 里的 skill 更适合作为 starter card，不应在未本地化前直接当作仓库事实来源
- 如果目标 `~/.codex/skills/` 已有同名 skill，安装前先决定是覆盖、备份后适配，还是保留原版本
- 对 skill 的语义改写应按 `writing-skills` + `test-driven-development` 的方式验证，而不是把外部文本直接拷进去
- 对 `AGENTS.md`、`rules/*`、`skills/*` 这类行为资产，验证结果必须落到仓库文件里可追溯，不能只存在聊天记录

## 说明

- 当前这套 kit 优先按 Python 3.11 + FastAPI 后端、Vue 3 + Vite 前端做了裁剪。
- 本轮治理类文档调整的 TDD 追溯记录见 `docs/tdd-traceability-20260410.md`、`docs/chat-install-tdd-20260410.md`、`docs/governance-followup-tdd-20260410.md`、`docs/feishu-sync-gate-tdd-20260413.md`、`docs/feishu-doc-writing-skill-tdd-20260413.md`。
