# audit/ — external audit of the package and its results

*October 13, 2026 · auditors: an independent session (Super Z) · commit e913629 (v2.0.0)*

## What is here

| File | Contents |
|------|----------|
| `HPB_audit_canonization_2026-10-13_ru.pdf` | the audit report (PDF, 30 pages, Russian) |
| `HPB_audit_canonization_2026-10-13_ru.docx` | the same report as DOCX |
| `src/` | the report's sources: content modules `audit_content.py`, `audit_content2.py`, `audit_content3.py`, the structured dump `content.json`, the PDF builder `audit_build.py` (ReportLab) and the DOCX builder `audit_docx.js` (docx-js) |

## The verdicts in one table

| Area | Verdict |
|------|---------|
| Reproducibility of the pixel pipeline | CONFIRMED (PNG bit-for-bit, witness 17/17, 1.26e-7) |
| Video ↔ README/H.8 | CONFIRMED WITH REMARKS (drift of the artifact scheme — fixed; the mp4 build script is missing) |
| The monograph layer | CANONIZED (canon_volume; the former volumes are detailed appendices) |
| Numbers content ↔ RESULTS ↔ preprint ↔ data | NO DISCREPANCIES (a 30-position sample) |
| The roadmap | EXTENDED (N7 — blind independence of H; N8 — literature anchors) |

## How to rebuild the report

```bash
python3 audit/src/audit_build.py                                  # PDF (output goes to audit/)
node   audit/src/audit_docx.js audit/HPB_audit_canonization_2026-10-13_ru.docx
```

The PDF output goes to the repository's `audit/` (the environment variables
`PDF_SKILL` and `AUDIT_OUT_DIR` override the cover-skill path and the output
directory). The DOCX table of contents is built by `audit_docx.js` itself; no
separate placeholder script is needed.

The report's content sources are `src/audit_content*.py`; text edits go only
there, followed by a rebuild.
