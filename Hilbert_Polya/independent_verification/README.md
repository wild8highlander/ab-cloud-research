# independent_verification/ — the IVP01–IVP10 protocol

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

<p align="center"><img src="../assets/illustrations/ill_direct_input_error.png" width="600" alt="Blind input checked against a pre-fixed threshold"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>The cast on duty: every check below is phrased so that the answer is yes or no, never a narrative.</em></p>

[← Back to the main README](../README.md)

## What this folder is

Ten blind checks with thresholds known before the launch. Each check re-reads
**committed** verdicts, recomputes cheap invariants, and/or uses an independent
implementation (the multilanguage twins in `multilang/`). No check requires a
zeros file and none recomputes the heavy campaigns — their verdicts are
committed and protected by reproduction hashes (see `data/README.md`).

This folder is the release gate of the series: a full run either reproduces
the committed protocol or stops the release.

## Contents

| File | Role |
|------|------|
| `PROTOCOL.md` | the rules and the registry of checks IVP01–IVP10 |
| `RESULTS.md` | the committed verdict table of the last run |

The checks themselves are implemented in `../hpbridge/validate.py`
(`run_all()`), which executes IVP01–IVP10 — and, since v2.0, IVP11–IVP18 —
directly from the committed data.

The four protocol rules behind the registry:

1. **Blindness to intent.** Every check is a statement with a numerical
   threshold fixed *before* the run; the verdict is binary.
2. **Positive control is mandatory.** A method check is valid only if the
   series contains a check where the method sees the identity (IVP06-PC0,
   IVP08 co-location, and the C3/C4 campaign controls).
3. **Independence.** IVP02/IVP03 recompute the Γ-closures and Z_id with their
   own implementation (`hpbridge.identity`), not from cache; IVP10 reconciles
   the C twin against the Python implementation.
4. **Commit of verdicts.** `RESULTS.md` is the committed protocol of the last
   run; a repeat run must reproduce it bit-for-bit.

Registry of checks (thresholds exactly as fixed in `PROTOCOL.md`):

| ID | Check | Threshold | Method |
|----|-------|-----------|--------|
| IVP01 | release integrity (files) | all present | manifest |
| IVP02 | Γ-closures T1 (dps = 40) | ≤ 1e-35 | hpbridge.identity |
| IVP03 | reality of Z_id (T2) | \|Im\| ≤ 1e-25 | hpbridge.identity |
| IVP04 | argument-principle anchors (T3) | 0/3/10/29/79/649 | data/c2 |
| IVP05 | count vs Riemann–von Mangoldt N̄ | S(T) ≤ 1.8 | data/c2 |
| IVP06 | trace formula T6 | \|ΔQ\| ≤ 1e-10, \|ΔK\| ≤ 5e-5 | data/c4 |
| IVP07 | GUE class of the extended family | ⟨r⟩ ∈ 0.5996±0.03 (C8 canon) | data/c5 |
| IVP08 | flow co-location (T4) | ≤ 1e-13 | data/c6 |
| IVP09 | ψ-ladder | corr ≥ 0.95 | data/c6 |
| IVP10 | multilanguage twin (C) | γ ≤ 1e-12; Λ match | multilang/c |

## How to use it

```bash
python3 -c "from hpbridge.validate import run_all; [print(r) for r in run_all()]"
```

The runner executes all ten checks (the IVP10 cross-language step rebuilds
the C twin with `cc` when the toolchain is present) and finishes with
the committed verdict table. Any difference from `RESULTS.md` is a
release stopper.

## Conventions

- Verdicts are binary (`passed` true/false) and are written to `RESULTS.md`
  together with the series version and the run date.
- The v1.0.0 registry covers IVP01–IVP10; the v2.0 extension IVP11–IVP18
  (campaigns C9–C16) lives in `hpbridge/validate.py` and is scored by the
  same binary convention.
- Thresholds are never tuned after a run; if a threshold must change, the
  change goes into `PROTOCOL.md` first and the run is repeated from scratch.

## See also

- [../multilang/README.md](../multilang/README.md) — the twins used by IVP10
- [../data/README.md](../data/README.md) — the committed verdicts and reproduction hashes
- [../results/RESULTS.md](../results/RESULTS.md) — the public ledger of numbers
- [../hpbridge/README.md](../hpbridge/README.md) — the `validate.py` implementation of the checks

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The IVP01–IVP10 protocol: ten independent checks performed outside the main campaign loop, each with its own document.
