## Why

The current README is accurate, but it still reads like a structured repository guide instead of a product-like entrypoint. The user wants it to learn from the `NousResearch/hermes-agent` README, which is stronger at opening with a clear identity, showing the fastest install path, and giving a scan-friendly command and documentation index.

## What Changes

- Restructure the root README to follow a Hermes-like top-level flow: strong opening statement, quick install, getting started commands, quick reference tables, and documentation map.
- Keep the repository's Chinese-first bilingual policy by presenting Chinese and English in separate sections rather than mixed paragraphs.
- Update the bootstrap README template so initialized repositories inherit the same entrypoint structure instead of a smaller legacy template.

## Capabilities

### New Capabilities

- `readme-entry-layout`: Define the expected structure for a high-signal, Hermes-inspired repository entry README for this workflow kit.

### Modified Capabilities

- `ai-chat-workflow-installer`: Clarify the way the installer model is introduced from the repository root so runtime readers can move from README to deeper docs without ambiguity.

## Impact

- Affected docs: root `README.md` and bootstrap-generated README content.
- Affected install output: `scripts/bootstrap_assets/README.md.template`.
- No code-path or CLI behavior changes beyond the generated template text.
