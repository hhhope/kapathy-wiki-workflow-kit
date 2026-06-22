# Lore Command-Level Fixture Results

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`
Command: `sh skills/lore/evals/run-fixture-checks.sh`

This file records the result of the executable fixture checks bundled with the Lore eval corpus.

---

## Result

```text
PASS | gate-propose-present has proposal.md
PASS | gate-propose-present has design.md
PASS | gate-propose-present has tasks.md
PASS | retrieval fixture has idempotency page
PASS | retrieval fixture has timeout-fallback page
PASS | retrieval fixture has boundary-first principle
PASS | index references idempotency page
PASS | index references timeout-fallback page
PASS | index references boundary-first principle
PASS | callback-processing domain references idempotency page
PASS | payment-retry domain references timeout-fallback page
PASS | payment-retry domain references boundary-first principle
PASS | noise-auth-unrelated fixture contains no auth pages
PASS | absorption fixture has project-domain log
PASS | absorption fixture has principle log
PASS | project-domain log declares a suggested destination
PASS | project-domain log maps to a domain page
PASS | principle log maps to a principle page
PASS | startup-budget-medium stays within the 6-page budget
SUMMARY | all fixture checks passed
```

This proves the fixture set is internally consistent and command-runnable.

It still does not prove:
- live agent retrieval quality
- live OpenSpec apply/archive integration
- multi-session adversarial behavior
