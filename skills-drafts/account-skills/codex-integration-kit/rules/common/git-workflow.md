# Git Workflow

## Base Constraints

- Global git discipline comes from `~/.codex/AGENTS.md`; this file only adds repository-specific details.
- If the repository config sets `core.hooksPath`, inspect and honor that configured hooks directory instead of assuming `.git/hooks` sample scripts are active.
- Hooks can enforce commit/push checks, but they do not replace manual worktree and HEAD verification.

## Commit Discipline

- Commit each completed and verified file-editing unit as soon as practical.
- Do not say `committed`, `clean`, or `synced` from memory.
- Before any such statement, rerun:
  - `git status --short`
  - `git log -1 --oneline`
- If a commit only includes part of the work, state which files are committed and which are still uncommitted.
- If unrelated local changes exist, preserve them; do not clean or reorder them opportunistically.
- Do not amend commits unless the user explicitly asks.
- Do not run destructive commands such as `git reset --hard` or `git checkout --` unless the user explicitly approves.

## Branch Constraints

- If the current branch is `main`, do not continue feature work and do not push directly from `main`.
- Create a feature branch named after the current PRD/REQ intent, push that branch, and open an MR into `main`.

## Branch Naming

- Use branch names in the form: `<type>/<intent-slug>`.
- Allowed branch types:
  - `feat`: new feature or user-visible capability
  - `fix`: bug fix or behavioral correction
  - `refactor`: internal restructuring without intended behavior change
  - `chore`: tooling, config, dependency, or maintenance work
  - `docs`: documentation-only work
  - `test`: test-only work
- Prefer a short lowercase slug with hyphens, for example:
  - `feat/multitenant-sql`
  - `fix/dashboard-refresh-state`
  - `docs/codex-governance-install`
- If a REQ or ticket clearly applies, prefer the branch slug to reflect that requirement intent rather than a vague implementation detail.
- Avoid spaces, uppercase letters, personal names, and meaningless suffixes such as `test`, `final`, or `new`.

## Commit Message Naming

- Use Conventional Commits in the form: `<type>: <short summary>`.
- Allowed commit types:
  - `feat`
  - `fix`
  - `refactor`
  - `docs`
  - `test`
  - `chore`
- Keep the summary short, concrete, and lowercase where practical.
- Describe the user-facing or engineering intent, not the editing action itself.
- Good examples:
  - `feat: add global AGENTS templates`
  - `fix: preserve selected team scope after refresh`
  - `docs: clarify codex installation modes`
- Avoid low-signal messages such as:
  - `update files`
  - `fix bug`
  - `final change`
  - `wip`

## Resume After Interruption

After interruption, the first git action is to re-check:

- `git status --short`
- `git log -1 --oneline`

Do not judge the current repository state from memory before those checks are complete.
