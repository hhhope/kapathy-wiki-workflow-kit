# Design: visual image delivery boundary

## Prior Art

- `openspec/specs/visual-agent-entry-route/spec.md` already requires ordinary
  visual work to enter through `visual-agent`, preserve mode ownership, and
  treat image-like references as image-mode pressure.
- `wiki/adr/0035-visual-reference-style-source-not-content-source.md` decides
  that reference images are style sources unless the user explicitly asks to
  reuse their content.
- `wiki/ops/imagegen-artifact-filesystem-bridge-explore-2026-06-24.md` records
  that the current Codex CLI can show built-in `Generated Image` artifacts while
  the shell has no repo-local PNG path, no normal `OPENAI_API_KEY`, and no
  documented export command.
- Existing skill authoring contracts require compact skill wording and
  behavior-proof evaluation for semantic skill changes.

## Runtime Behavior

### Source Role Map

When a visual request uses reference images, screenshots, posters, or prior
visuals as style examples, `visual-agent` must require a compact source-role
map before prompt/script generation:

- content source: current article, draft, markdown, oral brief, or user input;
- style source: reference images that only provide visual grammar;
- executor: image model, hybrid overlay, deterministic renderer, or whiteboard;
- output intent: what each image communicates;
- verification: what must be checked after generation.

The runtime rule should not become a brittle list of forbidden old nouns. A
targeted negative prompt is allowed only as a repair after actual generated
drift is observed.

### Delivery Capability Gate

When the selected route is `image_model` or image-model visual layer and the
user asks for local image files, `visual-agent` must distinguish:

- local file delivery is available: artifact export/path or valid API fallback;
- chat artifact only: image may be visible in the client but not accessible to
  the shell as a file;
- API fallback blocked: no usable `OPENAI_API_KEY` with image-generation scope;
- deterministic route chosen explicitly: HTML/SVG screenshot output may proceed
  but must be labeled as deterministic, not image-model generation.

If local file delivery is unavailable, the fallback output is client-mode prompt
markdown with reference image paths, source-role map, copyable prompt, and
verification checklist.

## Skill Shape

Keep `.codex/skills/visual-agent/SKILL.md` compact:

- add one short `Source Roles` section;
- add one short `Delivery Capability` section;
- add corresponding pressure scenarios to `evaluation.md`;
- keep longer rationale in this OpenSpec change and the existing ADR/ops trace.

## Verification

- Text checks prove the runtime skill contains the source-role and delivery
  capability boundaries.
- OpenSpec validation proves the spec delta is structurally valid.
- Behavior asset check is run and any unrelated pre-existing failures are
  recorded.
- `git diff --check` is scoped to the touched change and skill files.
