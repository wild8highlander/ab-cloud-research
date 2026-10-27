<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ V18_ab_processor/](README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# V18 · The AB Operator as a Processor

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does the AB operator work as a processor — gates, entanglement, a game? Three levels of computability on the Hamiltonian building blocks.**

[← Back to the main README](../../README.md)

## Contents

1. [Campaign question](#campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest remarks](#honest-remarks)
9. [Verdict](#verdict)

---

## Campaign question

Does the AB operator work as a processor — gates, entanglement, a game? Three levels of computability on the Hamiltonian building blocks.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V18 (plan Solution 18) | committed verdict |
| Key numbers | All six gate fidelities 1.0 − 2e-16; concurrence 0.984 (t = 2.373); an AB-Pong game: score 0:1, 10 intercepts, 411 events, bit-exact replay. | measured/proved |
| Verdict note | processor — YES | honest |

## Method

rpbridge/processor.py: P1 — analytic pulses {X,Y,Z,H,S,T} on the block H₂ = mσz − t·cosφ·σx − t·sinφ·σy; P2 — the exchange link −J, the Wootters concurrence; P3 — AB-Pong: a 64-site board at phase π/3, gauge-covariant mirrors e^{−2iφx}ψ(2p−x), lead-following AI, goals at x≤5/x≥58.

## Figures

| File | Where |
|---|---|
| `fig19_en.png` | 600 dpi — `../../figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v18_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v18     # fresh recomputation
python3 -m pytest tests/ -q                     # theorem machinery
```

## Honest remarks

- Metrics are pre-registered; verdicts are committed and independent of
  fresh recomputation.
- The zero file is the only external data; no third-party research code
  is imported.
- Every claim of this campaign has a claim file (V14 audit) with the
  list of what it does NOT prove.

## Verdict

**Processor — YES: exact gates, near-Bell entanglement, the game runs deterministically**

---

*AB Research Program v1.1.0 · V18 · The AB Operator as a Processor*

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
