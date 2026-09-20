# AB-Cloud v23 — Complete Academic Package (v34) — GitHub Edition

This folder is the complete, self-contained GitHub edition of the **AB-Cloud v23 SUPERCOMBO** submission package — the laboratory's 32,095-line Julia 1.12 verification apparatus for the Aharonov–Bohm lattice-operator framework of the Riemann ζ zeros, together with every document, dataset, run archive and source file that accompanies the monograph *"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros: A 38-Test Computational Verification Suite"*. Everything the original ZIP archive shipped is here: the ZIP itself (preserved bit-for-bit under [`zip_archive/`](zip_archive/) with its SHA-256 checksum) and the full unpacked tree (under [`unpacked/`](unpacked/)), reorganised so that **every single folder carries its own detailed README** explaining what it contains, why it exists, and how to read it.

## What is the AB-Cloud framework?

The AB-Cloud framework proposes a concrete statistical bridge between two objects that mathematics has been trying to reconcile for decades: the non-trivial zeros of the Riemann ζ function, and the spectrum of a Hermitian lattice Hamiltonian threaded by Aharonov–Bohm magnetic flux quanta. The construct is engineered so that its spectral statistics fall into the GUE (Gaussian Unitary Ensemble) universality class — the same class the Montgomery–Odlyzko programme predicts for the ζ zeros — while its exact layer (hermiticity, flux quantization, Byers–Yang invariance, chiral pairing, Connes self-duality, an identity chain of geometric phases) is verifiable to machine precision and to 256-bit arbitrary precision where needed. The verification record shipped in this package subjects that construct to **38 numbered computational tests**: statistical distribution batteries, long-range random-matrix statistics, exact structural certificates, topological invariants, finite-size scaling laws, robustness stress tests, and the direct AB-cloud-versus-ζ confrontation that gives the record its centrepiece.

## The verification record at a glance

- **Reference run:** `run_20260914_234626` — 38 tests in a single interactive session of 93,748 s (26.04 h) on Julia 1.12.0; two-pass protocol (primary verdict + HARDCORE pass-2 deep audit).
- **79 verdict entries** (66 PASS / 13 FAIL at the primary tier), preserved verbatim; **audit tier:** 35 HARDCORE/SERIES/AUDIT batteries, 127 individually logged sub-checks, 121 passed in-run.
- **Exact layer:** machine-zero residuals for hermiticity, flux quantization, Byers–Yang invariance, chiral pairing and the analytic identity chain; rational identities verified at 256-bit precision.
- **Spectral layer:** every class-discriminating statistic places the lattice spectrum and the ζ dictionary on the GUE side of its pre-registered window at effect size.
- **September 2026 addendum (Add.1–Add.8):** cross-language reproduction, disorder sweep, deep diagnostics, effective GUE+Poisson mixture decomposition, and the **Klein quartic PSL(2,7) ensemble pass at 100,000 zeros** — pooled D = 0.0808, d_GUE = 0.0044, composite criterion satisfied (GUE-CONSISTENT), the first such verdict on a closed Hurwitz surface.

## How this folder is organised

| Path | What it is |
|---|---|
| [`zip_archive/`](zip_archive/) | The original `AB_Cloud_v23_Full_Package_Academic_v34.zip` (39.4 MB), preserved untouched, with SHA-256 and verification instructions. |
| [`unpacked/`](unpacked/) | The full unpacked tree: monograph (PDF + DOCX), the Academic Essence companion, both LaTeX preprints, submission documents, the standalone Julia laboratories, the Python reimplementation, and the complete run-data archives — **each folder with its own detailed README.md**. |
| [`FILE_INDEX.md`](FILE_INDEX.md) | Every file in the package: path, size, description, plus the complete original-to-published filename mapping. |
| [`SHA256SUMS_unpacked.txt`](SHA256SUMS_unpacked.txt) | SHA-256 checksums of every file in `unpacked/` (published names), for byte-level verification. |

## The unique-filename edition

The original ZIP reuses a handful of file names across folders (`report.md` in each of the 38 test folders, `plot_01.png`, `animation.gif`, `index.html`, and so on). On GitHub, identical names in different folders are perfectly legal — but they make cross-referencing, checksumming and file search ambiguous. This edition therefore gives **every colliding file a globally unique name** by appending a short location code: the reference run's Test 4 report `report.md` became `report_A04.md` (run A, test 04), its log `computation_log_A04L.txt` (L = logs subfolder), its figure `plot_01_A04P.png` (P = plots subfolder). The original ZIP itself remains untouched under `zip_archive/`, and the complete mapping table is [`FILE_INDEX.md`](FILE_INDEX.md) — nothing is renamed silently.

## Reading paths for different visitors

- **"What is this project?"** — read this page, then [`unpacked/README.md`](unpacked/README.md), then the monograph PDF: `unpacked/AB_Cloud_v23_Monograph.pdf`.
- **"I want the evidence."** — go to [`unpacked/run_data/`](unpacked/run_data/README.md): the reference-run archive with all 38 test folders, the four-format FINAL_REPORT, the September 2026 addendum runs, and the audit-tier reading guide.
- **"I want the exact numbers of one test."** — `unpacked/run_data/run_20260914_234626/test_XX_<slug>/README.md` for the test you need; each such README carries the verdicts, the verification statement, the computation-log excerpt and the verbatim console capture.
- **"I want to run the code."** — the standalone Julia laboratories live in [`unpacked/lab_standalone/`](unpacked/lab_standalone/README.md) (the v3.3 suite `ab_cloud_v23.jl`, the finite-size laboratory `finite-size_lab.jl` v1.3, and the H-audit module), and a dependency-light **Python reimplementation** of all 38 tests ships in [`unpacked/python_clone/`](unpacked/python_clone/README.md).
- **"I want the publication paperwork."** — cover letter, submission forms, checklist and journal short-list sit at the top of [`unpacked/`](unpacked/README.md), each described in its README.

## Provenance and integrity

The package was frozen as **v34** on 2026-09-19 and supersedes the v33 freeze; the delta is documented in the original package README (preserved at [`unpacked/README_original.md`](unpacked/README_original.md)) and inside the monograph's addendum chapters. The ZIP's SHA-256 checksum is recorded in [`zip_archive/README.md`](zip_archive/README.md); every unpacked file is checksummed in `SHA256SUMS_unpacked.txt`. The dataset carries DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394), and the author's ORCID is [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701). All descriptive texts in this GitHub edition were prepared for this repository so that every folder explains itself; the underlying scientific content is quoted or summarised from the package's own documents.
