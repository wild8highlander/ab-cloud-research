# ❓ FAQ — Journal submission shelf

Answers to the questions this shelf actually triggers, for the Author, for
an editor handling a submission and for a curious reader. The sealed
packages themselves are described in [`README.md`](README.md); the
submission life-cycle lives in [`SUBMISSION_STATUS.md`](SUBMISSION_STATUS.md).

## 1. Which SciPost version should I submit — Publication or Core?

Submit **one** of the two, not both. The **Publication** version (60 pp.) is
the complete academic account of the study; the **Core** version (11 pp.) is
the condensed communication for SciPost's short-format article type, and it
typically moves through refereeing faster. Both share the same `figures/`
and `supplemental/`, so nothing else changes in the wizard. The decision is
taste and timing, not correctness: the Core version condenses the same
results and carries the same honesty layer.

## 2. Do the preview PDFs go to the journal?

**No.** The four `*_preview.pdf` files exist so that a human can read what
each package compiles to without unzipping anything. The actual upload is
the zip's content: for NSR and SciPost the venue wants the `.tex` source
plus figures (and the compiled PDF as reference), for arXiv you upload the
*contents* of the flat package (or re-zip them) rather than the preview.
The one legitimate exception: the NSR package's
`manuscript_NSR.pdf` — which is byte-identical to `NSR_manuscript_preview.pdf`
(verified, see [`SHA256SUMS.txt`](SHA256SUMS.txt)) — is itself part of the
NSR upload set.

## 3. How do I verify a package before trusting it?

Two levels, both one command each — see
["✅ Verify before you submit"](README.md#-verify-before-you-submit) in the
README:

1. **Folder level** — `sha256sum -c SHA256SUMS.txt` in this folder checks
   the four zips and four preview PDFs against the committed sums.
2. **Package level** — after unzipping, `sha256sum -c SHA256SUMS.txt`
   inside the package directory checks **every** file the venue will
   receive, as pinned by the package's own manifest (868 files for NSR,
   867 for SciPost, 50 for arXiv — every file except the manifest itself;
   the zip entry counters reported by `unzip -l`, 1,151 / 1,150 / 128,
   additionally include folder entries).

If a check fails, re-download first; if it fails again, do **not** upload
that copy — see question 9.

## 4. Can I recompile the manuscripts myself?

Yes. The NSR and SciPost zips ship the official class files they were built
with (`nsr.cls` v1.5 + `nsr.bst`; `SciPost.cls` + `SciPost_bibstyle.bst`),
and `compile_notes.md` in the NSR package records the exact build recipe:
the reference PDFs are compiled with Tectonic 0.15.0 (XeTeX bundle), with two
tiny local compatibility patches to a LOCAL copy of `nsr.cls` (fancyhdr
v4.0.1); with TeX Live (`fancyhdr` ≥ 4.1) the unpatched journal class
compiles the manuscript as-is via `pdflatex <manuscript>.tex` (run twice).
The arXiv package needs no extra files at all: it is deliberately
flat (standard `article` class, inline `thebibliography`), which is exactly
what arXiv's auto-builder accepts without surprises. Unicode-heavy
constructs were transliterated to standard macros during packaging for that
reason.

## 5. Does any of this prove the Riemann Hypothesis?

