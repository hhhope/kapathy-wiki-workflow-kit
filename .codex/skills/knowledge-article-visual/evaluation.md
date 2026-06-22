# Evaluation: knowledge-article-visual routing repair

## Pressure Scenarios

1. User asks for a report to become standalone visual assets, a knowledge-card
   series, or a one-page infographic.
2. User asks why image generation was not used after a H5 edit.
3. A section contains dense Chinese text and must become a final visual asset.

## RED Baseline

Observed before this change:

- The skill had no explicit intent routing table.
- The agent could stop at H5 visual blocks after the user asked for images.
- The skill did not require loading `infographic-onepager` for per-image format
  decisions.
- The one-page infographic template was hardcoded to a Skill/SOP flow:
  `先跑通目标 -> 复盘过程 -> 封装 Skill -> 回溯测试 -> 持续迭代`.

## GREEN Result

Expected after this change:

- Visual-asset requests must produce visual artifacts or prompts, not only H5
  sections.
- The skill must route each chapter to `infographic-onepager` for horizontal
  card vs vertical one-page infographic decisions.
- Dense Chinese or formal output must surface the mode tradeoff instead of silently
  changing from image-model output to deterministic SVG/HTML.
- The total infographic template is generic and topic-filled, not Skill-specific.

## Residual Risks

- Actual image-model output quality still depends on the available generator.
- Dense Chinese remains a risk note that should trigger confirmation or hybrid
  handling, not an automatic deterministic fallback.

## 2026-05-11 Output Mode Fork Repair

### Pressure Scenario

User rejects the deterministic H5/SVG route and asks to choose the visual output
mode.

### RED Baseline

- The old intent routing allowed image-model requests to fall back to
  deterministic SVG/HTML when dense Chinese text was present.
- The old dense-Chinese rule said to use deterministic SVG/HTML first, which
  overrode user-owned visual mode selection.
- The old skill had no required four-mode fork covering H5/HTML, SVG/HTML,
  direct image model, and hybrid output.

### GREEN Result

- Visual output mode is now user-owned.
- Unclear visual requests require the four-mode fork before implementation.
- Explicit image-model selection, image-generation confirmation, or rejection
  of H5/SVG routes to direct image generation or hybrid mode.
- Dense Chinese is only a risk note unless the user chooses deterministic output
  or an external exact-text constraint requires it.

### Behavior Replay

| Field | Evidence |
|---|---|
| Input shape | User asks for visual assets, selects image-model output, or rejects H5/SVG output quality. |
| Trigger condition | The same visual could be produced as H5/HTML, SVG/HTML, image model, or hybrid. |
| Expected route | Ask the four-mode fork; if image model was already selected, use direct image generation or hybrid. |
| Expected non-output | Do not silently produce H5/SVG screenshots and call them image-model output. |
| Proof boundary | This is skill-level behavior evidence; actual image quality still requires generator output QA. |

### Residual Risks

- Future agents may still need to state the tradeoff clearly when exact Chinese
  text conflicts with pure image-model output.
- Hybrid output can still look layout-like if the deterministic text overlay is
  designed poorly.

## 2026-05-11 Residual Fallback Tightening

### Pressure Scenario

User asks for direct image-model output, then the generated Chinese text looks
wrong. The agent must not silently relabel the work as deterministic SVG/HTML.

### RED Baseline

- Prompt handoff still allowed stopping when image generation was "unsafe for
  text accuracy".
- The quality checklist still said to switch to deterministic or hybrid mode
  when image generation distorted Chinese, without requiring a visible report or
  confirmation.
- Earlier evaluation wording still implied dense Chinese should use
  deterministic SVG/HTML or hybrid instead of making the mode decision visible.

### GREEN Result

- Direct image requests no longer stop at prompts because of text-accuracy risk.
- Text-accuracy risk must be reported before changing modes.
- Broken Chinese now prefers hybrid mode unless the user explicitly chose
  deterministic-only output.
- Dense Chinese remains a risk note that should trigger confirmation or hybrid
  handling, not an automatic deterministic fallback.

### Behavior Replay

| Field | Evidence |
|---|---|
| Input shape | User asks for image-model visuals, or asks why H5/SVG was used. |
| Trigger condition | Image model output is requested but Chinese text may distort. |
| Expected route | Report the text risk, prefer hybrid, and only use deterministic-only output when the user chooses it or an external constraint requires it. |
| Expected non-output | Do not silently stop at prompts or switch to SVG/HTML because text accuracy is risky. |
| Proof boundary | This verifies skill routing language; final visual quality still needs asset QA. |

### Residual Risks

- The agent still needs to explain hybrid clearly so it is not mistaken for pure
  image-model output.
- Pure image generation may remain unsuitable for final dense Chinese copy.
