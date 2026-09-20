# `preprint/` — The Monograph Preprint (LaTeX + PDF)
> The 305-page PLOS-style preprint of the monograph: LaTeX source, compiled PDF, the 225-page Appendix B code listing, and the addendum figures.

_Location: [unpacked/](../README.md) › [preprint/](README.md)_

This folder packages the **monograph preprint** — the arXiv/journal-distribution edition of the main manuscript, typeset in a PLOS-style single-column layout and compiled to 305 pages with the September 2026 addendum (Add.1–Add.8) integrated. It exists so the work can circulate before and alongside journal submission, and it is the edition whose LaTeX source is fully open: every table, figure reference and verdict line of the preprint can be diffed against the run archive published in this repository.

## The three artefacts

**`monograph_preprint.tex` (274 KB).** The complete LaTeX source. It compiles with [`tectonic`](https://tectonic-typesetting.github.io/) (the engine the package uses) or any recent TeX Live: `tectonic monograph_preprint.tex`. The source is self-contained apart from the two `addendum_figures/` PNGs and the Appendix B listing, which it ingests via `\includepdf` from `appendix_b_code.pdf`.

**`monograph_preprint.pdf` (305 pp.).** The compiled preprint. Structure mirrors the monograph: abstract, contents, Part I (framework), Part II (the 38 test chapters), Part III (synthesis and scope of validity), references, appendices A, C, D, E — and Appendix B as the included 225-page code listing — closed by the Test 34 addendum chapter with the Klein quartic pass.

**`appendix_b_code.pdf` (225 pp., 32,095 lines).** The complete v3.3 source of `../lab_standalone/ab_cloud_v23.jl` typeset as a standalone, line-numbered listing. It is included both inside the preprint (as Appendix B) and kept here as a separate artefact so referees can consult the code without opening the 305-page main file.

## The addendum figures

[`addendum_figures/`](addendum_figures/README.md) holds the two English-labelled figures that the September 2026 addendum chapters embed: the disorder (W) sweep panel and the GUE+Poisson mixture-decomposition panel. The same figures ship with `preprint2/` for the Academic Essence edition, and the post-processing behind them is documented in the `run_20260917_080329_m2/analysis_addendum/` folder of the run data.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `appendix_b_code.pdf` | 1.5 MB | Appendix B as a standalone listing — the complete v3.3 source, 32,095 lines, 225 pages. |
| `monograph_preprint.pdf` | 3.6 MB | The monograph preprint — compiled PDF (305 pages, Add.8 included). |
| `monograph_preprint.tex` | 267.9 KB · 2162 lines | The monograph preprint — complete LaTeX source (PLOS-style single column; compiles with tectonic). |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`addendum_figures/`](addendum_figures/README.md) | 2 files | Addendum figures of the monograph preprint |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../README.md](../README.md)._