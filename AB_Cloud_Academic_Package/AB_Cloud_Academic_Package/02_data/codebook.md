# Codebook

## Verdicts
- `YES` — the claim is supported within the protocol's numerical certificates.
- `NO` — the claim is not supported; the failure is measured and documented.
- `BLOCKED` — reserved for RH: the V13 obligation machine keeps the conclusion
  blocked while analytic prerequisites remain assumed. A `BLOCKED` verdict may
  never be changed by a numerical result.

## Campaign series
- `V*` — spectral core / processor campaigns (AB_Cloud_Quantum_Research)
- `E*` — blind-verification experiments (Julia platform)
- `ES*` — spinor study experiments
- `D*` — Dirac-skeleton tests (dirac-lab; Python canonical + Julia ports)
- `C*` — Hilbert–Pólya bridge campaigns (Hilbert_Polya)
- `heritage` — the superseded 38-test reference run + September addenda

## Honesty fields
- `does_not_prove` — mandatory on verdicts; what the result does NOT establish.
- Negative results carry the same schema and standing as positive ones.

## Precision conventions
- `2.59e-39` style = verbatim scientific notation from the source verdict file.
- `649 = 649` = an equality check that passed (both counts agree).
- `0.978 vs 0.0010 (×977)` = measured value vs control value with the ratio.
- Where sources differ by convention, both values are recorded (see
  `00_meta/dossier.md` §4).
