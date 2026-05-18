# harden-tool-executor-bypass-routing

## Why

The current H5 visual work exposed a workflow bypass: the request needed a
reader-facing report visual package, but execution jumped directly to
`imagegen` after the user mentioned image-model output.

This bypass skipped the parent public report gate, article-level visual
planning, per-image script compression, existing-visual inspection, and review
evidence. The repository already has pressure scenarios for this failure, but
the anti-pattern needs a reusable name and replay evidence so future agents do
not treat low-level tools as parent workflows.

## What Changes

- Add the `Tool Executor Bypass` anti-pattern to
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Add pressure scenarios that verify image generation, Feishu writing, and
  search/browser tools remain executors under parent workflows.
- Record the 2026-05-18 drift evidence in `wiki/ops`.
- Add evaluation evidence for RED baseline and GREEN corrected route.
- Use the corrected route before producing the H5 visual assets.

## Out of Scope

- Editing root agent rules.
- Replacing `knowledge-article-visual`, `infographic-onepager`, or `imagegen`.
- Adding a long trigger-word list to `AGENTS.md`.
- Regenerating the report share zip unless explicitly requested after H5 visual
  updates are accepted.

## Source Design

- `docs/superpowers/specs/2026-05-18-tool-executor-bypass-visual-routing-design.md`
