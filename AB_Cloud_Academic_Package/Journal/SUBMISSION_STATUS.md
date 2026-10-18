# 📮 Submission status — AB-Cloud journal deliverables

The sealed packages on this shelf are **ready to upload; none of the three
venues has been approached yet** as of the latest entry below. This file is
the single, hand-maintained source of truth for where each manuscript
actually stands in the peer-review pipeline. It exists so that the shelf
never has to guess: the README, the guides and the changelog describe what
was *prepared* — this board records what *happened*.

> [!IMPORTANT]
> **Hand-maintained, deliberately not auto-generated.** No script writes to
> this file. Every status change is entered by the Author together with a
> dated line in the event log. The honesty layer of this repository extends
> here: an unsubmitted manuscript is recorded as **Prepared**, not
> "in review" — statuses move only when reality does.

## Legend

| Status | Meaning |
|---|---|
| 🟡 Prepared | package sealed and committed, wizard not yet run |
| 🔵 Submitted | uploaded via the venue wizard, awaiting editorial check |
| 🟣 Under review | passed editorial triage, with referees |
| 🟢 Accepted | accepted (possibly after revisions) |
| 🔴 Declined / Withdrawn | not proceeding at this venue |
| ⚪ On hold | paused by choice or by editorial request |

## Status board

| Venue | Package | Article type | Status | Submitted on | Manuscript ID | Next action |
|---|---|---|---|---|---|---|
| **NSR (JINR)** — [nsr.jinr.int](https://nsr.jinr.int) | `NSR_JINR_submission_AB-Cloud.zip` | Full article, 100 pp., official `nsr.cls` v1.5 | 🟡 Prepared | — | — | Run the NSR wizard — [`guides/NSR_JINR_how_to_submit.md`](guides/NSR_JINR_how_to_submit.md) |
| **SciPost Physics** — [scipost.org](https://scipost.org) | `SciPost_Physics_submission_AB-Cloud.zip` | Publication (60 pp.) **or** Core (11 pp.) — pick one | 🟡 Prepared | — | — | Choose the article type, run the SciPost wizard — [`guides/SciPost_how_to_submit.md`](guides/SciPost_how_to_submit.md) |
| **arXiv** — [arxiv.org](https://arxiv.org) | `arXiv_submission_AB-Cloud.zip` | Preprint, math-ph (cross-lists math.NT, math.SP) | 🟡 Prepared | — | — | Request endorsement (first-time submitter), then submit — [`guides/arXiv_metadata.md`](guides/arXiv_metadata.md) |

> [!TIP]
> The three wizards are independent — there is no required ordering.
> A common pattern for this shelf would be arXiv first (fast, establishes
> priority), then the journal venues; but any order is legitimate. Update
> this board the same day you press "submit" anywhere.

## Event log

| Date | Event |
|---|---|
| 2026-10-08 | All three packages compiled from the unified edition, sealed with SHA-256 and committed to this shelf. |
| 2026-10-18 | Shelf uplift: folder-level checksums, visible `guides/`, FAQ, CITATION.cff — packages untouched at this point. |
| 2026-10-18 | **Full re-seal** (see [`CHANGELOG.md`](CHANGELOG.md)): all eight artifacts rebuilt with the original engine (Tectonic 0.15.0), manuscript text untouched; service files inside the zips corrected (stale v23 naming, cross-references, licence guidance); checksums regenerated everywhere; previews re-synced byte-identical to their in-zip sources. Statuses unchanged: nothing has been submitted yet. |
| 2026-10-19 | Verdict sync (editorial — **packages untouched**): the shelf's documents now carry the unified edition's 2026-10-16 audit state (G2 YES, G5 YES, C17 NEGATIVE, algebraic_map exact closure) — see [`CHANGELOG.md`](CHANGELOG.md) and the README's "Where the science stands now". The eight sealed artifacts, their sums and the `guides/` mirrors are unchanged. Statuses unchanged: nothing has been submitted yet. |

## How to update this file (Author's routine)

1. **Status change** — edit the `Status`, `Submitted on` and `Manuscript ID`
   cells of the relevant row. Keep the emoji legend consistent.
2. **Add an event line** — one row per event, newest first, ISO date
   (`YYYY-MM-DD`). Editorial letters, referee reports, resubmissions and
   decisions all belong here; link or quote the venue's reference number.
3. **Keep the honesty rule** — never advance a status without the venue's
   own confirmation (an upload receipt, a manuscript ID, a decision letter).
4. **Cross-reference decisions** — when a venue reaches 🟢/🔴, note in the
   event log which package version was under review (the zip's SHA-256
   prefix is enough, e.g. `2d6d74fc…`), so the record stays auditable even
   if the shelf is later re-sealed with a revised manuscript.
