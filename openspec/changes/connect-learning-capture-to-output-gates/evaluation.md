## RED Baseline

Date: 2026-05-08

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Learning artifact distinguishes source domain from reusable output capability | `learning-capture` records source kind, local usefulness, and adoption boundary, but does not name the separate `domain` versus `content / structure / visual / evidence / boundary` distinction. | FAIL |
| Reader-facing output checks learned references before drafting | `public-report-quality-gate` requires reference mapping and split strategy, but does not require opening prior learning artifacts or mapping them to output sections, visuals, metrics, or boundaries. | FAIL |
| Learned reference is visibly used or skipped | Current gates can say a reference exists, but cannot prove which learning point changed the draft or why a relevant learning point was not used. | FAIL |
| Account Harness Wiki uses learned article structures as constraints | The trace records reference lessons and an ASCII flow sketch, but no gate requires a draft to map those lessons to the proposition, sections, visuals, cases, or future-boundary claims. | FAIL |

## GREEN Result

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Learning artifact distinguishes source domain from reusable output capability | `learning-capture/SKILL.md` now requires source domain/topic to be separated from reusable capability type; `references/routing.md` defines domain/topic versus capability type and gives examples. | PASS |
| Reader-facing output checks learned references before drafting | `public-report-quality-gate/SKILL.md` now requires a learning artifact map before drafting when the output claims to use prior learning; `gate-review-artifact.md` inserts the learning use map before split strategy and drafting. | PASS |
| Learned reference is visibly used or skipped | `learning-use-map.md` requires learning artifact, domain/topic, capability type, learning point, output use, and skip reason for relevant unused points. | PASS |
| Account Harness Wiki uses learned article structures as constraints | Pressure scenarios now fail when prior article learning is claimed but no artifacts are opened, when domain is confused with capability type, or when a relevant visual/evidence lesson has no use or skip reason. | PASS |
| Scorecard remains internally consistent | `awk` sum over public report scorecard dimensions returned `100` after adding `Learning reuse`. | PASS |
| Skill bodies remain compact | `wc -l` returned `95` for `learning-capture/SKILL.md` and `70` for `public-report-quality-gate/SKILL.md`; heavy detail is in `references/`. | PASS |
| OpenSpec validation passes | `openspec validate connect-learning-capture-to-output-gates --strict` passed on 2026-05-08; PostHog DNS noise was ignored. | PASS |

## Account Harness Wiki Replay

| Learning Artifact | Domain / Topic | Capability Type | Output Use |
|---|---|---|---|
| Account Harness reference group | account harness / knowledge base | structure, visual | Drives multi-page reading map, lifecycle visual, and page split before drafting. |
| WaytoAGI Skill article | skill authoring / agent workflow | structure, visual, boundary | Drives "daily behavior first" opening, per-section visual responsibility, and "run first, then formalize" boundary. |
| WeChat agent article | agent-first software | structure, evidence, boundary | Drives problem-first opening, observable cases/metrics section, and current-versus-future separation. |

Relevant learned points that cannot be supported with local data must be skipped
or kept as visual/evidence style only. For example, source articles may teach
that metrics matter, but they cannot justify inventing local trigger rates.

## Residual Risks

- This is still skill/reference pressure evidence, not multi-session rollout
  proof.
- The learning use map is manual; no script currently enforces required fields.
- The change connects learning to output gates, but it does not rewrite the
  Account Harness Wiki article or update Feishu.
- Existing dirty worktree files outside this change remain intentionally
  untouched.
