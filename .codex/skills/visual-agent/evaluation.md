# visual-agent evaluation

## Pressure Scenarios

- Ambiguous request: "制图 agent，帮我决定 SVG、H5、图片模型。" Expected:
  response includes `Using visual-agent`, uses `mode_fork`, and presents the
  four output modes.
- Plain visual request: "帮我制图 / 出图 / 配图" without explicit mode. Expected:
  no silent H5/SVG default; ask the bounded mode fork unless strong content
  evidence selects a mode.
- Flow source: Mermaid sequence, payment clearing flow, or fund flow. Expected:
  route to `svg-flow-diagram` with `Output Mode: svg` unless the user overrides.
- Architecture source: system architecture, interface topology, or deployment
  diagram. Expected: route to `architecture-diagram`, not generic flow SVG.
- Reader-facing H5/report source. Expected: preserve
  `public-report-quality-gate` and route visual production through
  `visual-agent` before visual worker execution.
- Dense Chinese text plus image-model preference. Expected: warn about text
  accuracy and offer `hybrid` or deterministic overlay.
- Directly named worker: user asks for `infographic-onepager`,
  `svg-flow-diagram`, or `imagegen`. Expected: still enter through
  `visual-agent` first unless the task is worker debug review.
- Non-visual meeting notes request. Expected: visual-agent does not trigger.

## RED Baseline

Before this skill, visual routing depended on ad hoc model judgment. A request
could jump directly to image generation, confuse SVG workers, or skip the human
mode fork. Before the entry-route hardening, public-report delegation also
listed `knowledge-article-visual`, `infographic-onepager`, and `imagegen`
directly, and normal visual responses had no required `Using visual-agent`
marker.

## GREEN Result

The skill now defines a single controller, fixed response fields, mode routing,
bounded worker mapping, public-report gate preservation, and explicit
boundaries for image-model execution. The hardening adds an observable
`Using visual-agent` entry marker, treats named visual workers as child routes,
and blocks ambiguous H5/SVG defaulting without a mode fork or strong content
evidence.

## Residual Risks

This skill proves routing behavior only. Final SVG, H5, or bitmap quality still
depends on the selected worker and visual verification.
