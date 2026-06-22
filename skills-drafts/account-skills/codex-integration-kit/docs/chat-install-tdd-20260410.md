# TDD Traceability: Conversation-Driven Install

Date: 2026-04-10  
Branch: `codex-chat-install-kit`

## Scope

- `codex-integration-kit/skills/governance-install/SKILL.md`
- `codex-integration-kit/templates/cursor/.cursor/rules/codex-governance.mdc`
- `codex-integration-kit/templates/cursor/.cursor/mcp.json`
- `codex-integration-kit/templates/cursor/.cursorrules.example`
- `codex-integration-kit/README.md`
- `codex-integration-kit/AGENTS.md`
- `codex-integration-kit/templates/repo/AGENTS.repo-template.md`
- `codex-integration-kit/docs/feishu-codex-governance-share.md`

## RED Scenarios

### Scenario 1: The kit only supports shell-first Codex installation

Expected behavior:
- A user should be able to ask for installation directly in chat.
- The kit should include a reusable skill that routes installation requests by platform, mode, and scope.

Baseline evidence before the fix:

```bash
find codex-integration-kit/skills -maxdepth 2 -name 'SKILL.md' | sort
```

Observed failure before the change:
- There was no install-focused skill under `codex-integration-kit/skills/`.
- README content routed install through shell commands rather than a conversation-first flow.

### Scenario 2: Cursor has no direct-install templates

Expected behavior:
- The kit should include concrete Cursor files the agent can write into a target project.

Baseline evidence before the fix:

```bash
find codex-integration-kit -maxdepth 4 \
  \( -path '*/cursor*' -o -name '*.mdc' -o -name '.cursorrules' \) | sort
```

Observed failure before the change:
- No `.cursor/rules/*.mdc`
- No `.cursor/mcp.json`
- No `.cursorrules` example

## GREEN Changes

- Added `skills/governance-install/SKILL.md` for conversation-driven install routing.
- Added Cursor templates for:
  - `.cursor/rules/codex-governance.mdc`
  - `.cursor/mcp.json`
  - `.cursorrules.example`
- Updated kit documentation and template indexes so the install skill is discoverable.
- Updated Feishu source content to explain chat-first install for Codex and Cursor.

## GREEN Verification

### Verification Command 1

```bash
find codex-integration-kit/skills -maxdepth 2 -name 'SKILL.md' | sort
```

Expected pass condition:
- `codex-integration-kit/skills/governance-install/SKILL.md` exists.

### Verification Command 2

```bash
find codex-integration-kit/templates/cursor -maxdepth 5 | sort
```

Expected pass condition:
- Cursor template files exist at the expected paths.

### Verification Command 3

```bash
rg -n "Chat-First Install|governance-install|Cursor 直接安装产物|对话式安装" \
  codex-integration-kit/README.md \
  codex-integration-kit/AGENTS.md \
  codex-integration-kit/templates/repo/AGENTS.repo-template.md \
  codex-integration-kit/docs/feishu-codex-governance-share.md
```

Expected pass condition:
- Documentation now exposes the conversation-first install path.

### Verification Command 4

```bash
mkdir -p /tmp/cursor-install-verify
cp -R codex-integration-kit/templates/cursor/. /tmp/cursor-install-verify/
find /tmp/cursor-install-verify -maxdepth 5 | sort
```

Expected pass condition:
- The copied target contains `.cursor/rules/codex-governance.mdc`
- The copied target contains `.cursor/mcp.json`
- The copied target contains `.cursorrules.example`

## Notes

- This trace file exists because the new install flow changes agent behavior, not just prose.
- The verification is repository-backed and should not rely on chat memory alone.
