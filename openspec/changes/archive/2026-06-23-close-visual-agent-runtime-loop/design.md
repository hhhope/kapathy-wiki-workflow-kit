# Design: visual-agent runtime loop closure

## Runtime Surface

The repo-local runtime surface should be self-contained for ordinary visual
skill dispatch. `visual-agent` remains the controller, and ordinary child
workers that it names should exist under `.codex/skills/` in this repository.

The runtime surface includes:

- `visual-agent`
- `knowledge-article-visual`
- `infographic-onepager`
- `visual-knowledge-onepager`
- `svg-flow-diagram`
- `sequence-diagram`
- `architecture-diagram`
- `frontend-visual-governor`
- `project-weekly-report-gantt-map`
- `lark-whiteboard`

`imagegen` remains a runtime/system image tool. `public-report-quality-gate`
remains a host-repo parent gate, not a visual worker.

## Drift Closure

The previous gap was between package edits and repo runtime behavior. This
change treats runtime discovery as part of the completion gate:

- top-level skill discovery must find the bundled visual workers;
- `visual-agent` must not describe missing bundled workers as merely external
  companions;
- fixed colloquial examples may appear only as evidence of prior failures or
  examples, not as the route mechanism;
- the live drift trace must record what was fixed locally and what still belongs
  to the account-skills branch.

## Verification

Use text-level pressure checks rather than image generation:

- list `.codex/skills/*/SKILL.md` and verify visual workers are discoverable;
- scan the visual runtime surface for old fixed-trigger route wording and old
  channel-specific skill names;
- run `git diff --check`;
- run OpenSpec validation for this change.

