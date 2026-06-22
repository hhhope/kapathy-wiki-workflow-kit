# openspec-superpowers-bridge

将 OpenSpec 变更目录（explore / proposal / specs / design / tasks）规范化为 Superpowers `writing-plans` 的单一输入 brief，并约束实现阶段走 TDD 执行链而非 `/opsx:apply`。

## Cursor 安装

任选一种方式（不要放进 `~/.cursor/skills-cursor/`，该目录为 Cursor 内置 skill 保留）。

### 方式 A：个人 skill（推荐，跨仓库可用）

一键安装（优先目录联接，失败则复制）：

```powershell
powershell -ExecutionPolicy Bypass -File "D:\workspace-baofu\account-skills\skills\openspec-superpowers-bridge\scripts\install-cursor-personal.ps1"
```

或手动 junction：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills"
cmd /c mklink /J "%USERPROFILE%\.cursor\skills\openspec-superpowers-bridge" "D:\workspace-baofu\account-skills\skills\openspec-superpowers-bridge"
```

macOS / Linux：

```bash
mkdir -p ~/.cursor/skills
ln -s /path/to/account-skills/skills/openspec-superpowers-bridge ~/.cursor/skills/openspec-superpowers-bridge
```

重启 Cursor 或新开 Agent 会话后，在 **Settings → Rules → Agent Skills** 中应能看到 `openspec-superpowers-bridge`。

### 方式 B：项目内 skill（团队共享）

在目标业务仓库（如 `yqt-trade`）中：

```powershell
New-Item -ItemType Directory -Force -Path ".cursor\skills"
cmd /c mklink /J ".cursor\skills\openspec-superpowers-bridge" "D:\workspace-baofu\account-skills\skills\openspec-superpowers-bridge"
```

将 `account-skills` 路径换成团队统一的 clone 位置；或把本文件夹复制进 `.cursor/skills/`（无需 junction）。

### 方式 C：Codex / Claude Code

```bash
# 复制或 symlink 到 ~/.codex/skills/ 后，与 Cursor 相同触发 description
```

## 业务仓库前置条件

目标仓库建议具备：

- `openspec/changes/<change>/` 与 `proposal.md`（必需）
- `design.md`、`tasks.md`、`specs/**/spec.md`（桥接前应尽量齐全）
- 根目录 `AGENTS.md` 声明 OpenSpec 为范围真源、Superpowers 为执行工具（与 [yqt-trade AGENTS.md](https://github.com/your-org/yqt-trade) 同类）

## 快速运行脚本

在**含 `openspec/` 的业务仓库根目录**执行（脚本可在 account-skills 任意位置）：

```bash
python /path/to/account-skills/skills/openspec-superpowers-bridge/scripts/build-planning-brief.py openspec/changes/<change-id>
```

输出：`<change-dir>/planning-brief-for-superpowers.md`

## 文件结构

```text
openspec-superpowers-bridge/
├── SKILL.md
├── README.md
├── examples.md
├── references/
│   ├── openspec-artifacts.md
│   ├── writing-plans-handoff.md
│   └── explore-notes-template.md
└── scripts/
    └── build-planning-brief.py
```

## 相关 skill

- OpenSpec：`openspec-propose` / `openspec-continue-change` / `openspec-verify-change`
- Superpowers：`writing-plans`、`test-driven-development`、`executing-plans`
- 团队记忆：`lore`（大改动时的 proposal/design/tasks 门禁，若仓库启用）
