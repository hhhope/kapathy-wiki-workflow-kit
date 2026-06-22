# Pitfall — idempotency-keys

## Trigger signals

- repeated callback
- duplicate notification
- replayed provider event
- duplicate ledger write

## Failure mode

The same business event is processed twice, causing duplicate state mutation or ledger writes.

## Avoidance

- derive a stable idempotency key from provider event identity
- check dedupe before mutation
- keep write paths idempotent

## Boundary

Does not replace locking for true concurrent writes on different business keys.
