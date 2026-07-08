# Visual Agent

`visual-agent` is the controller skill for visual-production requests.

Use it as a normal Skill directory. Do not install it through Codex or Claude
Code plugin marketplace flow.

## Direct Use

Copy the controller and bundled workers into the target repo's skill directory:

```bash
mkdir -p /path/to/target-repo/.codex/skills
cp -R skills/visual-agent /path/to/target-repo/.codex/skills/
cp -R skills/knowledge-article-visual /path/to/target-repo/.codex/skills/
cp -R skills/infographic-onepager /path/to/target-repo/.codex/skills/
cp -R skills/visual-knowledge-onepager /path/to/target-repo/.codex/skills/
cp -R skills/svg-flow-diagram /path/to/target-repo/.codex/skills/
cp -R skills/sequence-diagram /path/to/target-repo/.codex/skills/
cp -R skills/architecture-diagram /path/to/target-repo/.codex/skills/
cp -R skills/frontend-visual-governor /path/to/target-repo/.codex/skills/
cp -R skills/project-weekly-report-gantt-map /path/to/target-repo/.codex/skills/
cp -R skills/lark-whiteboard /path/to/target-repo/.codex/skills/
```

Then route visual requests through `visual-agent` before any child visual worker
such as `svg-flow-diagram`, `architecture-diagram`, `infographic-onepager`, or
image generation.

This repository bundles the visual controller and its ordinary visual workers:
`knowledge-article-visual`, `infographic-onepager`,
`visual-knowledge-onepager`, `svg-flow-diagram`, `sequence-diagram`,
`architecture-diagram`, `frontend-visual-governor`,
`project-weekly-report-gantt-map`, and `lark-whiteboard`.

`imagegen` is a runtime/system image tool, not a repository worker.
`public-report-quality-gate` is a host-repo parent gate when the target runtime
provides it, not a visual worker bundled by this package.

## Contract

- Formal and casual visual requests both enter through `visual-agent`.
- Triggering is based on visual-deliverable intent, not fixed phrases.
- Ambiguous visual requests ask for `SVG`, `H5/HTML`, `Image model`, or
  `Hybrid` instead of silently defaulting to SVG or H5.
- Child visual skills are workers, not the top-level entry point.
- Child workers absent from the runtime are blockers, not implicit fallbacks.
- Visual quality claims require screenshot/readback or equivalent verification.
