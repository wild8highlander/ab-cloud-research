<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ 02_data/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
# external/ — third-party sources

| Source | What | Where | License/notes |
|---|---|---|---|
| Odlyzko zero tables | high-precision ζ zeros | dtc.umn.edu/~odlyzko/zeta_tables | public data; used as external control for the blind engines |
| mpmath | ζ-function evaluation (the oracle) | mpmath.org | BSD; the internal cache of the bridge campaigns |
| Arias de Reyna (2011) | Riemann–Siegel formulation | Math. Comp. 80(275) | the basis of the E16 independent engine |

Nothing is copied from external sources into this folder; `raw/` holds only
the programme's own curated tables (whose zeros derive from the internal
mpmath cache, not from external downloads).

<div align="center">

<img src="../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
