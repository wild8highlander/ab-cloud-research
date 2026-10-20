<!-- Provenance: render-friendly copy of `arxiv_submission/README_arxiv_metadata.md` inside
     `arXiv_submission_AB-Cloud.zip`, extracted on 2026-10-19 from the 2026-10-19 re-seal.
     The copy inside the zip is the source of truth; the zips are
     pinned by ../SHA256SUMS.txt. -->

> [!NOTE]
> **Provenance.** Render-friendly copy of `arxiv_submission/README_arxiv_metadata.md` inside
> `arXiv_submission_AB-Cloud.zip`, extracted on 2026-10-19 from the 2026-10-19 re-seal.
> The copy **inside the zip is the source of truth**; the zips are
> pinned by [`../SHA256SUMS.txt`](../SHA256SUMS.txt). Index and the
> provenance rule: [`README.md`](README.md) in this folder.

# arXiv submission package — AB-Cloud (Academic Essence)

Prepared: 8 October 2026. Flat, arXiv-ready: standard `article` class only, no
journal class files, inline `thebibliography` (no BibTeX run needed).

## Files

| Path | What it is |
|---|---|
| `main.tex` | Master file (arXiv auto-detects it) |
| `figures/` | All 48 figures (PNG), referenced by relative path |
| `README_arxiv_metadata.md` | This file — metadata to paste into the submission form |

Compile locally with `pdflatex main.tex` (twice) if you want to preview.

## Suggested metadata for the arXiv form (arxiv.org/submit)

- **Primary classification:** math-ph (Mathematical Physics)
- **Cross-lists:** math.NT (Number Theory); math.SP (Spectral Theory)
- **Title:**
  From Hilbert–Polya to a Lattice Hamiltonian: The Academic Essence of AB-Cloud v23
- **Authors:** Iskhak K. Isaev (ORCID 0009-0003-7299-0701)
- **Abstract (plain text):**

  The Hilbert-Polya programme seeks a self-adjoint operator whose spectrum is exactly
  the sequence of imaginary parts of the non-trivial zeros of the Riemann zeta function.
  This monograph presents, in purely academic form, a lattice-operator realisation of
  that programme built on three coordinated components: an exact arithmetic dictionary
  that couples Gram points to zeta zeros at the critical point alpha = 1/2 with a proven
  +/-E chiral pairing; an Aharonov-Bohm lattice Hamiltonian whose flux sector encodes
  the rational phase delta_C = pi/7; and a family of closed-form constants — the
  spinorial phase arg gamma* = 89.874 deg, the fractal factor of unit modulus, and the
  half-factorial normalisation (1/2)! = sqrt(pi)/2 — that tie the spectral data to the
  Gaussian unitary ensemble (GUE). The construction was subjected to a single,
  end-to-end computational examination of 26.04 hours on the first 50,000 zeta zeros,
  from which sixty publication-grade figures and seventy-nine quantitative judgements
  were distilled. The headline spectral facts: the level-spacing ratio statistic of the
  lattice ensemble converges to <r> = 0.5991 +/- 0.0075 against the GUE reference
  0.59960; the one-sample Kolmogorov-Smirnov distance to the GUE spacing law is
  D = 0.0216 on the full range; number variance and spectral rigidity track the GUE
  predictions across nine window scales; and the flux identity Phi_AB = pi/7 holds to
  256 binary digits. Where strict null hypotheses are rejected at this sample size, the
  accompanying effect-size windows are satisfied by the same data, and the distinction
  between statistical power and physical deviation is analysed explicitly. The monograph
  closes with an assessment of what the framework establishes — a computable,
  topologically anchored, GUE-consistent candidate operator — and what it does not: an
  analytic proof that the dictionary converges, and a closing of the residual
  direct-confrontation gap between the lattice spectrum and the zeros themselves. All
  artefacts, including the complete source of the reference implementation and the
  archived dataset, are openly available under DOI 10.5281/zenodo.21825394.

- **Comments field (suggested):**
  54 pages, 48 figures. Full verification record (code, run archive, audit tier):
  github.com/wild8highlander/ab-cloud-research — archived dataset DOI
  10.5281/zenodo.21825394.
- **License:** the **non-exclusive licence to distribute** — arXiv's default
  and most restrictive option, recommended here because it is consistent with
  the strictly personal licence of this repository. Choose CC BY 4.0 instead
  only if you deliberately want to grant reuse rights from the start (SciPost
  publishes its articles under CC BY 4.0).
- **Author affiliation entered in the form:** AB-Cloud Research Laboratory, Independent
  Researcher, Prospekt Lenina 29, Apt. 140, Nalchik, Kabardino-Balkarian Republic,
  Russian Federation.

## Submission steps

1. arxiv.org → **Submit** (ORCID/Google sign-in; first-time submitters need
   endorsement — request it from an author in math-ph before submitting).
2. Upload the ZIP of this folder (tex + figures) or the individual files.
3. Paste the metadata above into the corresponding wizard fields.
4. Check the compiled preview arXiv shows you, correct any warnings, and release.

---

## Shelf pointers (AB-Cloud Journal shelf)

This flat package lives in `AB_Cloud_Academic_Package/Journal/` of
[github.com/wild8highlander/ab-cloud-research](https://github.com/wild8highlander/ab-cloud-research)
(`arXiv_submission_AB-Cloud.zip`). The shelf around it:

- **Visible copy of this metadata guide** — `guides/arXiv_metadata.md` in the
  Journal folder; the copy inside the zip is the source of truth.
- **Folder-level integrity** — `SHA256SUMS.txt` in the Journal folder pins the
  arXiv zip and all preview PDFs (`sha256sum -c SHA256SUMS.txt`).
- **Submission life-cycle** — `SUBMISSION_STATUS.md` tracks every venue's status
  with a dated event log.
- **Editorial history** — `CHANGELOG.md` records the 19 October 2026 re-seal
  that produced the current bytes of this package.

Re-sealed: 19 October 2026.
