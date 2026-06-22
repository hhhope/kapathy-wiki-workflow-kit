# Lore Wiki Baseline Results

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`

This baseline records what has been validated in-repo after the first Lore Wiki refactor.

It is intentionally strict: documentation coverage is not treated as the same thing as runtime proof.

---

## Status summary

| Check | Status | Notes |
|---|---|---|
| G1 Propose gate | Partial | Live fixture-level integration run now exercises a local fixture `apply.sh`, but no external or production OpenSpec CLI exists in this repo |
| G2 Review/archive gate | Partial | Live fixture-level integration run now exercises a local fixture `archive.sh`, but no external or production OpenSpec archive command exists here |
| H1 Similar-task recall | Measured | Corpus-driven pressure run records `12/12 = 100%` in `skills/lore/evals/PRESSURE-RESULTS.md`; representative live-session cases now also exist in `skills/lore/evals/LIVE-AGENT-RETRIEVAL.md` |
| H2 Irrelevant-page noise | Measured | Corpus-driven pressure run records `0/8 = 0%` in `skills/lore/evals/PRESSURE-RESULTS.md`; representative live-session auth/noise separation is also recorded in `skills/lore/evals/LIVE-AGENT-RETRIEVAL.md` |
| H3 Log absorption success | Measured | Pressure run now records `8/8 = 100%` absorption plus weekly-review metrics in `skills/lore/evals/PRESSURE-RESULTS.md` |
| H4 Startup context budget | Measured | Pressure run now records `P50 = 4`, `P90 = 6`, `max = 6` across 10 startup scenarios |

---

## What was actually verified

### Verified green

- `skills/lore/SKILL.md` defines OpenSpec/Lore split and acceptance targets
- `skills/lore/README.md` matches the same split
- fixture assets now exist under `skills/lore/evals/`
- manual fixture walkthrough results exist under `skills/lore/evals/MANUAL-RESULTS.md`
- executable fixture check results exist under `skills/lore/evals/COMMAND-RESULTS.md`
- corpus-driven pressure results exist under `skills/lore/evals/PRESSURE-RESULTS.md`
- multi-session weekly-review results exist under `skills/lore/evals/MULTISESSION-WEEKLY-REVIEW.md`
- blind weekly-review comparison results exist under `skills/lore/evals/BLIND-WEEKLY-REVIEW.md`
- local end-to-end fixture results exist under `skills/lore/evals/E2E-FIXTURE-RESULTS.md`
- live retrieval, weekly review, and fixture integration results exist under `skills/lore/evals/LIVE-*.md`
- wiki templates exist for:
  - `index`
  - project overview
  - domain
  - pitfall
  - principle
  - log
- legacy `LORE-template` and `REQ-template` are explicitly marked compatibility-only
- `references/pre-commit` parses successfully with `sh -n`

### Still red or unproven

- No external or production OpenSpec CLI exists here; end-to-end proof remains local-fixture only
- No broader blind live-agent retrieval run has been executed beyond representative single-session cases plus the scripted corpus
- No external or production OpenSpec archive/apply command exists in this repo to prove end-to-end integration

---

## Next validation steps

1. Add a blind live-agent retrieval run against the same pressure corpus
2. Keep startup-budget scenarios aligned when the wiki taxonomy changes
3. If an external or production OpenSpec command surface is added, rerun the same path end to end
