# Proposal: stabilize wiki runtime layer contract

## Summary

Stabilize the wiki runtime architecture so users and agents can understand the
entrypoints, layers, and gates without drifting between wiki-react, wiki-apply,
scorecard, eval, and behavior-gate meanings.

## Motivation

The repo-local wiki skill runtime and first decision-trace eval harness exist,
but the architecture is still spread across skills, specs, README, and ops
notes. That dispersion caused repeated confusion:

- `wiki-react` looked like it might replace `wiki-status` or `wiki-apply`.
- `wiki-apply` looked like a Python precheck wrapper instead of a repair-domain
  ReAct skill.
- scorecard, eval harness, and behavior-asset gates were discussed as if they
  owned the same kind of judgment.
- active spec paths still carry obsolete slash-command names even after the
  runtime moved to repo-local skills.

## Scope

- Add a repo-visible wiki runtime layer contract with an architecture diagram.
- Update README to explain the layer model and how to use the skills.
- Rename active wiki runtime skill specs away from obsolete slash-command names.
- Add anti-drift tests for the layer contract, README, and active specs.

## Non-Goals

- Do not add new runtime capabilities.
- Do not restore plugin or slash command runtime.
- Do not change scorecard algorithms, eval case semantics, or frontmatter
  taxonomy rules.
- Do not archive completed changes as part of this implementation.
