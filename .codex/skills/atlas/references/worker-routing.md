# Worker Routing

Atlas routes work after the Continuation State Gate. It does not replace worker
skills.

## Routing Rules

- Atlas runs first for stateful learning/report continuation.
- The state block defines allowed actions and blocked actions.
- Worker skills must preserve relevant confirmed anchors.
- Worker skills must not expand Atlas scope.
- Worker blocker routes back to Atlas for re-anchor.

## Ownership Map

| Need | Route | Atlas boundary |
|---|---|---|
| Source role, learning level, evidence strength, source queue, output-use handoff | `learning-capture` | Atlas states what claim needs evidence and what action is blocked. |
| Reader-facing intent, output shape, report quality, judgment ownership, review/publish readiness | `public-report-quality-gate` | Atlas states confirmed structure, user-owned judgment, and completion gate. |
| Visual mode, visual task classification, visual proof binding, visual verification | `visual-agent` | Atlas states visual anchors and whether per-section visual compression is blocked. |
| Dropped materials, source-first wiki output, incremental material processing | `material-collaboration-defaults` | Atlas runs first only when the material work has confirmed anchors or drift history. |

## Worker Blocker Return

When a worker cannot preserve Atlas state, return:

```text
worker blocker -> Atlas re-anchor -> user confirmation or narrowed next output
```

The blocker should name:

- affected confirmed anchor
- evidence or visual gap
- blocked action
- smallest next decision

## Anti-Patterns

- Sending a stateful report directly to `visual-agent` because the next output
  is H5.
- Sending a weak organization claim directly to drafting instead of
  `learning-capture`.
- Letting `public-report-quality-gate` rewrite confirmed section names as a
  cleaner template.
- Treating material intake as enough when the user is actually continuing a
  confirmed report/H5 collaboration.
