# Evaluation: infographic-onepager generic-template repair

## Pressure Scenarios

1. User provides a non-Account-Wiki topic and asks for a one-page infographic.
2. User asks for a chapter card from a larger knowledge article.
3. User asks for images but the content has dense Chinese text.

## RED Baseline

Observed before this change:

- `Account Wiki` had a full hardcoded poster skeleton in the main skill body.
- The input recognition table routed `Account Wiki` to that skeleton by default.
- The skill did not explicitly describe how it should be called by
  `knowledge-article-visual`.

## GREEN Result

Expected after this change:

- The default skeleton is generic and topic-filled.
- Account Wiki is only an example topic, never the default.
- `knowledge-article-visual` can call this skill for total infographics,
  chapter one-pagers, and horizontal teaching cards.
- Requested images cannot silently become H5 without an exported PNG/SVG or a
  stated deterministic-text reason.

## Residual Risks

- Existing users who relied on the Account Wiki hardcoded example now need to
  provide or reference the Account Wiki source content explicitly.

## 2026-05-11 Output Mode Fork Repair

### Pressure Scenario

User rejects the deterministic H5 route and asks to choose the visual output
mode.

### RED Baseline

- The old format decision table routed formal, dense, exact, or Feishu-facing
  Chinese to SVG/HTML first.
- The old direct-image row allowed dense Chinese to make deterministic layout
  safer, which gave the agent a silent fallback from image model to SVG/HTML.
- The old skill only protected an unclear image-model vs H5/HTML fork, not the
  full H5/HTML, SVG/HTML, direct image model, and hybrid decision.

### GREEN Result

- Poster-script compression remains required, but output mode is user-owned.
- Unclear routes require the four-mode fork before file generation.
- Explicit image-model language or rejection of H5/SVG routes to direct image
  generation or hybrid mode.
- PNGs exported from HTML/SVG must be labeled deterministic rendering, not
  image-model output.

### Behavior Replay

| Field | Evidence |
|---|---|
| Input shape | Chinese infographic request where H5/HTML, SVG/HTML, image model, or hybrid could all satisfy part of the request. |
| Trigger condition | User has not chosen a mode, or user explicitly asks for image model / rejects H5/SVG. |
| Expected route | Ask the four-mode fork when unclear; otherwise honor image-model or hybrid selection. |
| Expected non-output | Do not switch to SVG/HTML solely because the text is dense. |
| Proof boundary | This verifies routing language, not the visual quality of any generated asset. |

### Residual Risks

- Direct image generation may still distort Chinese text; final assets need QA
  and possibly a hybrid overlay.
- Deterministic overlays can still fail visual style if treated as ordinary H5
  layout instead of image finishing.

## 2026-05-11 Residual Fallback Tightening

### Pressure Scenario

User asks for a Chinese infographic via image model, while the content also has
dense exact Chinese. The skill must not treat density as an automatic SVG/HTML
route.

### RED Baseline

- The SVG/HTML pattern still said to use SVG/HTML when dense exact Chinese text
  was needed, which could bypass the output-mode fork.
- The direct image route was fixed, but the deterministic route still had one
  ambiguous entrance.

### GREEN Result

- SVG/HTML is now for user-chosen deterministic rendering, explicitly confirmed
  deterministic handling for dense exact Chinese, or editable output.
- Dense exact Chinese is now a constraint to confirm, not an automatic SVG/HTML route.
- User rejection of H5/SVG continues to route to direct image generation or
  hybrid unless the user explicitly chooses H5/SVG again.

### Behavior Replay

| Field | Evidence |
|---|---|
| Input shape | User requests image-model or hybrid infographic output with dense Chinese text. |
| Trigger condition | Dense exact Chinese creates text-accuracy risk. |
| Expected route | Present or honor the output-mode choice; use SVG/HTML only after deterministic handling is chosen or confirmed. |
| Expected non-output | Do not auto-route to SVG/HTML solely because dense exact Chinese is present. |
| Proof boundary | This verifies routing text, not generated-image typography quality. |

### Residual Risks

- Hybrid execution still needs visual QA so deterministic text overlays do not
  look like ordinary slide layouts.
- Direct image generation can still require a follow-up correction pass.
