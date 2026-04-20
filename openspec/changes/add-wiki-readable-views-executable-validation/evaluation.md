## Baseline Scenarios

### Scenario 1: Reading views existed but proof was manual

- the readable-view pages existed
- index links existed
- verification was still narrative

### Scenario 2: Executable bundle validation

- the readable-view bundle is represented as a structured record
- the checker should fail if a required page or index entry is missing

## RED Baseline

Before this change:

- `wiki-readable-views` had implementation proof
- `wiki-readable-views` had archive review proof
- but it did not yet have executable TDD-style validation

So the pressure-test layer was still manual.

## GREEN Result

After this change:

- a checker validates the readable-view bundle structurally
- a sample validation record passes the checker
- a harness page makes the proof boundary explicit

Executable check command:

```bash
python3 scripts/check_wiki_readable_views.py scripts/examples/wiki_readable_views_validation_sample.json
```

Expected result:

- `PASS: wiki readable views bundle satisfies the executable contract.`

## Residual Risks

- this remains structural executable proof, not semantic proof
- the checker cannot decide whether the timeline or grouping is subjectively good enough
- the checker does not prove future pages will keep the same reading quality
