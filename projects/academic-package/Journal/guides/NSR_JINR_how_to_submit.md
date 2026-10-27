<!-- Provenance: render-friendly copy of `nsr_submission/README_how_to_submit.md` inside
     `NSR_JINR_submission_AB-Cloud.zip`, extracted on 2026-10-19 from the 2026-10-19 re-seal.
     The copy inside the zip is the source of truth; the zips are
     pinned by ../SHA256SUMS.txt. -->

> [!NOTE]
> **Provenance.** Render-friendly copy of `nsr_submission/README_how_to_submit.md` inside
> `NSR_JINR_submission_AB-Cloud.zip`, extracted on 2026-10-19 from the 2026-10-19 re-seal.
> The copy **inside the zip is the source of truth**; the zips are
> pinned by [`../SHA256SUMS.txt`](../SHA256SUMS.txt). Index and the
> provenance rule: [`README.md`](README.md) in this folder.

# Submission Package — Natural Science Review (JINR)

Prepared: 8 October 2026 · from the unified academic edition (github.com/wild8highlander/ab-cloud-research)

## Manuscript

- **Title:** An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros:
  A 38-Test Computational Verification Suite
- **Author:** Isaev Iskhak Khamzatovich (I. K. Isaev), ORCID 0009-0003-7299-0701,
  corresponding author e-mail aslan08_05@mail.ru
- **Affiliation:** AB-Cloud Research Laboratory (Independent Researcher),
  Prospekt Lenina 29, Apt. 140, Nalchik, Kabardino-Balkarian Republic, Russian Federation
- **Journal topic selected at submission:** Physics
- **Format:** `manuscript_NSR.tex` typeset with the journal's official **nsr.cls v1.5**
  template (11.12.2024) and `nsr.bst`; `manuscript_NSR.pdf` — compiled reference PDF
  (99 pp. in the journal print layout).

## How to submit (nsr.jinr.int)

1. Register / log in at the NSR Submission server (nsr.jinr.int → *Submit Your Article*).
2. Select topic **Physics** (or Mathematics — at your discretion).
3. Upload **`manuscript_NSR.pdf`** and **`manuscript_NSR.tex`** — the LaTeX-2e source
   is the preferred working format of the journal. Compile locally with
   `pdflatex manuscript_NSR.tex` (run twice) if the editors request a re-build.
4. Upload the **`figures/`** folder — all 48 figure files as separate files (PNG),
   exactly as referenced by the source.
5. Upload **`cover_letter_NSR.pdf`** via the Cover-Letter / Comments channel.
6. Upload **`supplemental/`** as Supplemental Material (see below).
7. Fill the metadata forms: CRediT roles (single author — all roles), Funding
   statement (already worded per journal requirements inside the manuscript),
   Conflicts of Interest ("The author declares no conflicts of interest."),
   Data Availability (already inside the manuscript).
8. The copyright agreement is signed at the editorial stage; as an independent
   researcher without a Russian institute affiliation, no institutional permission
   letter is required.

## Requirements checklist (nsr.jinr.int / For Authors — verified 08.10.2026)

- [x] LaTeX-2e template nsr.cls, no personal macros (only `longtable` added as a
      standard package)
- [x] Abstract ≤ 250 words (247 words), keywords 1–6 (6), English
- [x] Title page: title, author initials + ORCID, affiliation, corresponding author
      footnote with e-mail
- [x] Figures as separate files, referenced with original names, sequentially numbered
- [x] Equations displayed and numbered in order of reference
- [x] Sections follow the journal's recommended structure where applicable
      (Introduction … Conclusions) with appendices A–E
- [x] Declarations: Author contributions (CRediT), Funding (journal's standard
      wording), Conflicts of Interest, Data Availability Statement
- [x] Supplemental Material reference line included in the reference list
      ("See Supplemental Material at [URL will be inserted by publisher] …")
- [x] References in NSR style ("A. Author, Title, Journal Vol (Year) Pages. doi:…")
      with DOIs verified against Crossref on 08.10.2026
- [x] Table of contents included (allowed for articles > 30 pages), line numbers on

## Notes on the adaptation

- The complete 32,095-line Julia source listing was moved out of the manuscript body
  into Supplemental Material (`appendix_b_code_full_source_listing.pdf`), per the
  journal's Supplemental Material policy; Appendix B of the manuscript describes this
  and keeps the provenance text.
- Figure file names were restored from the repository's unique-filename edition
  (e.g. `plot_01_A01P.png` → `plot_01.png`) so that the LaTeX source of the original
  preprint references resolve as-is.

## Contents of this archive

| Path | What it is |
|---|---|
| `manuscript_NSR.tex` / `.pdf` | Manuscript (nsr.cls source + compiled PDF) |
| `nsr.cls`, `nsr.bst` | Official journal template files (v1.5, unchanged) |
| `cover_letter_NSR.tex` / `.pdf` | Cover letter addressed to the Editor-in-Chief |
| `figures/` | 48 figures (PNG, original names) |
| `supplemental/` | Lab code + Python clone + full run-data archive + code listing PDF |
| `supplemental/README_supplemental.md` | Reading guide for the supplementary data |
| `SHA256SUMS.txt` | Checksums of every file in this package |

**Local-compile note:** the bundled `nsr.cls` is byte-identical to the journal's
original. If you compile with TeX Live, no patches are needed. (A tiny compatibility
patch for `fancyhdr` v4.0.1, used only for the bundled reference PDF, is documented in
`compile_notes.md`.)

---

## Shelf pointers (AB-Cloud Journal shelf)

This package lives in `AB_Cloud_Academic_Package/Journal/` of
[github.com/wild8highlander/ab-cloud-research](https://github.com/wild8highlander/ab-cloud-research).
The shelf around it:

- **Visible copies of the wizard guides** (including this one) — `guides/`, one
  folder up in the Journal folder; the copy inside this zip is the source of truth.
- **Folder-level integrity** — `SHA256SUMS.txt` in the Journal folder pins this
  zip and all preview PDFs (`sha256sum -c SHA256SUMS.txt`).
- **Submission life-cycle** — `SUBMISSION_STATUS.md` tracks every venue's status
  with a dated event log.
- **Editorial history** — `CHANGELOG.md` records the 19 October 2026 re-seal
  that produced the current bytes of this package.

Re-sealed: 19 October 2026.
