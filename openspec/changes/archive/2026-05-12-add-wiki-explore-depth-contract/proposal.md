## Why

The repository has bounded wiki retrieval through `wiki-query` and an
OpenSpec-oriented explore stance through `openspec-explore`, but it does not
have a dedicated `wiki:explore` behavior contract.

That gap showed up in the agentic product-engineering collaboration thread. The
user repeatedly said the exploration was "not enough" until the work reached a
deeper evidence surface: source map, broad scan, public timeline,
podcast/video pool, article evidence matrix, gate review, residual risks, and a
clear "enough for internal discussion, not enough for public publication"
boundary.

The desired behavior is not to continue hardening that source set now. It is to
make future `wiki:explore` invocations start at a comparable exploration
standard instead of waiting for repeated user correction.

## What Changes

- Add a repo-local `wiki-explore` skill with an explicit trigger for
  `wiki:explore`.
- Add a behavior gate reference that defines required output sections:
  current object, opened evidence, evidence surface, enoughness judgment, and
  next boundary.
- Add a command contract at
  `plugins/report-wiki-portfolio/commands/wiki-explore.md`.
- Add OpenSpec coverage for the `wiki-explore` command/skill and update the
  runtime skill surface.
- Add RED/GREEN replay evidence using the
  `agentic-product-engineering-collaboration` thread as the GREEN standard.

## Impact

- Creates `.codex/skills/wiki-explore/`.
- Creates `plugins/report-wiki-portfolio/commands/wiki-explore.md`.
- Updates `README.md` wiki skill list.
- Adds OpenSpec coverage.
- Does not modify `wiki-query`; it remains bounded retrieval.
- Does not continue public-source hardening for the agentic collaboration
  article.
