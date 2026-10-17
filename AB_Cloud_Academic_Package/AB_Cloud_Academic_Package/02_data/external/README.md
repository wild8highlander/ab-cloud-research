# external/ — third-party sources

| Source | What | Where | License/notes |
|---|---|---|---|
| Odlyzko zero tables | high-precision ζ zeros | dtc.umn.edu/~odlyzko/zeta_tables | public data; used as external control for the blind engines |
| mpmath | ζ-function evaluation (the oracle) | mpmath.org | BSD; the internal cache of the bridge campaigns |
| Arias de Reyna (2011) | Riemann–Siegel formulation | Math. Comp. 80(275) | the basis of the E16 independent engine |

Nothing is copied from external sources into this folder; `raw/` holds only
the programme's own curated tables (whose zeros derive from the internal
mpmath cache, not from external downloads).
