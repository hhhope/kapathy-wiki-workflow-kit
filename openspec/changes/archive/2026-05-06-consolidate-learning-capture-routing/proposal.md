## Why

The repository now has separate skills for article learning and README/repo
learning, but the user's current need is earlier than either module: decide
whether a request is learning at all, and then route it by evidence object.

The `larksuite/cli` skill shape points to a better local structure: a thin
domain skill owns routing, while module references own detailed workflows. This
keeps learning capture explicit without letting every material type become a
separate top-level governance entry.

## What Changes

- Add a repo-local `learning-capture` skill as the domain router for learning
  requests.
- Add module references for:
  - intent routing
  - article / blog / paper / WeChat learning
  - GitHub / GitLab README or repo learning
  - example / structure reference learning
  - pressure scenarios
- Keep `article-learning-capture` and `readme-learning-capture` as compatibility
  entry points, with explicit routing back to `learning-capture`.
- Add an OpenSpec capability for learning capture routing.
- Add a wiki/ops trace for the explore decision that chose domain routing over
  another isolated skill expansion.

## Non-Goals

- Do not delete or archive the existing article or README skills in this change.
- Do not re-score existing article notes.
- Do not create an article crawler or automatic source importer.
- Do not promote external-source learning directly into `AGENTS.md`, specs, or
  hard skill rules without the evidence-backed gate.

## Impact

- Adds `.codex/skills/learning-capture/`.
- Touches `.codex/skills/article-learning-capture/SKILL.md` and
  `.codex/skills/readme-learning-capture/SKILL.md` only for compatibility
  routing.
- Adds `openspec/changes/consolidate-learning-capture-routing/`.
- Adds one repo-visible explore trace under `wiki/ops/`.
