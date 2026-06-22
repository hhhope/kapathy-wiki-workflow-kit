# Proposal — Payment Retry Safety

## Goal

Prevent duplicate ledger writes during repeated payment callbacks and retry worker execution.

## Outcome

- callback handling remains idempotent
- worker retries stay inside provider timeout boundaries

## Non-goals

- redesigning the settlement pipeline
- changing auth or session behavior
