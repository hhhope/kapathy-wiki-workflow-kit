# Solidify Go Rule Official Sources

## Why

The Go rule now avoids duplicating generic policy, but its evidence trail needs
to include official/GitHub Go best-practice sources instead of relying only on
article-derived learning. The user also confirmed that the relevant large-file
threshold should be the existing global Go/Rust/Java `>300` guardrail, not a
looser 500-line candidate.

## What Changes

- Preserve official/GitHub Go best-practice source evidence in the existing Go
  source-learning page.
- Keep the large-file threshold owned by global guardrails and record the
  current `>300` Go/Rust/Java threshold as referenced evidence.
- Add Go-specific official-source guidance for context propagation, interface
  placement, module layout, and project-layout caution.
- Add tests so the rule cannot drift back to article-only evidence or local
  generic thresholds.

## Out Of Scope

- Editing global `~/.codex/AGENTS.md`; it already owns the `>300` threshold.
- Copying full upstream style guides.
- Replacing the user-confirmed Gin/GORM/Redis stack.
