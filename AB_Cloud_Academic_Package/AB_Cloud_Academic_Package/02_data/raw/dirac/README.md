# 📈 Raw Zero Tables — the Dirac-lab input set

Three tables of Riemann zeta zeros on the critical line, stored raw with their
header comments intact — the shared numeric input of the dirac-lab notebooks
and of the package's zero-statistics chapters.

| File | Count | Window | Notes |
|---|---|---|---|
| [`zeta_zeros_2000.txt`](zeta_zeros_2000.txt) | 2 000 | γ₁ ≈ 14.1347 … | the main working table (s = ½ + i·t, ascending) |
| [`zeta_zeros_high_2000.txt`](zeta_zeros_high_2000.txt) | 2 000 | the high window | used for windowed (segment) statistics |
| [`zeta_zeros_low_600.txt`](zeta_zeros_low_600.txt) | 600 | the low window | small-N checks and fast examples |

**Provenance.** All three carry the same header: they are taken from Andrew
Odlyzko's official table [`zeros6`](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6)
via `ab-cloud-research/verification/data`, verbatim and unmodified — comments,
ordering and precision preserved. The header comment block at the top of each
file is the provenance stamp; keep it when re-distributing within the package.

> [!NOTE]
> These are raw inputs, not run artifacts. Derived quantities computed from
> them live with the runs that produced them (see
> [`../../../../results/`](../../../../../results/) and the package's
> [`processed/`](../../processed/README.md) registry); do not edit these files
> to "fix" anything — cite a different table instead.

Part of [`AB_Cloud_Academic_Package/02_data/raw/`](../)
