<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ 02_data/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
# 02_data/frozen — the frozen ζ-zero datasets

Byte-identical copies of the repo's canonical frozen datasets
(`verification/` — the same files the Julia canon, the ten language ports
and the formal Lean layer read). The golden rule of the programme applies:
**every arrow reads the same frozen dataset** — these files exist inside the
package so that the package is self-contained and any disagreement between
the package and the sources is immediately visible rather than hidden by
different inputs.

| File | Lines | What it is |
|---|---|---|
| `zeros50k.txt` | 50,000 | the embedded reference set of the full suite (first 50 000 zeros, one per line) |
| `zeros1.txt` | 100,000 | the 100k extension set (Test-14 rigidity grid and the L-scaling studies) |
| `zeta_zeros_13661.txt` | 5,000 | the 13 661-zero set (10 per line) used by the Riemann–Siegel blind-reading cross-checks |
| `zeta_zeros_highT_blocks.txt` | 30,003 | the high-T BLOCK-indexed strips (index=1e12 offsets) for the T-band count tests |

## What is deliberately NOT byte-copied here

The two large Odlyzko-derived tables (`zeta_zeros_500k_odlyzko.txt`,
8.3 MB; `zeta_zeros_2M_odlyzko.txt`, 34 MB) follow the package's own
`02_data/external/` policy: external bulk tables are referenced by link and
checksum, not duplicated. They live in the repository at
`verification/zeta_zeros_500k_odlyzko.txt` and
`verification/zeta_zeros_2M_odlyzko.txt`; their SHA-256 sums are pinned in
`verification/` and the sampling protocol (see `../sampling_protocol.md`)
documents how they enter the tests. If you need the package fully offline
including these two tables, copy them from the repository — nothing else is
required, the suite reads them by relative path.

## Integrity

Every file in `02_data/**` is covered by `../checksums.sha256`. After
editing anything here, regenerate it with `python3
06_code/scripts/update_checksums.py`.

<div align="center">

<img src="../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
