# Table template — the numbers registry format

Every table of numbers in the monograph follows this contract:

| # | Metric | Value | Campaign |
|---|---------|-------|----------|

Rules (enforced by `09_tests/python/test_monograph_structure.py`):

1. **Value verbatim** from the source verdict file — never re-typed.
2. **Campaign column mandatory** — an unattributed number is an error.
3. **Disagreements shown** — when two sources differ by convention, both
   rows appear with a note.
4. **Units / precision** carried in the value cell (e.g. `2.59e-39`,
   `649 = 649`, `0.978 vs 0.0010 (×977)`).
5. Markdown pipes escaped in values (`\|`) where needed.
