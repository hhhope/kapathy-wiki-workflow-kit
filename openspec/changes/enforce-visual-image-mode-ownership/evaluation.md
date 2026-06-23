# Evaluation: visual image mode ownership

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: workflow change gate, semantic skill edit gates, behavior replay
  gate, and visual-agent high-frequency route.
- `PROJECT.md`: OpenSpec source of truth.
- `.codex/skills/visual-agent/SKILL.md`: current controller mode rules.
- `.codex/skills/visual-agent/evaluation.md`: existing pressure scenarios.
- `openspec/specs/visual-agent-entry-route/spec.md`: stable route contract.
- `openspec/specs/skill-authoring-contract/spec.md`,
  `skill-evaluation-evidence`, `local-skill-pressure-tests`, and
  `behavior-replay-gate`.
- `~/.codex/skills/writing-skills/SKILL.md` and prerequisite
  `~/.codex/skills/test-driven-development/SKILL.md`.

Classification:

- Owns: visual-agent controller behavior for image-reference / similar-image
  mode ownership.
- References: public-report parent gate, child visual workers, imagegen runtime
  executor, and deterministic rendering tools.
- Rejects: using Chinese text accuracy, local renderer convenience, or existing
  H5 source material as permission to silently choose HTML/CSS screenshots.

Routing ownership:

- `visual-agent` is a high-level router/gate for visual mode selection.
- This change owns the mode-selection boundary only; child workers remain
  execution modules after mode confirmation.

## Pressure Scenarios

### Positive Scenario: reference PNG plus H5 source

- Input or situation shape: user says `stripe-ai-company-evolution-h5.html`
  should become an image similar to a local PNG reference.
- Trigger condition: visual artifact requested, image-like reference provided,
  no explicit mode chosen.
- Expected route or stop behavior: `visual-agent` exposes the route and asks or
  confirms the four-mode fork before file generation.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md` and this
  OpenSpec change.
- Expected output or non-output: no HTML/CSS/SVG/browser-screenshot production
  starts before user mode confirmation.
- Promotion or non-promotion boundary: this is route behavior proof, not proof
  of final image quality.
- Proof boundary: local text replay only; multi-session rollout is not proven.

### Negative Scenario: deterministic route chosen explicitly

- Input or situation shape: after the mode fork, user says to use deterministic
  HTML/CSS screenshot output.
- Trigger condition: explicit deterministic mode choice exists.
- Expected route or stop behavior: deterministic rendering may proceed and must
  be labeled as deterministic, not image-model output.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no false claim that an HTML screenshot is
  image-model generation.
- Promotion or non-promotion boundary: does not forbid deterministic rendering
  when the user chooses it.
- Proof boundary: mode ownership only.

### Negative Scenario: text accuracy rationalization

- Input or situation shape: dense Chinese text makes image-model output risky.
- Trigger condition: requested output is still image-like and mode is not chosen.
- Expected route or stop behavior: the agent states text accuracy as a tradeoff
  and asks the mode fork; it does not convert to HTML/SVG/screenshots.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no file edits and no renderer setup before the
  mode decision.
- Promotion or non-promotion boundary: text accuracy remains a real risk note,
  not a route override.
- Proof boundary: pressure replay only.

## RED Baseline

The live failure happened with this request shape:

> `stripe-ai-company-evolution-h5.html 基于这个 做一个 ...png 类似得图片 $report-wiki-portfolio:visual-agent`

The agent read the reference PNG, then stated:

> `我会用 HTML/CSS 做同风格海报并截图成 PNG。`

That was wrong because the user had not chosen deterministic rendering. The
rationalization was: Chinese accuracy matters, so deterministic HTML/CSS is
safer. Existing `visual-agent` wording had a general no-silent-H5/SVG rule, but
it did not explicitly classify PNG/image-reference requests as image-mode
pressure.

## GREEN Result

After this change:

- `.codex/skills/visual-agent/SKILL.md` explicitly says reference PNG /
  screenshot / poster / cover / image-like requests are image-mode pressure.
- It blocks HTML/CSS/SVG/browser screenshot work until the user chooses that
  deterministic route.
- The spec includes a replayable scenario for the exact H5 + PNG reference
  failure shape.

## Residual Risks

- This is behavior guidance, not a hard runtime type system. Future agents still
  must load and follow `visual-agent`.
- The rule does not choose image-model automatically; it preserves the user's
  mode decision and treats image-model/hybrid as route pressure.
- Final image quality still requires actual visual verification after the user
  chooses a production mode.
