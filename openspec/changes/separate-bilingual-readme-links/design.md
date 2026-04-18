## Context

The Hermes-inspired README restyle improved scanability, but two issues remain:

- the title block still contains Chinese and English sentences together
- several internal navigation targets are presented as code or text rather than hyperlinks

The repository language policy already requires Chinese-first with separate English sections. This change finishes that cleanup without changing behavior.

## Goals / Non-Goals

**Goals:**
- Ensure the root README has a Chinese-only opening block before the English section begins.
- Prefer markdown hyperlinks for repository entrypoints and documentation references.
- Mirror the same separation in the bootstrap README template.

**Non-Goals:**
- Rework the overall Hermes-inspired structure again.
- Change CLI commands into hyperlinks.
- Modify any runtime or verification logic.

## Decisions

### 1. Keep only the project title above both language blocks

The README will keep only the repository title before the Chinese section. English descriptive prose moves fully into `## English Guide`.

### 2. Use link-first navigation for repo entrypoints

Repository files and documentation pages in overview sections, quick reference tables, and documentation tables should use markdown links where practical. Command examples remain fenced code blocks.

### 3. Apply the same structure to the bootstrap template

The generated README must inherit the same language separation and link style so new repositories do not regress immediately.

## Risks / Trade-offs

- [Too many links reduce readability] → Keep command examples as code blocks and reserve links for navigation paths.
- [Template and root README drift again] → Update both in the same change and keep the bootstrap test asserting the shape.

## Migration Plan

1. Update the root README.
2. Update the bootstrap README template.
3. Re-run the bootstrap README test.

## Open Questions

- None.
