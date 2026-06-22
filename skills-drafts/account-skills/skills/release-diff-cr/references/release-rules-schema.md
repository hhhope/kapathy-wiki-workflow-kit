# Release Rules Schema

Place project overrides at:

```text
<repo-root>/.codex/release-rules.yaml
```

The bundled script intentionally supports a small YAML subset so it can run without third-party packages.

## Example

```yaml
main_ref: origin/master
baseline_strategy: same_branch_previous
release_tag_patterns:
  - release-*
release_branch_patterns:
  - release-*
  - origin/release-*
  - origin/release/*
allowed_branch_patterns:
  - feature/.*
  - bugfix/.*
  - hotfix/.*
  - release/.*
ticket_pattern: "[A-Z][A-Z0-9]+-[0-9]+"
merge_strategy: merge_commit
test_evidence_paths:
  - test
  - tests
  - src/test
  - __tests__
rollback_evidence_paths:
  - rollback
  - revert
  - db/rollback
sensitive_paths:
  - .env
  - secret
  - private
  - credentials
high_risk_paths:
  - .github/
  - Jenkinsfile
  - pom.xml
  - build.gradle
  - package.json
risk_weights:
  direct_main_commit: 30
  unknown_merge_source: 15
  illegal_branch: 20
  sensitive_path: 40
  secret_in_diff: 60
  missing_ticket: 15
  missing_test_evidence: 20
  missing_rollback: 20
  high_risk_change: 15
  large_diff: 15
owners:
  src/payment/**:
    - payment-team
  db/**:
    - dba
```

## Fields

| Field | Type | Meaning |
|---|---|---|
| `main_ref` | string | Default main branch ref. Defaults to `origin/master`. |
| `baseline_strategy` | string | Baseline selection strategy. Defaults to `same_branch_previous`, which compares `main~1..main` and requires the start version to be on the same first-parent branch. `release_ref` enables the older release tag/branch lookup but still must resolve to the same first-parent history unless `--allow-unrelated-range` is used. |
| `release_tag_patterns` | list[string] | Tag patterns for previous online baseline when `baseline_strategy: release_ref`. Defaults to `release-*`. |
| `release_branch_patterns` | list[string] | Branch patterns used when `baseline_strategy: release_ref` and no release tag is found. |
| `allowed_branch_patterns` | list[string] | Regex patterns for merge source branches. |
| `ticket_pattern` | string | Regex used to find requirement/defect IDs in branch names and commit subjects. |
| `merge_strategy` | string | One of `merge_commit`, `squash_allowed`, `rebase_allowed`. Defaults to `merge_commit`. |
| `test_evidence_paths` | list[string] | Paths that count as test evidence. |
| `rollback_evidence_paths` | list[string] | Paths or filenames that count as rollback evidence. |
| `sensitive_paths` | list[string] | Path fragments treated as sensitive. |
| `high_risk_paths` | list[string] | Path fragments treated as high-risk. |
| `risk_weights` | map[string,int] | Override risk scoring weights. |
| `owners` | map[string,list[string]] | Glob-like path pattern to owner/reviewer names. |

## CLI Precedence

Rules file defaults are lower priority than command-line refs.

| Compare side | Highest precedence | Next | Default |
|---|---|---|---|
| Start | `--from-version` | `--base-ref` | `main~1` on the same first-parent branch |
| End | `--to-version` | `--main-ref` | `main_ref` or `origin/master` |

`--from-version` and `--to-version` accept any ref that `git rev-parse --verify` can resolve, including commit SHA, tag, local branch, or remote branch.

The start ref must be an ancestor of the end ref and must appear on the end ref's first-parent history by default. This keeps release comparison on one branch. Use `--allow-unrelated-range` only when intentionally comparing unrelated branches or archaeology ranges, not for上线 comparison.

## CLI Gate Exit Codes

| Option | Exit behavior |
|---|---|
| `--fail-on never` | Always exit `0` if the report was generated. |
| `--fail-on gate` | Exit `3` when the gate conclusion is `阻塞上线`. |
| `--fail-on blocker` | Exit `3` when any blocker finding exists. |
| `--fail-on score` | Exit `3` when risk score is `>= 60`. |

## Validation

The script fails fast on:

- unknown rule keys
- invalid regex patterns
- non-integer risk weights
- invalid `merge_strategy`
- invalid `baseline_strategy`
- non-integer large diff thresholds

## Gate Defaults

Risk conclusion defaults:

| Condition | Conclusion |
|---|---|
| Any blocker finding or score >= 60 | `阻塞上线` |
| Score >= 30 | `有条件上线` |
| Otherwise | `允许上线` |

Secret findings and sensitive path changes are blockers by default.
