## Baseline 2026-05-08

| Check | Evidence | Result |
|---|---|---|
| Prior OpenSpec state | `openspec list` shows `add-public-report-quality-gate`, `connect-learning-capture-to-output-gates`, and `route-complex-public-reports-to-reviewer` as Complete | Existing completed changes cannot be extended |
| Failed packet state | `wiki/ops/team-knowledge-base-overview-report-gate-review.md` records `Reference Readback Failure 2026-05-08` and freezes the five-article packet | Feishu packet is failed draft, not review-ready |
| Runtime draft | `wiki/reports/team-knowledge-base-runtime.md` currently uses routing tables and generic closeout language | Too thin for release |
| Validation/cases draft | `wiki/reports/team-knowledge-base-validation-cases.md` currently summarizes evidence categories and non-claims | Too generic for release |
| Visual draft | `wiki/reports/account-wiki-visuals.html` has overview and generic cards only | Missing runtime and validation/cases visuals |
| Reference images 14-17 | `/mnt/c/Users/yan/Desktop/1/14.png` through `17.png` are 1672x941 horizontal hand-drawn teaching cards | Use horizontal chapter-card structure when content does not need a dense one-page infographic |

## RED Baseline

| Scenario | Current Behavior | RED Result |
|---|---|---|
| Account Wiki multi-page public draft is requested after failed reference readback | Existing local drafts can still be read as repairable prose without an active repair change | FAIL: repair scope was not yet isolated in a new OpenSpec change |
| Runtime page must explain real operating flow | Current runtime page lists stages and responsibilities but does not walk through a real material journey | FAIL |
| Validation page must prove claims with concrete cases | Current validation/cases page says evidence exists but does not expose the actual failed-freeze/readback/RED-GREEN data | FAIL |
| Visual style reference is present | Current visual artifact has no dedicated runtime or validation/cases diagrams | FAIL |
| `infographic-onepager` handles Account Wiki multi-page repair | Current skill focuses on a six-section vertical onepager and Account Wiki overview skeleton | FAIL |
| User asks for chapter illustrations or horizontal cards | Current skill has no explicit route for "章节配图", "横图", or "信息没那么多，不需要一图流" | FAIL |

### Reference Image Readback

| Image | Shape | Reusable Structure | Reuse Boundary |
|---|---|---|---|
| `14.png` | 16:9 teaching card | old/new contrast bar, four numbered cards, bottom takeaway | Reuse process-card layout, not Skill wording |
| `15.png` | 16:9 teaching card | three large numbered layers with icons and one bottom conclusion | Reuse three-layer chapter explanation |
| `16.png` | 16:9 teaching card | two-column scenario comparison plus lower examples | Reuse evidence/case contrast layout |
| `17.png` | 16:9 teaching card | two optimization questions, two lanes, iteration cards | Reuse chapter visual for focused improvement path |

### Skill RED Baseline

Input shape:

```text
给 Account Wiki 的运行态、验证与案例做章节配图。参考 14-17 的横图风格。
信息没有那么多，不需要一图流。
```

Old-skill route:

- `description` and overview bias toward "one-page infographic" and "long poster".
- `Default Style` says vertical 2:3 or 3:4 poster.
- `Six-Section Poster Skeleton` is the default unless a reference requires a
  different sequence.
- `Account Wiki Skeleton` forces a single six-section overview poster.

RED result:

- It can rationalize producing a vertical six-section Account Wiki poster even
  when the requested asset is a horizontal chapter-supporting illustration.
- It does not preserve separate visual jobs for runtime and validation/cases.
- It does not explicitly say that lower-information chapters should become
  focused horizontal cards instead of inflated onepagers.

## GREEN Result

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Runtime page must explain real operating flow | `wiki/reports/team-knowledge-base-runtime.md` now explains Wiki structure, skill routing, agent/reviewer roles, material flow, public-draft gate chain, and runtime boundaries. Static check found `Wiki 结构`, `skills`, `reviewer`, `gate`, `replay`, `learning-capture`, `public-report`, and `infographic-onepager`. | PASS |
| Validation page must prove claims with concrete cases | `wiki/reports/team-knowledge-base-validation-cases.md` now uses six cases with data: `92 / 100 -> INVALID`, Reference Gate `PASS -> FAIL`, Feishu update/read-back log ids, read-back length `12818`, RED/GREEN counts, scorecard sum `100`, and 14-17 image dimensions `1672 x 941`. | PASS |
| Chapter visuals should not be forced into onepager format | `/home/yan/.codex/skills/infographic-onepager/SKILL.md` now has a format decision table that routes `横图`, `章节配图`, `信息不多`, and `不需要一图流` to horizontal teaching cards. | PASS |
| Account Wiki page-specific visuals stay separate | The skill's Account Wiki article-set map keeps `Runtime` as source -> route -> asset -> output -> writeback and `Validation / cases` as claim -> evidence -> replay -> gate decision -> boundary. | PASS |

## Current Static Checks

| Check | Result |
|---|---|
| Runtime page contains structure / skill / agent / gate terms | PASS |
| Validation page contains concrete case/data markers | PASS |
| Infographic skill contains horizontal teaching-card route | PASS |
| Skill length | `302` lines; acceptable as a patched existing global skill for this run, but a later cleanup should move long prompt patterns to references if this becomes frequently loaded |

## Residual Risks

- This change does not update Feishu.
- Local HTML verification proves only local visual structure, not final Feishu
  rendering.
- Skill behavior proof will be local pressure-test evidence, not multi-session
  rollout proof.
