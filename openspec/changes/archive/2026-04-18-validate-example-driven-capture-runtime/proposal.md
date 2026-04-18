## Why

The repository has already formalized `example-driven wiki capture` and archived that change.

But the archived change was validated only at the rule and artifact level:

- repo guidance exists
- wiki pages exist
- OpenSpec specs exist

It did not include a fresh runtime replay that demonstrates the new behavior in action:

- user provides an example or external source
- no extra reminder says `write this to wiki`
- the agent still creates the wiki record in the same turn

That gap matters because this workflow change is about agent behavior, not just static documentation. The user explicitly challenged the closure standard and asked for the missing replay validation.

## What Changes

- Add a follow-up validation change for `example-driven wiki capture`
- Record a concrete `RED/GREEN` replay
- Store the runtime validation result as a repo-visible `wiki/ops` page
- Record evaluation and verification evidence inside the change directory
- Add a narrow spec delta that requires repo-visible replay evidence when validating this behavior

## Capabilities

### Modified Capabilities

- `example-driven-wiki-capture`

## Impact

- Adds a validation-only OpenSpec change under `openspec/changes/validate-example-driven-capture-runtime/`
- Produces a concrete replay artifact that shows the workflow behaved as intended
- Raises confidence in the already-published repository-default behavior
