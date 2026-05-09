## 1. Change Setup

- [x] 1.1 Create OpenSpec proposal, design, spec delta, tasks, and evaluation artifacts.
  <!-- 2026-05-09 — created constrain-feishu-image-delivery artifacts and public-report-quality-gate spec delta -->
- [x] 1.2 Record RED baseline before changing skill behavior.
  <!-- 2026-05-09 — evaluation.md records missing text-only default, broad Feishu sync ambiguity, image-token usability overclaim, and missing client-freeze replay -->

## 2. Skill And References

- [x] 2.1 Update `public-report-quality-gate` hard rules for local visual assets versus Feishu image insertion.
  <!-- 2026-05-09 — SKILL.md now defaults generated visuals to local assets and separates Feishu image insertion from text sync -->
- [x] 2.2 Update gate-review artifact guidance for text-only Feishu sync and local asset paths.
  <!-- 2026-05-09 — gate-review-artifact.md adds Visual Asset Boundary and text-only default when local images exist -->
- [x] 2.3 Add pressure scenarios for manual image insertion, explicit image-insert approval, and client-freeze read-back boundaries.
  <!-- 2026-05-09 — pressure-scenarios.md adds Feishu Image Delivery Replay -->

## 3. Evaluation

- [x] 3.1 Record GREEN result for the new image-delivery boundary.
  <!-- 2026-05-09 — evaluation.md records PASS for manual-image route, explicit image-insert approval, audit-only read-back, and client-freeze stop -->
- [x] 3.2 Verify skill body remains compact.
  <!-- 2026-05-09 — wc -l shows SKILL.md 89 lines; heavier scenarios remain in references -->
- [x] 3.3 Run static checks for required wording.
  <!-- 2026-05-09 — rg found local assets, text-only, client-freeze, image-token, Visual Asset Boundary, and Feishu Image Delivery Replay wording -->
- [x] 3.4 Run `openspec validate constrain-feishu-image-delivery --strict`.
  <!-- 2026-05-09 — passed: Change 'constrain-feishu-image-delivery' is valid; PostHog DNS flush errors ignored -->
- [x] 3.5 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git status remains dirty with task-related skill/OpenSpec files plus unrelated local material; latest commit 1b5d328 docs: trace Feishu image freeze explore -->
- [ ] 3.6 Record fresh runtime replay evidence that the public-report gate chooses local visual assets plus text-only Feishu sync when the user says images will be added manually.

## 4. Stop Boundary

- [ ] 4.1 Stop after skill/reference/spec evidence and runtime replay evidence are complete.
  <!-- 2026-05-09 — reopened after user challenge: static skill/spec evidence is not enough to claim runtime behavior is complete -->
- [x] 4.2 Do not modify Feishu documents or generate additional images in this change.
  <!-- 2026-05-09 — no Feishu calls or image generation performed -->
