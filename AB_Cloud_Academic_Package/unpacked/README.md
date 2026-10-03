# `unpacked/` — The Complete Package Tree, Explained Folder by Folder

This directory is the full content of `AB_Cloud_v23_Full_Package_Academic_v34.zip`, unpacked and published with three enhancements: **every folder carries its own detailed README.md**, **every colliding filename has been made globally unique** with a traceable location code, and every file is listed — with size, type and description — in the package-wide [`FILE_INDEX.md`](../FILE_INDEX.md). The original package README (the v34 changelog) is preserved one level up as [`README_original.md`](README_original.md), and the untouched ZIP lives in [`../zip_archive/`](../zip_archive/README.md).

## The documents at the root of this folder

The eleven files at this level are the package's "front matter": the monograph in both editions, the Academic Essence companion, the two compiled preprints with their LaTeX sources one level down, the journal-submission paperwork, the cover-design source, the checksum register of the original freeze, and the original run archive of the reference run. Each is described in detail in the contents table below; the monograph is the centrepiece and the natural entry point for a new reader.

| File | What it is |
|---|---|
| `AB_Cloud_v23_Monograph.pdf` | **The monograph (PDF)** — cover, abstract, table of contents, Part I (the framework), Part II (38 test chapters with 46 figures and 10 data tables), Part III (synthesis, scope of validity, conclusions), references, Appendix A (full results tables), Appendix B (the complete v3.3 source, 32,095 lines reproduced verbatim), Appendix C (code audit and patch record v3.1–v3.2), Appendix D (Python guide), Appendix E (audit-tier data guide), plus the September 2026 Test 34 addendum (Add.1–Add.8). |
| `AB_Cloud_v23_Monograph.docx` | The monograph in editable Microsoft Word form; the TOC refreshes via right-click → *Update Field*. |
| `AB_Cloud_v23_Academic_Essence.pdf` / `.docx` | **The Academic Essence companion** — the framework's academic account in fourteen chapters (with a bilingual EN + RU annotation), integrating the v3.2 estimator-audit resolution and the v1.3 Klein-quartic ensemble pass (Add.8). |
| `cover_letter.pdf` / `.docx` | The cover letter to the Editor-in-Chief, referencing the repository, the packaged run archive and the Zenodo DOI. |
| `submission_forms.pdf` | CRediT contributions, declarations, funding, data availability, ethics, author summary, licence. |
| `submission_checklist.md` | The pre-submission checklist: venue selection, TOC refresh, reviewer slots. |
| `journal_recommendations.md` | The interdisciplinary journal short-list: scope fit, APCs, code/data policies, registration steps, GitHub integration. |
| `cover_design_source.html` | The editable HTML source of the PDF cover design; the fonts it references ship in [`fonts/`](fonts/README.md). |
| `SHA256SUMS.txt` | The original freeze's checksum register (original filenames). This GitHub edition adds `../SHA256SUMS_unpacked.txt` for the renamed tree. |
| `run_20260914_234626.zip` | The original run archive of the reference run, preserved exactly as shipped (its content is published unpacked under [`run_data/`](run_data/README.md)). |

## The folder map

| Folder | README | What lives there |
|---|---|---|
| `Monograph/` | [README](Monograph/README.md) | Alternate copies of the monograph (DOCX + PDF). |
| `fonts/` | [README](fonts/README.md) | The Inter and Playfair Display web fonts (40 faces) and CSS used by the cover design. |
| `lab_standalone/` | [README](lab_standalone/README.md) | The three standalone Julia codes: the v3.3 full suite, the finite-size Test 34 laboratory (v1.3), and the HP·MERIDIAN H-audit module. |
| `preprint/` | [README](preprint/README.md) | The monograph preprint: LaTeX source, compiled 305-page PDF, the 225-page Appendix B code listing, and the addendum figures. |
| `preprint2/` | [README](preprint2/README.md) | The Academic Essence preprint: LaTeX source, compiled 53-page PDF, addendum figures. |
| `python_clone/` | [README](python_clone/README.md) | The faithful Python reimplementation of all 38 tests, with CLI, report writer, plot engine and the embedded 50,000-zero dataset. |
| `run_data/` | [README](run_data/README.md) | The complete run archives: the reference run (38 test folders + FINAL_REPORT), the three September 2026 Test 34 addendum runs, and the audit-tier reading guide. |

## How the location codes work

Files whose names collided across folders carry a suffix code: `A04` = reference run, test 04; `A04L` / `A04P` = its logs/plots subfolders; `AFR12` = FINAL_REPORT, raw reports of test 12; `P1` / `P2` = preprint 1 / 2; `PC` = Python clone; `MG` = Monograph copies; `FT` = fonts; `B`, `C`, `D` = the three September 2026 addendum runs. The full mapping — every original name, its published name, and the reason — is tabulated in [`../FILE_INDEX.md`](../FILE_INDEX.md). Files whose names were already unique package-wide are published unchanged.

## Suggested reading order

1. This README and the original v34 changelog ([`README_original.md`](README_original.md)).
2. The monograph PDF — at minimum the abstract, Part III, and the Test 34 addendum chapter.
3. The reference-run archive guide [`run_data/AUDIT_DATA.md`](run_data/AUDIT_DATA.md) and the FINAL_REPORT ([`run_data/run_20260914_234626/FINAL_REPORT/`](run_data/run_20260914_234626/FINAL_REPORT/README.md)).
4. Two or three test folders that interest you — every one has a full README.
5. The laboratories and the Python clone, if you want to reproduce.

## Complete inventory of this folder

| File | Size | Description |
|---|---|---|
| `AB_Cloud_v23_Academic_Essence.docx` | 2.0 MB | The Academic Essence companion — editable Microsoft Word edition. |
| `AB_Cloud_v23_Academic_Essence.pdf` | 4.2 MB | The Academic Essence companion — PDF edition: the framework's academic account in fourteen chapters, bilingual EN + RU annotation, v3.2 audit resolution and Add.8 integrated. |
| `AB_Cloud_v23_Monograph_ROOT.docx` | 3.1 MB | The monograph — editable Microsoft Word edition (TOC updates via right-click → Update Field). |
| `AB_Cloud_v23_Monograph_ROOT.pdf` | 11.1 MB | The monograph — PDF edition (cover, abstract, TOC, Parts I–III with 38 test chapters and 46 figures, references, Appendices A–E, September 2026 addendum Add.1–Add.8). |
| `README_original.md` | 8.2 KB · 90 lines | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `SHA256SUMS.txt` | 85.1 KB · 640 lines | The original v34 freeze's SHA-256 checksum register (original filenames). |
| `cover_design_source.html` | 3.4 KB · 55 lines | Editable HTML source of the PDF cover design (uses the fonts shipped in fonts/). |
| `cover_letter.docx` | 38.3 KB | Cover letter to the Editor-in-Chief — editable Word edition. |
| `cover_letter.pdf` | 36.2 KB | Cover letter to the Editor-in-Chief — PDF edition (references the repository, the run archive and the Zenodo DOI). |
| `journal_recommendations.md` | 10.7 KB · 144 lines | Interdisciplinary journal short-list: scope fit, APCs, code/data policies, registration steps, GitHub integration. |
| `run_20260914_234626.zip` | 4.6 MB | The original run archive of the reference run, preserved exactly as shipped. |
| `submission_checklist.md` | 4.5 KB · 76 lines | Pre-submission checklist: venue selection, TOC refresh, reviewer slots. |
| `submission_forms.pdf` | 42.5 KB | Journal submission forms: CRediT contributions, declarations, funding, data availability, ethics, author summary, licence. |
