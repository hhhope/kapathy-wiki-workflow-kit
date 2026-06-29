---
layer: ops
domain: none
ops_area: learning-capture
canonical_object: learning-skill-scope-drift
artifact_type: trace
---

# learning-skill-scope-drift / brainstorm trace

## Trigger

User invoked `$superpowers:brainstorming` and flagged drift: the previous
discussion treated the learning work as mostly implemented by changing
`learning-capture`, but the repository has many existing skills and the
Superpowers design discussed a broader learning-agent / method split.

## Re-anchor

Current brainstorming must not continue from the assumption that
`learning-capture` alone is the complete target.

The evidence shows two separate ideas:

- `learning-capture` as the active source-learning runtime entry.
- a broader learning method layer described as `Learning Agent Controller +
  modular references / workers + structured output contract + checker / replay`
  in `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`.

## Drift Risk

If the next change only expands `learning-capture`, it may fail to make learning
methods reusable by existing repo skills such as public-report, visual,
interview, meeting-note, product-discovery, req-agent, or skill-authoring
workflows.

## Current Gate

OpenSpec artifacts remain read-only while `$superpowers:brainstorming` is
active. The next step is to clarify whether the desired design is:

- a narrower `learning-capture` controller fix;
- a cross-skill learning method layer;
- or a phased bridge that leaves `learning-capture` as the source-learning entry
  while exposing shared learning method contracts to other skills.
