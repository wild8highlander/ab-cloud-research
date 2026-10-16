# run_20260919_085734_m2 — Test 34, MODE 2 HARDCORE (Klein quartic, 100,000 zeros)

**What ships here:** the reconstructed protocol of the 19 September 2026 ensemble pass —
the third independent Test 34 confrontation record, and the first on a Hurwitz surface.

| file | what it is |
|---|---|
| `FINAL_REPORT.md` | Reconstructed final report (config, composite verdict, pooled statistics, per-realization table, forensics). |
| `data_realizations.csv` | Per-realization statistics (verbatim from the console) + the pooled row. |
| `config.json` | Run configuration; every derived field is flagged with its derivation. |
| `logs/console_output.txt` | The cleaned console protocol (final table, pooled line, forensics, verdict — complete blocks). |
| `logs/console_capture_raw.txt` | The raw capture as received (progress-bar lines are IM-wrapped/truncated; final blocks are complete). |

**Why "reconstructed":** the run executed on the operator device; the console capture
travelled, the device directory (`results/run_20260919_085734_m2/` with plots, CSV arrays
and the machine config.json) did not. Nothing here is re-simulated: every number is the
console's own. The two provenance-derivable facts (geometry = PSL(2,7) ×56 lift; full
seeds) follow from the laboratory's deterministic arithmetic and match the console
truncations exactly.

**Headline:** pooled D = 0.0808, p = 1.187e-107, d_GUE = 0.0044, d_Pois = 0.2817,
plateau = 0.9734, mean |R2−GUE| = 0.0299; median D = 0.0817, IQR = 0.0017, no MAD
outliers; composite criterion satisfied on all three counts (GUE-CONSISTENT).
Context: the torus ensemble of 17 September (run 20260917_080329_m2, 20 realizations)
read D = 0.0970, d_GUE = 0.0768 at 50,000 zeros.
