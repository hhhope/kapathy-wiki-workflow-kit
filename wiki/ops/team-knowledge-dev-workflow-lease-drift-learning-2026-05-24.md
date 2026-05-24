---
title: team-knowledge-dev-workflow-lease-drift / source-learning
type: learning
canonical_object: team-knowledge-dev-workflow-lease-drift
artifact_type: source-learning
language: zh-CN
audience: agent
knowledge_level: working
layer: ops
domain: ai-workflow
ops_area: learning-capture
status: active
confidence: candidate
updated_at: 2026-05-24
ai_generated: true
derived_from:
  - /mnt/d/cloud/team-knowledge/team-knowledge/logs/20260524-092808-yan-dev-workflow-lease-drift-p4m8.md
notes_scope: Adjacent-repo drift log learning. This page records reusable workflow
  lessons and adoption boundaries; it does not promote the source into repo rules,
  OpenSpec requirements, or behavior assets.
---

# Team Knowledge Dev Workflow Lease Drift / Source Learning

## Source

- Source kind: example-shaped drift log.
- Source domain/topic: Team Knowledge requirement development collaboration and
  completion-check workflow.
- Reusable capability type: structure, boundary, evidence.
- Selected module: learning-capture example/reference route.
- Topic anchor: adjacent Team Knowledge workflow; keep as candidate learning for
  report-wiki workflow governance and future agent-collaboration discussions.

## What Was Learned

The useful object is not the proposed Team Knowledge feature itself. The useful
object is the recovery pattern after a brainstorming thread drifted from the
user's target:

- Name the drift cause explicitly before continuing design.
- Separate the attractive external reference from the actual design center.
- Re-anchor new concepts in existing tables, migrations, pages, and lifecycle
  surfaces before inventing new abstractions.
- Preserve the user's page-level requirement, not only backend mechanics.
- Freeze a corrected scope before turning brainstorming into OpenSpec design.

## Reused

| Learning | Local Use |
|---|---|
| External reference boundary | Treat Multica-like examples as boundary inspiration only; do not let them become dependencies or design centers. |
| Existing-model grounding | Before proposing `WorkTarget`, lease, run, or binding concepts, map them to existing project data structures. |
| Page-level requirement recovery | A backend workflow can be correct and still miss the user's target if the core page/workbench experience is not modeled. |
| Trusted evidence gate | Completion claims should depend on linked runtime evidence, not on an actor saying a task is complete. |
| Stale/conflict states | Branch, commit, content hash, policy, or mapping changes should turn previous evidence stale instead of silently staying green. |

## Modified

- Do not import Team Knowledge's exact table names into this repo as a rule.
- Keep this as process learning for workflow design and drift recovery, not a
  requirement for report-wiki runtime behavior.
- Translate the lesson into a general design habit: when a workflow has a
  user-facing lifecycle surface, keep data model, API, evaluation, and page
  information architecture in the same corrected scope.

## Not Formalized

- No changes to `AGENTS.md`, skills, rules, OpenSpec specs, or ADRs.
- No claim that this repo needs claim/lease semantics.
- No claim that future report-wiki material workflows should implement Git or
  MR readiness checks.
- No archive-ready or behavior-trigger claim.

## Local Usefulness

This is useful for future design reviews where an agent starts from a polished
architecture analogy but has not yet anchored the proposal in the current repo's
actual data model, accepted lifecycle, and primary page surface.

It also gives a compact checklist for spotting drift in brainstorming:

1. Did the external reference become the center?
2. Did the design invent names before reading existing runtime facts?
3. Did backend mechanics crowd out the user's requested UI/workbench shape?
4. Are missing design areas listed before implementation starts?
5. Is "submit for check" separated from "complete"?

## Adoption Boundary

Adopt the recovery pattern, not the Team Knowledge feature shape. Promotion into
repo-level behavior would need a future OpenSpec change with behavior replay
evidence, because this note only proves that the pattern helped summarize one
adjacent-repo drift correction.

## Next Step

Use this as a candidate reference when reviewing future workflow designs. If the
same drift pattern appears again in this repo, update or promote the learning
through the normal workflow-governance path instead of editing behavior assets
directly.
