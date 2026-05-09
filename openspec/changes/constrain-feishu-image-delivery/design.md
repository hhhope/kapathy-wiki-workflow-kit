## Scope

This change tightens the public-report delivery gate for visual assets in
Feishu-facing work.

It covers:

1. local image / one-pager / chapter-card asset generation
2. Feishu text sync
3. Feishu image insertion as a separate high-risk fork
4. gate-review evidence and pressure scenarios

It does not cover image compression, Feishu client debugging, or removing
already-inserted images.

## Current Behavior

`public-report-quality-gate` already says to ask at output fork-points and to
use `lark-doc` for Feishu writes after explicit approval. The Account Wiki
repair also recorded the client-freeze finding in the repair change.

The remaining weakness is wording ambiguity:

- "Feishu sync" can still be interpreted as text plus images.
- "image-only update" is listed as a fork, but the default is not clearly
  text-only.
- Image token read-back is not explicitly demoted in the skill body and
  pressure scenarios.

## Decision

Reader-facing reports may require visual assets, and the agent should still
produce local image assets when requested. However, Feishu image insertion is a
separate operation from Feishu text sync.

Default route:

```text
generate local visual asset
  -> record or link local asset path
  -> text-only Feishu sync if approved
  -> user manually adds images, unless they separately approve image insertion
```

If the user explicitly asks the agent to insert images into Feishu, the agent
must state the known client-freeze risk, get explicit confirmation for that
operation, and record that read-back is audit evidence only.

## Verification

- RED/GREEN evidence in `evaluation.md`.
- Static checks for the new skill wording and reference scenarios.
- `openspec validate constrain-feishu-image-delivery --strict`.
- Git status/log verification before completion claim.
