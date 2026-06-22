---
project: account-skills
status: active
primary_area: codex-integration-kit
---

# Account Skills

## Summary

Skill library and integration kit for Codex and related agent workflows.

## Current Focus

- Improve `codex-integration-kit` governance content and migration quality.
- Prefer conversation-first install flows for Codex and Cursor over shell-first instructions.
- Keep governance constraints, TDD evidence, and migration boundaries aligned.

## Working Memory

- Any material change to this project must also update the Feishu-facing share content in the same work cycle.
- Primary in-repo Feishu source: `codex-integration-kit/docs/feishu-codex-governance-share.md`
- Published Feishu doc: `https://my.feishu.cn/docx/GgKadcZzpoqz8lxrBd0clQY1n2f?from=from_copylink`
- When the user changes direction or asks for governance/content updates, refresh the Feishu source in the same work cycle instead of deferring it silently.
- Traceable verification evidence for behavior-asset changes must live in-repo, not only in chat.

## Boundaries

- Preserve unrelated dirty worktree changes.
- Do not continue feature work directly on `main`.
- Treat `codex-integration-kit` as reusable kit content; remove repo-private assumptions when found.

## Completion Gates

- Any material change under `codex-integration-kit/**`, `skills/**`, governance rules, installation flow, or Lore/Graphify usage is incomplete until `codex-integration-kit/docs/feishu-codex-governance-share.md` is updated in the same work cycle.
- Do not close the task, summarize it as complete, or treat the work as ready for rollout until that Feishu-facing source markdown has been reviewed against the final repo truth.
