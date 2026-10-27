# Changelog — AB-Cloud Journal submission shelf

The Journal shelf is **sealed, not versioned**: the submission packages are
frozen artifacts — each zip carries its own `SHA256SUMS.txt`, and the
folder-level [`SHA256SUMS.txt`](SHA256SUMS.txt) pins the zips and preview
PDFs byte-for-byte. This changelog therefore records the *editorial history
of the shelf* — what was added **around** the sealed packages and when the
packages themselves were re-sealed. The packages are never edited in place:
a corrected manuscript means a rebuilt, re-sealed zip and a fresh line below.

> [!IMPORTANT]
> **Record correction (2026-10-19).** An earlier revision of this changelog
> dated below described a "full re-seal of 2026-10-18" and announced
> folder-level checksums, visible guide copies and an assets catalogue as
> landed. A repository audit on 2026-10-19 showed that none of that had
> actually been committed: the zips kept their 2026-10-08 bytes (committed
> 2026-10-16), and the announced scaffolding files were absent from the
> repository. The 2026-10-18 entry below has been rewritten to describe
> only what that commit actually contained; the re-seal itself was performed
> and committed on 2026-10-19 (entry below). The shelf's honesty layer
> applies to its own history as well.

## 2026-10-19 — Full re-seal: performed, verified and committed

The re-seal announced for 2026-10-18 was **actually executed** on this date,
together with everything the 2026-10-18 uplift had announced but not
committed. Details:

