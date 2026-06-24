# Enforce visual image delivery boundary

## Why

The visual-agent controller now protects image-like reference requests from
silent HTML/SVG fallback, but two drift paths remain:

1. Reference images can still contaminate the content source. ADR-0035 already
   decides that reference images used for style are not semantic content
   sources, but the runtime skill does not yet enforce that source-role map.
2. In Codex CLI, built-in `Generated Image` artifacts can be visible in chat
   while no repo-local PNG path is exposed. Without a valid Images API key or
   artifact export path, the agent must not promise "generated files"; it should
   produce client-mode prompt markdown instead.

## What Changes

- Add a source-role boundary to `visual-agent` for reference-image-driven
  visual work: content source, style source, executor, route, and verification.
- Add an image delivery capability boundary before promising repo-local image
  files.
- Add OpenSpec scenarios and behavior-proof evaluation for:
  - reference image as style source only,
  - Codex CLI artifact-without-file fallback to prompt markdown,
  - valid local/API delivery when capability exists.

## Non-Goals

- No generated images.
- No Feishu sync or image insertion.
- No Codex CLI or OpenAI API implementation changes.
- No broad cleanup of unrelated visual workers.
- No new negative-prompt vocabulary list for historical contaminants.

## Impact

Future image-model visual work that uses reference images must state source
roles before prompting or generation. Future Codex CLI runs that cannot obtain
a repo-local image file must deliver prompt markdown/client-mode instructions
instead of claiming file generation.
