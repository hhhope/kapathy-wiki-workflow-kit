# Evaluation: public output skill routing boundaries

## Pressure Scenarios

1. User asks: `基于这个对外 H5 生成知识卡和一图流`.
2. User asks: `这篇分享稿每家公司一张知识卡，最终一张总览图`.
3. Contributor creates a new visual skill for public materials.

## RED Baseline

Before this change:

- `public-report-quality-gate` gated reader-facing output, but did not clearly
  state that it owns the outer route when visual, image-generation, Feishu, or
  learning skills are also needed.
- The public report skill said to keep visual generation under its own skills,
  but did not include a parent-to-child delegation map.
- Repo skill authoring guidance required repo-constraint scanning and
  evaluation evidence, but did not require classification as high-level
  router/gate, module, tool wrapper, or reference helper.
- A visual skill could be treated as the primary route for a public article
  visual package without first preserving the public report gate's Article
  Intent, Visual Gate, Judgment Ownership Gate, and Publish Gate.

## GREEN Result

After this change:

- `public-report-quality-gate` states that for reader-facing output it owns the
  outer gate.
- The public report skill includes a delegation map:
  `learning-capture`, `knowledge-article-visual`, `infographic-onepager`,
  `imagegen`, `lark-doc`, and gate-review/read-back/visual QA.
- Public report pressure scenarios now include reader-facing H5/article visual
  requests for knowledge cards and one-page infographics.
- Repo skill authoring guidance now requires routing ownership classification
  and parent gate preservation for delivery-sensitive module skills.

## Behavior Replay

| Field | Expected behavior |
|---|---|
| Input shape | Reader-facing H5/article/share draft asks for knowledge cards, chapter visuals, or a one-page infographic. |
| Trigger condition | The output is external-facing or review/share-ready, even if the immediate work is visual production. |
| Expected route | Load `public-report-quality-gate` first, preserve its hard gates, then delegate visual series work to `knowledge-article-visual`, per-image scripts to `infographic-onepager`, and bitmap generation to `imagegen` when selected. |
| Expected non-output | Do not let visual/image skills claim publish readiness, bypass Article Intent, or bypass the Visual/Publish/Judgment gates. |
| Repo-visible artifact | This OpenSpec change, updated public-report skill text, updated pressure scenarios, and updated repo `AGENTS.md` skill authoring contract. |
| Proof boundary | This proves routing text and pressure coverage. It does not prove final image quality or Feishu client usability. |

## Residual Risks

- Runtime skill selection is still model-mediated; the wording improves routing
  pressure but is not a mechanical dispatcher.
- Existing global visual skills are not edited in this change. If future replay
  still bypasses the public report gate, a narrower follow-up may add explicit
  parent-gate wording to those child skills.
- This change does not generate or QA the company knowledge-card visual assets.
