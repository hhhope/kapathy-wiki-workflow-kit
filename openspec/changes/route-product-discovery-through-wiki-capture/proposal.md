# route-product-discovery-through-wiki-capture

## Why

PM/product-discovery plugin output can produce reusable market, customer,
opportunity, assumption, and experiment judgments. Today that output can remain
only in chat even when the user expects repository memory.

The observed incident was a `$pm-product-discovery` analysis of AI Agent
subscription payments. The analysis identified opportunity framing and
validation steps, but did not create a repo-visible wiki record. The user then
flagged that the skill should record wiki output and asked to remodel the
workflow.

## What Changes

- Add a repo-local product-discovery wiki-capture route for PM/product-discovery
  analysis that has explicit wiki, reuse, follow-up, or durable-memory intent.
- Preserve `learning-capture` ownership for external source learning and avoid
  treating every PM/product-discovery answer as durable wiki material.
- Add compact skill guidance for product-discovery wiki capture.
- Add behavior replay and prior-art evidence for the new routing behavior.
- Add focused tests for the positive route, negative one-off route, and parent
  gate preservation.

## Out of Scope

- Editing external plugin cache files such as `$pm-product-discovery`.
- Turning all PM analysis into wiki output.
- Creating a full PM research knowledge system.
- Publishing reader-facing reports or H5 artifacts.
- Validating the AI Agent payments market thesis itself beyond the captured
  discovery note.
