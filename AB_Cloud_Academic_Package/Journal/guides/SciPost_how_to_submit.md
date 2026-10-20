<!-- Provenance: render-friendly copy of `scipost_submission/README_how_to_submit.md` inside
     `SciPost_Physics_submission_AB-Cloud.zip`, extracted on 2026-10-19 from the 2026-10-19 re-seal.
     The copy inside the zip is the source of truth; the zips are
     pinned by ../SHA256SUMS.txt. -->

> [!NOTE]
> **Provenance.** Render-friendly copy of `scipost_submission/README_how_to_submit.md` inside
> `SciPost_Physics_submission_AB-Cloud.zip`, extracted on 2026-10-19 from the 2026-10-19 re-seal.
> The copy **inside the zip is the source of truth**; the zips are
> pinned by [`../SHA256SUMS.txt`](../SHA256SUMS.txt). Index and the
> provenance rule: [`README.md`](README.md) in this folder.

# Submission Package — SciPost Physics (article type: Publication)

Prepared: 8 October 2026 · from the unified academic edition (github.com/wild8highlander/ab-cloud-research)

## Manuscript

- **Title:** From Hilbert–Pólya to a Lattice Hamiltonian: The Academic Essence of AB-Cloud v23
- **Author:** Iskhak K. Isaev (corresponding), ORCID 0009-0003-7299-0701,
  e-mail aslan08_05@mail.ru
- **Affiliation:** AB-Cloud Research Laboratory, Independent Researcher,
  Prospekt Lenina 29, Apt. 140, Nalchik, Kabardino-Balkarian Republic, Russian Federation
- **Suggested specialties (wizard):** Statistical Physics; Mathematical Physics;
  (optional) Quantum Information / Condensed Matter — choose at submission
- **Format (Publication, primary):** `scipost_manuscript.tex` typeset with the official
  **SciPost.cls** template (line numbers enabled); `scipost_manuscript.pdf` — compiled
  reference PDF (60 pp.), header "SciPost Physics | Submission".
- **Format (SciPost Core, alternative):** `scipost_core_manuscript.tex` — a condensed
  11-page rendition of the same results for the short-format **Core** article type,
  same template; `scipost_core_manuscript.pdf` — compiled reference PDF. Submit ONE of
  the two versions; if you choose Core, the wizard article type is **Core** and the
  abstract/keyword fields are taken from the Core file.
- **Related delivery:** `arXiv_submission_AB-Cloud.zip` — an arXiv-ready flat
  package (standard `article` class, no journal classes) for a parallel preprint deposit.

## How to submit (scipost.org)

1. Create an account at scipost.org (orcid.org sign-in recommended).
2. *Submit* → **SciPost Physics** → type **Publication** → fill mandatory wizard fields:
   Title, Author list, Abstract (copy from the manuscript), Specialties.
3. Upload the LaTeX source archive: this ZIP's manuscript files
   (`scipost_manuscript.tex`, `SciPost.cls`, `SciPost_bibstyle.bst`, `figures/`) —
   SciPost recompiles the source on their side.
4. Cover letter: paste `cover_letter_SciPost.pdf` / its text into the submission form
   (SciPost handles the letter as a form field; the PDF is included for reference).
5. Supplementary: upload `supplemental/` or (preferred for size) reference the Zenodo
   archive DOI 10.5281/zenodo.21825394 and the GitHub repository in the Data
   Availability section (already present in the manuscript).
6. Licence: SciPost publications are CC BY 4.0 — acceptance is stated in the cover letter.
7. Suggested referees (wizard, optional): profiles in random-matrix theory / quantum
   chaos; computational condensed matter; numerical analysis of spectral statistics.

## Notes on the adaptation

- The bilingual (EN+RU) annotation of the original preprint was reduced to the English
  abstract, keywords and declarations — SciPost publishes in English only.
- Unicode characters authored for the XeTeX original (Greek letters, ⟨r⟩, ±, ≈, °, √ …)
  were transliterated to standard LaTeX macros so the document compiles with pdfLaTeX
  under the SciPost class (`\RequirePackage[utf8]{inputenc}`).
- `\part*` dividers of the monograph were converted to unnumbered visual dividers;
  the TOC was removed (SciPost articles carry no TOC); `\linenumbers` is enabled for
  refereeing.
- Declarations (Funding, Conflicts of interest, Data availability, CRediT author
  contributions) were added before the reference list, as expected by SciPost.

## Contents of this archive

| Path | What it is |
|---|---|
| `scipost_manuscript.tex` / `.pdf` | Manuscript, article type **Publication** (SciPost.cls source + compiled PDF) |
| `scipost_core_manuscript.tex` / `.pdf` | Alternative condensed manuscript for the **Core** article type (11 pp.) |
| `SciPost.cls`, `SciPost_bibstyle.bst` | Official SciPost template files (unchanged) |
| `cover_letter_SciPost.tex` / `.pdf` | Cover letter for the submission wizard |
| `figures/` | 48 figures (PNG, original names) |
| `supplemental/` | Lab code + Python clone + full run-data archive + code listing PDF |
| `supplemental/README_supplemental.md` | Reading guide for the supplementary data |
| `SHA256SUMS.txt` | Checksums of every file in this package |

**Related delivery:** the arXiv-ready flat package is shipped separately as
`arXiv_submission_AB-Cloud.zip` (standard `article` class, no journal class files,
inline bibliography, arXiv metadata README).

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
