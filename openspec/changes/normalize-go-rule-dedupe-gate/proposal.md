# Normalize Go Rule Dedupe Gate

## Why

The Go engineering/security rule was added with behavior evaluation, but the
gate did not explicitly check whether a proposed rule duplicates existing
global/common guidance. This lets external article learning drift into local
rules as repeated generic policy.

## What Changes

- Add a behavior-asset prior-art/common-rule dedupe gate before rule ownership
  changes.
- Normalize the Go engineering/security rule so it owns Go-specific guidance
  and references common/global gates for generic constraints.
- Add executable tests and evaluation replay evidence for the dedupe gate and
  Go rule boundary.

## Out Of Scope

- Changing the user-confirmed Go stack.
- Promoting repo-local rules into global `~/.codex` files.
- Rewriting historical completed OpenSpec changes.
