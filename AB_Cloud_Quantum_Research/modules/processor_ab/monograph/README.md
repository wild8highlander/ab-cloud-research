# monograph/

Монографии серии AB Quantum Processor.

- `content/` — DOCS-исходники (ru_v20.py, en_v20.py) и `_json/`
  (собранные JSON-исходники, включены в ZIP — устранённая причина
  «битых» документов v1.0.0 материнского пакета);
- собранные монографии: `computations/V20_processor_compiler/
  monograph_{ru,en}.{pdf,docx}`.

Пересборка: `python3 scripts/make_monographs.py`.
