# Historical Julia Versions (v19_v1, v20, v21) — Provenance Archive

This subfolder preserves the **author's Julia sources as supplied** during
the v1.1.0 preparation, so that every number in the reports can be traced to
the exact code version that produced it. Nothing here is required to run the
project — use the canonical suite `../ab_cloud_v19.jl` — but the folder is
kept for reproducibility archaeology.

## Files

| File | Lines | Version notes |
|---|---|---|
| `ab_cloud_v19.jl` | 23 342 | author's v19 as received (differs from the canonical cleaned `../ab_cloud_v19.jl` by the report-engine fixes FIX-R1…R5b documented in `monographs/PACKAGE_README.md`) |
| `ab_cloud_v19_v1.jl` | 23 956 | v19_v1 — intermediate revision; contains the **embedded 50 000-zero table** from which `verification/data/zeta_zeros_50000_embedded.txt` was extracted verbatim |
| `ab_cloud_v20.jl` | 24 596 | v20 — adds extended diagnostics over v19_v1 |
| `ab_cloud_v21.jl` | 25 519 | v21 — the version the original author monograph v21 accompanied |
| `ab_cloud_v21_v1.jl` | 25 519 | v21_v1 — minor revision of v21 supplied together with it |

## What each version contributes

- **v19 (canonical)** — the two-pass 37-test protocol with the fixed report
  engine (before the fixes, a `(kind, text)` tuple bug degraded all 37
  verdicts to FAIL/WARN and silently skipped pass 2 — see
  `../../monographs/PACKAGE_README.md`, "v18 → v19").
- **v19_v1** — introduces the embedded ζ-zero dataset (50 000 Odlyzko zeros
  as a literal Julia array); the extraction script wrote the standalone
  text file now used by the dashboard and all Test-38 ports.
- **v20** — extended diagnostics pass; intermediate between the suite and
  the monograph-v21 code state.
- **v21 / v21_v1** — the code state referenced by the original v21
  monograph (including its spinor experiment whose idx=38 claim was later
  corrected by `verification/spinor64/`).

## Running any historical version

Each file is standalone (stdlib-only Julia), so:

```bash
julia code/julia/ab_cloud_v21.jl --quick      # example: fast check of v21
julia code/julia/ab_cloud_v19_v1.jl --test 1  # example: single test from v19_v1
```

Flags match the canonical suite (`--quick`, `--test all|N`, `--zeros`,
`--source`). Historical versions may print slightly different report
layouts — that is expected; the canonical numbers come from
`../ab_cloud_v19.jl` only.

## Кратко (по-русски)

- Папка — архив авторских версий кода (v19, v19_v1, v20, v21, v21_v1,
  всего ~122 тыс. строк) для прослеживаемости результатов.
- Из встроенной таблицы нулей в `ab_cloud_v19_v1.jl` извлечён файл
  `verification/data/zeta_zeros_50000_embedded.txt`.
- Рабочая версия проекта — `../ab_cloud_v19.jl`; исторические запускаются
  так же (`julia <файл> --quick`), но канонические числа даёт только она.
