## Context

The previous README work improved installation guidance but still failed the user's intended reading experience. The desired model is closer to `larksuite/cli`:

- language switching is handled through explicit links near the top
- each language has its own full document body
- the top of the README is optimized for scanning and navigation

The repository language policy still applies: Chinese remains the primary language for the root document, while English is provided as a separate companion file rather than mixed into the same reading flow.

## Goals / Non-Goals

**Goals:**
- Make `README.md` Chinese-only and `README.en.md` English-only.
- Add top-level language switch links in both files.
- Use a `larksuite/cli`-style section order: install, quick start, runtime, documentation, source note.
- Keep repository navigation targets link-first.
- Ensure bootstrap output matches the repository README structure.

**Non-Goals:**
- Copy `larksuite/cli` wording or claim feature parity.
- Change workflow logic, OpenSpec behavior, or verification rules.
- Add new runtime adapters beyond documenting existing boundaries.

## Decisions

### 1. Root README stays Chinese-first and standalone

`README.md` will contain only the Chinese body plus the shared language switch line.

### 2. English content moves into `README.en.md`

The English README mirrors the same high-level structure but remains a separate file. This avoids stacked bilingual reading and aligns with the user's explicit requirement.

### 3. Top navigation uses section links plus repository hyperlinks

Each README will include:

- a language switch line
- a short one-line positioning statement
- section navigation links near the top

Repository entrypoints inside the body stay as markdown links. Shell commands remain code blocks.

### 4. Bootstrap output must generate both README files

The bootstrap template layer becomes the source for generated `README.md` and `README.en.md`, so new repositories inherit the same language split and navigation structure.

## Risks / Trade-offs

- [Docs drift between Chinese and English files] → Keep the section shape parallel and test that both files are emitted by bootstrap.
- [Too many links reduce readability] → Use links for navigation targets and keep commands in code blocks.
- [User intent drifts again] → Anchor the structure explicitly to the `larksuite/cli` reference pattern rather than the earlier Hermes-inspired layout.

## Migration Plan

1. Replace the root README with the new Chinese-only structure.
2. Add `README.en.md`.
3. Update bootstrap templates and generation.
4. Update bootstrap tests and verify the generated output.

## Open Questions

- None.
