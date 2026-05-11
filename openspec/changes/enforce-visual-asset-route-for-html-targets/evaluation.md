# Evaluation: visual asset route for HTML targets

## Pressure Scenarios

1. User asks: `agentic-product-engineering-collaboration-company-playbook.html要增加一图流，每个公司要增加章节知识卡`.
2. User asks: `这个 H5 加一组章节配图，别再做成 H5/SVG 卡片`.
3. User asks: `更新这个 html 的来源边界和错别字`.

## RED Baseline

Before this change:

- `public-report-quality-gate` required asking at output fork-points and
  delegated visual work, but it did not say that an `.html` target path loses to
  visual-deliverable wording.
- Existing public-report pressure scenarios covered generic H5/article visual
  requests:
  - `基于这个对外 H5 生成知识卡和一图流`
  - `这篇分享稿每家公司一张知识卡，最终一张总览图`
- No pressure scenario covered the exact ambiguous shape:
  - existing `.html` report path
  - plus `一图流` / `知识卡`
  - plus the expected non-output: do not add only in-page HTML sections.
- The live failure reproduced the missing test: the agent added HTML visual
  modules and only later recognized that image-model / hybrid visual assets
  should have been the route.

## GREEN Result

After this change:

- `public-report-quality-gate` has an explicit hard rule: reader-facing `.html`
  targets combined with `一图流`, `知识卡`, `章节配图`, `图片`, `生图`, `跑图`, or
  `图片模型` must stop direct HTML section editing and route to visual assets
  first.
- `public-report-quality-gate` pressure scenarios include the exact
  company-playbook request shape.
- The OpenSpec spec delta requires visual package scripting, output-mode
  selection or inference, and standalone visual asset production or planning
  before HTML embedding.
- Ordinary HTML text/report edits remain allowed when visual-deliverable wording
  is absent.

## Behavior Replay

| Field | Expected behavior |
|---|---|
| Input shape | User names an existing `.html` report and asks to add `一图流`, `知识卡`, or chapter visuals. |
| Trigger condition | Reader-facing HTML target plus visual-deliverable wording, especially after H5/SVG-like output has been rejected. |
| Expected route / stop | Stop before direct HTML body edits; route to visual package script, output-mode selection/inference, and standalone visual asset production or planning. |
| Repo-visible artifact | This OpenSpec change, updated `public-report-quality-gate` hard rule, updated pressure scenarios, and the prior explore trace. |
| Expected output / non-output | Output visual script / asset plan / image-model or hybrid route first; do not output only new H5 sections and call the task complete. |
| Promotion boundary | This does not force image generation for ordinary HTML report edits or for explicitly requested in-page H5 modules. |
| Residual risk / proof boundary | Local pressure text proves the route decision. It does not prove generated image quality, prompt quality, or multi-session automatic dispatch reliability. |

## Residual Risks

- Runtime routing remains model-mediated; the rule is explicit but not a
  mechanical dispatcher.
- Global visual skills may still need a follow-up if they independently weaken
  this public-report route.
- This change does not generate the company-playbook visual assets.