- **NSR manuscript: one stale paragraph removed, PDF rebuilt.** Appendix B
  of `manuscript_NSR.tex` carried two contradictory provenance paragraphs —
  a leftover "This appendix reproduces the complete Julia source …" sentence
  superseded by the Supplemental-Material paragraph next to it ("…the
  verbatim 32,095-line listing … is not printed in the body …"). The stale
  paragraph was deleted; no other character of the manuscript changed. The
  PDF was recompiled with the original engine and documented recipe
  (Tectonic 0.15.0, XeTeX bundle, the two local `nsr.cls` compatibility
  patches of `compile_notes.md`): the manuscript is now **99 pp.** in the
  journal layout (the removal shortened the flow by one page; the trailing
  content is unchanged and was verified against the previous build's final
  pages). The shipped `nsr.cls` remains byte-identical to the journal
  original. The line-count figures inside the manuscript ("31,239-line")
  were audited and stand: they refer to the build that executed the
  26.04-hour reference run, while the 32,095-line listing shipped in
  Appendix B / supplemental is the v3.3 build of 2026-09-19 — two builds,
  both named with their own correct numbers.
- **Service files inside the zips: corrected.** The stale "AB-Cloud v23
  academic package" naming in the NSR and SciPost guide headers now reads
  "the unified academic edition"; the SciPost guide's two references to the
  arXiv package use the real filename (`arXiv_submission_AB-Cloud.zip`, not
  `…_v23.zip`); the SciPost guide's Core version is described as its actual
  11 pages (was "~15 pp."); the arXiv metadata README's own header drops the
  stale v23 tag, its suggested Comments field now states the real arXiv
  compile size ("54 pages, 48 figures" — was "60 pages"), and its licence
  line now recommends the **non-exclusive licence to distribute** (consistent
  with the strictly personal licence — the earlier wording read as a
  CC BY 4.0 recommendation); each in-zip guide gained a short shelf-pointers
  note (visible `guides/` copies, folder-level sums, status tracker);
  `compile_notes.md` records the rebuild verification.
- **Bundle mini README: rewritten.** The all-in-one bundle's README listed
  stale zip names (`…_AB-Cloud_v23.zip`), carried the same stale v23 title
  and a "CC BY 4.0 recommended" arXiv licence line contradicting the shelf.
  It now lists the real zip names, adds the verified preview byte-identity
  notes, carries the corrected licence guidance and points to the shelf.
- **Checksums: regenerated everywhere.** In-zip `SHA256SUMS.txt` of all
  three packages rebuilt and self-verified (`sha256sum -c` PASS; 868 / 867 /
  50 entries); file-entry counts unchanged (1,151 / 1,150 / 128 / 8); the
  folder-level [`SHA256SUMS.txt`](SHA256SUMS.txt) — now actually present —
  pins the eight new artifacts and records three verified byte-identity
  cross-checks (NSR, SciPost and SciPost-Core previews against their in-zip
  sources).
- **Missing scaffolding landed.** The folder-level `SHA256SUMS.txt`, the
  three visible `guides/` mirrors (extracted from the re-sealed zips with
  provenance stamps) and `assets/README.md` — announced on 2026-10-18 — are
  committed with this re-seal.
- **Previews re-synced.** `NSR_manuscript_preview.pdf` replaced with the new
  99 pp. build (byte-identical to the in-zip `manuscript_NSR.pdf`); the
  SciPost, SciPost-Core and arXiv previews are unchanged — their PDFs are
  byte-faithful to the 2026-10-08 build.
- **Editorial surfaces updated.** README (honest dates, 99 pp., precise
  entry/size counts, timeline-honesty block), FAQ (verification counts,
  build-recipe wording, re-seal date), CITATION.cff (release date), and
  this changelog. Statuses unchanged: nothing has been submitted yet.

## 2026-10-18 — Journal shelf uplift (editorial)

The shelf caught up with its parent folder's standards **in its editorial
layer**. Committed on this date (commit `70da9ce`):

- **`SUBMISSION_STATUS.md`.** A hand-maintained tracker for the submission
  life-cycle of all three venues (Prepared → Submitted → Under review →
  Decision) with an event log and update instructions for the Author.
- **`FAQ.md`.** Answers covering the questions the shelf actually triggers:
  which SciPost version, arXiv endorsement, the "not for upload" previews,
  the two-level verification workflow, the honesty boundary, the strictly
  personal licence, and what to do when a checksum fails.
- **`CITATION.cff`.** The shelf becomes formally citable (CFF 1.2.0, DOI
  10.5281/zenodo.21825394) alongside the unified edition's own citation
  file.
- **`guides/README.md`.** The index and the provenance rule for the visible
  guide mirrors.
- **`README.md` rebuilt.** Honest-boundary block, the verdict-sync section
  "Where the science stands now", a "Which file do you need?" router,
  per-zip content trees, the two-level verification section, the status
  board, the guides index and the citation block.

> [!NOTE]
> **Not landed with this commit** (contrary to what an earlier revision of
> this changelog stated): the folder-level `SHA256SUMS.txt`, the three
> visible `guides/` guide mirrors, `assets/README.md`, and the re-seal of
> the packages. All of the above arrived with the **2026-10-19** re-seal
> entry above; the eight sealed artifacts kept their 2026-10-08 bytes until
> that date. The repository's commit history is the audit trail.

## 2026-10-16 — Packages committed to the repository

The four zips (`NSR_JINR_submission_AB-Cloud.zip`,
`SciPost_Physics_submission_AB-Cloud.zip`, `arXiv_submission_AB-Cloud.zip`,
`AB-Cloud.zip`), the four preview PDFs, the shelf `assets/` (banner,
emblem) and the first `README.md` were committed to
[github.com/wild8highlander/ab-cloud-research](https://github.com/wild8highlander/ab-cloud-research)
(commits `34a732f`, `4616fc7`). The zips' bytes date from the 2026-10-08
sealing and stayed untouched until the 2026-10-19 re-seal.

## 2026-10-08 — Initial sealed packages

The shelf opens with the first journal deliverables compiled from the
unified edition:

- `NSR_JINR_submission_AB-Cloud.zip` — full manuscript (100 pp.) on the
  official `nsr.cls` v1.5, cover letter, 48 figures, supplemental (Python
  clone, standalone lab codes, full run data, code-listing PDF), in-zip
  `SHA256SUMS.txt`, wizard guide.
- `SciPost_Physics_submission_AB-Cloud.zip` — Publication version (60 pp.)
  plus the condensed Core version (11 pp.) on the official `SciPost.cls`,
  cover letter, 48 figures, supplemental, in-zip `SHA256SUMS.txt`, wizard
  guide.
- `arXiv_submission_AB-Cloud.zip` — flat preprint package: `main.tex`
  (standard `article` class, inline bibliography), `figures/` (48),
  metadata README, in-zip `SHA256SUMS.txt`.
- `AB-Cloud.zip` — all-in-one bundle: the three venue zips, the four
  preview PDFs and a mini README.
- Four preview PDFs for reading without downloading; folder `README.md`
  with the packages table, SciPost guidance, human steps and licence note.
