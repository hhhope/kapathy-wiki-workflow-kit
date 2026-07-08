# visual-agent evaluation

## Pressure Scenarios

- Ambiguous visual-controller request: user asks the agent to decide among SVG,
  H5/HTML, image-model, and hybrid visual production. Expected:
  response includes `Using visual-agent`, uses `mode_fork`, and presents the
  four output modes.
- Plain visual request without explicit mode. Expected: no silent H5/SVG
  default; ask the bounded mode fork unless strong content evidence selects a
  mode.
- Colloquial visual request with no canonical keyword, such as asking to make
  material more scannable, turn notes into a shareable thing, prepare a visual
  version, add presentation form, or make a page/image/card-like output.
  Expected: trigger `visual-agent`, expose `Using visual-agent`, and ask the
  mode fork unless strong content evidence selects a route.
- Non-keyword mode request: user asks "别直接给我默认做网页或 SVG，先判断该用什么形态".
  Expected: trigger `visual-agent` because the requested action is visual
  medium selection, even without naming a final artifact.
- Flow source: Mermaid sequence, payment clearing flow, or fund flow. Expected:
  route to `svg-flow-diagram` with `Output Mode: svg` unless the user overrides.
- Architecture source: system architecture, interface topology, or deployment
  diagram. Expected: use `architecture-diagram` only if it is available;
  otherwise keep ownership in `visual-agent` and mark the missing worker.
- Reader-facing H5/report source. Expected: preserve
  `public-report-quality-gate` only if it is available; otherwise keep the
  public/report concern visible as a missing parent gate and do not bypass
  `visual-agent`.
- Dense Chinese text plus image-model preference. Expected: warn about text
  accuracy and offer `hybrid` or deterministic overlay.
- H5 source plus reference PNG / similar-image target. Expected: treat
  `image_model` or `hybrid` as active route pressure and ask or confirm the
  mode fork; do not start HTML/CSS/SVG/browser-screenshot production because
  Chinese text would be safer in deterministic rendering.
- Directly named worker: user asks for `infographic-onepager`,
  `svg-flow-diagram`, or `imagegen`. Expected: still enter through
  `visual-agent` first unless the task is worker debug review; execute only
  workers that are actually available.
- Bundled worker availability: this repository bundles
  `knowledge-article-visual`, `infographic-onepager`,
  `visual-knowledge-onepager`, `svg-flow-diagram`, `sequence-diagram`,
  `architecture-diagram`, `frontend-visual-governor`,
  `project-weekly-report-gantt-map`, and `lark-whiteboard`. Expected: route only
  to a child worker that is present in runtime discovery; otherwise keep
  ownership in `visual-agent`, mark the unavailable worker in `Blocked Action`,
  and ask for mode/source confirmation or installation.
- Runtime/system visual routes: `imagegen` is usable only when the runtime
  provides the image tool/skill; `public-report-quality-gate` is preserved only
  when the host repo provides it. Expected: neither is falsely described as a
  bundled account-skills worker.
- Visual worker matrix coverage: article/card set requests route to
  `knowledge-article-visual`; one-pager/poster/long-image requests route to
  `infographic-onepager`; architecture/topology requests route to
  `architecture-diagram`; sequence/call-order authoring routes to
  `sequence-diagram` when present; UI/dashboard polish routes to
  `frontend-visual-governor`; Gantt/capability-map/weekly-report visuals route
  to `project-weekly-report-gantt-map`; whiteboard requests route to
  `lark-whiteboard`; image-model output routes to `imagegen` after mode and
  verification boundaries are set.
- Non-visual meeting notes request. Expected: visual-agent does not trigger.

## RED Baseline

Before this skill, visual routing depended on ad hoc model judgment. A request
could jump directly to image generation, confuse SVG workers, or skip the human
mode fork. Before the entry-route hardening, public-report delegation also
listed `knowledge-article-visual`, `infographic-onepager`, and `imagegen`
directly, and normal visual responses had no required `Using visual-agent`
marker. The first compact version still leaned on a short list of casual
Chinese examples; that was not enough because it described phrases instead of
the generalized visual-deliverable intent class. It also had an incomplete
route table that omitted available companion visual workers and blurred bundled
workers with runtime-provided workers, which could make a future agent claim a
route without checking runtime availability.

## GREEN Result

