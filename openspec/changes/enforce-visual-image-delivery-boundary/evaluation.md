# Evaluation: visual image delivery boundary

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: workflow change gate, semantic skill edit gates, behavior replay
  gate, behavior asset prior-art gate, and visual-agent high-frequency route.
- `PROJECT.md`: OpenSpec source of truth and repository purpose.
- `wiki/index.md`: ops and ADR entry paths.
- `wiki/adr/0035-visual-reference-style-source-not-content-source.md`: source
  role boundary for reference images.
- `wiki/ops/imagegen-artifact-filesystem-bridge-explore-2026-06-24.md`: Codex
  CLI artifact/file/API-key boundary.
- `.codex/skills/visual-agent/SKILL.md`: current controller mode rules.
- `.codex/skills/visual-agent/evaluation.md`: existing pressure scenarios.
- `openspec/specs/visual-agent-entry-route/spec.md`: stable route contract.
- `openspec/specs/skill-authoring-contract/spec.md`,
  `skill-evaluation-evidence`, `local-skill-pressure-tests`, and
  `behavior-replay-gate`.
- `~/.codex/skills/writing-skills/SKILL.md` and prerequisite
  `~/.codex/skills/test-driven-development/SKILL.md`.

Classification:

- Owns: visual-agent controller behavior for reference-image source roles and
  image-model delivery capability claims.
- References: imagegen runtime executor, OpenAI Images API credential boundary,
  public-report parent gate, and deterministic rendering workers.
- Rejects: brittle forbidden-noun prompt lists as the primary fix, treating
  Codex login tokens as API credentials without scope proof, and claiming local
  image files from chat-only artifacts.

Routing ownership:

- `visual-agent` is a high-level router/gate for visual source, mode, executor,
  and delivery capability decisions.
- Child workers and runtime image tools remain executors after the controller
  boundary is satisfied.

## Pressure Scenarios

### Scenario: reference image source-role drift

- Input or situation shape: user asks for three image-model knowledge cards
  based on a current article and provides old hand-drawn images as references.
- Trigger condition: visual request plus prior image reference.
- Expected route or stop behavior: `visual-agent` maps current article as
  content source, old images as style source, selected executor, output intent,
  and verification before prompt generation.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`,
  `wiki/adr/0035-visual-reference-style-source-not-content-source.md`, and this
  OpenSpec change.
- Expected output or non-output: prompt/script does not reuse old reference
  topics as new content unless the user explicitly asks for that.
- Promotion boundary: targeted negative prompts are repair tools only after
  observed generation drift.
- Proof boundary: text replay proves route behavior, not final image quality.

### Scenario: Codex CLI image artifact has no local file

- Input or situation shape: user says "directly generate files" for image-model
  output in Codex CLI.
- Trigger condition: local file delivery requested but the current runtime only
  exposes a chat `Generated Image` artifact; no artifact export path or usable
  Images API key is available.
- Expected route or stop behavior: the agent does not claim local file
  generation and instead writes client-mode prompt markdown.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`,
  `wiki/ops/imagegen-artifact-filesystem-bridge-explore-2026-06-24.md`, and
  this OpenSpec change.
- Expected output or non-output: no "generated PNG file" claim; prompt md
  includes reference paths, source-role map, prompt, and verification checklist.
- Promotion boundary: this does not declare a Codex CLI bug root cause or API
  implementation fix.
- Proof boundary: local credential/artifact evidence is runtime-specific.

### Scenario: valid delivery capability exists

- Input or situation shape: selected mode is image-model and a valid local
  artifact export path or Images API credential is available.
- Trigger condition: file delivery capability is verified.
- Expected route or stop behavior: local image generation may proceed while
  preserving source-role and visual verification boundaries.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: local file claim is allowed only after delivery
  capability is verified.
- Promotion boundary: valid credentials do not remove public-report, Feishu, or
  visual verification gates.
- Proof boundary: this change does not test a live successful Images API call.

## RED Baseline

Before this change, `visual-agent` already treated reference PNGs as image-mode
pressure and blocked silent HTML/SVG fallback. It did not require a source-role
map for reference-image-driven work, so a style reference could still become a
semantic content source. It also said imagegen could be used after mode/source
prompt/script boundaries were set, but it did not require delivery capability
verification before promising repo-local image files.

The live failures were:

- a historical Account Wiki visual reference influenced the generated content
  topic instead of only the style grammar;
- Codex CLI displayed `Generated Image` artifacts but no repo-local PNG was
  available, while the local fallback path lacked a usable Images API key.

## GREEN Result

After this change:

- `visual-agent` requires content source, style source, executor, output intent,
  and verification for reference-image-driven visual work.
- `visual-agent` requires delivery capability before promising local image
  files.
- When only chat artifacts are available and API fallback is blocked, the
  expected deliverable is client-mode prompt markdown rather than a false local
  file claim.

## Residual Risks

- This is behavior guidance, not a hard runtime type system. Future agents still
  must load and follow `visual-agent`.
- The current Codex CLI artifact bridge remains unresolved; this change only
  prevents false delivery claims.
- It does not prove live OpenAI Images API success.
- Final image quality still requires visual inspection after generation.
