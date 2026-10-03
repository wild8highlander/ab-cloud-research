# AB-Cloud v23 — Journal Submission Package (v3.3 Reference Build, v34)

Complete verification record of the **AB-Cloud v23 SUPERCOMBO** suite — the
AB-Cloud research laboratory's 32,095-line Julia 1.12 verification apparatus for the
Aharonov–Bohm lattice-operator framework of the Riemann ζ zeros — prepared from the
reference run `run_20260914_234626` (38 tests, 79 verdict entries, 127 audit-tier
sub-checks, 60 figures, 26.04 h wall time).

**Author:** Isaev Iskhak Khamzatovich · AB-Cloud Research Laboratory · ORCID 0009-0003-7299-0701
**Repository:** https://github.com/wild8highlander/ab-cloud-research
**Dataset DOI:** 10.5281/zenodo.21825394

## What changed in v34 (2026-09-19)

This package supersedes the v33 freeze. Delta:

* **New Test 34 ensemble run on a Hurwitz surface.** The laboratory's MODE 2 HARDCORE
  pass re-ran the confrontation on the Klein quartic PSL(2,7) (magnetic Cayley graph,
  ×56 voltage lift, 9,408 sites) against **100,000 ζ zeros**: 5 realizations, 23,320
  pooled spacings, **pooled D = 0.0808, p = 1.187e-107, d_GUE = 0.0044, d_Pois = 0.2817,
  plateau = 0.9734, mean |R2−GUE| = 0.0299**; median D = 0.0817, IQR = 0.0017, zero MAD
  outliers (STABLE). The Test 34 composite criterion is satisfied on all three counts
  (GUE-CONSISTENT) — for the first time on a closed Hurwitz surface. Documented as
  **Addendum Add.8** in the monograph, the Academic Essence, and both preprints; the
  reconstructed protocol ships at `run_data/run_20260919_085734_m2/`.
* **Code updated to v3.3.** `lab_standalone/ab_cloud_v23.jl` gains the **TEST 34G
  geometry sweep (Test 39)** — the finite-size laboratory ported into the suite (seven
  closed surfaces, big-matrix parity, pooled + UNIVERSAL verdicts);
  `lab_standalone/finite-size_lab.jl` is now **v1.3** (MODE 5 universal geometry sweep,
  the PSL(2,27) Hurwitz surface, voltage-lift stretching of all Hurwitz geometries).
  `hp_audit_standalone.jl` unchanged.
* **Appendix B of the monograph** now reproduces the v3.3 source verbatim (32,095
  lines); `preprint/appendix_b_code.pdf` regenerated (225 pp., 32,095 lines).
* All PDFs regenerated from the updated sources; `SHA256SUMS.txt` rebuilt.

## Contents

