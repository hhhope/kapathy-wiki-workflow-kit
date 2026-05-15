# Tasks

- [x] 1. Create OpenSpec proposal, design, tasks, spec delta, drift trace, Superpowers repair artifacts, and initial evaluation evidence.
- [x] 2. Add RED replay/test showing separate surgery output can drift from confirmed decisions.
- [x] 3. Implement a case-file builder or updater under `wiki/ops/wiki-medical-cases/`.
- [x] 4. Add case-file source wiring for surgery planning.
- [x] 5. Preserve generated stage records as evidence attachments.
- [x] 6. Add verification that surgery derives from confirmed case decisions.
- [x] 7. Update relevant skills only after behavior replay evidence exists. No skill update was required for this implementation.
- [x] 8. Run focused tests, frontmatter precheck for new case pages, OpenSpec validation, and behavior-asset checks if skills change.
- [x] 9. Commit verified implementation and stop at the OpenSpec hard stop.
- [x] 10. Repair missed intent judgment in `.codex/skills/wiki-confirm/SKILL.md` and `.codex/skills/wiki-surgery/SKILL.md`: confirm now creates a case file, and surgery now routes through an existing case file before raw adjudication.
- [x] 11. Repair confirm-to-case self-contamination: confirmation records now carry machine decision data, case generation loads that data instead of rescanning, and adjudication excludes generated medical case files.
