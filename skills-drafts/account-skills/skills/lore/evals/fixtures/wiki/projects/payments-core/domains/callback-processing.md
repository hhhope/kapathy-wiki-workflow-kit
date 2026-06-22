# Domain — callback-processing

## Scope

Inbound payment callbacks, replay handling, and duplicate-write prevention.

## Current facts

- callbacks can be repeated by providers
- duplicate ledger writes are unacceptable

## Risks and watchpoints

- replayed callbacks without idempotency protection
- ledger writes before dedupe is confirmed

## Related pitfalls

- [[pitfalls/idempotency-keys]]

## Related principles

- [[principles/boundary-first]]
