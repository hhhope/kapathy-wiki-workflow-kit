## 1. Spec And Baseline

- [x] 1.1 Add OpenSpec requirements for execution-overlay authority boundaries.
- [x] 1.2 Record RED baseline from the real `add-product-status-contract`
      `implementation-plan.md`.

## 2. Skill Update

- [x] 2.1 Update `.codex/skills/openspec-apply-change/SKILL.md` with compact
      execution-overlay hard rules.
- [x] 2.2 Add a linked real example showing bad task-ledger drift and good
      overlay shape.

## 3. Replay And Verification

- [x] 3.1 Record GREEN replay evidence in `evaluation.md`.
- [x] 3.2 Run focused text checks for forbidden overlay patterns.
- [x] 3.3 Run OpenSpec strict validation.
- [x] 3.4 Run graph identity check for new repo-visible artifacts.
- [x] 3.5 Inspect git status and commit only task-related files.

<!-- Evidence: old add-product-status-contract implementation-plan.md matched drift patterns; Good Shape overlay section matched no independent task headings or progress checkboxes; openspec validate clarify-openspec-superpowers-overlay --strict passed; graph identity focused test passed. -->
<!-- Evidence: git status inspected before commit; staged only .codex/skills/openspec-apply-change and openspec/changes/clarify-openspec-superpowers-overlay files. -->
