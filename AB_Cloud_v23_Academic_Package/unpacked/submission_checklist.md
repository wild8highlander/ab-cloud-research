# Journal Submission Checklist — AB-Cloud v23 Monograph (v3.2 Reference Build)

Manuscript: *An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros:
A 38-Test Computational Verification Suite*
Author: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701)

## 1. Manuscript files

- [x] `AB_Cloud_v23_Monograph.docx` — full monograph (DOCX, editable, TOC field-based)
- [x] `AB_Cloud_v23_Monograph.pdf` — full monograph (PDF, typeset cover)
- [x] `preprint/monograph_preprint.tex` — LaTeX source (PLOS-style single column;
      compiles against `run_data/`)
- [x] `preprint/monograph_preprint.pdf` — compiled preprint (299 pp., includes the September 2026 addendum)
- [x] `preprint/appendix_b_code.pdf` — complete v3.2 source listing (220 pp.,
      included via `\includepdf`)
- [x] `AB_Cloud_v23_Academic_Essence.pdf` / `.docx` — companion volume
- [x] `preprint2/academic_essence_preprint.tex` + `.pdf` — Essence source + compiled

## 2. Submission kit

- [x] `cover_letter.docx` / `cover_letter.pdf` — cover letter (Editor-in-Chief),
      with the repository link https://github.com/wild8highlander/ab-cloud-research
- [x] `submission_forms.pdf` — CRediT contributions, declarations of interests, funding,
      data availability, ethics, author summary, licence
- [x] This checklist

## 3. Supplementary code & data

- [x] `julia_patched/ab_cloud_v23_v3.2.jl` — **reference build** (estimator-validity
      patch series BF-02…BF-06 + v3.1 print-path fix; thresholds unchanged)
- [x] `julia_patched/ab_cloud_v23_v3.1.jl` — v3.1 build (provenance)
- [x] `julia_patched/BUGFIX_CHANGELOG.md` — full audit record (BF-01…BF-06 +
      verified-clean table)
- [x] `run_data/run_20260914_234626/` — complete reference-run archive (38 test folders,
      four-format FINAL_REPORT, consolidated logs, one-line verdict register, 60 figures)
      with the reading guide `run_data/AUDIT_DATA.md`
- [x] `python_clone/` — full Python reimplementation (all 38 tests, CLI, reports, plots;
      requirements.txt + pyproject.toml + README with equivalence table)
- [x] Repository links (verify live before submission):
      https://github.com/wild8highlander/ab-cloud-research (code + record)
      https://github.com/wild8highlander/research-papers (research record)
      https://doi.org/10.5281/zenodo.21825394 (archived dataset)

## 4. Before you submit

1. **Choose the venue.** The manuscript is formatted as a universal single-column
   preprint (PLOS-style). Suitable no-APC / free-for-independent-authors venues and
   archives: an arXiv-affiliated mirror the author can post to (endorsement required),
   Zenodo (already minted, DOI 10.5281/zenodo.21825394), HAL, or an open-access
   journal matching the computational-physics scope.
2. **Refresh the DOCX TOC** after any edit: right-click the Table of Contents →
   *Update Field* → *Update entire table*.
3. **Reviewer slots.** Suggested expertise profiles: random-matrix theory / quantum
   chaos; computational condensed matter (lattice models); numerical analysis
   (spectral statistics and unfolding estimators).
4. **Optional v3.2 re-run (20 min).** `julia julia_patched/ab_cloud_v23_v3.2.jl --test 34`
   executes the confrontation test against the v3.2 reference build; the predicted
   pooled D = 0.03–0.06 (window < 0.10, falsifiability clause at 0.08) can be appended
   to Chapter 34 as a one-line confirmation with its own console capture.
5. **Verify the archive checksum** after any transfer and before upload
   (`sha256sum` manifest can be regenerated with `find . -type f | sort | xargs sha256sum`).

## 4. September 2026 addendum (v3.3 build)

- [x] New final chapter "Addendum: Post-v3.2 Independent Verification and Deep Diagnostics of
      Test 34" inserted in `AB_Cloud_v23_Monograph` (DOCX + PDF, TOC refreshed), in
      `AB_Cloud_v23_Academic_Essence` (DOCX + PDF, TOC refreshed), and in both LaTeX preprints
      (recompiled).
- [x] `cover_letter.docx` / `.pdf` — new paragraph reporting the addendum outcome (pooled
      D = 0.0970 > 0.08 → pre-registered promotion to a physical effect; effective Poisson
      admixture w* ≈ 0.28; residual at the ζ-vs-GUE floor).
- [x] `lab_standalone/` — the three standalone codes (finite-size laboratory, suite working
      copy, HP·MERIDIAN) with folder README.
- [x] `run_data/run_20260917_080329_m2/` and `run_data/run_20260917_084900_m3/` — raw runs
      behind every number of the addendum (reports, spacing arrays, plots, mixture-fit analysis).
- [x] `SHA256SUMS.txt` regenerated for the v3.3 tree.
