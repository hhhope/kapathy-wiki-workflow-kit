## Why

The current repository README still follows an older bilingual layout that places Chinese and English content in one file. The user wants the repository to follow the `larksuite/cli` README pattern instead: language switching should happen through links, the Chinese and English bodies should live in separate files, and the root README should work as a clearer navigation surface.

## What Changes

- Replace the root README with a Chinese-only document that links to a separate English README.
- Add `README.en.md` as the English-only companion document.
- Update bootstrap assets and bootstrap generation so initialized repositories get both README files.
- Update bootstrap tests to verify the split-language structure and link-first navigation style.

## Capabilities

### New Capabilities

- `split-readme-language-switch`: Define the repository rule that language switching happens through linked README files rather than stacked bilingual content.

### Modified Capabilities

- `readme-entry-layout`: Refine the README entry structure to align with the `larksuite/cli` style of language links, section navigation, and quick-start flow.

## Impact

- Affected docs: root `README.md`, new `README.en.md`, and bootstrap-generated README content.
- Affected tooling: bootstrap generation and bootstrap README tests.
- No runtime behavior changes outside repository entry documentation generation.