The skill now defines a compact runtime controller: `Using visual-agent`, mode
fork, no silent H5/SVG fallback, child worker routes, public-report gate
preservation, and verification/Feishu stops. The trigger model covers the
visual-deliverable intent class by artifact role, transformation role, medium
selection role, and visual repair role, instead of depending on fixed trigger
phrases. Child routing now requires runtime availability and uses a complete
bundled visual worker matrix for ordinary visual skills in this repository.
`imagegen` remains a runtime/system tool and `public-report-quality-gate`
remains a host-repo parent gate. Unavailable workers are explicit blockers, not
implicit fallbacks.

## Residual Risks

This skill proves routing behavior only. Final SVG, H5, or bitmap quality still
depends on the selected worker and visual verification.

## 2026-06-22 Bundled Worker Migration

### Pressure Scenarios

- Visual request routes to `knowledge-article-visual`,
  `infographic-onepager`, `visual-knowledge-onepager`, `architecture-diagram`,
  `frontend-visual-governor`, `project-weekly-report-gantt-map`,
  `lark-whiteboard`, or `sequence-diagram`.
- The account-skills package is installed into a runtime that only has this
  repository's `skills/` directory.
- A future agent scans top-level skill directories with
  `find skills -maxdepth 2 -name SKILL.md`.

### RED Baseline

The prior branch version mentioned these visual workers in `visual-agent` but
bundled only `svg-flow-diagram`. That meant a future agent could claim a child
route that was not actually shipped by account-skills. `sequence-diagram` also
had its `SKILL.md` nested under `skills/sequence-diagram/skills/`, so ordinary
top-level skill discovery missed it.

### GREEN Result

The repository now bundles ordinary visual workers as top-level skill
directories: `knowledge-article-visual`, `infographic-onepager`,
`visual-knowledge-onepager`, `svg-flow-diagram`, `sequence-diagram`,
`architecture-diagram`, `frontend-visual-governor`,
`project-weekly-report-gantt-map`, and `lark-whiteboard`.

`imagegen` is explicitly documented as a runtime/system image tool, and
`public-report-quality-gate` is explicitly documented as a host-repo parent
gate. Neither is falsely presented as an account-skills worker.

### Evidence

- `find skills -maxdepth 2 -name SKILL.md` includes all bundled visual workers.
- Fixed-phrase trigger scan over the visual controller and bundled workers no
  longer finds route-controlling colloquial trigger rows.
- `git diff --check` passes.

### Residual Risks

Copied worker internals may still contain style examples or scene references
that mention visual vocabulary. Those references are not route triggers; future
localization can shrink them if account-skills needs a smaller package.

## 2026-06-22 Repo-Local Runtime Closure

### Pressure Scenarios

- This repository's runtime loads `.codex/skills` directly and receives a
  visual request that routes through `visual-agent`.
- The controller names a child worker such as `knowledge-article-visual`,
  `infographic-onepager`, `visual-knowledge-onepager`, `architecture-diagram`,
  `frontend-visual-governor`, `project-weekly-report-gantt-map`,
  `lark-whiteboard`, or `sequence-diagram`.
- The user expects the current report-wiki runtime to behave like the
  account-skills visual package branch.

### RED Baseline

Before the repo-local repair, this command found only the controller:

```bash
find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'visual|infographic|knowledge|architecture|frontend|project-weekly|lark|sequence|svg'
```

The installed `.codex/skills/visual-agent/SKILL.md` still described only
`svg-flow-diagram` as bundled and treated the other visual workers as runtime
companions.

### GREEN Result

The repo-local `.codex/skills` surface now includes the controller and ordinary
visual child workers:

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

The controller now distinguishes bundled visual workers from runtime/system
`imagegen` and host-gate `public-report-quality-gate`.

### Evidence

- Repo-local discovery lists all visual worker `SKILL.md` files under
  `.codex/skills`.
- Fixed-trigger scan over the repo-local visual runtime surface finds no
  route-controlling old colloquial trigger rows and no old channel-specific
  visual one-pager skill name.
- Remaining visual-word hits are style-reference wording inside
  `lark-whiteboard`, not route rules.

### Residual Risks

This closes the current repo runtime surface. Account-skills package README and
integration-kit cleanup remains a separate branch phase.

## 2026-06-23 Image Reference Mode Ownership

### Pressure Scenarios

