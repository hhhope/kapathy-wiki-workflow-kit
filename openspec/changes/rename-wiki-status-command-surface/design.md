# Design: rename wiki status command surface

## Problem

The repository has a wiki status capability, but the user-facing invocation
surface is ambiguous:

- product-shaped name: `/wiki:status`
- package/plugin-shaped name: `/report-wiki-portfolio:wiki-status`

The trace suggests `/wiki:status` is clearer for users because it matches the
product/capability namespace. However, command exposure may be constrained by
the runtime packaging model. The implementation must verify the command system
instead of assuming that a short alias is possible.

## Proposed Model

Treat command naming as two layers:

- `capability_name`: stable repo concept, `wiki-status`.
- `invocation_surface`: runtime command or alias exposed to the user.

The preferred invocation is `/wiki:status` when the local runtime can support
it. If the runtime only supports package-prefixed names, the implementation
should preserve `/report-wiki-portfolio:wiki-status` and record the reason.

## Verification Strategy

Implementation should verify:

- current command/package files that expose wiki status;
- whether aliases or shorter command names are supported locally;
- the command still resolves to the same status-only behavior;
- no command shape implies apply, repair, graph, query, or archive behavior.

## Boundaries

- This change is about naming and routing only.
- It must not alter generated status content or product status semantics.
- It must not weaken `wiki-status-skill` boundaries.
- If runtime support is unclear, stop at documented decision evidence rather
  than guessing.
