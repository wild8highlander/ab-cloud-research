# monograph/

The monographs of the AB Quantum Processor series.

- `content/` — the DOCS sources (`__init__.py`, `common.py`,
  `ru_v20.py`, `en_v20.py`) and `_json/` (assembled JSON sources,
  included in the ZIP — the eliminated cause of the "broken" documents
  of the mother package v1.0.0);
- the assembled monographs: `computations/V20_processor_compiler/
  monograph_{ru,en}.{pdf,docx}`.

Rebuild: `python3 scripts/make_monographs.py`.
