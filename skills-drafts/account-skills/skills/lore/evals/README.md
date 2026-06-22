# Lore Eval Fixtures

This directory contains the minimum fixture set needed to validate the Lore Wiki workflow without depending on a live external repo.

## Contents

- `evals.json`
  Defines the first-pass evaluation cases for gates, retrieval, absorption, and startup-budget checks.
- `fixtures/openspec/change-payment-retry/`
  Minimal OpenSpec change fixture with `proposal.md`, `design.md`, and `tasks.md`.
- `fixtures/wiki/`
  Minimal wiki corpus with one project, two domains, two pitfalls, one principle, and an index.
- `fixtures/logs/`
  Sample logs for weekly review and absorption checks.
- `openspec-fixture/`
  Minimal command surface for fixture-level `apply` and `archive` gating.
- `pressure/`
  Expanded retrieval, weekly-review, and startup-budget corpus for second-pass pressure testing.

## Suggested manual run order

1. Gate checks
   - Remove the fixture `proposal.md` or `tasks.md` mentally and confirm the workflow should block.
   - Use the intact fixture and confirm the workflow can continue.
2. Retrieval checks
   - Run the query prompts in `evals.json` against `fixtures/wiki/index.md`.
   - Confirm the expected target pages are chosen.
3. Log absorption checks
   - Read logs in `fixtures/logs/`.
   - Confirm each accepted log maps to the expected target wiki page.
4. Startup budget checks
   - Count unique pages needed for each startup scenario.
   - Keep startup context within the target budget from `TDD-SPEC.md`.
5. Pressure checks
   - Run `python3 skills/lore/evals/run-pressure-checks.py`.
   - Review `PRESSURE-RESULTS.md` for measured recall, noise, weekly-review metrics, and startup-budget distribution.
6. Multi-session weekly review checks
   - Run `python3 skills/lore/evals/run-multisession-weekly-review.py`.
   - Review `MULTISESSION-WEEKLY-REVIEW.md` for per-session and aggregate weekly-review metrics.
7. Blind weekly review checks
   - Run `python3 skills/lore/evals/run-blind-weekly-review.py`.
   - Review `BLIND-WEEKLY-REVIEW.md` for blind decision accuracy against the oracle mapping.
8. Knowledge-plane routing checks
   - Run `python3 skills/lore/evals/run-knowledge-routing-checks.py`.
   - Review `KNOWLEDGE-ROUTING-RESULTS.md` for process, Lore, Graphify, and mixed-question routing behavior.
9. End-to-end fixture checks
   - Run `sh skills/lore/evals/run-e2e-fixture.sh`.
   - Review `E2E-FIXTURE-RESULTS.md` for the full local path from apply gate to archive gate.

## Limits

- This is a fixture corpus, not a full automated harness.
- It supports repeatable manual or future scripted evaluation.
- `run-pressure-checks.py` is corpus-driven validation, not a live multi-session adversarial run.
