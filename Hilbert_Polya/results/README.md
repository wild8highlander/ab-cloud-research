# results/ — the ledgers of the series

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
make ivp
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
