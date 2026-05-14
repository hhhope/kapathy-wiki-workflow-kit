# Proposal: formalize wiki runtime layer boundary

## Summary

Formalize the boundary between `$wiki-react`, decision-trace eval,
`/wiki:apply`, repair-route labels, and OpenSpec lifecycle.

## Motivation

The 2026-05-14 wiki runtime discussion exposed a stable architecture gap. The
repository has runtime layers and diagnostics, but the boundary between routing,
validation, preview, repair labels, and lifecycle is still easy to confuse in
conversation.

The specific failure was not only that brainstorming drift happened. The deeper
issue was that these layers were substituted for each other:

- `$wiki-react` was treated as interchangeable with eval output.
- `eval_wiki_decision_trace.py` was treated like a repair path.
- `/wiki:apply` was treated like a repair executor.
- repair-route labels were treated like implemented executable repair
  infrastructure.
- OpenSpec lifecycle was blurred with runtime preview and validation.

This change records the stable boundary so future agents have a durable source
for what each layer owns.

## Scope

- Add an ops distill that explains the misread and the corrected layer model.
- Add ADR-0033 as the stable decision for wiki runtime layer boundaries.
- Add an OpenSpec delta that captures the required separation.
- Keep the previous brainstorming drift retro as incident evidence, not the
  architecture decision itself.

## Non-Goals

- Do not implement new runtime repair executors.
- Do not change `$wiki-react`, eval, or `/wiki:apply` behavior in code.
- Do not add repair-route output schemas.
- Do not modify Superpowers upstream skills.
- Do not reopen `improve-wiki-routing-diagnostics`.
