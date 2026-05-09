## 1. Restart And Baseline

- [x] 1.1 Re-check project health, git state, and latest commit before relying on prior context.
  <!-- 2026-05-08 — PROJECT.md found; logs unreviewed count 0; git status dirty with unrelated local material; latest commit ea56653 docs: record account wiki publish readiness -->
- [x] 1.2 Confirm prior relevant OpenSpec changes are complete and cannot be extended.
  <!-- 2026-05-08 — openspec list shows add-public-report-quality-gate, connect-learning-capture-to-output-gates, and route-complex-public-reports-to-reviewer all Complete -->
- [x] 1.3 Record local draft and visual baseline.
  <!-- 2026-05-08 — runtime and validation/cases local pages exist but are thin; account-wiki-visuals.html lacks dedicated runtime and validation/cases visuals; 14.png-17.png found at /mnt/c/Users/yan/Desktop/1 and read as horizontal hand-drawn teaching cards -->

## 2. Repair Local Drafts

- [x] 2.1 Rewrite `wiki/reports/team-knowledge-base-runtime.md` around a concrete material journey.
  <!-- 2026-05-08 — runtime page now covers Wiki structure, skills, agent/reviewer roles, material flow, public-draft gate chain, and runtime boundaries -->
- [x] 2.2 Rewrite `wiki/reports/team-knowledge-base-validation-cases.md` with concrete replay, failed-freeze, Feishu readback, visual gate, and skill RED/GREEN evidence.
  <!-- 2026-05-08 — validation page now uses case/data tables: 92/100->INVALID, update/read-back log ids, read-back length 12818, RED/GREEN counts, and 14-17 image dimensions -->
- [x] 2.3 Preserve reader-facing voice and non-claim boundaries in both pages.
  <!-- 2026-05-08 — static rg confirms runtime boundaries and validation proof-boundary sections are present -->

## 3. Repair Visuals

- [x] 3.1 Generate a runtime horizontal teaching-card image through the image model.
  <!-- 2026-05-08 — generated and archived wiki/reports/assets/account-wiki-runtime-card.png -->
- [x] 3.2 Generate a validation/cases horizontal teaching-card image through the image model.
  <!-- 2026-05-08 — generated and archived wiki/reports/assets/account-wiki-validation-card.png -->
- [x] 3.3 Verify generated images exist and match the chapter-card direction.
  <!-- 2026-05-08 — file reports runtime 1672x941 RGB and validation 1671x941 RGB; both are horizontal teaching cards -->

## 4. Skill Gap

- [x] 4.1 Record RED baseline for `infographic-onepager` against the failed Account Wiki multi-page scenario.
  <!-- 2026-05-08 — evaluation.md records old skill bias toward six-section vertical onepager and missing horizontal chapter-card route -->
- [x] 4.2 Patch the selected `infographic-onepager` skill only after the RED baseline is recorded.
  <!-- 2026-05-08 — /home/yan/.codex/skills/infographic-onepager/SKILL.md now routes 横图 / 章节配图 / 信息不多 / 不需要一图流 to horizontal teaching cards -->
- [x] 4.3 Record GREEN result showing runtime and validation/cases visual jobs are preserved separately.
  <!-- 2026-05-08 — evaluation.md records GREEN route: runtime keeps source->route->asset->output->writeback, validation keeps claim->evidence->replay->gate->boundary -->

## 5. Gate Review And Verification

- [x] 5.1 Update `wiki/ops/team-knowledge-base-overview-report-gate-review.md` with the local repair decision and proof boundary.
  <!-- 2026-05-08 — appended Runtime And Validation Local Repair section; Feishu remains blocked for this repair round -->
- [x] 5.2 Fix the Feishu write skill chain and confirmation fork.
  <!-- 2026-05-08 — public-report-quality-gate now requires user confirmation at image/H5 and Feishu-write forks, routes Feishu writes through lark-doc, and requires read-back -->
- [x] 5.3 Write runtime and validation/cases repairs back to Feishu after explicit user approval.
  <!-- 2026-05-09 — gate-review records runtime/validation Feishu update, media insert, and read-back logs; post-sync user observation says image-bearing docs can freeze Codex and Feishu clients, so no further image-included Feishu sync is allowed in this change -->
- [x] 5.4 Run static checks for required evidence headings and visual sections.
  <!-- 2026-05-09 — rg checks passed for runtime structure/skill/reviewer/gate/replay terms, validation 92/100->INVALID/read-back/RED-GREEN/image-dimension markers, and local image asset references -->
- [x] 5.5 Run `openspec validate repair-account-wiki-public-drafts --strict`.
  <!-- 2026-05-09 — passed: Change 'repair-account-wiki-public-drafts' is valid; PostHog DNS flush errors ignored -->
- [x] 5.6 Verify git status/log before any commit or completion claim.
  <!-- 2026-05-09 — git status remains dirty with task-related repair files plus unrelated local material; latest commit 11e0123 docs: repair account wiki runtime validation drafts -->

## 6. Stop Boundary

- [x] 6.1 Stop after local drafts, skill evidence, gate review, Feishu read-back, and validation pass.
  <!-- 2026-05-09 — stop boundary reached with image-bearing Feishu docs downgraded to audit evidence only because client freeze was reported -->
- [x] 6.2 Do not perform further Feishu sync or publishing work without a new explicit user approval.
  <!-- 2026-05-09 — no further image-included Feishu writes in this change; future route must be text-only, local asset link, or separately approved client-safe image workflow -->
