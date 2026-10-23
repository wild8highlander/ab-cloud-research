<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ realtime_spinor_memory/](../../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# TS3 · The real-time theorem

**Status:** proved (analytically + a microbenchmark) · **Certificate:**
campaign ES3, verdict PASS · **Documents:**
`theorem_ts3_{ru,en}.{pdf,docx}` (4 documents) · **Figure:**
`figures/ts3_4dim_{lang}.png` (2×2, 600 dpi).

## Statement

1. **The step of the phase machine executes in a constant time c**, not
   depending on the uptime t: the state is a single register of fixed
   width, the history is absent. The measured slope of the step-cost
   profile: −1.5e−12 ms/step per step (no growth within the measurement
   resolution); the 1 ms deadline was met on **200 000 of 200 000** steps.
2. **The machine with an eternal log** and full periodic re-checking
   carries an **Ω(t)** verification cost: the slope of the replay cost is
   positive (R² = 0.999), the growth of the mean step cost by t = 2¹⁷ is
   **×129** (for the phase machine — ×1.0).
3. Corollary: for any deadline Δt there exists a t*, after which the
   machine with the log misses the deadlines, whereas the phase machine
   meets them at all t. **Hard real time and long-term memory are
   incompatible in this architecture; volatility is not a defect but the
   condition of determinism.**

## Derivation idea

(i) The step is a single modular addition over a register of fixed width ⇒
O(1) by construction. (ii) A full re-check reads all t cells of the log ⇒
Ω(t); at c_max — the maximal step cost with the re-check — for
t > Δt/c_max the next step with replay exceeds the deadline. The phase
machine never reads the history, so its cost does not depend on t. The
full proof is in the documents.

## The four dimensions of the certificate (ES3)

| Dimension | What is measured | Result |
|-----------|--------------|------|
| metric | the slope of the machine's step cost over t | −1.5e−12 ms/step (≤ 1e-11) |
| per-instance behaviour | 200 000 steps, the models S1 and S3 | 0 deadline misses (Δt = 1 ms) |
| control | LogMachine (the eternal log + replay) | growth ×129–132; replay Ω(t), R² = 0.999 |
| threshold | C1–C4 pre-registered | all PASS |

## Boundaries (honest)

The theorem certifies the O(1) step cost of the **model** and the linear
growth of the log re-checking in the **contrast model**. It does not
measure the performance of physical devices, does not claim that all
memory is harmful, and does not exclude buffers of bounded length — the
prohibition concerns exactly the eternal log under hard deadlines.
Measurements: CPython, GC disabled during the microbenchmark (honestly
documented in the verdict).

## How to reproduce

```bash
python3 experiments/run_es3_realtime.py    # verdict data/es3_realtime_verdict.json
python3 make_figures.py                    # figures/{ru,en}/ts3_4dim_*.png
python3 make_theorem_docs.py TS3           # 4 documents
python3 -m pytest tests/ -q                # invariants (test_footprint_constant)
```

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../../README.md">⬆ parent section</a></sub>

</div>
