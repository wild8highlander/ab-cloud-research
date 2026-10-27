<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ computations/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# C16 · Quantum-information layer (T18)

> **🧭 Navigation:** [computations/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

<p align="center"><img src="../../assets/illustrations/ill_pixel_encoding.png" width="640" alt="The quantum-information layer: entanglement, mutual information, form factor"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
*What can entanglement, mutual information and the form factor see that rank correlations cannot?*

> Fermionic entanglement of the Slater Fermi sea (correlation-matrix protocol), mutual information of halves, SFF ramp slopes.

[← Back to the main README](../../README.md)

## The question

The v2 layer has measured the wall in traces, designs, statistics and characters (C9–C15). C16 asks the last question: does the *information theory* of the states remember the zeros? Three diagnostics run on the same L = 24 resonator: fermionic entanglement S_A of the Slater Fermi sea (correlation-matrix protocol), mutual information of the halves, and the spectral form factor's ramp slopes. Each is compared against the H_ξ zero window and against random-matrix baselines.

## Where it sits in the v2 roadmap

This campaign settles **Theorem T18** and answers the v2 question "what do entanglement and complexity see?". The answer: they erase arithmetic along with spectral statistics. C9/T11 proved the wall is locality, not the trace; C16 is its quantum-information echo — the same locality that keeps the prime weight out of the heat trace keeps volume-law entanglement out of the states and the zero order out of the MI.

## Method in brief

The committed run (24.4 s) works at five fillings ν = 0.25, 0.4, 0.5, 0.6, 0.75 and performs three measurements:

- **Q1 — entanglement.** The correlation matrix of the Slater Fermi sea, restricted to half the system, is diagonalised; its eigenvalues give S_A for the vortex gate and the clean lattice, with the Haar Page baseline computed at the same fillings.
- **Q2 — mutual information.** MI = 2S_A − 2S_AB between the halves (S_AB ≈ 1.65e-08, numerically negligible), correlated against the zero-window profile and a random window.
- **Q3 — SFF ramps.** The form factor's ramp slope for the gate (Nv16), a GUE reference, the H_ξ zero window and the clean lattice.

<p align="center"><img src="../../assets/avatars/hp_agent_lyra.svg" width="110" alt="Agent Lyra"/></p>

## Results

Locality suppresses volume-law entanglement (S_A ≈ 12–16 nats vs 160–220 Haar, z > 100) — the quantum echo of C9; MI carries no zero signature (−0.018 vs −0.121 random).

At the band edges (ν = 0.25, 0.75) the gate reaches S_A = 12.76 and 12.75 nats, the clean lattice 15.75 nats — the source of the headline 12–16; at half filling both drop to ≈ 7.3–7.5 nats. The Page/Haar baseline means run 160.21, 211.46, 222.45, 211.91, 160.18 nats over the same fillings; the gate MI deviates from it by up to z = 437.2. Q2 returns MI 22.94 ± 3.16 with correlation −0.0181 against the zero window and −0.1210 against a random window — both in the null cone. Q3's slopes read −1.4693 (gate, Nv16), −1.2526 (GUE), −1.1746 (H_ξ zero window), −0.3435 (clean lattice) — the verdict's reading: gate ramp = GUE class; zero window: no ramp (rigid sequence); clean lattice: Poisson plateau.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="110" alt="Riemann"/></p>

## Why it matters

T18 completes the v2 verdict with a statement about *states*, not only spectra. Arithmetic enters the lattice spectrum through the counting law of zero modes (T13) but not through the rank channel (C3–C5, C13 — the rank branch at its resolution limit, with the level identity at the zeros' band); C16 shows it never enters the states' information content either: no Haar volume law, no zero-window MI, complexity stopping at GUE. The wall of locality is visible in the entanglement structure. Any future bridge must be an object whose locality is not of this kind.

## Reproduction

```bash
python3 campaigns/run_c16_qinfo.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`../../data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).
The committed run completes in 24.4 s.

## Data and figures

| File | Where |
|---|---|
| `fig24_qinfo_{ru,en}.png` | this folder's `figures/{ru,en}/`; 600 dpi mirrors — top-level `figures_hires/{ru,en}/fig24_qinfo_{ru,en}.png` |
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

`data/results.json` stores the two S_A profiles (gate and clean, five fillings each, with S_B, S_AB), the Page baseline mean and std, the MI alignment block, the SFF slope table; `data/curves.npz` holds the curves behind `fig24_qinfo_{ru,en}.png`.

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`../../monograph/v2_volume/`) and `../../independent_verification/` (IVP11–18).

The committed English verdict reads: *"Three measurements. Q1: locality suppresses the volume-law fermionic entanglement of the Fermi sea (S_A ≈ 12-16 nats vs 160-220 for the GUE Haar baseline, z > 100) — the quantum-information echo of the wall of locality (C9/T11). […] Conclusion: entanglement and complexity erase arithmetic along with spectral statistics (T18)."* (The Q2 and Q3 clauses are quoted in Results above.)

## FAQ

**What is the correlation-matrix protocol?**
For a Slater determinant the entropy of a region is a functional of the single-particle correlation matrix restricted to it: S_A = −Σ λₖ ln λₖ − Σ (1 − λₖ) ln (1 − λₖ) over its eigenvalues. The many-body problem reduces to one diagonalisation.

**Why compare against a Haar baseline?**
Haar-random states obey Page's volume law. The gap, a factor of ≈13 between 160–220 and 12–16 nats, quantifies how strongly locality suppresses entanglement.

**What does "MI carries no zero signature" mean numerically?**
The MI profile correlates at −0.0181 with the zero window and −0.1210 with a random window. Both sit in the null cone: the zero window explains no more MI structure than a random one.

**What does the SFF ramp add beyond C14's statistics?**
C14 classifies the gates by spacing statistics; the ramp slope is a complexity-adjacent diagnostic. It agrees (gate −1.47 vs GUE −1.25), separates the clean lattice (−0.34, Poisson plateau), and confirms the rigid zero sequence is in a class of its own.

## See also

- [C9 · Nonlocal trace primitive](../C9_nonlocal_trace/README.md) — the wall of locality in the trace language (T11).
- [C11 · α=1/3 zero modes](../C11_alpha_third/README.md) — where arithmetic *does* enter the lattice spectrum (T13).
- [C14 · Anomaly hunt](../C14_anomaly_hunt/README.md) — the statistics layer this echoes (T16).
- `../../docs/v2/overview.md`, `../../monograph/v2_volume/`, `../../results/RESULTS.md` (row 30).

---
*Hilbert Polya Bridge v2.0.0 · C16*

---

<!-- enriched-r3 -->

This folder documents one **campaign of the Hilbert–Pólya Bridge series**. The computational kernel is shared — every campaign builds its Hamiltonians and spectra through [`engine/`](../../engine/README.md) — while the committed verdicts for all campaigns live in [`data/`](../../data/README.md). This page narrates the campaign's question, method and measured outcome; the numbers it quotes are frozen in the evidence base and are reproducible bit-for-bit. The campaign map of the whole series is in [`computations/`](../README.md).

## Folder contents

**Subfolders:** `data/` · `figures/`


**Where next:** [engine/](../../engine/README.md) · [data/](../../data/README.md)

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
