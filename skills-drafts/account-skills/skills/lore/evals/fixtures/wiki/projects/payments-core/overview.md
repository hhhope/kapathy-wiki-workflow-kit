# Project Overview — payments-core

## Summary

Owns payment orchestration, callback handling, retry workers, and ledger write coordination.

## Boundaries

- Owns: payment state transitions, retry scheduling
- Calls: notification provider, settlement service
- Must not: own frontend auth/session behavior

## Key domains

- [[projects/payments-core/domains/payment-retry]]
- [[projects/payments-core/domains/callback-processing]]
