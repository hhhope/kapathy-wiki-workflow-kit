# Lore Live Integration Results

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`
Command: `sh skills/lore/evals/run-live-integration-checks.sh`

This file records a live gate-integration run using temporary copies of the OpenSpec and log fixtures plus the local fixture command surface under `skills/lore/evals/openspec-fixture/`.

---

## Result

```text
PASS | apply gate allows execution when proposal/design/tasks are present
PASS | apply gate blocks execution when proposal.md is missing
PASS | archive gate blocks when unreviewed logs exist
PASS | archive gate allows progression after logs are marked reviewed with destinations
SUMMARY | all live integration checks passed
```

This proves fixture-level gate behavior for:
- apply entry with full OpenSpec change docs
- apply block when `proposal.md` is missing
- archive block when logs remain unreviewed
- archive progression after reviewed markers and destinations are present
- gate behavior exercised through local `apply.sh` / `archive.sh` commands, not only inline assertions

This still does not prove:
- an external or production OpenSpec CLI
- multi-session adversarial behavior
