# Evaluation: visual-agent entry route hardening

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: high-frequency skill routing and behavior-asset gates.
- `PROJECT.md`: OpenSpec source-of-truth model.
- `.codex/skills/visual-agent/SKILL.md`: current controller route.
- `.codex/skills/public-report-quality-gate/SKILL.md`: public output parent
  gate and visual delegation map.
- `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`:
  replay cases that currently name child visual workers directly.
- `openspec/changes/add-visual-agent-routing/*`: original visual controller
  proposal, design, spec, and evaluation.
- `openspec/specs/public-report-quality-gate/spec.md`: existing HTML-target
  visual route requirements.
- `wiki/ops/visual-output-routing-drift-explore-2026-05-11.md` and related
  visual drift records: prior H5/SVG fallback failure.
- `/home/yan/.codex/rules/common/development-workflow.md`,
  `/home/yan/.codex/skills/writing-skills/SKILL.md`, and
  `/home/yan/.codex/skills/test-driven-development/SKILL.md`: semantic
  behavior-asset evaluation requirements.

Classification:

- Owns: repo-local observable visual-agent entry, child-route map, and public
  gate delegation wording.
- References: global visual worker skills, image generation executor behavior,
  public-report quality gate, OpenSpec lifecycle.
- Rejects: editing global worker skills in this change, making `imagegen` a
  planner, or treating deterministic H5/SVG as the silent fallback for ambiguous
  visual requests.

## Pressure Scenarios

### Scenario 1: ambiguous visual request

- Input or situation shape: user says "帮我制图 / 出图 / 配图" without naming a
  desired mode.
- Trigger condition: visual-deliverable wording is present and no strong
  content evidence chooses a mode.
- Expected route or stop behavior: response exposes `Using visual-agent` and
  asks the bounded SVG / H5/HTML / image-model / hybrid fork.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no immediate H5/SVG production.
- Promotion or non-promotion boundary: repo-local behavior only.
- Proof boundary: text-level route replay, not visual quality proof.

### Scenario 2: reader-facing H5 asks for visuals

- Input or situation shape: user says "这个 H5 加一组章节配图 / 知识卡 / 一图流".
- Trigger condition: public-report artifact plus visual deliverable wording.
- Expected route or stop behavior: `public-report-quality-gate` stays the outer
  parent for reader-facing quality, but visual production route is
  `public-report-quality-gate -> visual-agent -> child worker`.
- Repo-visible artifact:
  `.codex/skills/public-report-quality-gate/SKILL.md` and
  `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`.
- Expected output or non-output: no direct HTML body edit that substitutes H5
  sections for standalone visual assets.
- Promotion or non-promotion boundary: does not modify global worker skills.
- Proof boundary: route proof only; final report quality still needs visual QA.

### Scenario 3: user names a worker directly

- Input or situation shape: user says "用 infographic-onepager 做一图流" or
  "用 svg-flow-diagram 画这个".
- Trigger condition: named worker is a visual child worker and the task is
  ordinary production, not debug review.
- Expected route or stop behavior: response still exposes `Using visual-agent`,
  confirms mode/evidence, then delegates to the named worker if appropriate.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no direct child-worker execution before the
  controller confirms route.
- Promotion or non-promotion boundary: named workers keep execution ownership.
- Proof boundary: route replay only.

### Scenario 4: prior H5/SVG rejection

- Input or situation shape: user says the workflow repeatedly made H5/SVG when
  they wanted image-model-like visuals.
- Trigger condition: user flags H5/SVG fallback as the failure mode.
- Expected route or stop behavior: `visual-agent` treats image-model or hybrid
  as active route pressure until deterministic output is explicitly chosen.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no fresh deterministic fallback based only on
  Chinese text reliability.
- Promotion or non-promotion boundary: does not claim image-model text accuracy
  is solved.
- Proof boundary: route proof only; generated bitmap quality remains separate.

### Scenario 5: non-visual public report edit

- Input or situation shape: user asks to polish a reader-facing report's prose
  without visual-deliverable wording.
- Trigger condition: public report gate applies, but no visual production is
  requested.
- Expected route or stop behavior: no `visual-agent` requirement; public-report
  quality gate owns the work.
- Repo-visible artifact: public-report pressure scenarios.
- Expected output or non-output: no unnecessary visual mode fork.
- Promotion or non-promotion boundary: visual-agent is not made universal.
- Proof boundary: negative trigger evidence only.

## RED Baseline

Baseline checks against the pre-change wording:

- `rg -n "Using visual-agent|visual-agent -> knowledge-article-visual|visual-agent -> infographic-onepager|public-report-quality-gate -> visual-agent|visual-agent first|direct visual worker" .codex/skills/visual-agent/SKILL.md .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/public-report-quality-gate/references/pressure-scenarios.md .codex/skills/visual-agent/evaluation.md`
  returned no matches.
- `public-report-quality-gate` directly mapped article-level visual packages to
  `knowledge-article-visual`, per-image scripts to `infographic-onepager`, and
  bitmap assets to `imagegen`.

Observed loophole:

- A future agent could load the public gate and follow its delegation map
  directly to child workers without first exposing the `visual-agent` mode fork.
- The current visual-agent did not require an observable entry marker, so a
  bypass was hard to detect in normal responses.

## GREEN Result

After the patch:

- `visual-agent` requires the visible entry marker `Using visual-agent`.
- Directly named worker requests still route through `visual-agent` first.
- Ambiguous visual terms cannot silently default to H5/HTML or SVG.
- Public-report visual delegation maps visual production through
  `visual-agent` before child workers and image executors.
- Pressure scenarios cover visual-agent-first routing for reader-facing visual
  requests and named worker requests.

GREEN checks:

- `rg -n "Using visual-agent|public-report-quality-gate -> visual-agent|visual-agent -> knowledge-article-visual|visual-agent -> infographic-onepager|visual-agent -> svg-flow-diagram|visual-agent -> architecture-diagram|visual-agent -> imagegen|direct visual worker|H5/SVG" ...`
  found the required entry marker, public-gate visual route, child-worker route
  map, and H5/SVG fallback replay text in the changed files.
- `rg -n 'article-level visual package \| `knowledge-article-visual`|per-image poster or card script \| `infographic-onepager`|generated bitmap assets \| `imagegen`|visual-agent -> public-report-quality-gate' ...`
  returned no matches, confirming the old direct public-gate child mappings and
  reversed reader-facing route were removed.
- `openspec validate harden-visual-agent-entry-route --strict` reported
  `Change 'harden-visual-agent-entry-route' is valid`. The CLI then emitted
  PostHog network flush warnings because the environment cannot resolve
  `edge.openspec.dev`; the validation result itself was local and valid.
- `python3 scripts/check_behavior_assets.py` returned non-zero only for the
  pre-existing `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
  gaps. It did not report this change.

## Residual Risks

- This change hardens repo-local routing. It cannot guarantee all external
  clients or global skill registries will dispatch the same way unless they
  load this repo's AGENTS/skill context.
- Global worker skills under `/home/yan/.codex/skills` were not edited.
- Route proof does not prove final visual quality, Chinese typography quality,
  Feishu usability, or image-model accuracy.
