---
artifact_type: runtime-replay
title: team-knowledge-base-overview / paragraph-drift-runtime-replay
canonical_object: team-knowledge-base-overview
related_objects:
  - public-report-quality-gate
  - public-report-reviewer
derived_from:
  - wiki/reports/team-knowledge-base-overview.md
  - .codex/skills/public-report-quality-gate/SKILL.md
  - .codex/skills/public-report-quality-gate/references/scorecard.md
  - .codex/skills/public-report-quality-gate/references/gate-review-artifact.md
  - .codex/agents/public-report-reviewer.md
validates:
  - openspec/changes/add-public-report-paragraph-drift-gate
created: 2026-05-11
---

# team-knowledge-base-overview / paragraph-drift-runtime-replay

## Replay Target

Target draft: `wiki/reports/team-knowledge-base-overview.md`

Replay purpose: validate the new public-report paragraph drift and judgment
ownership gate on a real existing report draft, not only on pressure-scenario
wording or unit tests.

This replay does not rewrite the article and does not sync Feishu.

## Result

Runtime replay result: PASS for gate behavior.

The gate did not claim the draft is ready. It produced concrete blockers:

- reference linked-page readback is incomplete
- learning-use mapping is incomplete
- several proof-strength claims need local source evidence
- some user-owned judgments are not explicitly confirmed
- overall score remains `INVALID`
- diagnostic paragraph drift scores remain available for repair

This is the expected behavior. A real gate should catch these issues instead of
turning a smooth article into a publish-ready claim.

## Reviewer Routing

Reviewer routing: required and applied manually in this replay.

Checked signals:

| Signal | Result | Evidence |
|---|---|---|
| Multi-page or series output | true | Section 10 links overview, runtime, migration, validation, and roadmap pages. |
| External reference structure | true | The draft cites Karpathy `LLM Wiki` and uses Feishu linked pages as the report group. |
| Public target | true | The target is a reader-facing report page. |
| Evidence decision | true | The replay asks whether the new scorecard/gate behavior holds. |
| Drift history | true | The change was created because the prior process missed paragraph drift and judgment ownership. |
| Template / visual / learning choice | true | The draft depends on reference learning and a multi-page reading path. |

Template selection status: not applicable for this replay because no rewrite was
requested. If this article is rewritten, template candidates must be presented
before drafting.

## Article Intent Contract

| Field | Contract |
|---|---|
| Reader | Internal stakeholder or teammate evaluating whether Account Wiki is a useful knowledge-base operating model. |
| Reader decision or action | Decide whether Account Wiki should be understood as a maintained knowledge compilation layer, not a folder or one-shot RAG answer. |
| Main line | Account Wiki sits between raw sources and future questions/reports/decisions; AI can maintain structure, but source truth and final judgment remain human-owned. |
| Non-goals | Do not prove full automation. Do not claim Feishu sync quality. Do not make implementation-roadmap promises. Do not replace the linked runtime, migration, validation, or roadmap pages. |
| User-owned judgments | Whether this framing is the official public position; whether current capabilities are mature enough to say "already done"; what next-stage priorities are accepted. |
| Agent-allowed work | Map structure, identify drift, classify judgment source, suggest retain/compress/rewrite/delete/ask-user actions. |

## Reference Structure Map

| Field | Result |
|---|---|
| Source | `wiki/reports/team-knowledge-base-overview.md`; cited source: Karpathy `LLM Wiki`; linked Feishu pages for runtime, migration, validation, and roadmap. |
| Reader job | Understand what Account Wiki is, why it is different from folders/RAG, how it operates, and where to read next. |
| Page group | Multi-page group: overview plus runtime, migration, validation/cases, roadmap. |
| Reading path | Section 10 gives a concrete path, but this replay did not fetch/read the Feishu-linked pages. |
| Visual logic | The draft has tables and a simple flow block. It has no dedicated visual asset in this replay. |
| Writing standard | Explanatory public-facing Chinese report prose with tables and boundaries. |
| Reuse boundary | Karpathy can support the persistent wiki framing. Local maturity claims require local evidence. |

Reference Structure Gate: FAIL for review-ready status because concrete linked
pages were not read back in this replay.

## Learning Use Map

| Learning artifact | Domain / topic | Capability type | Learning point | Output use | Skip reason |
|---|---|---|---|---|---|
| Karpathy `LLM Wiki` link cited in the draft | LLM-maintained wiki | content, boundary | A wiki can be a persistent compounding artifact rather than a one-shot answer. | Sections 01, 02, 04, 11. | Source link was not fetched in this replay, so source fidelity remains unverified. |
| Prior Account Wiki gate history | Public report gate calibration | boundary, evidence | Failed drafts need repo-visible evidence and invalid scores when gates fail. | This replay artifact and hard gate decision. | Not used as public article content. |

Learning Use Gate: PARTIAL. The draft cites learning, but a complete
output-use map and linked-source readback are not present in the article itself.

## Section And Paragraph Drift Review

Scale: 0 means fully serves the main line; 5 means violates target or replaces
user judgment.

