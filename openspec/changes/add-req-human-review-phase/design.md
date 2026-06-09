# Design

## Route Position

The requirements route becomes:

```text
req-agent
  -> req-intake
  -> req-domain-analysis
  -> req-scope
  -> req-stories
  -> req-acceptance
  -> req-human-review
  -> req-handoff
```

`req-agent` remains the normal controller. `req-human-review` is a worker phase,
not a user-facing alternative entry point.

## Worker Responsibility

`req-human-review` converts a requirements case into a human-readable review
artifact after structured stories and acceptance functions exist.

It owns:

- source-material coverage review;
- domain and exclusion judgment review;
- scope and non-scope review;
- user story sufficiency review;
- scenario coverage matrix;
- rule/status matrix;
- acceptance scope review;
- gap classification;
- detailed-design gate recap;
- synchronization proof and agent usage instructions.

It does not own:

- raw source intake;
- first-pass domain taxonomy classification;
- replacing machine case status;
- OpenSpec draft generation;
- API, DDL, state-machine, or engineering design.

## Human Review Synchronization Gate

Human Review entries are classified as:

- `demand_fact`: changes or adds domain, scope, user stories, acceptance, roles,
  readiness, or blockers. These must be synchronized back to the machine case.
- `review_prompt`: a human review prompt that is not yet a requirement fact.
- `design_gate_gap`: a detailed-design material gap that blocks detailed design
  but does not block requirement review by itself.

`req-handoff` may proceed only when every Human Review `demand_fact` is
represented in the machine requirements case and the requirements checker still
passes.

## Template Contract

Human Review documents use `wiki/templates/requirements-human-review-template.md`
as the canonical output shape. The template includes the fields needed for a
human reviewer to see source coverage, story sufficiency, scenario coverage,
acceptance boundaries, and synchronization proof.

## Behavior Evidence

This is a behavior-asset change because it modifies `.codex/skills/*`. The
change includes `evaluation.md` with:

- RED baseline from the Baofu legal SMS incident;
- GREEN expected behavior after adding the worker and template;
- pressure scenarios;
- prior-art/common-rule dedupe;
- residual risks.

## Proof Boundary

This change proves the repo-local skill route, template, and manual
synchronization gate. It does not prove a full automatic consistency checker for
Human Review documents.
