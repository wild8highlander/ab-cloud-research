<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ Hilbert_Polya/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# audit/ — external audit of the package and its results

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

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

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The external audit of the package and its results: the audit document (DOCX + PDF) produced outside the main development loop.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `HPB_audit_canonization_2026-10-13_ru.docx` | 62 KB | Word document |
| `HPB_audit_canonization_2026-10-13_ru.pdf` | 232 KB | PDF document |

**Subfolders:** `src/`

<div align="center">

<img src="../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
