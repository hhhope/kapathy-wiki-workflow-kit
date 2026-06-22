# Java Rules Manual Check

## Scope

Traceable verification evidence for adding Java backend rules to `codex-integration-kit`.

## Expectations

1. The kit exposes Java backend rules in `rules/java/patterns.md` and `rules/java/security.md`.
2. The Java rules mirror the Python rule style: scope, boundaries, defaults, and explicit do-not-do guidance.
3. The Java patterns document includes request-string trimming guidance and length validation requirements for interface inputs.
4. Kit entrypoints mention the Java rules so an installed repository can discover them.
5. The Feishu-facing share source mentions the Java rules in the standing rule inventory.

## Manual Verification

- Verified `rules/java/patterns.md` contains boundary rules for Bean Validation, DTO normalization, default string trimming, and request length limits.
- Verified `rules/java/security.md` contains boundary rules for normalized input, length limits, SQL parameterization, tenant or team scope, and sensitive logging restrictions.
- Verified `AGENTS.md`, `templates/repo/AGENTS.repo-template.md`, and `templates/global/AGENTS.base.md` now reference the Java rules.
- Verified the Feishu-facing share source was updated in the same work cycle to mention the Java rule set.

## Result

The Java rule set is discoverable, aligned with the existing Python rule structure, and covers the API-boundary examples requested for string trimming and length validation.
