---
name: release-diff-cr
description: Use when preparing a project release review by comparing the default main branch origin/master with the previous reachable release version on the same main branch, including requests about上线比较, 上线评审, 主分支版本比较, release diff, 合并分支统计, 改动人员统计, Owner/Reviewer建议, 测试证据, or generating release code-review reports. This skill does not define coding standards; it reuses the currently installed code-review and domain-specific skills.
---

# Release Diff CR

## Purpose

Prepare a standardized release-diff audit before上线. The comparison must use two versions on the same main branch. By default, compare the nearest reachable matching release tag on `origin/master` (`release-*` or `v*`) to `origin/master`; if no matching tag exists, fall back to `origin/master~1..origin/master`. The run produces one human-readable Markdown CR report, per-author comparison files, and optional JSON data for CI or dashboards.

Do not treat this skill as the final code review rule source. It prepares release evidence and generates a CR report that follows the local CR output format, then routes detailed code-rule checks to currently installed code-review or domain skills.

## CR Agent Role

When `cr-agent` is available, this skill acts as the first `cr-diff` provider
for release and mainline comparison. It produces deterministic release-diff
evidence and CR scan issues. Blocking CR scan issues are gate inputs and must
drive `cr-gate` or `--fail-on blocker` to a blocked result.

## Do Not

- Do not write personal absolute paths, drive-letter paths, fixed usernames, or machine-specific repository paths into outputs.
- Do not invent coding standards inside this skill.
- Do not claim CR is complete unless the installed code-review skills were actually used or the report clearly marks CR rules as unavailable.
- Do not compare different branches, merge-bases, or guessed common ancestors as an上线 baseline.
- Do not use graph/tag guesses as durable truth when explicit `--base-ref` or project rules are provided.
- Do not mutate the target repository except writing the requested report file.

## Quick Start

Run the bundled script from the skill root or by absolute script path:

```bash
python scripts/release_diff_report.py --repo <repo-root>
```

Common overrides:

```bash
python scripts/release_diff_report.py \
  --repo <repo-root> \
  --main-ref origin/master \
  --base-ref <previous-commit-on-origin/master> \
  --rules-file <repo-root>/.codex/release-rules.yaml \
  --cr-output <repo-root>/cr/my-project/2026-06-10.md
```

When no release tag exists, specify the previous online version explicitly:

```bash
python scripts/release_diff_report.py \
  --repo <repo-root> \
  --from-version <previous-online-commit-or-branch-or-tag>
```

Compare two explicit versions on the main branch or any reachable refs:

```bash
python scripts/release_diff_report.py \
  --repo <repo-root> \
  --from-version <old-commit-or-tag> \
  --to-version <new-commit-or-tag>
```

CI gate mode:

```bash
python scripts/release_diff_report.py \
  --repo <repo-root> \
  --from-version <old-commit-or-tag> \
  --to-version <new-commit-or-tag> \
  --fail-on gate
```

JSON output for CI or a dashboard writes the full release-diff data as JSON:

```bash
python scripts/release_diff_report.py --repo <repo-root> --format json --output cr/my-project/2026-06-10.json
```

## Workflow

1. Confirm the target repository root. Use `<repo-root>` in instructions and report examples, not local absolute paths.
2. Read project rules from `.codex/release-rules.yaml` when present. If absent, use built-in defaults.
3. Compare `base..main`:
   - `main` defaults to `origin/master`.
   - `base` defaults to the nearest reachable release tag matching `release-*` or `v*`; if no matching tag exists, it falls back to `main~1`.
   - Explicit `--main-ref` and `--base-ref` override defaults.
   - `--from-version` overrides `--base-ref`.
   - `--to-version` overrides `--main-ref`.
   - Versions may be commit SHA, tag, branch, or any Git ref accepted by `git rev-parse`.
   - The start ref must be an ancestor of the end ref unless `--allow-unrelated-range` is explicitly passed.
   - A baseline from another branch, including a release branch or a merge-base with another branch, is invalid for上线 comparison unless this is explicitly marked as archaeology with `--allow-unrelated-range`.
4. Generate the release-diff evidence:
   - merged branches
   - authors and committers
   - change categories
   - Owner/Reviewer suggestions
   - secret-scan findings
   - revert/cherry-pick/large-diff hints
   - CR report summary
5. Run the currently installed CR skills:
   - Use the installed general code-review skill first.
   - Add installed domain skills when paths match the change, for example DDL review, exception scanning, channel integration, API migration, or project-specific review cards.
   - If no applicable CR skill is installed, mark `CR rules missing` in the report and tell the user.

## Rule Configuration

Default project rule path:

```text
<repo-root>/.codex/release-rules.yaml
```

