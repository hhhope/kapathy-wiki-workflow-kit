# Design: visual image mode ownership

## Failure Shape

The failing request shape is:

- source artifact: existing H5/report/content
- reference artifact: PNG image or image-like visual
- requested output: "make a similar image" or equivalent
- no explicit user choice of `H5/HTML`, `SVG`, `Image model`, or `Hybrid`

The bad route is:

`visual-agent -> deterministic HTML/CSS renderer -> screenshot PNG`

when the user did not choose deterministic rendering.

## Correct Route

The controller must classify this as image-mode pressure:

- expose `Using visual-agent`;
- set `Output Mode` to `mode_fork` or `pending`;
- ask or confirm the four-mode fork;
- state Chinese text accuracy as a tradeoff, not as a reason to pick
  deterministic rendering;
- block HTML/CSS/SVG/browser screenshot work until the user chooses it.

If the user explicitly chooses deterministic output later, HTML/CSS/SVG may be
used as an image renderer, but the response must say that it is deterministic
rendering and not image-model generation.

## Skill Boundary

This is a controller hard rule. Child workers such as `infographic-onepager`
remain execution routes after mode selection. They do not get to infer the
mode from Chinese text accuracy when the controller has not confirmed it.

## Verification

- Text scan for the new rule in `.codex/skills/visual-agent/SKILL.md`.
- Evaluation evidence with RED/GREEN replay.
- OpenSpec strict validation.
- `git diff --check`.
