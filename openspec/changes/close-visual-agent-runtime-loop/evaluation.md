# Evaluation: visual-agent runtime loop closure

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: workflow change gate, semantic skill edit gates, high-frequency
  visual routing, behavior replay gate.
- `PROJECT.md`: OpenSpec source of truth.
- Existing visual-agent changes:
  `add-visual-agent-routing`, `harden-visual-agent-entry-route`, and
  `compress-visual-agent-colloquial-route`.
- Existing specs: `skill-authoring-contract`, `skill-evaluation-evidence`,
  `local-skill-pressure-tests`, `repo-skill-namespace-surface`, and
  `visual-agent-entry-route` deltas from earlier changes.
- `wiki/ops/visual-agent-skill-drift-explore-2026-06-22.md`: live drift trace.

Classification:

- Owns: repo-local runtime skill surface under `.codex/skills/` and
  repo-visible evidence that the controller's child routes are discoverable.
- References: account-skills as upstream package source, public-report parent
  gate, imagegen runtime/system tool, writing-skills/TDD gates.
- Rejects: editing account-skills during the repo-local phase, treating
  account-skills branch state as proof of this repo's runtime state, or using
  fixed colloquial phrase lists as the trigger mechanism.

## Pressure Scenarios

### Positive Scenario 1: repo runtime discovers visual workers

- Input or situation shape: this repo is loaded with `.codex/skills` as the
  runtime skill surface.
- Trigger condition: user asks for a visual artifact that `visual-agent` routes
  to a child worker.
- Expected route or stop behavior: the child worker named by `visual-agent` is
  discoverable under `.codex/skills/<worker>/SKILL.md`.
- Repo-visible artifact: `.codex/skills/*/SKILL.md`.
- Expected output or non-output: no false claim that a missing worker is
  bundled.
- Promotion or non-promotion boundary: this promotes repo-local runtime
  discovery only; it does not promote account-skills package cleanup as done.
- Proof boundary: discovery proof only, not final visual quality proof.

### Positive Scenario 2: ambiguous visual request

- Input or situation shape: user asks for a visual deliverable without choosing
  SVG, H5/HTML, image-model, or hybrid.
- Trigger condition: visual deliverable intent is present.
- Expected route or stop behavior: `visual-agent` exposes the mode fork or
  states strong content evidence before selecting a mode.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no silent H5/SVG default.
- Promotion or non-promotion boundary: promotes the controller route only, not
  any generated asset quality claim.
- Proof boundary: text-level route proof only.

### Negative Scenario 3: account-skills branch differs from repo runtime

- Input or situation shape: account-skills contains a newer visual-agent package
  than this repository's installed `.codex/skills` surface.
- Trigger condition: user expects current repo behavior to match the package
  branch.
- Expected route or stop behavior: repo-local repair must update this
  repository's runtime copy before claiming the behavior is fixed here.
- Repo-visible artifact: this change and the drift trace.
- Expected output or non-output: no completion claim based only on a pushed
  account-skills branch.
- Promotion or non-promotion boundary: account-skills branch work remains a
  follow-up phase until that repository's package-level cleanup is completed.
- Proof boundary: local runtime proof only; account-skills package cleanup is a
  follow-up phase.

### Negative Scenario 4: non-visual request should-not-trigger visual-agent

- Input or situation shape: user asks for prose-only meeting notes or a
  non-visual wiki update.
- Trigger condition: no visual deliverable, visual transformation, visual mode
  decision, or visual repair is requested.
- Expected route or stop behavior: `visual-agent` should-not-trigger; the
  applicable meeting-note, wiki, or public-report route owns the work.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no visual mode fork and no child visual worker
  route.
- Promotion or non-promotion boundary: does not make visual-agent a universal
  router for all casual requests.
- Proof boundary: negative route proof only.

### Parent Gate Preservation Scenario

- Input or situation shape: user asks for a reader-facing report, H5/share
  draft, or Feishu-facing visual.
- Trigger condition: public-report output and visual deliverable intent are both
  present.
