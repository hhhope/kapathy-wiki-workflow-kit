---
name: cr-scope
description: Use only inside cr-agent to map diff evidence into technical review dimensions and evidence needs.
---

Classify impact scope from diff evidence.

Trigger dimensions for:

- account, payment, settlement, clearing, merchant onboarding, or customer paths
- certificate, keyType, cryptography, terminal key, encryption, or decryption changes
- DB, DDL, migration, data repair, or rollback scripts
- external channel, old frontend gateway, third-party, or upstream/downstream contracts
- auth, authorization, role, token, PII, or compliance-sensitive paths
- scheduled jobs, MQ, async processing, idempotency, or retry paths
- config center, environment-specific config, registry, or deployment settings

Output triggered technical dimensions, required evidence checks, suggested reviewers, and uncertainty items.
