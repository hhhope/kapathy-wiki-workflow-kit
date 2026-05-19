# Design: initialize LLM-WIKI seed repo

## Architecture

Add a manifest-driven seed generation path:

```text
scripts/llm_wiki_seed_manifest.py
  -> scripts/build_llm_wiki_seed.py
  -> target seed repository
  -> scripts/verify_llm_wiki_seed.py
  -> minimal runtime verification commands
```

The manifest is the single allowlist for copied skill directories, copied
config/scripts, generated root files, generated sample wiki pages, created
runtime directories, and excluded history/private paths.

## Builder

`scripts/build_llm_wiki_seed.py`:

- refuses non-empty targets unless `--force` is passed;
- copies only allowlisted directories and files;
- creates required wiki runtime directories with `.gitkeep`;
- writes minimal root files and sanitized seed pages;
- checks that excluded paths were not created.

The existing `scripts/bootstrap_wiki_workflow_kit.py` is not reused for this
change because it represents an older, narrower workflow kit. It does not
preserve the current wiki runtime, scorecard, medical-loop, and output-gate
surface.

## Verifier

`scripts/verify_llm_wiki_seed.py` performs structural verification:

- required root files exist;
- required `.codex/skills/` entries exist;
- required `wiki/config/` and script files exist;
- sanitized examples exist;
- forbidden archive/private paths are absent;
- key public/sanitized markers are present.

This verifier proves seed shape, not product readiness.

## Seed Content

Generated seed pages are intentionally small and sanitized:

- LLM-Wiki method reading note;
- Li Xiang interview reading shape;
- interview deep-reading-board example;
- LLM-WIKI core product contract;
- medical-loop model;
- seed boundary ADR;
- initial wiki status page and indexes.

These pages preserve workflow shape and public-source vocabulary, not internal
project history.

## Verification Flow

In the target repository:

```text
verify seed shape
run frontmatter checker
build wiki status
extract graph and relation diagnostics
run scorecard and utilization
run medical-loop preview commands
inspect target git diff
```

If copied scripts expose missing assumptions, fix the seed path narrowly:

- prefer adding missing helper files to the manifest;
- fix generated seed pages or seed taxonomy when the seed content violates the
  current checker;
- do not import private historical content to satisfy a check.

## Boundaries

README is a file target but not a quality gate in this change. Final README
copywriting follows after the system seed passes minimal verification.

The seed does not authorize automatic wiki repair. Medical-loop writes remain
bounded by doctor, review, treatment, surgery, and recovery contracts.