- Expected route or stop behavior: preserve the `public-report-quality-gate` as
  the parent gate, then route visual production through `visual-agent` to the
  selected child worker.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md` and
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Expected output or non-output: no direct child-worker route that bypasses the
  parent gate.
- Promotion or non-promotion boundary: parent gate preservation is repo-local;
  it does not claim external runtimes will enforce the same chain.
- Proof boundary: route proof only; final reader-facing quality still needs the
  public-report quality checks.

## RED Baseline

Before this change:

- `find .codex/skills -maxdepth 2 -name SKILL.md | rg 'visual|infographic|knowledge|architecture|frontend|project-weekly|lark|sequence|svg'`
  returned only `.codex/skills/visual-agent/SKILL.md`.
- `.codex/skills/visual-agent/SKILL.md` still said the repository bundled only
  `svg-flow-diagram` and treated other visual workers as companion runtime
  skills.
- The account-skills branch had newer bundled-worker wording than this repo's
  installed runtime copy.

## GREEN Result

After the repo-local patch:

- `find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'visual|infographic|knowledge|architecture|frontend|project-weekly|lark|sequence|svg'`
  returns:
  - `.codex/skills/architecture-diagram/SKILL.md`
  - `.codex/skills/frontend-visual-governor/SKILL.md`
  - `.codex/skills/infographic-onepager/SKILL.md`
  - `.codex/skills/knowledge-article-visual/SKILL.md`
  - `.codex/skills/lark-whiteboard/SKILL.md`
  - `.codex/skills/project-weekly-report-gantt-map/SKILL.md`
  - `.codex/skills/sequence-diagram/SKILL.md`
  - `.codex/skills/svg-flow-diagram/SKILL.md`
  - `.codex/skills/visual-agent/SKILL.md`
  - `.codex/skills/visual-knowledge-onepager/SKILL.md`
- `.codex/skills/visual-agent/SKILL.md` now describes bundled visual workers,
  runtime/system `imagegen`, and host-gate `public-report-quality-gate`
  accurately.
- The fixed-trigger scan over the repo-local visual runtime surface no longer
  finds route-controlling fixed colloquial trigger rows or the old
  `xiaohongshu-retro-grid-content` name.
- The only scan hits are in `.codex/skills/lark-whiteboard/references/style.md`
  where the wording describes visual styling examples, not routing triggers.
- The drift trace records the local repair and account-skills follow-up
  boundary.

## Residual Risks

- This closes the repo-local runtime surface only. The account-skills branch
  still needs package-level README / integration-kit cleanup after this repo
  phase is committed.
- Child worker descriptions are still discoverable by the runtime. The
  controller relies on `visual-agent` routing plus worker body reminders rather
  than a hard runtime mechanism that prevents direct child-skill discovery.
- Final visual quality still requires screenshot/readback or equivalent visual
  verification during actual production work.

## Verification Results

- Runtime discovery check: passed; all visual worker `SKILL.md` files are
  discoverable under `.codex/skills`.
- Fixed-trigger / old-name scan: passed for route-controlling text. Remaining
  hits are style-reference wording in `lark-whiteboard/references/style.md`,
  not route rules.
- `git diff --check -- .codex/skills openspec/changes/close-visual-agent-runtime-loop wiki/ops/visual-agent-skill-drift-explore-2026-06-22.md`:
  passed.
- `openspec validate close-visual-agent-runtime-loop --strict`: passed. The CLI
  still emitted PostHog network flush warnings for `edge.openspec.dev`; the
  local validation result was valid.
- `python3 scripts/check_behavior_assets.py`: returned non-zero only for the
  pre-existing `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
  gaps. It did not report this change after evaluation markers were added.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target
  wiki/ops/visual-agent-skill-drift-explore-2026-06-22.md`: returned non-zero
  because of existing whole-repo `wiki/reports` frontmatter blockers and
  `target.entry_count=0` for this new trace. The trace retains this proof
  boundary instead of claiming taxonomy completion.