| Section | Section objective | Paragraph claim | Mainline role | Target fit | Narrative drift | Evidence fit | Judgment source | Action |
|---|---|---|---|---:|---:|---:|---|---|
| Opening callout | Give the article's thesis. | Account Wiki is the middle layer between raw sources and future questions. | Setup | 0 | 0 | 1 | Article draft / source framing | Retain. |
| 01 | Separate Wiki from folder and one-shot RAG. | Folder and retrieval do not create accumulated judgment. | Contrast | 0 | 0 | 1 | Source material + agent organization | Retain; cite source if publishing. |
| 02 | Define Account Wiki. | Raw sources, wiki, and future outputs are distinct layers. | Definition | 0 | 0 | 1 | Article draft | Retain. |
| 03 | Explain minimum architecture. | Source, Wiki, and maintenance rules are all required. | Structure | 0 | 0 | 2 | Agent inference from local model | Retain, but source local rules if review-ready. |
| 04 | Explain operation model. | Ingest, Query, and Lint decide whether the wiki accumulates. | Mechanism | 0 | 0 | 2 | Source framing + local interpretation | Retain; add local examples or links. |
| 05 | Show current structured capabilities. | Account Wiki already has Obsidian compatibility, intake classification, domain routing, typed relations, and graph extraction. | Evidence | 1 | 1 | 4 | Unknown / local repo evidence not cited in article | Ask the user or cite local evidence; do not publish as mature capability proof without support. |
| 06 | Define human/AI split. | AI maintains structure; humans own sources, priorities, and release decisions. | Boundary | 0 | 0 | 1 | User-stated principle + article draft | Retain. |
| 07 | Distinguish Index and Log. | Current content index exists; timeline-style wiki evolution log is not clear enough and should be next-stage work. | Gap / roadmap bridge | 1 | 1 | 4 | Agent inference / unknown priority owner | Ask the user whether this is an accepted next-stage priority. |
| 08 | Explain value. | Account Wiki makes synthesis and reuse compound. | Benefit | 0 | 0 | 2 | Article draft + local examples | Retain; add source links for examples if review-ready. |
| 09 | State boundaries. | Account Wiki is not fully automated and does not replace source truth or human judgment. | Boundary | 0 | 0 | 1 | Article draft + user-stated principle | Retain. |
| 10 | Provide reading path. | Readers should read overview, runtime, migration, validation, and roadmap in order by need. | Navigation | 0 | 0 | 3 | Article draft; linked pages not read in replay | Retain as navigation, but Reference Gate cannot pass until linked pages are read. |
| 11 | Close with final judgment. | If it does not update, link, expose contradictions, and write back valuable answers, it is only a cleaner folder. | Conclusion | 0 | 1 | 3 | Agent synthesis from source framing | Ask user to confirm public stance or soften as a working thesis. |

Paragraph Drift Gate: PARTIAL / FAIL for review-ready status. The article's
main line is stable, but sections 05, 07, and 11 contain proof-strength or
priority/public-stance judgments that need source evidence or user confirmation.

## Judgment Ledger

| Judgment | Source class | Status | Required action |
|---|---|---|---|
| Account Wiki is a compilation layer between raw sources and future outputs. | Source material + article draft | Acceptable | Keep, with source citation if public. |
| AI maintains structure while humans own judgment. | User-stated principle + article draft | Acceptable | Keep. |
| Current system already has a set of structured capabilities. | Unknown / local repo evidence not cited | Blocker | Cite local source evidence or downgrade wording. |
| Index exists but Log is not clear enough and is next-stage work. | Agent inference / unknown priority owner | Blocker | Ask user to confirm priority before public claim. |
| Without sustained updating/linking/writeback, this is only a cleaner folder. | Agent synthesis | Needs confirmation | Ask user to confirm as public stance or rewrite as a bounded thesis. |

Judgment Ownership Gate: FAIL for review-ready status. The replay found
user-owned or source-required judgments that are not yet explicitly confirmed in
the artifact.

## Hard Gate Results

| Gate | Result | Reason |
|---|---|---|
| Reviewer routing | PASS | Required and applied manually in this replay. |
| Learning use | PARTIAL | Karpathy learning is cited, but source readback and output-use mapping are incomplete. |
| Reference structure | FAIL | Linked Feishu pages in the reading path were not fetched/read in this replay. |
| Split | PASS | The draft is an overview and points to separate runtime/migration/validation/roadmap pages. |
| Voice | PASS | The draft is mostly report prose, not chat or worklog narration. |
| Narrative | PASS | The main line stays consistent: compiled wiki layer between sources and future use. |
| Paragraph drift | FAIL | Sections 05, 07, and 11 need evidence or user confirmation. |
| Judgment ownership | FAIL | Current-capability maturity, next-stage priority, and final public stance are not fully source-backed or user-confirmed here. |
| Visual | NOT TESTED | No visual reference or visual asset readback was performed in this replay. |
| Publish | FAIL | Hard gates are not all passed; no Feishu sync or review-ready claim is allowed. |

## Scorecard

Overall score: `INVALID`

Reason: Reference Structure Gate, Paragraph Drift Gate, Judgment Ownership Gate,
Visual Gate, and Publish Gate are not fully passed.

Diagnostic scores are retained only for repair. They are not a public-quality
score and cannot be used for Feishu sync.

## Decision

Decision: not review-ready.

The new gate behavior is validated because it forces the article to expose
paragraph-level drift and judgment ownership gaps instead of assigning a false
numeric score.

## Residual Risks

- This replay reviewed one real article only. It does not prove every future
  public report will route correctly.
- The replay did not fetch Feishu linked pages or the Karpathy source link.
- The replay did not rewrite the draft, so it does not prove the repaired
  article would pass.
- Paragraph drift scores are manual reviewer judgments. They make the judgment
  auditable; they do not replace user confirmation.

## Verification Boundary

Verified:

- The new gate can be applied to an existing real draft.
- It produces Article Intent Contract, Section And Paragraph Drift Review, and
  Judgment Ledger evidence.
- It blocks review-ready status while preserving diagnostic drift scores.

Not verified:

- Feishu page readback.
- External source fidelity.
- Visual asset adequacy.
- A repaired article passing the gate.
