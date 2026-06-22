# Eval README — language and routing hardening

This directory records RED/GREEN evidence for the follow-up hardening slice.

## Target slice

- `drafts/wiki/index.md`
- `drafts/projects/account-skills/overview.md`
- `drafts/pitfalls/behavior-assets-without-evidence.md`

## Evaluation dimensions

1. `mixed-language first-load support`
   - can a mixed-language prompt not only route to the right page, but also load the first working facts from the first screen
2. `routing automation`
   - can representative `process / lore / graphify / mixed` cases be checked by script instead of narrative-only walkthrough

## Commands

- `python3 openspec/changes/harden-team-lore-language-and-routing/evals/check-language-hardening.py`
- `python3 openspec/changes/harden-team-lore-language-and-routing/evals/check-routing-automation.py`

## Result files

- `LANGUAGE-HARDENING-RESULTS.md`
- `ROUTING-AUTOMATION-RESULTS.md`
