---
name: cr-replay
description: Use only inside cr-agent to evaluate CR behavior against incident and gate replay fixtures.
---

Provide behavior replay and regression evidence.

Initial scenarios:

- mandao-customer keyType release range
- feature branch compared to master for release CR
- DDL without rollback evidence
- sensitive token or private key committed
- missing tests for high-risk integration change
- unrelated commits in release range

Replay evidence must capture input situation, triggered worker, expected issue, expected gate, proof boundary, and residual risk.
