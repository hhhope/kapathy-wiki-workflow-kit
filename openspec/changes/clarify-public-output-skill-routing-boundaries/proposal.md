## Why

Reader-facing output work now spans multiple specialized skills: public report
gating, learning capture, article visual packaging, per-image infographic
formatting, image generation, Feishu writing, and verification. The existing
public report gate is strong on publish blockers, but it does not clearly state
that it owns the outer route when the target is an external-facing article, H5,
share draft, or Feishu review draft.

That gap allowed a visual request for a public article to route directly into
visual/image skills. The visual skills did useful local work, but the work was
not first re-anchored to the public report gate's Article Intent Contract,
Visual Gate, Judgment Ownership Gate, and Publish Gate.

The repository already has a better pattern in `learning-capture`: a parent
router owns the intent class and delegates to narrower modules. Public output
needs the same explicit parent-child boundary.

## What Changes

- Clarify `public-report-quality-gate` as the high-level gate/router for
  reader-facing output.
- Add a subordinate skill map for public output work:
  source/learning, article visual package, per-image poster/card, image
  generation, Feishu write, and verification.
- Require skill authoring to classify created or semantically edited skills as
  high-level router/gate, module, tool wrapper, or reference helper.
- Require module skills that affect delivery-sensitive output to preserve the
  parent router/gate boundary instead of silently becoming independent routes.
- Add pressure scenarios for public article visual requests and new visual
  skills that must not bypass the public report gate.

## Impact

- A user asking to turn an external-facing article/H5 into knowledge cards or a
  one-page infographic will first route through `public-report-quality-gate`,
  then delegate to visual skills.
- `knowledge-article-visual` does not need an immediate semantic edit if the
  public report gate clearly owns the outer route.
- Future skill changes must record whether the skill is a router, module, tool
  wrapper, or reference helper before claiming the behavior is complete.
- This change does not publish or sync any report, and does not generate final
  visual assets.
