## Context

`principle-skills-layer` published four high-frequency mistake-correction
skills in repo `.codex/skills/`: `clarify-before-acting`,
`simplicity-first`, `surgical-changes`, and `verify-before-claiming`.

`govern-repo-agents-loaded-context` then compressed repo `AGENTS.md` into a
loaded-context entrypoint and listed those skills in High-Frequency Skills.
That made runtime trigger discovery better, but it did not classify ownership.

The gap appeared when `verify-before-claiming` was compared with root git
truth-source gates. The skill was useful as a generic reminder, but its core
capability was not repo-specific. Similar pressure applies to the other
principle skills and part of OpenSpec skill routing.

## Decision

Repo High-Frequency Skills is a runtime trigger map, not an ownership map.

Each repo-local skill row that could be mistaken for a generic capability
should be classified as one of:

- `repo-owned`: the behavior is specific to this repository's workflows,
  outputs, or wiki/Feishu delivery boundaries.
- `root-candidate`: the behavior is generally useful across repositories but is
  currently incubated or referenced here.
- `root-owned-reference`: the behavior is already owned by root/global
  guidance and the repo only adds local tightening or source links.
- `shared`: the core mechanism is general, while this repo adds local gates or
  archive/wiki detail.

The classification prevents accidental promotion. Root candidates remain
candidates until a root-focused OpenSpec change edits root assets with
evaluation evidence.

## Boundary

This change only classifies ownership and records the gap. It does not:

- edit root `~/.codex/AGENTS.md`;
- edit `~/.claude/CLAUDE.md`;
- move repo-local skills to global skills;
- rewrite skill bodies;
- add new runtime automation.

## Evidence

Use static replay evidence:

- Before: repo `AGENTS.md` listed High-Frequency Skills without ownership
  status, while root guidance already owned git truth-source and cross-repo
  execution discipline.
- After: repo `AGENTS.md` says High-Frequency Skills is runtime routing only
  and classifies root-candidate / repo-owned / shared rows.

This is documentation-level behavior evidence, not multi-session rollout proof.
