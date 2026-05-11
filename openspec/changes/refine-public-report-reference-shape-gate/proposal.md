## Why

The previous public-report article-flow gate captured a real failure, but its
wording was too close to one incident. It named specific bad layouts and one
article style instead of expressing the reusable rule: when a user or reference
selects an output shape, the agent must not silently replace that shape.

Hard rules in skills need to be observable and replayable. Subjective or
over-specific labels make future behavior harder to validate.

## What Changes

- Rename the core gate from article-flow-specific wording to a generic
  Reference Output Shape Gate.
- Require the gate review to record the selected output shape, retained
  patterns, rejected patterns, and any user-approved shape changes.
- Move incident-specific examples into pressure scenarios rather than the core
  skill rule.
- Treat production instructions, image prompts, tool notes, and Hybrid routing
  text in reader-facing content as leakage unless the selected output shape is
  explicitly an asset brief or production note.

## Impact

- A newspaper/article drift case still fails.
- Cards, grids, tables, dashboards, visual panels, and image prompts are not
  banned when the user asks for them or the reference uses them.
- Future skill replay can check objective signals: selected shape, primary
  structure replacement, explicit user approval, and reader-facing leakage.
