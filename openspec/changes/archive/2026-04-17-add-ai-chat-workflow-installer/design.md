## Context

This repository already contains strong workflow assets, but they are coupled to the local Codex-oriented shape:

- `AGENTS.md` carries repo-default governance and execution boundaries
- `.codex/skills/` carries formal local workflow and principle skills
- `wiki/` carries durable operating guidance and examples

That is enough for a local repository operator, but not enough for cross-runtime installation. The main mismatch is structural:

- Codex can consume `AGENTS.md` directly as a repo instruction surface
- Cursor prefers rule files and can also use `AGENTS.md` as a simpler compatibility surface
- Claude uses a different memory and command surface

Because of that mismatch, the repository should not pretend that one raw skill or one raw instruction file can be copied unchanged to all targets.

## Goals / Non-Goals

**Goals**

- Define one canonical workflow source for installation.
- Define adapter outputs for Cursor, Claude, and Codex.
- Keep the repository as the source of truth for workflow semantics.
- Produce a Feishu-shareable explanation of the installer model.

**Non-Goals**

- Do not claim byte-for-byte identical runtime files across all platforms.
- Do not publish a vague "AI prompt pack" with no repo governance boundary.
- Do not implement unrelated workflow changes while defining the installer.
- Do not treat repo-local skills as the only installation artifact.

## Decisions

### Decision: Model this as an installer workflow, not as a single universal skill

The user-facing idea may be "one-click install", but the repository should model the solution as an installer workflow with multiple output adapters.

Alternative considered:
- Publish one universal `SKILL.md`.
  - Rejected because the runtime surfaces are different enough that a single skill file would either lose behavior or become misleading.

### Decision: Keep one canonical source and multiple adapter outputs

The repository should maintain one canonical description of:

- workflow goals
- hard boundaries
- reusable workflow units
- platform mapping rules

The installer then renders platform-specific outputs from that source.

Alternative considered:
- Author each platform package independently.
  - Rejected because drift would appear quickly and the Feishu explanation would become hard to trust.

### Decision: Separate three layers explicitly

The installer design should separate:

1. Canonical governance and workflow source
2. Platform adapter outputs
3. Share/explainer artifacts

This keeps the runtime instructions, installation mechanics, and communication material from being conflated.

### Decision: Treat Codex, Cursor, and Claude as first-class but different targets

- Codex adapter centers on `AGENTS.md` and references to repo-local skills
- Cursor adapter centers on rule-file output and compatibility guidance for `AGENTS.md`
- Claude adapter centers on its memory/command entry surfaces

Alternative considered:
- Use Codex as the canonical runtime and describe the others informally.
  - Rejected because the request is explicitly cross-platform.

### Decision: Feishu share is a formal deliverable, not an afterthought

The change should include a repository-owned explanation artifact that covers:

- why the installer exists
- how the mapping works
- what each platform receives
- where the hard boundaries are

Alternative considered:
- Leave explanation to chat or a later manual summary.
  - Rejected because the user explicitly wants a shareable Feishu output.

## Proposed Shape

```text
canonical workflow source
    ├─ governance boundary
    ├─ workflow units
    ├─ adapter mapping rules
    └─ validation checklist
            ↓
       installer workflow
            ├─ codex output
            ├─ cursor output
            ├─ claude output
            └─ feishu explainer
```

## Minimum Platform Mapping

| Platform | Primary Surface | Installer Responsibility |
|----------|------------------|--------------------------|
| Codex | `AGENTS.md` | install repo instruction entry and connect repo-local workflow assets |
| Cursor | rule files and compatibility entry | generate rules-compatible output from canonical workflow source |
| Claude | memory / command entry surfaces | generate claude-compatible workflow and command guidance |

## Evaluation Plan

### Baseline scenario A: Workflow is repo-local only

- The repository has governance, skills, and wiki guidance.
- There is no formal installer model that maps those assets across Codex, Cursor, and Claude.

### Baseline scenario B: Cross-platform story is underspecified

- A contributor wants to "install the workflow" into multiple AI chats.
- The repository does not yet define which assets are canonical and which are adapter outputs.

### After-change expectation

- The repository has a formal change describing the installer model.
- The canonical source, adapter outputs, and Feishu explainer are separated explicitly.
- The design rejects the misleading "single raw file for every platform" approach.

## Risks / Trade-offs

- [Risk] The canonical source could become too abstract to be useful. -> Mitigation: keep the first version tightly scoped to existing workflow assets only.
- [Risk] Platform adapters may drift from real runtime capabilities. -> Mitigation: record explicit mapping rules and validate each target before claiming installability.
- [Risk] The Feishu explainer could oversimplify platform differences. -> Mitigation: make the differences a required section of the share artifact.
