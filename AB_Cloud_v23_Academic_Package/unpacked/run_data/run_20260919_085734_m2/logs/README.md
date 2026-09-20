# `logs/` — The Console Protocol of the Klein Quartic Pass
> The two console captures that carry the entire evidence of the 100,000-zero Hurwitz run: the cleaned protocol and the raw capture as received.

_Location: [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260919_085734_m2/](../README.md) › [logs/](README.md)_

This folder holds the only direct execution evidence of the Klein quartic pass — the console output of the standalone laboratory's MODE 2 HARDCORE run of 19 September 2026. Two files, two roles:

**`console_output.txt`** (the clean protocol) — the cleaned console protocol: the configuration header, the Cayley-graph construction line ("H built Cayley …"), the per-realization table, the pooled statistics line, the forensics block (median D, IQR, MAD-outlier census), and the composite verdict block — complete and untruncated. This is the file the reconstructed `FINAL_REPORT.md` and `config.json` were transcribed from; every number in those documents traces to a line here.

**`console_capture_raw.txt`** — the raw capture **as received** via IM paste from the operator device. Progress-bar lines are IM-wrapped and truncated; the final blocks (the ones carrying the statistics and verdicts) are complete. The file is preserved verbatim precisely so that the cleaning step is auditable: a reader can diff the raw capture against the cleaned protocol and verify that no number was altered, only formatting repaired.

Together with the provenance-flagged `config_D.json` in the parent folder, these captures satisfy the package's reconstruction policy for run records whose device-side directories were lost — the policy documented in the parent README and in monograph chapter Add.8. The seed ladder and the 9408 = 168 × 56 geometry identification can be re-derived from the laboratory source (`../../lab_standalone/finite-size_lab.jl`) and checked against the console truncations, exactly as the config's derivation fields describe.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `console_capture_raw.txt` | 11.1 KB · 33 lines | The raw console capture as received (IM-wrapped progress lines; final blocks complete). |
| `console_output.txt` | 3.1 KB · 38 lines | The cleaned console protocol: config header, per-realization table, pooled line, forensics, composite verdict (complete blocks). |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../../README.md](../../../README.md)._