# Design: visual-agent entry route hardening

## Entry Marker

`visual-agent` remains the controller. The hardening adds an observable marker:
normal visual-routing responses must start the routing block with
`Using visual-agent`. This gives future review a simple way to detect whether a
request bypassed the controller.

## Parent / Child Route

Visual production can still use child workers, but the route must be described
as a chain:

- `public-report-quality-gate -> visual-agent -> knowledge-article-visual`
- `public-report-quality-gate -> visual-agent -> infographic-onepager`
- `visual-agent -> svg-flow-diagram`
- `visual-agent -> architecture-diagram`
- `visual-agent -> imagegen`

The child worker owns its narrow execution step. It does not own the initial
mode decision unless `visual-agent` has already selected or confirmed the mode.

## Ambiguous Mode Handling

For ambiguous visual requests, the controller must not default to H5/HTML or
SVG simply because those are deterministic and easy to render. It must either:

- ask the bounded mode fork; or
- state the strong content evidence that selects a mode.

If the user mentions prior H5/SVG dissatisfaction, direct image terms, or
image-model quality, image-model or hybrid is the default route pressure until
the user explicitly chooses deterministic SVG/H5.

## Public Report Gate Alignment

`public-report-quality-gate` remains the outer parent for reader-facing
artifacts, but visual production delegation must go through `visual-agent`
before child visual workers. This keeps Article Intent, Visual Gate, Judgment
Ownership, and Publish Gate intact while still preserving the controller's
output-mode fork.
