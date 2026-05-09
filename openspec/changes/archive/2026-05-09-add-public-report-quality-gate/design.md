## Context

This repository already separates source capture, ops traces, reports, examples,
and workflow changes. However, reader-facing output currently depends on the
agent remembering to apply multiple scattered checks:

- material-processing flow
- learning/reference capture
- report template
- visual/H5 conventions
- Lark document creation
- verification before claiming completion

The failure mode is not that these skills are absent. The failure mode is that
none of them owns the moment before an internal draft becomes a public-facing
review draft.

## Decision

Create one repo-local gate skill:

`public-report-quality-gate`

The skill is a trigger and quality gate for reader-facing output. It does not
own source reading, material extraction, H5 rendering, or Feishu API calls. It
owns the decision that a draft is ready, or not ready, to become a public/report
review artifact.

## Gate Model

The gate has two layers:

1. Hard gates: any hard-fail blocks publishing or Feishu sync.
2. Scorecard: if hard gates pass, the draft still needs an 80+ total score to
   be considered publish/review-ready.

Hard gates:

- reference structure map exists when a reference artifact is provided
- split strategy is explicit when the material spans multiple reader jobs
- voice gate has no hard-fail
- core narrative remains consistent with the stated purpose
- visual plan explains what each diagram carries
- publish gate has explicit review status and residual risks

## Skill Boundary

The skill coordinates existing skills:

- `learning-capture` or example-reference guidance for external references
- `material-collaboration-defaults` for source/material processing
- visual/H5 skills for rendered one-pagers
- `lark-doc` for Feishu creation/update after the gate passes
- `verify-before-claiming` before completion claims

It does not replace those skills and does not weaken their gates.

## Non-Goals

- No rewrite of the failed account knowledge-base draft in this change.
- No automatic Feishu publishing.
- No new agent template unless a later change proves a manual reviewer role is
  needed.
- No global/root skill promotion.
