# Model card

**Model**: none in the machine-learning sense — the package ships
*computational protocols*, not trained models. The closest analogues:

| Component | Type | Card |
|---|---|---|
| AB-cloud ensemble (V-series) | random-matrix ensemble construction | seed-pinned, config in `config.yaml: monte_carlo` |
| Givens–QR compiler (V20) | deterministic compiler | fidelity certificate $1-F \le 4.4\times10^{-16}$ |
| ζ→vortex coder (D-series) | deterministic phase coder | spec in dirac-lab README; cross-verified in Julia |
| Blind engines (E16/E17) | zero-finding algorithms | Euler–Maclaurin + Riemann–Siegel; cross-engine 0.0 |

**Intended use.** Scholarly reproduction and exploration of the programme's
claims. **Out-of-scope use.** Any claim about the Riemann hypothesis beyond
`certified` (unlocked, v1.2.1 — see `00_meta/dossier.md`).

**Honesty layer.** Every verdict file carries `does_not_prove`; the V13
obligation machine governs RH statements. Negative results (locality wall,
null zones, correspondence failures) are part of the model cards' "limitations"
sections by construction.