| File / folder | What it is |
|---|---|
| `AB_Cloud_v23_Monograph.pdf` | **The monograph (PDF)** — cover, abstract, TOC, Part I (framework), Part II (38 test chapters with 46 figures and 10 data tables), Part III (synthesis, scope of validity, conclusions), references, Appendix A (full results tables), Appendix B (complete v3.3 source), Appendix C (code audit and patch record v3.1–v3.2), Appendix D (Python guide), Appendix E (audit-tier data guide), plus the September 2026 Test 34 addendum (Add.1–Add.8). |
| `AB_Cloud_v23_Monograph.docx` | **The monograph (DOCX)** — same content, editable; TOC updates via right-click → *Update Field*. |
| `Monograph/` | Alternate copies of the monograph (docx + pdf). |
| `AB_Cloud_v23_Academic_Essence.pdf` / `.docx` | **The Academic Essence companion** — the framework's academic account in fourteen chapters (bilingual EN + RU annotation), with the v3.2 estimator-audit resolution and the v1.3 Klein-quartic ensemble pass (Add.8) integrated. |
| `preprint/monograph_preprint.tex` | **LaTeX preprint source** (PLOS-style single column; compiles with `tectonic`). |
| `preprint/monograph_preprint.pdf` | Compiled preprint (305 pp., Add.8 included). |
| `preprint/appendix_b_code.pdf` | The complete v3.3 source as a standalone listing (225 pp., 32,095 lines; included in the preprint via `\includepdf`). |
| `preprint2/academic_essence_preprint.tex` + `.pdf` | Academic Essence preprint (source + compiled, 53 pp., Add.8 included). |
| `cover_letter.docx` / `cover_letter.pdf` | Cover letter for the Editor-in-Chief, referencing the repository, the packaged run archive, and the Zenodo DOI. |
| `submission_forms.pdf` | CRediT contributions, declarations, funding, data availability, ethics, author summary, licence. |
| `submission_checklist.md` | Pre-submission checklist (venue selection, TOC refresh, reviewer slots). |
| `journal_recommendations.md` | **Interdisciplinary journal short-list for submission** (scope fit, APCs, code/data policies, registration steps, GitHub integration). |
| `cover_design_source.html` | Editable HTML source of the PDF cover design (fonts included in `fonts/`). |
| `python_clone/` | **Python reimplementation of the suite**: all 38 tests, two-pass verdict algebra, report writer, plot engine, CLI (`python -m abcloud.cli --test all`), the identical embedded 50,000-zero dataset, README with the equivalence/deviation table. |
| `run_data/run_20260917_080329_m2/` | **Test 34 standalone-laboratory HARDCORE run** (September 2026 addendum): 20 realizations, 91,360 pooled spacings, pooled D = 0.0970, full report + spacing arrays + post-processed mixture-fit analysis. |
| `run_data/run_20260917_084900_m3/` | **Test 34 MODE 3 DEEP DIAG run** (September 2026 addendum): differential CDF, short-range zone, seed forensics, finite-size probe D(L), bootstrap. |
| `run_data/run_20260919_085734_m2/` | **NEW — Test 34 HARDCORE pass on the Klein quartic PSL(2,7)** (19 September 2026): 5 realizations, 100,000 zeros, pooled D = 0.0808, d_GUE = 0.0044 — composite criterion satisfied (GUE-CONSISTENT). Reconstructed protocol: console capture, FINAL_REPORT.md, CSV, provenance-flagged config.json. |
| `lab_standalone/` | **Standalone research codes**: `finite-size_lab.jl` (**v1.3** — Test 34 laboratory, modes 1–5, eight geometries incl. PSL(2,27)), the **v3.3** working copy of the full suite (`ab_cloud_v23.jl`, TEST 34G / Test 39 inside), and `hp_audit_standalone.jl` (HP·MERIDIAN H-audit module), each with a folder README. |
| `run_data/run_20260914_234626/` | **The complete reference-run archive** — all 38 test folders (reports in four formats, logs, console captures, plots), the four-format FINAL_REPORT, the consolidated execution log (9,921 lines), the one-line verdict register, and the index page. `run_data/AUDIT_DATA.md` is its reading guide. |

## The verification record at a glance

* **79 verdict entries** (66 PASS / 13 FAIL), all preserved verbatim in Appendix A.2.
* **Audit tier:** 35 HARDCORE/SERIES/AUDIT batteries, **127 individually logged
  sub-checks, 121 passed in-run** (Appendix A.3; full console captures in `run_data/`).
* **Exact layer:** hermiticity, flux quantization, Byers–Yang invariance, chiral pairing,
  zero-mode index, and the analytic identity chain — machine-zero residuals; the rational
  identities verified at 256-bit precision.
* **Spectral layer:** every class-discriminating statistic places the lattice spectrum and
  the ζ dictionary on the GUE side of its pre-registered window at effect size.
* **Post-run estimator audit (v3.2):** the run's one adverse composite statistic
  (pooled D = 0.1096) traced to the ζ-side reference unfolding; the R₂ sub-check defects
  located and repaired; a GUE-2000² calibration gate added.
* **Post-v3.2 verification chain (September 2026, Addendum Add.1–Add.8):** cross-language
  reproduction, disorder sweep, deep diagnostics, mixture decomposition — and the v1.3
  Klein-quartic ensemble pass at 100,000 zeros: pooled D = 0.0808 with d_GUE = 0.0044
  (the lattice statistically indistinguishable from pure GUE), composite criterion
  satisfied on a genus-3 Hurwitz surface.

## The September 2026 addendum (Test 34: independent verification and deep diagnostics)

After the v3.2 package was frozen, the Test 34 confrontation was re-examined with the
standalone laboratory (`lab_standalone/finite-size_lab.jl`) and a validated Python/SciPy
port. The addendum — a final chapter in the monograph, the Academic Essence, and both
preprints — documents the chain: the pre-registered falsifiability branch (Add.1), the
cross-language reproduction (Add.2), the disorder sweep (Add.3), the deep diagnostics
(Add.4), the effective GUE+Poisson decomposition (Add.5), the corrected reference
constants (Add.6), the composite-verdict impact (Add.7), and — new in this package — the
v1.3 ensemble pass on the Klein quartic at 100,000 zeros (Add.8): the confrontation's
residual distance is geometry-independent, the lattice side is GUE to within the
sampling floor, and the composite criterion of Test 34 is satisfied on all three counts.
