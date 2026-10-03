# `python_clone/abcloud/data/` — The Embedded ζ-Zero Dataset
> `zeta_zeros_50000.txt`: the 50,000 Riemann ζ zeros (Odlyzko-sourced) embedded in both implementations — the shared raw material of every statistic in the record.

_Location: [unpacked/](../../../README.md) › [python_clone/](../../README.md) › [abcloud/](../README.md) › [data/](README.md)_

This single file is the empirical substrate of the entire verification record: the ordinates (heights) of the first 50,000 non-trivial zeros of the Riemann ζ function, one per line, in ascending order — the Odlyzko-sourced dataset that the Julia suite embeds verbatim and that this Python clone embeds identically, so that the two implementations consume byte-identical input.

## Role in the record

Every statistical verdict in the package touches this file at least once: the Gram-point ladder of Tests 1–3 measures its approximation against these zeros; the distributional family (Tests 4–6, 11, 12) unfolds their spacings and compares them against GUE references; the long-range statistics (13–14) window them; the confrontation of Test 34 unfolds both this dataset and the lattice spectrum into a common coordinate and measures the distance; the Python clone's cross-language reproduction (Add.2) reads the same numbers. The suite reports the dataset's extent as T ≤ 40,434 — the height of the 50,000th zero — which is also why the record is explicit that asymptotic high-T claims (T ≳ 10^6) remain the province of larger external datasets.

## Format

Plain ASCII text, one ordinate per line, no header, no comments, ascending order; the first lines are 1.5 × 10¹ and the parse is `float(line)` per line. The file is checksummed in this edition's `../../SHA256SUMS_unpacked.txt`. Anyone can independently swap in a different zero list (the CLI's `--zeros N` scales the analysis depth) — the suite treats the file as data, not as scripture.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `zeta_zeros_50000.txt` | 770.7 KB · 5000 lines | The embedded dataset: the first 50,000 non-trivial ζ zeros (Odlyzko-sourced), one ordinate per line — byte-identical input for both implementations. |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../../README.md](../../../README.md)._