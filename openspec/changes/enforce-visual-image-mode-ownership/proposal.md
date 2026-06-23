# Enforce visual image mode ownership

## Why

The visual-agent controller still allowed a drift path: when a user provided a
PNG reference and asked for a similar image, the agent could treat Chinese text
accuracy as "strong content evidence" and silently choose deterministic
HTML/CSS screenshot output.

That violates the mode-ownership contract. A reference PNG, image-like target,
poster-quality request, or "similar image" request is image-mode pressure, not
permission to replace the output with HTML/SVG/screenshots.

## What Changes

- Add an explicit visual-agent hard rule for image-reference and
  image-like-output requests.
- Add a spec scenario requiring the mode fork instead of deterministic fallback.
- Add behavior replay evidence for the exact failure shape.

## Non-Goals

- No Stripe H5 content changes.
- No generated image output.
- No Feishu sync or image insertion.
- No changes to unrelated visual workers.

## Impact

Future visual requests that use a reference PNG or ask for a similar image must
ask or confirm `Image model` / `Hybrid` / deterministic alternatives before any
file generation. Chinese text reliability can be stated as a tradeoff, but it
cannot be used as a silent override.
