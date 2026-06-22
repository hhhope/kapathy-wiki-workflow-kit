---
id: log-02
project: payments-core
reviewed: false
---

# Log — boundary drift on callback dependency

## Deviation signal
Design discussion introduced a new outbound dependency during callback handling without checking service ownership.

## What happened
The change drifted from internal callback processing into a new external provider call.

## Why it matters
This should reinforce a shared rule about boundaries, not just a project-local note.

