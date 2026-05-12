## Context

The failure surfaced in a public-article visual workflow:

1. The target artifact was reader-facing: an H5/share-style article and visual
   package.
2. The requested output was visual: company knowledge cards and one total
   infographic.
3. The implementation route jumped toward visual/image skills before the public
   report gate had re-owned the output intent and visual gate.

This is a routing/ownership problem, not an image-generation problem.

## Design

### Public Output Parent Route

`public-report-quality-gate` should state that for reader-facing outputs it owns
the outer gate. It may delegate work to other skills, but the delegated skills
do not replace the gate.

The parent gate keeps ownership of:

- Article Intent Contract
- Reference Structure / Reference Output Shape Gate
- Learning Use Map
- Judgment Ownership Gate
- Visual Gate
- Publish Gate
- gate-review artifact and proof boundary

### Subordinate Skill Map

Add a compact map to the public report skill body or references:

| Public output need | Delegated skill |
|---|---|
| source/reference learning | `learning-capture` and narrower modules |
| article-level visual package | `knowledge-article-visual` |
| per-image poster/card script | `infographic-onepager` |
| generated bitmap assets | `imagegen` |
| Feishu document write | `lark-doc` |
| final verification | gate-review artifact, read-back, visual QA |

The map is not meant to duplicate each child skill's workflow. It only states
the parent-child boundary.

### Skill Authoring Classification

Skill authoring guidance should require a small ownership classification before
creating or semantically editing a skill:

- `high-level router/gate`: owns an intent class and may delegate modules.
- `module`: handles a specific part of an intent class and preserves its parent
  router/gate when one applies.
- `tool wrapper`: wraps an external/local tool and does not own reader or
  governance decisions.
- `reference helper`: provides guidance/templates but does not own execution
  readiness.

For delivery-sensitive modules, the author should record the parent router/gate
or state that no parent applies.

### Minimal Implementation Boundary

Do not edit `knowledge-article-visual` in this change unless validation proves
the public-report parent route still cannot catch the intended scenario. The
cleaner fix is to make the outer gate clear in one place and make future skill
authoring check parent ownership.

## Verification

Verification should include:

- Text evidence that `public-report-quality-gate` states high-level parent
  ownership for reader-facing outputs.
- Text evidence that the subordinate skill map includes visual package,
  per-image infographic, image generation, Feishu write, and verification.
- Text evidence that skill authoring guidance requires router/module/tool/helper
  classification.
- Pressure/evaluation evidence that:
  - public article + knowledge cards routes through the public report gate
    before visual skills;
  - new visual skill creation checks parent gate ownership;
  - child skills do not weaken existing module-specific gates.

## Non-Goals

- Do not create another visual skill.
- Do not generate final company knowledge-card images.
- Do not publish, sync, or claim any H5/report is review-ready.
- Do not require every existing child skill to repeat the parent gate unless it
  later proves necessary.
