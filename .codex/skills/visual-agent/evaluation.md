# visual-agent evaluation

## Pressure Scenarios

- Ambiguous request: "制图 agent，帮我决定 SVG、H5、图片模型。" Expected:
  `visual-agent` triggers, uses `mode_fork`, and presents the four output modes.
- Flow source: Mermaid sequence, payment clearing flow, or fund flow. Expected:
  route to `svg-flow-diagram` with `Output Mode: svg` unless the user overrides.
- Architecture source: system architecture, interface topology, or deployment
  diagram. Expected: route to `architecture-diagram`, not generic flow SVG.
- Reader-facing H5/report source. Expected: preserve
  `public-report-quality-gate` before visual worker execution.
- Dense Chinese text plus image-model preference. Expected: warn about text
  accuracy and offer `hybrid` or deterministic overlay.
- Non-visual meeting notes request. Expected: visual-agent does not trigger.

## RED Baseline

Before this skill, visual routing depended on ad hoc model judgment. A request
could jump directly to image generation, confuse SVG workers, or skip the human
mode fork.

## GREEN Result

The skill now defines a single controller, fixed response fields, mode routing,
bounded worker mapping, public-report gate preservation, and explicit
boundaries for image-model execution.

## Residual Risks

This skill proves routing behavior only. Final SVG, H5, or bitmap quality still
depends on the selected worker and visual verification.
