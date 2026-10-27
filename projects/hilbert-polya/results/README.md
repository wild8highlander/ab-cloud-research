<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ Hilbert_Polya/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# results/ — the ledgers of the series

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

<p align="center"><img src="../assets/illustrations/ill_spectrum_emerge.png" width="600" alt="The spectrum emerging from the ledger rows"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>The cast reports in: two living documents that turn committed verdicts into a public story.</em></p>

[← Back to the main README](../README.md)

## What this folder is

The front desk of the series. Everything measurable ends up either committed
in `data/` or summarized here, and these two documents are the summary layer:
a living ledger of numbers and verdicts, and the roadmap of what comes after
the released baseline. Raw campaign verdicts live in `data/`; interpretations
live in the monographs and in `docs/`; this folder only curates.

## Contents

| File | Contents |
|------|------------|
| [RESULTS.md](RESULTS.md) | the living ledger of numbers and verdicts, v1.0.0 |
| [ROADMAP.md](ROADMAP.md) | the directions after 1.0.0 |

- `RESULTS.md` opens with the headline numbers of v1.0.0 (a table of value
  and campaign) and states the governing rule of the series: every number is
  committed in `data/`, the ledger is only the showcase, and a repeat run of
  the campaigns must reproduce the committed values bit-for-bit (see
  `data/README.md`).
- `ROADMAP.md` tracks the horizon after the released baseline. Its headline
  metric is the main measured verdict — the zeros'-level result in the distance metric (D_nn 0.0079), with the rank/thermal branches as the conservative limits — and
  its directions are ordered by expected effect on that gap. The v2.0 block
  records what was already executed from the original R1–R5 list, e.g.
  R1 → C9/T11: the nonlocal primitive exists (r_H7 = 1, r_EF = PC0).

## How to use it

Read `RESULTS.md` first: it is the one-stop table of what the series
measured and which campaign produced each number. When a figure interests
you, follow it back to the campaign folder under `computations/` and to the
committed verdict in `data/`. To regenerate the numbers themselves, run the
campaigns; to re-verify the committed layer afterwards, run:

```bash
python3 -c "from hpbridge.validate import run_all; [print(r) for r in run_all()]"
```

A repeat campaign run must land bit-for-bit on the committed values; any
drift is a release stopper and belongs in the changelog, not in a silent
edit of the ledger.

## Conventions

- The ledger quotes only committed numbers; nothing here is computed on the
  fly, and no figure appears in `RESULTS.md` without a home in `data/`.
- Versions are explicit: the v1.0.0 ledger is the released baseline, and the
  roadmap explicitly separates the post-1.0.0 directions from the completed
  v2.0 items (the former R1–R5 list).
- Interpretation is kept out of the ledger: the "what does it mean" prose
  lives in the monographs (`monograph/`, `computations/C*/`) and in `docs/`,
  while this folder stays a registry.

## See also

- [../data/README.md](../data/README.md) — the committed verdicts and reproduction hashes behind every number
- [../docs/README.md](../docs/README.md) — the interpretive layer: theory, methods, validation
- [../CHANGELOG.md](../CHANGELOG.md) — the release history between ledger versions
- [../independent_verification/README.md](../independent_verification/README.md) — the protocol that guards the committed layer

---

<!-- enriched-r3 -->

This folder is the **ledger layer** of its module: the committed verdicts, run summaries and cross-verification records. The convention is that a result does not exist until its ledger row is committed — everything downstream (figures, monographs, README claims) replays these files rather than recomputing. The honest FAIL rows are kept verbatim: a negative result is a citizen here, not an embarrassment.

The ledgers of the series: the committed verdict documents that every figure, theorem and monograph quote traces back to.

<div align="center">

<img src="../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
