## 1. Change Setup

- [x] 1.1 Confirm the target root files and alignment question
- [x] 1.2 Confirm that this step is SDD/design-only, not root dotfile or wiki
  method implementation
- [x] 1.3 Confirm this step does not edit root dotfiles, repo skills, or wiki
  method pages
- [x] 1.4 Record the RED baseline for premature implementation or wiki landing

## 2. Open Decisions

- [x] 2.1 Decide the final repo-vs-root governance alignment model
  <!-- D1 adopted 2026-05-06 — see evaluation.md §Archive-readiness Review Outcome -->
- [x] 2.2 Decide which layers must align and which may diverge
  <!-- D1 adopted 2026-05-06 — four-layer model in design.md L230–402 -->
- [x] 2.3 Decide file ownership and update responsibility
  <!-- D1 adopted 2026-05-06 — Pattern Catalog Owns / Must Not Own fields -->
- [x] 2.4 Decide the final root AGENTS / repo AGENTS / rules / skills /
  OpenSpec / harness / wiki governance-stack responsibility model
  <!-- D1 adopted 2026-05-06 — full stack in design.md §Pattern Catalog -->
- [x] 2.5 Decide whether a targeted wiki trace, retro, method page, or ADR is
  needed after review
  <!-- decided 2026-05-06 — trace already landed; retro/method/ADR deferred -->
- [x] 2.6 Decide whether harness Phase 1 should proceed as manual templates
  only
  <!-- decided 2026-05-06 — manual templates only; checker deferred to Phase 2 -->
- [x] 2.7 Decide claude-side symmetry scope (out of scope now, reopen after the
  Codex protocol is accepted)
  <!-- decided 2026-05-06 — confirmed out of scope; reopen post Codex adoption -->

## 3. Reviewable Design

- [x] 3.1 Rewrite `design.md` around confirmed boundaries, candidate design,
  open questions, and review criteria
- [x] 3.2 Mark the hybrid ownership split as a candidate pending review
- [x] 3.3 Define replay harness v1 as an evidence contract, not a runtime gate
- [x] 3.4 Expand the design framework to include rules, skills, OpenSpec,
  routing examples, durable knowledge layers, and harness proof boundaries
- [x] 3.5 Add quantified review criteria and a phased path for harness/template
  adoption
- [x] 3.6 Land the current learning in the existing wiki intake without
  promoting a method page or ADR
- [x] 3.7 Complete review and either adopt, revise, or reject the
  root/repo-aware governance model
  <!-- D1 adopted 2026-05-06 — see evaluation.md -->

## 3a. Codex Interaction Protocol

- [x] 3a.1 Record Codex source order and conflict adjudication as candidate in
  `design.md`
- [x] 3a.2 Record interaction protocol covering trigger, edit gate, decision
  record, and harness hook
- [x] 3a.3 Record intake issue routing table covering C1-C3 / S1-S5 / A1-A5 /
  M1-M5 and §5 open questions
- [x] 3a.4 Mark routing table entries as candidate pending review
- [x] 3a.5 Review each routing entry and either confirm, revise, or reject it
  <!-- confirmed 2026-05-06 — routing table adopted as-is; 18 rows remain executable by successor change -->

## 3b. Design Principles, Minimum Process, Self-Check

- [x] 3b.1 Record Design Principles in `design.md` (sources drawn from
  `Benchmark Signals` only)
- [x] 3b.2 Record Minimum Process for behavior-asset changes in `design.md`
- [x] 3b.3 Record Self-Check Checklist in `design.md`
- [x] 3b.4 Bind Self-Check Checklist to `spec.md` with a single requirement
  (first paragraph single-line)
- [x] 3b.5 Retract the three candidate-protocol requirements from `spec.md`;
  keep their content in `design.md`
- [x] 3b.6 Correct authority-vs-load-order wording in `Codex Source Order`
- [x] 3b.7 Publish design trace to `wiki/ops/` with ASCII diagrams for
  layer-domain map, authority-vs-load-order, and minimum-process rhythm
- [x] 3b.8 Review Design Principles list and either confirm, revise, or add
  entries
  <!-- confirmed 2026-05-06 — six principles adopted as-is -->
- [x] 3b.9 Review Self-Check Checklist and mark unused items for removal
  <!-- confirmed 2026-05-06 — all four panels kept; none marked for removal -->
- [x] 3b.10 Record Candidate Pattern Catalog (seven pattern types with five
  fields each) in `design.md`; bind a spec requirement for field declaration
- [x] 3b.11 Propose `design-trace` as a `wiki/ops` artifact_type value in
  `design.md`; align wiki trace title, artifact_type, and filename
- [x] 3b.12 Record seven Pattern Skeleton Examples in `design.md`, one
  minimal markdown shape per pattern type
- [x] 3b.13 Tag Benchmark Signals by verification class (A / B / C) and
  re-anchor principles 1, 3, and 5 on class A or B sources only
- [x] 3b.14 Update Quantified Review Criteria to list the design trace as
  an allowed touched file
- [x] 3b.15 Review Candidate Pattern Catalog and decide whether to promote
  the field-declaration requirement in `spec.md` from SHOULD to SHALL; if
  SHALL, update `spec.md` accordingly and close this task
  <!-- D2 decided 2026-05-06 — keep SHOULD; promotion deferred until three real pattern additions; spec.md unchanged -->
- [x] 3b.16 Review Interaction Protocol §1 (skill rule-preamble) and decide
  whether `rules/` preamble becomes a required Skill pattern field or stays
  opt-in; record the decision in `design.md`
  <!-- D3 decided 2026-05-06 — stays opt-in; required would retroactively invalidate 70 existing SKILL.md files -->
- [x] 3b.17 Review renamed routing class `candidate-root-edit` and confirm
  every row still reads correctly under the new name
  <!-- confirmed 2026-05-06 — name preserved; rows read correctly -->

## 4. Optional Minimum Sync

- [x] 4.1 If alignment requires edits, apply only the minimum root-level changes
  <!-- not applicable 2026-05-06 — this change performs 0 root-level edits per design.md Quantified Review Criteria -->
- [x] 4.2 Verify the reviewed repo-vs-root relationship is visible in durable
  artifacts
  <!-- verified 2026-05-06 — visible in design.md, spec.md, evaluation.md, trace, zh companion -->

## 5. Evaluation

- [x] 5.1 Record the previous drift/deferral state
- [x] 5.2 Record the candidate design and SDD gate
- [x] 5.3 Record residual risks while final decisions remain open
- [x] 5.4 Record the RED/GREEN result for missing wiki landing, unclear harness
  shape, and missing quantified review criteria
- [x] 5.5 Complete archive-readiness review against `design.md` §Archive
  Readiness Criteria; record the outcome in `evaluation.md`
  <!-- PASS 2026-05-06 — see evaluation.md §Archive-readiness Review Outcome -->
