---
layer: ops
domain: ai-workflow
ops_area: agent-governance
canonical_object: skill-runtime-governance-root-install
artifact_type: retro
title: skill-runtime-governance root install / retro
type: retro
language: zh-CN
status: active
created_at: 2026-05-24
updated_at: 2026-05-24
ai_generated: true
derived_from:
  - docs/superpowers/specs/2026-05-24-skill-runtime-governance-design.md
  - docs/superpowers/plans/2026-05-24-skill-runtime-governance.md
related_objects:
  - skill-runtime-governance-scope-drift
  - behavior-replay-gate
  - skill-authoring-contract
notes_scope: 记录 root skill-runtime-governance 的本机安装和局部 RED/GREEN 证据边界；不声明 root AGENTS 路由或多端 rollout。
---

# skill-runtime-governance root install / retro

## Installed Files

- `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

## Evidence

- RED baseline: recorded in root evaluation file.
- GREEN replay: recorded in root evaluation file.
- Residual risks: recorded in root evaluation file.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/skill-runtime-governance-root-install-2026-05-24.md` returned no blockers.
- `python3 scripts/check_wiki_frontmatter.py` exited 0.
- `python3 scripts/check_behavior_assets.py` exited 1 on an existing unrelated evaluation file:
  `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`.

## RED Boundary

The prompted RED probes all returned `PASS`, but they were too explicit because
the prompts already named the expected evaluation surface. The failing RED
evidence therefore comes from the live incident before the skill existed:

- English-first behavior-asset guidance leaked into a `wiki/ops` note.
- `$writing-skills` was treated as the center of an evaluation-routing question.
- `skill-runtime-governance` was narrowed back into `$superpowers:brainstorming`
  and then into "user questioning" as a trigger.
- Continuation followed the visible technical chain until the user stopped and
  re-anchored the scope.

## GREEN Boundary

GREEN replay was run for all ten scenarios after installing the root skill. The
replays selected fixed triage fields and routed to the expected evaluation
surface before action.

This is still local pressure evidence only. It does not prove automatic loading,
root `AGENTS.md` routing, or multi-client rollout.

## Boundary

This note records local root skill installation evidence. It does not claim:

- root `AGENTS.md` routing;
- automatic skill discovery in every future incident;
- plugin/cache skill changes;
- multi-client or multi-session rollout proof.
- repository behavior-asset checker cleanliness; the observed non-zero result is unrelated to the new root skill files.
