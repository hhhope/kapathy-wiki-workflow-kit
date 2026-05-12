# Evaluation

## Pressure Scenarios

1. A future agent applies an OpenSpec change and wants a Superpowers plan for
   TDD, commit slicing, and subagent strategy.
2. The plan is useful for execution, but must not become a second progress
   ledger beside `tasks.md`.
3. The agent resumes after interruption and needs to know whether to trust
   `tasks.md` or the Superpowers plan for completion state.

## RED Baseline

The real `add-product-status-contract` implementation plan contained the drift
signals this change is meant to prevent:

```text
openspec/changes/add-product-status-contract/implementation-plan.md:32:## Task 1: RED Tests For Product Status Contract
openspec/changes/add-product-status-contract/implementation-plan.md:37:- [ ] **Step 1: Add contract skeleton RED test**
openspec/changes/add-product-status-contract/implementation-plan.md:135:## Task 2: RED Tests For Unresolved Items And Markdown
openspec/changes/add-product-status-contract/implementation-plan.md:221:## Task 3: Product Status Computation Module
openspec/changes/add-product-status-contract/implementation-plan.md:415:## Task 6: OpenSpec Task Sync And Final Verification
openspec/changes/add-product-status-contract/implementation-plan.md:442:- [ ] **Step 4: Update OpenSpec tasks with verification notes**
openspec/changes/add-product-status-contract/implementation-plan.md:449:git add openspec/changes/add-product-status-contract/tasks.md
```

The prior `openspec-apply-change` skill had no guidance for execution overlays:

```text
rg "tasks.md is the only progress|execution overlay|Task [0-9]|\\- \\[ \\]" .codex/skills/openspec-apply-change/SKILL.md
# no matches
```

## GREEN Result

The skill now states:

- `tasks.md` remains the only progress and completion ledger.
- Execution overlays must not define independent task ids.
- Execution overlays must not use progress checkboxes.
- Commit slices are recovery evidence, not OpenSpec task completion.
- `tasks.md` is updated when an OpenSpec task completion boundary is verified.

The linked reference provides a real good overlay for
`add-product-status-contract` using strategy sections instead of `Task 1..6`.

Expected replay for a future agent:

1. User asks to use Superpowers planning while applying an OpenSpec change.
2. Agent loads `openspec-apply-change`.
3. Agent may create or use an execution overlay.
4. Overlay contains authority, TDD, module, commit, verification, and handoff
   sections.
5. Overlay contains no independent task ids or progress checkboxes.
6. `tasks.md` remains the only completion ledger.

## Residual Risks

- This is documentation-level behavior proof, not multi-session rollout
  telemetry.
- A future agent may still ignore the skill if it is not triggered or loaded.
- The rule does not decide whether every change needs an overlay; it only
  constrains overlays when one is used.
- The rule does not replace archive review or completion-bridge summaries.