- User provides an H5 source and a PNG reference, then asks for a similar image.
- User provides a poster/screenshot/cover reference without choosing SVG,
  H5/HTML, image model, or hybrid.
- Dense Chinese text makes image-model text accuracy risky.

### RED Baseline

The live failure converted a PNG-reference image request into:

```text
我会用 HTML/CSS 做同风格海报并截图成 PNG。
```

That skipped the user's output-mode decision. The rationalization was that
Chinese text would be safer through deterministic rendering.

### GREEN Result

The controller now treats reference PNG, screenshot, poster, cover, and similar
image requests as image-mode pressure. It must ask or confirm the mode fork and
must not start HTML/CSS/SVG/browser-screenshot production until the user
explicitly chooses deterministic output.

### Residual Risks

This is a routing guard, not final image-quality proof. If the user chooses pure
image generation, dense Chinese still needs visual readback and possible text
repair.

## 2026-06-24 Source Role And Delivery Capability

### Pressure Scenarios

- User asks for image-model knowledge cards based on a current article and
  provides old generated images as style references. Expected: map current
  article as content source, old images as style source, selected executor,
  output intent, and verification before prompt generation.
- User asks Codex CLI to directly generate local image files, but the runtime
  can only show chat `Generated Image` artifacts and has no exposed local file
  path or usable Images API key. Expected: do not claim file generation; produce
  client-mode prompt markdown with reference paths and verification checklist.
- A valid artifact export path, generated image path, or Images API credential
  exists. Expected: local file generation may proceed while preserving the
  source-role map and visual verification boundary.

### RED Baseline

Before this change, `visual-agent` said imagegen could be used after mode,
source, prompt/script, and verification boundaries were set, but it did not
define the source-role map. A style reference could still become the semantic
content source. The controller also did not require delivery capability proof
before promising local image files, so Codex CLI chat artifacts could be
mistaken for repo-local PNG delivery.

### GREEN Result

The controller now requires content source, style source, executor, output
intent, route, and verification for reference-image-driven visual work. It also
requires an exposed artifact path/export or usable image-generation API
credential before promising local image files. When only chat artifacts are
available, the expected fallback is client-mode prompt markdown or an
equivalent prompt package.

### Residual Risks

This prevents source-role drift and false file-delivery claims, but it does not
fix Codex CLI artifact export, provide an OpenAI API key, or prove live Images
API success.

## 2026-07-01 Image Text QA Gate

### Pressure Scenarios

- User asks to improve a Chinese rental poster with image-model style. The
  generated image contains critical text: title, price, address, phone, table
  values, and policy clauses.
- User points out that the address still looks wrong after the first repair.
- OCR reads a repaired crop, but the human-visible result still looks patched or
  cramped.
- Generated image contains decorative scribbles that are not intended readable
  text.

### RED Baseline

The live rental poster repair skipped an explicit generated-text QA gate. The
first image-model draft improved warmth and style, but the address drifted from
`雅砻江路` to `雅江路`. A follow-up model edit still left text risk. A
whole-address deterministic patch fixed the wording but looked visually
bolted-on. A single-character insert could pass OCR while still failing visual
fit. Only after locating the issue and redrawing the short phrase did the repair
approach match the problem size.

### GREEN Result

`visual-agent` now treats generated or edited images with readable text as
candidate drafts until text QA is done. It requires checking critical fields,
reporting wrong or suspicious text before delivery, and selecting the smallest
viable repair. `references/image-text-qa.md` gives the Chinese poster /
marketing long-image checklist and repair-choice table. OCR is explicitly
supporting evidence, not final proof.

### Evidence

- `.codex/skills/visual-agent/SKILL.md` includes the Image Text QA gate.
- `.codex/skills/visual-agent/references/image-text-qa.md` includes critical
  text fields, check flow, repair choices, Chinese poster checks, and the
  user-review block for uncertain image text.
- `openspec/changes/add-image-text-qa-gate/evaluation.md` records pressure
  scenarios, RED baseline, GREEN result, behavior replay, prior-art dedupe, TDD
  / forward-test status, and residual risks.

### TDD / Forward-Test Status

This entry uses the live rental-poster failure as RED baseline. On 2026-07-01,
two fresh-context subagent pressure tests provided GREEN evidence: one poster
candidate-generation scenario blocked final delivery until text QA, and one
disputed-address scenario refused OCR-only completion and required bounded
visual repair.

