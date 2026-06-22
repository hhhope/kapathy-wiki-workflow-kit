# Design — Payment Retry Safety

## Summary

Use idempotency keys on callback and worker paths, and enforce timeout/fallback behavior on provider calls.

## Interfaces

- payment callback handler
- retry worker
- notification provider client

## Risks

- duplicate callback writes
- long-hanging provider calls
