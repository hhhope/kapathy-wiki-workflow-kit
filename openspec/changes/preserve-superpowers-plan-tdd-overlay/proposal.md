# Native Superpowers With OpenSpec Check/Archive

## Why

The repository needs Superpowers-native design and implementation planning to
remain uninterrupted. OpenSpec is still useful for acceptance, evidence,
scope-change stops, validation, and archive review, but it must not become a
second implementation plan.

The observed failure is not lack of OpenSpec. The failure is letting OpenSpec
rewrite or replace the approved Superpowers spec/plan. The Stripe H5 repair
recorded the same class of drift: Superpowers design was used as supporting
context rather than an acceptance checklist, and verification accepted keywords
and screenshots while the intended reader path stayed unverified.

## What Changes

- Keep Superpowers design spec and writing-plan as the implementation
  authority during native Superpowers execution.
- Treat OpenSpec tasks as check/archive lifecycle items only.
- Put the Acceptance Spec inside the Superpowers design spec.
- Run plan-check as part of Superpowers plan review, not as OpenSpec progress.
- Use OpenSpec during execution only when scope changes; otherwise use it after
  implementation for acceptance evidence, validation, and archive review.

## Out Of Scope

- Do not edit the upstream Superpowers plugin.
- Do not change OpenSpec CLI behavior.
- Do not continuously sync OpenSpec progress during Superpowers execution.
- Do not require OpenSpec for small one-session work.
- Do not turn OpenSpec `tasks.md` into a second implementation plan.
