---
name: governance-install
description: "Use when the user wants to install, bootstrap, preview, or directly apply the Codex governance kit into Codex or Cursor by conversation, including prompts like install governance, set up Codex, set up Cursor rules, preview installation, or apply the minimal/team variant."
---

# Governance Install

Conversation-first installer for this governance kit. Use it when the user wants the agent to perform installation directly, without sending them to shell scripts or `/plan` mode first.

If the request also includes installing or relocating the shared Lore Wiki repository itself, route that part to `lore-bootstrap` and keep the conversation-first flow. Do not reduce Lore Wiki setup to a README pointer.

## Do Not

- Do not stop at README instructions when the user clearly wants the agent to perform the installation.
- Do not assume `Codex` and `Cursor` use the same target paths.
- Do not overwrite existing config files without first showing the target paths and whether the action is preview-only or apply.
- Do not install Cursor files into `.codex/`, or Codex global files into `.cursor/`.
- Do not claim installation succeeded without checking the created target files.

## Intent Routing

| User intent | Platform | Mode | Action |
|---|---|---|---|
| "帮我把这套规范装到 Codex" | Codex | apply | Install global/repo governance files into `~/.codex` or the requested target |
| "先预览 Codex 安装" | Codex | dry-run | Show target files and planned copy set without writing |
| "给 Cursor 装这套规则" | Cursor | apply | Create `.cursor/rules/` and related Cursor config files in the target project |
| "先预览 Cursor 安装" | Cursor | dry-run | Show the Cursor files that would be created |
| "装最小版" | Codex or Cursor | apply or dry-run | Install only the minimal baseline for that platform |
| "装团队版" | Codex or Cursor | apply or dry-run | Install the richer baseline plus shared rules/skills for that platform |
| "初始化 lore wiki" / "把 team-lore 装到 D 盘" | Codex + Lore | apply or dry-run | Keep governance-install for Codex/Cursor config, then route shared wiki bootstrap to `lore-bootstrap` with explicit install path confirmation |

## Platform Targets

### Codex

- Global baseline: `~/.codex/AGENTS.md`
- Optional personal overlay: `~/.codex/AGENTS.personal.example.md`
- Repo template: `~/.codex/AGENTS.repo-template.md`
- Shared references: `~/.codex/rules/`, `~/.codex/agents/`, `~/.codex/skills/`

### Cursor

- Project rule file: `.cursor/rules/codex-governance.mdc`
- Optional MCP example: `.cursor/mcp.json`
- Optional legacy compatibility example: `.cursorrules.example`

## Install Modes

### Dry-run

- Show target platform
- Show target paths
- Show whether each file already exists
- Show minimal vs team scope
- Do not write files

### Apply

- Write the selected files
- Preserve unrelated existing files
- If overwriting, surface the exact path first
- Verify created files after writing

## Variants

### Minimal

Install only what is needed to make the governance entrypoint work immediately:

- Codex: `AGENTS.md`
- Cursor: `.cursor/rules/codex-governance.mdc`

### Team

Install the richer shared kit:

- Codex: global baseline + repo template + `rules/` + `agents/` + `skills/`
- Cursor: rule file + MCP example + any shared project-level reference files the template depends on

## Apply Steps

1. Detect requested platform: `codex`, `cursor`, or both
2. Detect requested mode: `dry-run` or `apply`
3. Detect requested scope: `minimal` or `team`
4. Resolve the target paths
5. If shared Lore Wiki install is in scope, confirm or default its path explicitly; current preferred default is `/mnt/d/team-lore`
6. Preview the exact files
7. Apply only if the user asked to apply or clearly said "install"
8. Verify the created files and report the result

## Verification

After apply, verify by listing the exact created files for the chosen platform.

Expected examples:

- Codex minimal:
  - `~/.codex/AGENTS.md`
- Cursor minimal:
  - `.cursor/rules/codex-governance.mdc`
- Cursor team:
  - `.cursor/rules/codex-governance.mdc`
  - `.cursor/mcp.json`
  - `.cursorrules.example`

## Common Failures

| Failure | Root cause | Fix |
|---|---|---|
| User asked for installation but only got README instructions | The agent treated install as documentation instead of execution | Switch to this skill and perform dry-run or apply directly |
| Codex files were written into project `.cursor/` paths | Platform routing was blurred | Re-route by platform before writing |
| Cursor install created nothing persistent | The agent described files but did not write them | Use apply mode and verify the created `.cursor/` files |
| Existing config got clobbered without warning | Overwrite paths were not previewed first | Surface exact target paths before apply and preserve unrelated files |
| Lore Wiki path was silently assumed under `$HOME` | Installer treated wiki location as an implementation detail | Ask or default explicitly, then report the chosen path in the result |
