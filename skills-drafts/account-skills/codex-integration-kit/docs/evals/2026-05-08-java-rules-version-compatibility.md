# Java Rules Version Compatibility Check

## Scope

Traceable verification evidence for removing the newer-JDK-only baseline from `codex-integration-kit/rules/java/patterns.md`.

## Expectations

1. Java rules must support projects targeting Java 8 or newer.
2. The rule text must not imply a newer JDK is the required backend baseline.
3. Feishu-facing share content must stay aligned with the Java rule inventory.

## Manual Verification

- Verified `rules/java/patterns.md` now states `Java 8+`.
- Verified the scope guidance requires following the target project's configured JDK.
- Verified `docs/feishu-codex-governance-share.md` mentions Java 8+ compatibility in the Java patterns row.

## Result

The Java patterns rule no longer excludes Java 8 projects and now makes project JDK compatibility explicit.
