## Why

The repository already connects learning artifacts to reader-facing outputs,
and the public report gate already protects reference-shaped article flow. The
remaining gap is citation visibility for newspaper-style H5/share packages.

The new AI Agent Product Engineering Collaboration newspaper exposed this
specific risk: the output can have a source map, learning use map, visual
assets, and a gate review, while the shareable newspaper itself still lacks a
clear citation surface that tells a reader which public sources carry the
claims.

Reference case:

- `wiki/reports/agentic-product-engineering-collaboration-newspaper.html`
- `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`
- `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`

## What Changes

- Add a newspaper citation surface requirement for H5/share packages and
  newspaper-style public drafts.
- Extend the learning-output reuse gate so newspaper outputs distinguish:
  internal learning reuse evidence from reader-visible citations.
- Extend the public report gate so a newspaper cannot be review-ready when
  load-bearing claims, figures, or visual panels have no visible citation route.
- Add pressure scenarios using the new newspaper as the replay example.

## Impact

- Updates OpenSpec coverage for `learning-output-reuse-gate`.
- Updates OpenSpec coverage for `public-report-quality-gate`.
- Later implementation should update `.codex/skills/public-report-quality-gate/`
  and `.codex/skills/learning-capture/references/output-use.md`.
- Does not rewrite the current newspaper H5 in this change setup step.
- Does not sync Feishu or publish the newspaper.
