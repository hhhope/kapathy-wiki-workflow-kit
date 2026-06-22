# Eval README — team-lore agent memory contract

This directory records RED/GREEN evidence for the first draft migration slice.

## Evaluation dimensions

The draft set is evaluated on four separate dimensions:

1. `hit-rate`
   - can the expected page still be identified for the scenario

2. `first-load readability`
   - can an agent answer applicability, top facts, and next hop from the first screen

3. `boundary clarity`
   - can an agent reject neighboring pages more confidently

4. `mixed-language compatibility`
   - can the page support mixed-language routing and first-load interpretation

## Important rule

These dimensions must not be merged into a single vague "works for agents" claim.

In particular:

- hit-rate alone is not enough
- readability gains do not imply mixed-language completion
- boundary clarity must be judged separately from both routing and readability

## Files

- `BASELINE-RESULTS.md` — current pages scored against the RED scenarios
- `DRAFT-RESULTS.md` — draft pages scored against the same scenarios
- `LANGUAGE-SUPPORT-RESULTS.md` — minimal alias contract evidence
- `FRESH-CONTEXT-RESULTS.md` — context-reset routing evidence
- `KNOWLEDGE-PLANE-RESULTS.md` — Lore versus Graphify routing and responsibility evidence
- `KNOWLEDGE-ROUTING-RESULTS.md` — representative behavior checks across process, Lore, Graphify, and mixed questions
- `run-draft-section-checks.sh` — structural checks for required draft headings
