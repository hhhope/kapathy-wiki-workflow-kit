## RED Baseline

Date: 2026-05-12

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Public report gate blocks review-ready newspaper claims without citation surface | `rg "citation surface|reader-visible citation|Newspaper Citation"` found no matching rule in `.codex/skills/public-report-quality-gate`, `.codex/skills/learning-capture`, or existing specs before this change. | FAIL |
| Learning output-use map distinguishes internal learning reuse from reader-visible citations | `.codex/skills/learning-capture/references/output-use.md` says final public drafts need not expose internal wiki paths unless citations are requested, but it does not define newspaper citation-surface routing. | FAIL |
| Existing newspaper replay has a gate-level citation condition | `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md` records source maps, learning use, and final citation selection risk, but the skill gate does not require a citation surface before future newspaper review-ready claims. | FAIL |

## Intended GREEN Result

| Scenario | Expected Evidence | Result |
|---|---|---|
| Public report gate blocks review-ready newspaper claims without citation surface | `public-report-quality-gate/SKILL.md`, `gate-review-artifact.md`, and pressure scenarios name the Newspaper Citation Surface Gate. | PASS |
| Learning output-use map distinguishes internal learning reuse from reader-visible citations | `learning-capture/references/output-use.md` states that output-use maps are not a substitute for reader-visible newspaper citations. | PASS |
| Existing newspaper replay has a gate-level citation condition | Pressure scenarios cite `wiki/reports/agentic-product-engineering-collaboration-newspaper.html` and its source map as the replay case. | PASS |
| OpenSpec validation passes | `openspec validate add-newspaper-citation-output-gate --strict` passed on 2026-05-12; PostHog DNS noise was ignored. | PASS |

## Verification

| Check | Result |
|---|---|
| Citation-surface wording exists in skill/reference files | `rg "Newspaper Citation Surface|reader-visible citation|citation surface"` found the new SKILL.md rule, gate-review artifact fields, pressure scenarios, learning output-use boundary, and OpenSpec deltas. |
| Text whitespace check | `git diff --check` passed. |
| Skill body remains compact | `wc -l` returned `147` for `public-report-quality-gate/SKILL.md`; heavy details remain in references. |

## Residual Risks

- This is behavior replay evidence for skill guidance, not automatic linting.
- The current newspaper may already contain source UI elements, but this change
  governs future review-ready claims and citation-surface checks.
- Reader-visible citation wording still needs per-output editorial judgment.
