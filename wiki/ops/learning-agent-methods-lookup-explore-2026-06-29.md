---
layer: ops
domain: none
ops_area: learning-capture
canonical_object: learning-agent-methods-lookup
artifact_type: trace
---

# learning-agent-methods-lookup / explore trace

## Trigger

User invoked `$report-wiki-portfolio:openspec-explore` and asked to carefully
locate the remembered learning agent and its defined learning methods.

## Scope

- Read-only lookup across repo-local skills, drafts, OpenSpec changes, and wiki
  ops records.
- Do not implement, archive, or promote behavior rules from this lookup.
- Preserve distinction between standalone `SKILL.md` assets and reference
  modules under an existing skill.

## Current Evidence Target

Primary suspected object: `.codex/skills/learning-capture/` and related
learning workflow matrix artifacts.

## Findings

- Draft learning agent found:
  `skills-drafts/account-skills/skills/compound-learning/SKILL.md`.
- Published runtime skill found:
  `.codex/skills/learning-capture/SKILL.md`.
- Learning workflow matrix design found:
  `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`.
- Current OpenSpec implementation evidence:
  `openspec/changes/add-learning-workflow-matrix/`.

## Boundary

The draft `compound-learning` skill is an experience-compounding / mistake-log
agent in `skills-drafts`. The published repo runtime path is
`learning-capture`; the many learning methods are implemented as references
under `.codex/skills/learning-capture/references/`, not as separate top-level
skills.
