# Proposal: initialize LLM-WIKI seed repo

## Summary

Create a reproducible migration path for initializing `hhhope/LLM-WIKI` as a
runnable seed repository based on the current repo's real LLM-Wiki runtime
surface.

## Problem

The current repository has grown a working LLM-Wiki system: repo-local skills,
wiki frontmatter configuration, status / graph / scorecard scripts, output
gates, learning capture, and a medical-loop maintenance model. The new
`hhhope/LLM-WIKI` repository should start from that system.

A full copy of this repository would leak history and private project material.
A generic starter kit would lose the real `wiki-*`, learning, public-output,
OpenSpec, and medical-loop surface. The repository needs a seed migration path
that copies the system, not the history.

## Scope

In scope:

- Add a manifest-driven seed builder for the LLM-WIKI seed repository.
- Preserve the real `.codex/skills/` wiki runtime, learning, output-gate,
  OpenSpec, and medical-loop skill surface.
- Copy required `wiki/config/` files and minimal runtime scripts.
- Generate sanitized seed wiki pages and required runtime directories.
- Add a seed verifier.
- Generate the local target repository and run minimal structural/runtime
  verification.
- Defer final README copywriting until after migration and verification.

Out of scope:

- Full productized CLI such as `llm-wiki init/ingest/query/lint`.
- Full archive migration from `openspec/changes/archive`.
- Private inbox, logs, report bundles, private meeting material, or historical
  medical-loop records.
- Replacing the real skill surface with generic `ingest`, `query`, `lint`, or
  `medical-agent` placeholders.
- Pushing the external repository without explicit user approval.

## Success Criteria

- The current repo has tests covering the seed manifest and builder.
- The builder can generate a seed tree under `/tmp` and the target checkout.
- The verifier passes on the generated seed.
- The target seed preserves required skill, config, script, and wiki layer
  paths.
- Minimal verification commands for taxonomy, status, graph, scorecard, and
  medical-loop preview either pass or produce bounded seed-safe fixes.
- Current-repo tooling changes and target-repo seed changes are committed
  separately.