Read `references/release-rules-schema.md` before changing rule names or adding new rule keys. The script supports a small YAML subset without external dependencies: mappings, lists, strings, booleans, and integers.

Important defaults:

| Setting | Default |
|---|---|
| Main ref | `origin/master` |
| Baseline strategy | `same_branch_previous` |
| Release tag patterns | `release-*`, `v*` |
| Release branch patterns | `release-*`, `origin/release-*`, `origin/release/*` (only when `baseline_strategy: release_ref`) |
| Ticket pattern | `[A-Z][A-Z0-9]+-[0-9]+` |
| Merge strategy | `merge_commit` |
| CR report path | `<repo-root>/cr/{project}/YYYY-MM-DD.md` |
| Per-author comparison path | `<repo-root>/cr/{project}/YYYY-MM-DD-release-diff-{author}.md` |

CLI precedence:

| Compare side | Highest precedence | Next | Default |
|---|---|---|---|
| Start | `--from-version` | `--base-ref` | nearest reachable `release-*`/`v*` tag, else `main~1` |
| End | `--to-version` | `--main-ref` | `origin/master` |

Professional gate options:

| Option | Purpose |
|---|---|
| `--allow-unrelated-range` | Permit comparison when start is not on the same first-parent branch as end. Use only for explicit archaeology or branch-diff cases, not上线 comparison. |
| `--fail-on never` | Always exit `0` after writing a report. Default. |
| `--fail-on gate` | Exit `3` when the report conclusion is `阻塞上线`. |
| `--fail-on blocker` | Exit `3` when any blocker finding exists. |
| `--fail-on score` | Exit `3` when the internal release-diff score is `>= 60`; do not turn this score into CR issue output. |

## Output Contract

Each Markdown run must generate one CR report plus per-author comparison files. Do not generate a separate release-diff summary Markdown file.

1. `cr/{project}/YYYY-MM-DD.md`
   - Keep this as the code CR report file, using the same format as existing project CR files.
   - Include the release comparison summary and per-author comparison file index.
   - Do not expand every changed file or full commit log here.
   - Include frontmatter, gate conclusion, scorecard, high-priority issues, logic issues, test evidence, and a concise author review assignment.
   - Link to the per-author comparison files.
   - Include CR issue/TODO/risk/disposition sections only when issues were produced by the real CR scan.

2. `cr/{project}/YYYY-MM-DD-release-diff-{author}.md`
   - Generate one file per author when author data exists.
   - Keep it in the same folder as the CR report file.
   - Put that author’s changed scope, key commits, and priority files here.
   - If the real CR scan produced issues, assign those CR report issues to concrete people by file ownership/touch history first, then by merge responsibility when no file owner applies.
   - Every displayed issue/confirmation item must reference a `CR-xxx` ID that exists in the CR report issue list.

CR Markdown must include these release comparison sections in Chinese:

- 上线比较专项结论
- 按人对比文件

Per-author comparison Markdown must include:

- 基本信息
- 本人关键提交
- 本人优先复核文件
- 复核完成标准

Author issue sections must only appear when the real CR report has scanned issues assigned to that author. Do not invent generic personal review tasks, release-diff-derived issues, branch-rule issues, ticket issues, high-risk-path issues, or rollback issues. If no CR-scanned item is assigned to an author, omit the whole section.

JSON output must preserve the same data categories with stable snake_case keys.
## CR Skill Routing

Use release-diff data to decide which installed review skills to call. Do not copy their rules here.

Suggested routing:

| Change evidence | Suggested installed skill |
|---|---|
| Any code change | General code-review skill |
| `*.sql`, migration paths, table changes | DDL or database migration review skill |
| exception classes, handlers, error codes | Exception review/scanner skill |
| bank/payment channel integration paths | Channel integration skill |
| API migration docs, DTO or controller migration | API migration review skill |

If a suggested skill is not installed in the current environment, record that as a missing CR dependency instead of substituting improvised rules.

## Acceptance Checklist

- Default comparison uses the nearest reachable `release-*`/`v*` tag to `origin/master`; when no tag exists, it uses `origin/master~1..origin/master`.
- Non-override上线 comparison rejects baselines that are not ancestors of the selected main branch.
- Overrides work through CLI arguments and `.codex/release-rules.yaml`.
- `from..to` ranges are ancestor-checked by default.
- CI can use `--fail-on` for deterministic exit codes.
- Markdown output includes exactly one CR report plus per-author comparison files; no separate release-diff summary Markdown file.
- CR report links per-author comparison files when generated.
- Markdown contains no local absolute paths.
- JSON output is valid.
- `quick_validate.py <skill-root>` passes.
