# Evaluation: visual-agent routing

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: repo workflow gate, high-frequency skill routing, public-report
  boundary, behavior-asset evaluation requirements.
- `PROJECT.md`: OpenSpec as source of truth.
- `.codex/skills/public-report-quality-gate/SKILL.md`: parent quality gate for
  reader-facing artifacts.
- `.codex/skills/wiki-medical-agent/SKILL.md`: controller response shape and
  bounded worker routing pattern.
- `/home/yan/.codex/skills/cr-agent/SKILL.md`: CR controller entry pattern and
  fixed response fields.
- `/home/yan/.codex/skills/knowledge-article-visual/SKILL.md`,
  `/home/yan/.codex/skills/infographic-onepager/SKILL.md`,
  `/home/yan/.codex/skills/svg-flow-diagram/SKILL.md`, and
  `/home/yan/.codex/skills/architecture-diagram/SKILL.md`: existing visual
  worker responsibilities.
- `openspec/specs/skill-authoring-contract/spec.md`,
  `openspec/specs/skill-evaluation-evidence/spec.md`, and
  `openspec/specs/local-skill-pressure-tests/spec.md`: behavior-asset evidence
  requirements.

Classification:

- Owns: repo-local visual entry routing, mode fork, state fields, worker
  selection boundary.
- References: public-report quality gate, visual worker skills, image model as
  executor, Feishu whiteboard routing.
- Rejects: duplicating worker prompts, editing global visual skills, making
  image generation the planner, or auto-inserting visuals into Feishu.

## Pressure Scenarios

### Scenario 1: ambiguous visual mode request

- Input or situation shape: "帮我做一个制图 agent，最后看人的偏好，或者提供的内容决定 SVG、H5、图片模型。"
- Trigger condition: user asks for visual production routing and mode selection.
- Expected route or stop behavior: `visual-agent` routes first, exposes SVG /
  H5/HTML / image-model / hybrid choices, then dispatches to a bounded worker.
- Repo-visible artifact: `.codex/skills/visual-agent/SKILL.md` and this
  OpenSpec change.
- Expected output or non-output: controller response with `Intent`,
  `Output Mode`, `Allowed Action`, and `Next Action`.
- Promotion or non-promotion boundary: route behavior is repo-local and does not
  promote to global skills.
- Proof boundary: text-level behavior proof only; runtime rendering remains a
  follow-up per selected worker.

### Scenario 2: Mermaid or fund-flow source

- Input or situation shape: user provides a `sequenceDiagram` or a payment
  clearing fund-flow outline and asks "这个画图。"
- Trigger condition: diagram-like source strongly selects deterministic
  structure.
- Expected route or stop behavior: `visual-agent` selects `svg` mode and routes
  to `svg-flow-diagram`, unless the user has explicitly chosen another mode.
- Repo-visible artifact: visual-agent routing table and spec requirement
  `Visual mode choice SHALL be explicit or evidence-based`.
- Expected output or non-output: no image-model jump before deterministic SVG
  route is stated.
- Promotion or non-promotion boundary: does not alter `svg-flow-diagram`
  internals.
- Proof boundary: route proof only; final SVG quality requires worker-specific
  verification.

### Scenario 3: architecture diagram source

- Input or situation shape: user asks for "系统架构图 / 接口架构图 / 部署拓扑图".
- Trigger condition: technical topology or integration architecture content.
- Expected route or stop behavior: `visual-agent` routes to
  `architecture-diagram` and keeps SVG/H5/image only as output-mode options.
- Repo-visible artifact: worker routing section in
  `.codex/skills/visual-agent/SKILL.md`.
- Expected output or non-output: no misclassification as generic
  `svg-flow-diagram` just because both can produce SVG.
- Promotion or non-promotion boundary: keeps architecture ownership in the
  architecture worker.
- Proof boundary: controller-level distinction only.

### Scenario 4: reader-facing H5 or article visual

- Input or situation shape: user asks to enrich an H5 report or Feishu-facing
  article with structured visuals.
- Trigger condition: reader-facing report or share artifact.
- Expected route or stop behavior: `visual-agent` preserves
  `public-report-quality-gate` before routing to `knowledge-article-visual`,
  `infographic-onepager`, or H5 worker output.
- Repo-visible artifact: `AGENTS.md` high-frequency route and visual-agent
  boundary rules.
- Expected output or non-output: no direct image generation or HTML rewrite
  before source structure, audience, and mode are established.
- Promotion or non-promotion boundary: public-report gate remains the parent.
- Proof boundary: final page quality still requires screenshot/readback checks.

### Scenario 5: direct image-model preference with Chinese text risk

- Input or situation shape: user asks for an image-model poster but provides
  dense Chinese compliance text or table labels.
- Trigger condition: explicit image preference conflicts with exact text needs.
- Expected route or stop behavior: `visual-agent` presents the tradeoff and
  offers hybrid or deterministic text overlay instead of blindly generating.
- Repo-visible artifact: mode-decision requirement and skill mode fork.
- Expected output or non-output: no unverified bitmap with critical Chinese text
  as the only source of truth.
- Promotion or non-promotion boundary: image model remains an executor.
- Proof boundary: actual image generation is outside this routing change.

### Scenario 6: non-visual material processing

- Input or situation shape: user provides a transcript and asks for text-only
  meeting notes.
- Trigger condition: no visual or drawing request.
- Expected route or stop behavior: `visual-agent` does not trigger; meeting note
  or material-processing skills own the task.
- Repo-visible artifact: AGENTS route row only triggers on visual/drawing
  requests.
- Expected output or non-output: no SVG/H5/image fork.
- Promotion or non-promotion boundary: existing meeting-note behavior remains
  unchanged.
- Proof boundary: negative trigger evidence only.

## RED Baseline

Before this change, the repo had no single visual controller. Agents could:

- answer ad hoc questions about `knowledge-article-visual` versus
  `infographic-onepager` without creating a reusable route;
- confuse `svg-flow-diagram` and `architecture-diagram` because both can emit
  SVG;
- jump directly to `imagegen` for "出图" without preserving source extraction,
  Chinese text reliability, or public-report gates;
- silently choose H5, SVG, or bitmap output without exposing the human
  preference fork.

## GREEN Result

This change adds:

- a repo-visible `visual-agent` controller;
- a four-mode decision model: `svg`, `h5_html`, `image_model`, and `hybrid`;
- bounded worker routing that preserves existing visual worker ownership;
- public-report quality gate preservation for reader-facing artifacts;
- fixed response fields modeled after `cr-agent` and `wiki-medical-agent`;
- positive and negative replay scenarios for future agents.

## Residual Risks

- This is a routing and behavior-asset change, not a proof that every downstream
  visual worker produces polished output.
- External global skills may evolve independently; the controller references
  them by responsibility rather than restating their full instructions.
- Image-model text accuracy remains a known risk and is mitigated by hybrid or
  deterministic overlay routing, not eliminated.
