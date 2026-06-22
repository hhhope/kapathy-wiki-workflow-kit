# visual-agent evaluation

## Pressure Scenarios

- Ambiguous request: "制图 agent，帮我决定 SVG、H5、图片模型。" Expected:
  response includes `Using visual-agent`, uses `mode_fork`, and presents the
  four output modes.
- Plain visual request: "帮我制图 / 出图 / 配图" without explicit mode. Expected:
  no silent H5/SVG default; ask the bounded mode fork unless strong content
  evidence selects a mode.
- Colloquial visual request: "弄个图", "画一下", "整张图", "做成卡片",
  "配几张图", or "图像化一下". Expected: trigger `visual-agent`, expose
  `Using visual-agent`, and ask the mode fork unless strong content evidence
  selects a route.
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
marker. Before compacting the runtime card, `visual-agent/SKILL.md` was 917
words and mixed route rules with governance-style explanation. Trigger wording
also leaned on fixed examples instead of the broader colloquial visual request
class.

## GREEN Result

The skill now defines a compact runtime controller: `Using visual-agent`, mode
fork, no silent H5/SVG fallback, child worker routes, public-report gate
preservation, and verification/Feishu stops. The trigger model covers formal
and colloquial visual-deliverable requests as a class, with examples treated as
non-exhaustive.

## Residual Risks

This skill proves routing behavior only. Final SVG, H5, or bitmap quality still
depends on the selected worker and visual verification.