**No.** Everything on this shelf is a numerical and formal study of a
mathematical model. The V13 obligation machine of the unified edition keeps
the RH conclusion **unlocked** (`verdict: certified`, v1.2.1): the path
O01→O12 carries no assumptions — the classical Li criterion (O12) plus
certified convergence (O08/O09/O11) — but RH as a theorem still requires
O11 for **all** n. Around that boundary the programme's gate ledger
(unified edition, synced with the 2026-10-16 audit) reads: G1
self-adjointness **YES**, G2 spectral identity **YES** (D_nn = 0.0079 —
the level of the ζ zeros themselves; C3, audit v2.0.7), G3 GUE class
**YES** (the whole C5 family in class: 0.569–0.633, mean 0.601), G4 Dirac
dynamics **YES**, G5 primes in the operator **YES** (the convergence
ladder, audit v2.0.8). Negative results are first-class citizens: C17
(blind phase B) is **NEGATIVE** by the letter of its pre-registered
criterion (1.04× over the primes-free null, z_GUE = −3.3), and the vortex
scan does not prove Hilbert–Pólya (G10 **NO**). This honesty layer
(`does_not_prove` fields, exact verdicts) is part of the scientific
record, travels inside every package, and is protected by the licence; it
must be preserved verbatim in any quotation. The full table — including
the algebraic_map closure — is in the README's
[Where the science stands now](README.md#-where-the-science-stands-now).

## 6. Why does arXiv need an endorsement?

arXiv requires endorsement for submitters with no prior arXiv record in a
given category. The arXiv package's
[`guides/arXiv_metadata.md`](guides/arXiv_metadata.md) carries the full
checklist: request endorsement for **math-ph** (primary classification),
cross-list **math.NT** and **math.SP**, paste the prepared metadata block,
and choose the **non-exclusive licence to distribute** — arXiv's default
and most restrictive option, consistent with the strictly personal licence
of this repository.

## 7. What licence applies here?

The repository-wide **strictly personal licence** of the Author
(**Isaev Iskhak Khamzatovich** — see [`../../LICENSE`](../../LICENSE)): you
may view, read, run locally for scholarly verification and cite with
attribution (quote limit ≤ 400 characters per excerpt, with the DOI
[10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394));
redistribution, republishing, mirroring, derivative publications, commercial
use and ML training are **not licensed** without separate written consent.
Once a venue accepts a manuscript, **that venue's own publication
agreement** governs the published version — everything else on the shelf
stays under the Author's exclusive control.

## 8. Where do the numbers come from — can I reproduce them?

Every number in the manuscripts traces back to the **unified edition**
one shelf up: [`../AB_Cloud_Academic_Package/README.md`](../AB_Cloud_Academic_Package/README.md)
— curated data with schemas and checksums, the six-language CLI, the web
laboratory, 410+ tests and the machine-readable honesty ledger. The
packages' `supplemental/` folders carry a self-contained **Python clone**
(`abcloud`), the standalone lab codes and the full run data, and the
unified edition's [`reproduce.sh`](../AB_Cloud_Academic_Package/reproduce.sh)
re-runs the pipeline end-to-end. A referee can therefore verify any figure
without trusting anything on faith.

## 9. A checksum failed: what now?

First, re-download the artifact and re-run `sha256sum -c` — a truncated
download is by far the most common cause. If the mismatch persists, compare
your sum against the values in [`SHA256SUMS.txt`](SHA256SUMS.txt) manually
(one line per artifact). A *file you produced* (an edited PDF, a rebuilt
zip) will legitimately fail — the sums pin the current sealed bytes
(re-sealed 2026-10-19; the 2026-10-08 originals and the rebuild record live
in [`CHANGELOG.md`](CHANGELOG.md)); that is the design, not a bug. If a
fresh download from this repository still fails, do not upload it anywhere:
open the issue with the Author at
[aslan08_05@mail.ru](mailto:aslan08_05@mail.ru) quoting both sums.

## 10. May I edit the packages — fix a typo, swap a figure?

No — not in place. The packages are **sealed**: editing any file invalidates
the in-zip `SHA256SUMS.txt` and makes the folder-level sums meaningless. The
correct routine (mirrored in [`CHANGELOG.md`](CHANGELOG.md)) is: revise the
source in the unified edition, rebuild the affected package, re-seal it
(fresh in-zip sums), regenerate the folder-level `SHA256SUMS.txt`, and add a
dated changelog line describing what changed and why. The old version's
bytes are then replaced deliberately — and the
[`SUBMISSION_STATUS.md`](SUBMISSION_STATUS.md) event log records which
checksum was under review at each venue, keeping the audit trail intact.

## 11. Where do the current verdicts live?

In the **unified edition's machine-readable ledger**, one shelf up — that
is the single authoritative surface for what the programme claims and does
not claim. It was last synced with the Hilbert–Pólya audit wave of
16 October 2026: G2 (spectral identity) flipped NO → **YES** on the gates'
D_nn = 0.0079, the level of the shifted zero windows and of the GUE zero
class themselves (C3, audit v2.0.7); G5 (primes in the operator) flipped
NO → **YES** on the convergence ladder (audit v2.0.8); the blind campaign
C17 returned **NEGATIVE** by the letter of its pre-registered criterion;
and the new algebraic_map section proved the pixel encoding's Jacobi map
to close exactly in ℚ (all 25 char-poly coefficients, D_25 = 0). The
**sealed packages** carry the verification record they were compiled with
— the 38-test reference run, 79 pre-registered verdicts (66 favourable,
13 honest adverse entries), frozen 8 October 2026 — and do not contain the
gate ledger at all, so there is no contradiction to manage: each layer is
dated, and [Where the science stands now](README.md#-where-the-science-stands-now)
on the README shows both together. If a package re-issue synced to the new
verdicts is ever wanted, it follows the sealed-package routine of
[CHANGELOG.md](CHANGELOG.md) — revise the source in the unified edition,
rebuild, re-seal, regenerate the sums, add the dated changelog line.
