## Context

The current repository already contains the validated source material for a reusable workflow kit:

- repo entry behavior in `AGENTS.md`
- repo-local workflow and principle skills under `.codex/skills/`
- durable wiki structure under `wiki/`
- change governance under `openspec/`
- human workspace support through Obsidian-compatible markdown structure

The missing piece is packaging. Re-creating this setup by hand would force users to copy files selectively and guess which parts are essential versus incidental.

## Goals / Non-Goals

**Goals**

- Add one bootstrap script that creates a usable starter repository.
- Install Obsidian, OpenSpec, and examples by default in the first version.
- Reuse the current repository's validated best practices as the source for scaffold assets.
- Generate both `AGENTS.md` and `CLAUDE.md` entry files from the same kit.

**Non-Goals**

- Do not support arbitrary remote installation targets or package managers yet.
- Do not install every historical change artifact from this repository.
- Do not infer new examples beyond currently validated task families.
- Do not create different workflow assets for Codex, Cursor, and Claude beyond their entry file differences.

## Decisions

### Decision: Use local scaffold assets plus a bootstrap script

The first version should use repository-owned scaffold assets plus one bootstrap script that copies and lightly templates them into a target directory.

Alternative considered:
- Generate everything inline inside one large script.
  - Rejected because scaffold files need to stay reviewable and maintainable.

### Decision: Install Obsidian, OpenSpec, and examples by default

These are not optional extras in the first version. They are part of the working kit:

- Obsidian is the default human-facing workspace
- OpenSpec is the change-governance layer
- examples are part of onboarding and usage, not decoration

### Decision: Use current validated task families as examples

The example set should reflect current supported capabilities:

- meeting notes
- project management
- learning / knowledge notes
- Weixin article reading
- GitHub repository analysis
- explore trace

### Decision: Platform compatibility stays in the entry layer

- `AGENTS.md` covers Codex and Cursor
- `CLAUDE.md` covers Claude
- the rest of the assets remain shared

## Bootstrap Outputs

```text
target/
├─ PROJECT.md
├─ AGENTS.md
├─ CLAUDE.md
├─ wiki/
│  ├─ index.md
│  ├─ ai-workflow.md
│  ├─ ops/
│  ├─ reports/
│  ├─ sources/
│  ├─ adr/
│  ├─ templates/
│  └─ examples/
├─ .codex/skills/
├─ openspec/
├─ .obsidian/
└─ scripts/
```

## Script Responsibilities

1. Create the target skeleton.
2. Install shared scaffold assets.
3. Install the validated skill set.
4. Generate `AGENTS.md` and `CLAUDE.md`.
5. Install OpenSpec and Obsidian scaffolds.
6. Install example files.
7. Print verification and next-step guidance.

## Validation Plan

### Baseline

- No script currently creates a reusable workflow kit from the validated repository state.

### After change

- Running the bootstrap script against a new target creates the intended starter structure.
- The result includes Obsidian, OpenSpec, and examples.
- The generated repo contains `AGENTS.md` and `CLAUDE.md`.
- The installed examples map to current validated task families.
