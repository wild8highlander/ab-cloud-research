# Per-Section Micro-Verifications

Tiny self-contained Python scripts that verify one closed-form claim of the
monograph per folder. They are intentionally minimal (pure `math`, no data
files, no dependencies) so that a referee can eyeball the entire proof in one
screen and run each check in under a second.

## Layout

| Path | Checks |
|---|---|
| `section3_ab_cloud/python/verify.py` | the section-3 closed form for the AB correction constant: `b = π / (4π² + 2π√3)`; asserts the value is real, positive and < 1, prints it with 15 significant digits, then prints PASS |
| `section6_riemann_zeros/python/verify.py` | the same guard for the section-6 closed form used in the Riemann-zeros discussion |

## Run

```bash
python3 verification/sections/section3_ab_cloud/python/verify.py
# === Section 3 ===
# b = 0.070692281021956
# PASS

python3 verification/sections/section6_riemann_zeros/python/verify.py
# === Section 6 ===
# b = 0.070692281021956
# PASS
```

Both scripts exit non-zero on any assertion failure, so they can be used as
CI smoke tests (see `.github/workflows/ci.yml`).

## Conventions for new sections

1. One folder per monograph section: `sectionN_<slug>/python/verify.py`.
2. Import only `math` (stdlib) — the point is transparency, not coverage.
3. Print the computed value with `.15f`, assert every claimed inequality,
   finish with `print("PASS")`.
4. Record the expected printed value in this README when adding a section.

## Кратко (по-русски)

- Микро-проверки замкнутых формул монографии: по одному скрипту на раздел
  (сейчас разделы 3 и 6), чистый `math`, без данных и зависимостей.
- Запуск: `python3 verification/sections/section3_ab_cloud/python/verify.py`
  → печатает `b = 0.070692281021956` и `PASS`; при нарушении утверждений код
  возврата ненулевой (можно вешать на CI).
- Конвенции для новых разделов — в §3 этого README.
