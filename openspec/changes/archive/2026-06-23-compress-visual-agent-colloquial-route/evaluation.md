# Evaluation: compact colloquial visual-agent route

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: high-frequency visual route row.
- `PROJECT.md`: OpenSpec source-of-truth model.
- `.codex/skills/visual-agent/SKILL.md`: current runtime skill body.
- `.codex/skills/visual-agent/evaluation.md`: current pressure scenarios.
- `.codex/skills/public-report-quality-gate/SKILL.md` and
  `references/pressure-scenarios.md`: reader-facing visual route wording.
- `openspec/changes/harden-visual-agent-entry-route/*`: previous bypass
  hardening.
- `/home/yan/.codex/skills/writing-skills/SKILL.md` and
  `/home/yan/.codex/skills/test-driven-development/SKILL.md`: skill TDD and
  compact body rules.
- `/home/yan/.codex/rules/common/development-workflow.md`: semantic
  behavior-asset evaluation gate.

Classification:

- Owns: repo-local runtime compactness for `visual-agent` and generalized
  colloquial visual trigger wording.
- References: public-report parent gate, visual child workers, behavior-asset
  evidence rules.
- Rejects: adding another visual agent, copying replay history into the runtime
  skill, or relying only on fixed Chinese trigger words.

## Pressure Scenarios

### Scenario 1: compact runtime skill

- Input or situation shape: a routine request loads `visual-agent`.
- Trigger condition: the skill body is read at runtime.
- Expected route or stop behavior: the body is short enough to scan and places
  mode fork / no silent H5-SVG / child routes before detail.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no governance-history wall in the runtime
  skill body.
- Promotion or non-promotion boundary: detailed proof stays in evaluation and
  OpenSpec, not in `SKILL.md`.
- Proof boundary: word-count and scoped text checks, not agent-subagent runtime
  automation.

### Scenario 2: positive trigger - casual visual wording

- Input or situation shape: user says "帮我弄个图", "这段画一下", "整张图",
  "做成卡片", "给这个配几张图", or "图像化一下".
- Trigger condition: the user asks for a visual deliverable without explicit
  mode.
- Expected route or stop behavior: `visual-agent` triggers, exposes
  `Using visual-agent`, and asks the mode fork unless content strongly selects a
  route.
- Repo-visible artifact: `AGENTS.md` and `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no default H5/SVG output.
- Promotion or non-promotion boundary: examples remain non-exhaustive.
- Proof boundary: route proof only.

### Scenario 3: positive trigger - reader-facing H5 casual visual request

- Input or situation shape: user says "这个 H5 再弄几张图" or "这篇分享稿做得更
  图像化一点".
- Trigger condition: reader-facing artifact plus colloquial visual request.
- Expected route or stop behavior: public-report gate remains outer gate and
  visual production routes through `visual-agent`.
- Repo-visible artifact:
  `.codex/skills/public-report-quality-gate/SKILL.md` and pressure scenarios.
- Expected output or non-output: no HTML-only section edit that substitutes for
  visual deliverables.
- Promotion or non-promotion boundary: does not bypass publish/review gates.
- Proof boundary: route proof only.

### Scenario 4: negative should-not-trigger - non-visual colloquial request

- Input or situation shape: user says "帮我整理一下这段话".
- Trigger condition: casual language is present, but no visual deliverable is
  requested.
- Expected route or stop behavior: `visual-agent` does not trigger only because
  the wording is colloquial.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no unnecessary mode fork.
- Promotion or non-promotion boundary: visual-agent stays visual-specific.
- Proof boundary: negative trigger evidence only.

## RED Baseline

Baseline checks against the pre-change wording:

- `wc -w .codex/skills/visual-agent/SKILL.md` returned `917`, which is too large
  for a frequently loaded runtime controller.
- The skill body included separate `Intent Classes`, detailed mode explanation,
  worker routing, hard boundaries, and evidence notes in the runtime file.
- `AGENTS.md` and the skill description listed fixed examples such as 制图, 出图,
  配图, and 一图流, but did not name the broader colloquial request class.
- `public-report-quality-gate` pressure scenarios covered specific visual words,
  but not the generalized casual class such as "弄个图" or "图像化一下".

Observed loophole:

- A future agent could satisfy the literal listed examples while still missing
  new casual visual wording.
- The correct route was present, but the runtime body was thick enough to hide
  the user-facing mode-fork rule.

## GREEN Result

After the patch:

- `visual-agent/SKILL.md` is compressed into a short runtime card.
- `AGENTS.md`, `visual-agent`, and public-report visual wording refer to
  colloquial visual request classes, not only fixed examples.
- The compact card keeps `Using visual-agent`, mode fork, no silent H5/SVG, and
  child routes visible without governance history.
- Evaluation scenarios include compactness and casual visual wording.

GREEN checks:

- `wc -w .codex/skills/visual-agent/SKILL.md` returned `410`, down from the RED
  baseline of `917`.
- `rg -n 'formal or casual|casual wording|colloquial|弄个图|画一下|整张图|做成卡片|配几张图|图像化一下|not a closed list|fixed phrase list|917|Using visual-agent|H5/SVG' ...`
  found generalized trigger wording, casual examples, non-exhaustive wording,
  the baseline word count record, and the retained no-H5/SVG guard.
- `rg -n 'Intent Classes|Evidence Notes|controller pattern|do not become the renderer|If no preference is given|Route to the smallest bounded worker|Hard Boundaries' .codex/skills/visual-agent/SKILL.md`
  returned no matches, confirming the old thick runtime sections were removed.
- `openspec validate compress-visual-agent-colloquial-route --strict` reported
  `Change 'compress-visual-agent-colloquial-route' is valid`. The CLI then
  emitted PostHog network flush warnings because the environment cannot resolve
  `edge.openspec.dev`; the validation result itself was local and valid.
- `git diff --check` passed for the scoped files.
- `python3 scripts/check_behavior_assets.py` returned non-zero only for the
  pre-existing `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
  gaps. It did not report this change after the positive/negative scenario
  markers were added.

## Residual Risks

- This change proves repo-local routing text and compactness. It does not prove
  every future client loads repo context correctly.
- It does not change global worker skills or visual rendering quality.
