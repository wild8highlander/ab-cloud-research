<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ Hilbert_Polya/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# tests/ — the pytest suite of the series

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

<p align="center"><img src="../assets/illustrations/ill_direct_input_error.png" width="600" alt="Committed verdicts fed straight into the test bench"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>The referees of the cast: twenty-one tests that re-ask the series' promises, one committed verdict at a time.</em></p>

[← Back to the main README](../README.md)

## What this folder is

The regression layer. A pytest suite — 21 tests across 7 files — that keeps
the committed verdicts of the series honest: some tests recompute the cheap
invariants live (at protocol precision), others re-check the committed
outputs of the heavy campaigns bit-for-bit. The suite runs offline, needs no
network, and none of the tests requires a zeros file.

## Contents

| File | Theorem/criterion | Source |
|------|-------------------|--------|
| test_gamma_closures.py | T1 | live recount (dps 40) |
| test_zid_reality.py | T2 | live recount |
| test_trace_formula.py | T6 | committed C4 |
| test_gates_gue.py | T7 | committed C5 |
| test_protocol_repro.py | C3 base | live recount (bit-for-bit) |
| test_colocation.py | T4 | committed C6 |

Two more files complete the suite:

| File | Role |
|------|------|
| test_v2_campaigns.py | 9 tests over the v2.0 layer — campaigns C9–C16 and their theorems |
| conftest.py | bootstrap: inserts the repository root into `sys.path` so the tests import `hpbridge` from a bare checkout |

## How to use it

```bash
python3 -m pytest tests/ -q
```

That single line is the whole workflow. The suite runs against the working
tree: the "live recount" tests re-derive their invariants through
`hpbridge` at the stated precision (for example dps 40 for the Γ-closures of
T1), while the "committed" tests load the verdict JSON of the named campaign
(C4, C5, C6) and check the series still reproduces it exactly. A failure
means the code and the committed data have diverged — stop and reconcile
before touching `results/` or the monographs.

## Conventions

- **Live recount vs committed verdict.** Cheap invariants are recomputed
  from first principles; expensive campaign outputs are read from the
  committed files in `data/` and compared exactly.
- **Bit-for-bit.** Where the source table says so, the comparison is exact:
  no tolerances, no rounding, a repeat run must reproduce the committed
  bytes of a verdict.
- **No zeros file.** None of the 21 tests requires the high-precision zero
  file; the suite stays runnable in a bare checkout.
- **Bootstrap once.** `conftest.py` is the only path machinery: every test
  module imports `hpbridge` as a top-level package.

## Glossary

- **Committed verdict** — the JSON verdict of a campaign as committed under
  `data/`; the reference state of the series.
- **Live recount** — recomputing an invariant on the spot through the
  `hpbridge` package, at the precision named in the table (e.g. dps 40).
- **Positive control** — a test configuration in which the method must see
  the identity exactly; the guard against a method that "passes" everything.
- **dps** — decimal places of precision for the `mpmath` computations behind
  the live recounts.

## FAQ

**Why do some tests read committed files instead of recomputing?**
Because reproducing a full campaign run on every `pytest` invocation would
defeat the purpose of a fast regression layer; the heavy campaigns are
guarded by reproduction hashes and by the IVP protocol instead, and the
tests pin their committed outputs.

**What if a live recount and a committed verdict disagree?**
That is precisely what the suite is for: the series treats any such
disagreement as a defect to be reconciled before any release step, in the
same spirit as the release stopper of `independent_verification/`.

**How does this relate to IVP01–IVP10?**
The IVP protocol is the release-time audit (thresholds fixed in advance,
verdicts committed); this suite is the development-time guard. They share
the same `hpbridge` machinery and the same committed data, so a green suite
and a green IVP run are two views of one consistent state.

## See also

- [../hpbridge/README.md](../hpbridge/README.md) — the package every test imports
- [../independent_verification/README.md](../independent_verification/README.md) — the release-time protocol over the same verdicts
- [../data/README.md](../data/README.md) — the committed files the "committed" tests read
- [../results/RESULTS.md](../results/RESULTS.md) — the ledger that assumes a green suite

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The pytest suite of the series: it replays the committed verdicts and checks the invariants the theorems claim, so a regression cannot pass silently.

<div align="center">

<img src="../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
