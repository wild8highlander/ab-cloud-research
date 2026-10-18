# Changelog — AB-Cloud Journal submission shelf

The Journal shelf is **sealed, not versioned**: the submission packages are
frozen artifacts — each zip carries its own `SHA256SUMS.txt`, and the
folder-level [`SHA256SUMS.txt`](SHA256SUMS.txt) pins the zips and preview
PDFs byte-for-byte. This changelog therefore records the *editorial history
of the shelf* — what was added **around** the sealed packages — rather than
version bumps. The packages themselves are never edited in place: a corrected
manuscript means a rebuilt, re-sealed zip and a fresh line below.

## 2026-10-19 — Verdict sync: the shelf speaks the 2026-10-16 audit state

Editorial sync only — **no sealed byte touched**: the eight artifacts, the
folder-level sums, the in-zip manifests and the `guides/` mirrors are
exactly as the 2026-10-18 re-seal left them. What changed is the shelf's
prose about the science, now aligned with the unified edition's verdict
ledger as synced on 2026-10-16 (see
`../AB_Cloud_Academic_Package/CHANGELOG.md`):

- **README gains "Where the science stands now"** — a compact ledger table
  mirroring the unified edition's honesty discipline: G1–G5 all **YES**
  (G2 flipped NO → YES on the gates' D_nn = 0.0079, C3 audit v2.0.7, with
  the bit-level branch T18 recorded as the verdict's stated boundary; G5
  flipped NO → YES on the convergence ladder, audit v2.0.8: gate
  ψ-correlation −0.12 → +0.09 → +0.24, floor 0.0324 → 0.0220, best
  D = 0.0318), RH **CERTIFIED — not proved** (V13, unlocked v1.2.1), the
  blind campaign **C17 NEGATIVE** by its pre-registered criterion (1.04×
  over the primes-free null, z_GUE = −3.3; the C17b valley windows read
  the blind count exactly, 19.0004 → 19 and 25.00005 → 25), and the
  **algebraic_map** exact closure in ℚ (all 25 char-poly coefficients,
  D_25 = 0; the two branches of Φ agree to 10⁻³⁰³; the Weyl bound explains
  the decoding error).
- **FAQ §5 extended** with the same gate state and the negative results; a
  new **FAQ §11** explains the layering — the packages carry the
  reference-run record they were compiled with (2026-10-08), the living
  ledger lives in the unified edition (2026-10-16) — and why the two
  coexist without contradiction.
- **CITATION.cff** abstract names the current gate state; the FAQ badge
  moves 10 → 11 answers; `guides/README.md` and the status board's event
  log point to the synced ledger.
- Timeline honesty is explicit throughout: the 16 October 2026 audit wave
  postdates the packages' compilation (8 October 2026); a verdict-synced
  re-issue of the packages would follow the sealed-package routine below
  and has not been performed.

## 2026-10-18 — Full re-seal: all eight artifacts rebuilt

Every upload-bound artifact on the shelf — the three venue zips, the
all-in-one bundle and all four preview PDFs — was **rebuilt and re-sealed**.
The rebuild is a faithful reproduction, not a revision:

- **Manuscript text: untouched.** No character of any manuscript, cover
  letter or form-metadata block changed. All six PDFs were recompiled with
  the same engine the original build used (Tectonic 0.15.0, XeTeX bundle,
  following the documented recipe in `compile_notes.md`), and every
  recompiled PDF matches its predecessor page-for-page — 100 pp. (NSR),
  60 pp. + 11 pp. (SciPost Publication + Core), 54 pp. (arXiv) — with byte
  sizes within 5 bytes of the sealed originals (the delta is PDF build
  metadata only).
- **Service files inside the zips: corrected.** The stale "AB-Cloud v23"
  package naming in the guides' headers now reads "the unified academic
  edition"; the SciPost guide's two references to the arXiv package use the
  real filename (`arXiv_submission_AB-Cloud.zip`, not `…_v23.zip`); the
  arXiv metadata README's own header drops the stale v23 tag while its
  paste-ready form metadata (title included) stays untouched; the bundle's
  mini README now lists the real zip names, fixes its preview byte-identity
  notes, and corrects the arXiv licence guidance to the **non-exclusive
  licence to distribute** (consistent with the strictly personal licence —
  the old "CC BY 4.0 recommended" line contradicted it); each in-zip guide
  gained a short shelf-pointers note (visible `guides/` copies, folder-level
  sums, status tracker); `compile_notes.md` records the rebuild
  verification.
- **Checksums: regenerated everywhere.** In-zip `SHA256SUMS.txt` of all
  three packages rebuilt and self-verified (`sha256sum -c` PASS);
  file counts unchanged (1,151 / 1,150 / 128 / 8); the folder-level
  [`SHA256SUMS.txt`](SHA256SUMS.txt) re-pins the eight new artifacts;
  the four preview PDFs remain byte-identical to their in-zip sources.
- **`guides/` mirrors re-extracted** from the re-sealed zips in the same
  commit, per the provenance rule.
- The 2026-10-08 sealing remains the scientific reference point: the
  manuscripts' content identity across the re-seal is documented above and
  in `nsr_submission/compile_notes.md`.

## 2026-10-18 — Journal shelf uplift (parity with the Academic Package)

The shelf catches up with its parent folder's standards. At this stage the
eight sealed artifacts still kept their 2026-10-08 bytes; the same-day
**full re-seal** above then rebuilt them. The scaffolding below is new
relative to the original shelf:

- **Folder-level checksums.** `SHA256SUMS.txt` now pins the four zips and
  four preview PDFs with SHA-256, so integrity is verifiable *before* any
  download is trusted (previously the sums existed only *inside* the zips —
  a chicken-and-egg gap for first-time verifiers). The file also records a
  verified cross-check: `NSR_manuscript_preview.pdf` is byte-identical to
  `nsr_submission/manuscript_NSR.pdf`, and `SciPost_manuscript_preview.pdf`
  is byte-identical to `scipost_submission/scipost_manuscript.pdf`.
- **`guides/` — the wizard guides leave the zips.** Visible, render-ready
  copies of `README_how_to_submit.md` (NSR, SciPost) and
  `README_arxiv_metadata.md` (arXiv), each stamped with a provenance note:
  the copy inside the zip remains the source of truth.
- **`SUBMISSION_STATUS.md`.** A hand-maintained tracker for the submission
  life-cycle of all three venues (Prepared → Submitted → Under review →
  Decision) with an event log and update instructions for the Author.
- **`FAQ.md`.** Ten answers covering the questions the shelf actually
  triggers: which SciPost version, arXiv endorsement, the "not for upload"
  previews, the two-level verification workflow, the honesty boundary, the
  strictly personal licence, and what to do when a checksum fails.
- **`CITATION.cff`.** The shelf becomes formally citable (CFF 1.2.0, DOI
  10.5281/zenodo.21825394) alongside the unified edition's own citation
  file.
- **`assets/README.md`.** The banner and emblem art get their own
  catalogue note, matching the parent assets folder convention.
- **`README.md` rebuilt.** Honest-boundary block, "What this shelf is",
  a "Which file do you need?" router, per-zip content trees, the two-level
  verification section, the status board, the guides index and the citation
  block — while preserving every existing guarantee of the previous
  revision (packages table, SciPost choice guidance, human steps, licence).

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