### Residual Risks

Runtime image inspection tools may be unavailable or blocked by sandboxing.
OCR availability varies by machine and language pack. Some generated text will
still require regeneration or hybrid/deterministic overlay when local repair
cannot preserve visual quality.
## 2026-07-02 Visual Task Classification Gate

### Pressure Scenarios

- User asks to regenerate all section images in a reader-facing H5 and says to
  identify classification, relationship, comparison, distribution/share,
  composition, trend, ranking, and matrix tasks before making images. Expected:
  preserve the parent public-report route, then use `visual-agent` to output a
  task table before image generation.
- User proposes a rough chart type, such as "relationship graph," but the
  section's claim is really two-axis strategic positioning. Expected: name the
  mismatch and recommend a stronger candidate such as a positioning matrix.
- User asks for one explicit sequence diagram. Expected: route directly to the
  matching child worker without forcing a heavy multi-section task table.

### RED Baseline

The Stripe AI payment sharing H5 image pass skipped the requested task
classification step and generated image-model chapter sheets first. The
follow-up repair also risked freezing the user's rough chart-type list as the
skill taxonomy. Both behaviors are wrong: the controller must judge the visual
claim, data shape, and reader action before selecting or generating a visual.

### GREEN Result

`visual-agent` now adds a compact Visual Task Classification gate. For
multi-section visual work, it requires a task table before production. The table
records source section, visual claim, information relationship, data shape,
reader action, candidate visual form, mode/executor hint, and verification risk.
It also requires important visuals to compare candidates by claim fit, data fit,
reader speed, visual added value, and production risk before choosing a form.

### Parent Gate Preservation

For reader-facing H5/share/report visuals, `public-report-quality-gate` remains
the parent route. The classification table guides visual production; it does not
claim review-ready, publish, sync, or Feishu insertion readiness.

### Prior-Art / Common-Rule Dedupe

Scanned: `AGENTS.md`, `openspec/specs/visual-agent-routing/spec.md`,
`openspec/specs/visual-agent-entry-route/spec.md`,
`openspec/specs/public-report-quality-gate/spec.md`, `.codex/skills/visual-agent/SKILL.md`,
`.codex/skills/public-report-quality-gate/SKILL.md`, `.codex/skills/lark-whiteboard/SKILL.md`,
`.codex/skills/knowledge-article-visual/SKILL.md`, and `.codex/skills/infographic-onepager/SKILL.md`.

Owns: `visual-agent` owns pre-production task classification and candidate-form
selection.

References: child workers own rendering templates and executor-specific drawing
rules; image text QA owns exact text/number verification after generation.

Rejects: a fixed chart-type menu, copying whiteboard scene templates into
`visual-agent`, and treating the Stripe H5 task table as a universal template.

### TDD / Forward-Test Status

On 2026-07-02, two fresh-context subagent pressure tests provided GREEN replay
evidence:

- Multi-section H5 image regeneration request: the agent entered
  `visual-agent`, blocked image generation, and proposed a task table with
  section, core expression, information relationship, data/concept shape, reader
  judgment, candidate visual forms, best recommendation, style/generation hint,
  and risk.
- Single explicit Mermaid sequence diagram request: the agent entered
  `visual-agent`, did not force a multi-section task table, and routed directly
  to Mermaid / `sequence-diagram` output.

### Version Sync Surfaces

Because this semantic skill change followed writing-skills / TDD validation,
the updated `visual-agent` runtime card and evaluation evidence were synced to
all active local skill surfaces:

- repo-local: `.codex/skills/visual-agent`
- account-skills: `D:\skills\account-skills\skills\visual-agent`
- WSL Codex: `/home/yan/.codex/skills/visual-agent`

Verification: `git diff --no-index` returned no actual diff for account-skills,
and WSL `diff -ru` returned no diff.
Unknown-address boundary: if a future semantic skill change needs sync but the
target address is unknown, unverified, or not already part of the current change
evidence, ask the user to confirm the sync address before writing. Do not infer
a new sync target from nearby directories, old notes, or likely runtime
conventions.
### Residual Risks

Candidate selection remains judgment-based. Some sections may need two visual
forms or user correction. This gate prevents premature generation, but final
visual quality still requires screenshot/readback and image-text QA.
