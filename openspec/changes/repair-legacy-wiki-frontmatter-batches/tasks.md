# Tasks

- [x] 1. Create OpenSpec change artifacts and define the legacy frontmatter
  repair boundary.
- [x] 2. Record baseline whole-wiki frontmatter precheck and first-batch planner
  output.
- [x] 3. Apply batch 1 to `wiki/adr/0001` through `wiki/adr/0010` using only
  approved frontmatter fields.
- [x] 4. Record before/after target precheck evidence for every batch 1 page.
- [x] 5. Record whole-wiki residual blocker count after batch 1.
- [x] 6. Review and apply batch 2 to `wiki/adr/0011` through `wiki/adr/0020`;
  preserve existing relation fields on pages that already had them.
- [x] 7. Review and apply batch 3 to `wiki/adr/0021` through `wiki/adr/0030`;
  preserve existing relation fields on partial-frontmatter pages.
- [ ] 8. Review the next planner batch and decide whether it is deterministic,
  needs manual approval, or should split into a follow-up change.
- [ ] 9. Re-run medical recovery/status only after verified frontmatter batches
  change the blocker state.
- [ ] 10. Add final evaluation evidence and run OpenSpec validation.
