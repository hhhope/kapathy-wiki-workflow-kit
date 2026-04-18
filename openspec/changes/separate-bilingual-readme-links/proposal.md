## Why

The current README still places Chinese and English introductory text together at the top, and several repository entrypoints are shown as code-style paths instead of obvious links. The user wants the bilingual sections fully separated and the navigational paths presented as hyperlinks.

## What Changes

- Separate Chinese and English README content so the opening block is no longer bilingual in one place.
- Convert repository navigation references in the root README and bootstrap README template from plain code-style paths to markdown links.
- Keep the Hermes-inspired high-signal layout, but tighten it so each language stands alone.

## Capabilities

### New Capabilities

- `bilingual-readme-separation`: Define the repository rule that bilingual README sections must be structurally separated and navigational entrypoints should be link-first.

### Modified Capabilities

- `readme-entry-layout`: Refine the root README layout so the top section and navigation tables are link-driven and language-separated.

## Impact

- Affected docs: root `README.md` and bootstrap-generated README content.
- No workflow, CLI, or runtime behavior changes beyond documentation structure.
