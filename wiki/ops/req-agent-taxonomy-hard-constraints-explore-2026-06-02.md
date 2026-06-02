---
title: req-agent taxonomy hard constraints explore
type: intake
language: zh-CN
source_path: chat://openspec-explore/req-agent-taxonomy-hard-constraints/2026-06-02
source_type: conversation
audience: self
knowledge_level: working
domain: report-workflow
layer: ops
ops_area: workflow-trace
canonical_object: req-agent-taxonomy-hard-constraints
artifact_type: explore
period: active
confidence: medium
status: active
updated_at: 2026-06-02
ai_generated: true
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# req-agent taxonomy hard constraints explore

## Trigger

User invoked `$report-wiki-portfolio:openspec-explore` and asked to inspect the
`req-agent` skill, its corresponding taxonomy, and related hard constraints.

## Focus

- `req-agent` as the normal Codex-facing requirements controller.
- Separation between requirements readiness taxonomy and wiki frontmatter
  taxonomy.
- Hard routing, mutation, and handoff boundaries before OpenSpec draft or
  implementation work.

## Current Hypotheses

- `requirements/config/requirements-taxonomy.yaml` owns requirements readiness.
- `wiki/config/frontmatter-taxonomy.yaml` owns wiki page identity only.
- `req-agent` should report bounded state and route to one worker, not become a
  general workflow editor.

## Open Questions

- Whether the current `req-agent` skill wording is compact enough to preserve
  the taxonomy split at runtime.
- Whether the hard constraints are fully backed by OpenSpec evidence and
  behavior replay.
- Whether any future wording change would need a dedicated OpenSpec change
  rather than an ad hoc skill edit.

## Next Step

Continue read-only inspection of the skill, taxonomy files, OpenSpec change
artifacts, and repo governance constraints before proposing any change.
