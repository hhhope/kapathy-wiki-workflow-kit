## Baseline Evidence

### Before change

- `wiki/ai-workflow.md` described repository AI workflow stages, but not a formal multi-platform installer model.
- The repository had repo-local skills and governance guidance, but no canonical-source vs adapter-output split for Codex, Cursor, and Claude.
- There was no repository-owned Feishu explainer for cross-platform installation.

## After-change Evidence

- Added [wiki/ai-chat-workflow-installer.md](../../../../wiki/ai-chat-workflow-installer.md) as the canonical installer model page.
- Added [wiki/adr/0011-canonical-ai-chat-installer-source-with-platform-adapters.md](../../../../wiki/adr/0011-canonical-ai-chat-installer-source-with-platform-adapters.md) to capture the stable workflow decision.
- Added [wiki/reports/ai-chat-workflow-installer-feishu-share.md](../../../../wiki/reports/ai-chat-workflow-installer-feishu-share.md) as the shareable explainer.

## Validation Commands

```bash
openspec validate add-ai-chat-workflow-installer
sed -n '1,260p' wiki/ai-chat-workflow-installer.md
sed -n '1,220p' wiki/adr/0011-canonical-ai-chat-installer-source-with-platform-adapters.md
sed -n '1,260p' wiki/reports/ai-chat-workflow-installer-feishu-share.md
```

## Boundary Confirmation

- The design defines one canonical workflow source plus platform adapters.
- It does not collapse all platforms into one misleading universal skill.
- The Feishu share artifact explains platform differences and scope boundaries without becoming the runtime source of truth.
