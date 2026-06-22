---
id: log-04
project: settlements-core
reviewed: false
---

# Log — reconciliation replay gap

## Deviation signal
Replay of reconciliation input could create duplicate settlement writes.

## What happened
The design treated replayed records as fresh writes instead of idempotent events.

## Why it matters
This belongs in settlement reconciliation domain guidance.

