# kapathy-wiki-workflow-kit

[中文](README.md) | [English](README.en.md)

Put Feishu materials, meeting notes, report drafts, and agent entrypoints into one installable, reusable, traceable Markdown workspace.

[Install](#install) · [Quick Start](#quick-start) · [Runtime](#runtime) · [Documentation](#documentation) · [Feishu Source Note](#feishu-source-note)

## Install

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

If you want Feishu / Lark automation, finish the extra setup steps:

```bash
lark-cli config init
lark-cli auth login --recommend
lark-cli auth status
```

## Quick Start

### What This Is

This repository is a workflow knowledge-base template for individuals and small teams:

- use [inbox/README.md](inbox/README.md) for raw intake
- use [wiki/index.md](wiki/index.md) to navigate durable knowledge, report drafts, and operating traces
- use [openspec/](openspec/) for repository-level workflow changes
- use [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md) as agent-facing runtime entrypoints

It is not just a passive wiki skeleton, and it is not a single-platform prompt repo.

### Suggested Order

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

## Runtime

| Use Case | Entry / Command | Notes |
|---|---|---|
| Codex repo entry | [AGENTS.md](AGENTS.md) | repository-level rules and routing |
| Claude repo entry | [CLAUDE.md](CLAUDE.md) | Claude-facing startup file |
| Cursor adapter guidance | [wiki/ai-chat-workflow-installer.md](wiki/ai-chat-workflow-installer.md) | this repository documents Cursor as an adapter target |
| Workflow change governance | [openspec/](openspec/) | proposal / design / tasks / specs |
| Raw source intake | [inbox/README.md](inbox/README.md) | drop first, refine later |
| Knowledge navigation | [wiki/index.md](wiki/index.md) | domains / reports / timeline / sources / ops |
| Installation verification | `python3 scripts/verify_wiki_workflow_kit.py` | supports optional-mode flags |
| Feishu / Lark automation | `lark-cli` | requires separate install, config, and login |

### Common Commands

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

## Documentation

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

## Feishu Source Note

The referenced Feishu article is still unavailable from the current execution environment, so the README reflects the repository itself first. Source alignment is tracked in:

- [wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md](wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md)

That page records:

- the original source link
- what is already reflected in this repository
- what still needs a later sync pass
