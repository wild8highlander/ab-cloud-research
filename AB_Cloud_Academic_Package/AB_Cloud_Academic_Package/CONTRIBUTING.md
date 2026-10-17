# Contributing

Thank you for considering a contribution to the AB-Cloud Research Programme
unified academic package. This document is short because the rules are few —
and strict where they matter.

## The one rule that overrides everything

**Never weaken the honesty layer.** Every claim in this package carries its
boundary: `does_not_prove` fields, exact verdicts, negative-result
registers. If your contribution adds a result, it must add its boundary too.
A PR that presents a numerical success without its boundary will be closed
with a reference to this section.

## Ways to contribute

1. **Replication.** Run a campaign in a language it has not been run in;
  publish the numbers either way. The three sources did this (Python ↔ Julia);
  the programme rewards it.
2. **Negative results.** If a construction fails, the failure is the map.
  C16 (locality wall) was such a contribution — arguably the most valuable
  one of the series.
3. **Translations.** The monograph is full in RU/EN; abstracts exist in
  zh/de/es/fr/ar. Full translations are welcome — see
  `01_monographs/_templates/` for the chapter template.
4. **Documentation and figures.** Captions exist in RU/EN; add languages.
5. **Code parity.** The CLI contract is implemented in six languages;
  Rust/Go ports of deeper campaign code are open.
6. **Data curation.** Checksums, provenance records, dataset cards.

## Workflow

1. Fork the repository; create a branch.
2. Make your change. Keep files where the structure expects them
   (`00_meta` … `10_notebooks` — see `README.md`).
3. Add or update the corresponding provenance row in
   `00_meta/provenance.jsonl`.
4. Run `python3 -m pytest 09_tests/python -q` — it must pass.
5. Open a PR describing: what changed, which campaign/theorem it touches,
   and the boundary of any new claim.

## Style

- Text: Markdown, one language per file suffix (`*.ru.md`, `*.en.md`, …).
- Code: the language's standard formatter (ruff for Python, gofmt for Go,
  rustfmt for Rust). The CLI contract (`06_code/shared/contract.json`) is
  binding: same flags, same JSON, same metrics keys.
- Numbers: verbatim from verdict files; never re-typed from memory.

## Citation of contributions

Contributors are acknowledged in `AUTHORS.md` following the
all-contributors spirit: documentation, data, translation, replication and
negative results all count.
