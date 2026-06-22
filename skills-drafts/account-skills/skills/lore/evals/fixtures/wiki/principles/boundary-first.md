# Principle — boundary-first

## Rule

External calls must stay inside approved system boundaries and always define safe timeout and fallback behavior.

## Why

This keeps retries, degradation, and ownership predictable across services.

## Applies when

- HTTP, queue, webhook, or third-party calls are involved

## Anti-patterns

- [[pitfalls/timeout-fallback]]
- [[pitfalls/idempotency-keys]]
