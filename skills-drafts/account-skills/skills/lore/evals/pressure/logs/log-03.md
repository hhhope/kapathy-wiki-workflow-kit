---
id: log-03
project: payments-core
reviewed: false
---

# Log — duplicate callback write

## Deviation signal
Repeated callback events could write the ledger twice.

## What happened
Dedupe was assumed but not enforced at the callback identity level.

## Why it matters
This is a recurring anti-pattern that should live in a pitfall page.

