# Evaluation: Restore Repo-Local Runtime Skills

## Pressure Scenarios

| Scenario | Expected Behavior | Evidence |
|---|---|---|
| Codex has no usable plugin marketplace runtime | Repo-local `.codex/skills/wiki-*` provides the wiki runtime entrypoints | Targeted tests and README/spec checks passed |
| User/root skill install drifts or misses `openspec-explore` | Repo-local `.codex/skills/openspec-explore` remains present in git | Targeted OpenSpec skill namespace test passed |
| Future contributor audits skill behavior from the repo | Skill bodies are readable under `.codex/skills/*/SKILL.md` | Full unittest discovery passed |
| Some Codex surface adds `report-wiki-portfolio:` prefix | Repo-owned availability remains the priority; README documents repo-local source | Design and residual risk recorded |

## RED Baseline

- `python3 -m unittest tests.test_openspec_skill_namespace
  tests.test_wiki_runtime_skills tests.test_wiki_status_command
  tests.test_codex_plugin_marketplace` failed after adding repo-local
  expectations and before restoring skills.
- Failures showed the intended missing behavior: `.codex/skills/openspec-*`
  and `.codex/skills/wiki-*` did not exist, README still pointed to
  `plugins/report-wiki-portfolio/skills`, and AGENTS still referenced plugin
  source paths for OpenSpec helpers.

## GREEN Result

- The same targeted test command passed after restoring repo-local OpenSpec and
  wiki runtime skills and updating README, AGENTS, and specs.
- `python3 -m unittest discover -s tests` passed: 56 tests.
- `openspec validate restore-repo-local-runtime-skills --strict` passed.
- `openspec validate --all` passed: 47 items, 0 failed. The PostHog DNS flush
  warnings were telemetry noise after validation success.
- Repo-local skill files now exist for:
  - `.codex/skills/openspec-apply-change/SKILL.md`
  - `.codex/skills/openspec-archive-change/SKILL.md`
  - `.codex/skills/openspec-explore/SKILL.md`
  - `.codex/skills/openspec-propose/SKILL.md`
  - `.codex/skills/wiki-status/SKILL.md`
  - `.codex/skills/wiki-manifest/SKILL.md`
  - `.codex/skills/wiki-inbox/SKILL.md`
  - `.codex/skills/wiki-query/SKILL.md`
  - `.codex/skills/wiki-graph/SKILL.md`
  - `.codex/skills/wiki-scorecard/SKILL.md`
  - `.codex/skills/wiki-route/SKILL.md`
  - `.codex/skills/wiki-context/SKILL.md`
  - `.codex/skills/wiki-apply/SKILL.md`
  - `.codex/skills/wiki-queue/SKILL.md`

## Behavior Replay

Input shape: the user asks to fix the missing OpenSpec skill problem and states
that Codex has no plugin functionality, so skills should be restored according
to the repository skill surface.

Trigger condition: a required runtime skill exists only under plugin source or
machine-local user/root skill directories, but not under `.codex/skills`.

Expected route: treat `.codex/skills` as the supported repo runtime surface;
restore OpenSpec helper skills and wiki runtime skills there; keep root/user
skills optional rather than authoritative.

Expected output: future sessions can find the repo-owned runtime skill bodies in
the repository without plugin installation or copying into `/home/yan/.codex`.

Non-promotion boundary: this does not promote all repo skills to global/root
scope, and it does not remove plugin files unless a later cleanup change chooses
to retire them.

Residual proof boundary: repo-local file and test evidence proves the checkout
contains the required skill source. It does not prove every Codex UI will choose
the same display name for repo-local skills.

## Residual Risks

- Some Codex surfaces may display repo-local skills with the
  `report-wiki-portfolio:` namespace prefix. This is accepted for this repo
  because source-of-truth stability is preferred over plain global names.
- Existing plugin files remain in the repo as legacy/source compatibility and
  may need a later cleanup change if the repo decides to retire plugin
  packaging entirely.
