# Test 38 -- 64 spinor structures of the Klein quartic (Julia port)

Julia port of the validated C++ reference `verification/cpp/spinor38/spinor38.cpp`.
Uses ONLY the frozen data files and the stdlib `LinearAlgebra`; the Jacobi
eigenvalue algorithm is implemented in-file (no LAPACK calls).

## Run

    julia spinor38.jl [repo-root]

## Validated reference output (C++ / JavaScript, this environment)

    isospectrality within the odd orbit: max|dlambda| = 3.419e-14 -> PASS
    zero modes (representative): 2 (expected 2)
    <r> (representative): 0.4515710793 (reference 0.4515710793) -> PASS
    VERDICT: PASS

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `README.md` | 615 B | file |
| `spinor38.jl` | 4.5 KB | file |
| **Total (recursive)** | **2 files, 5.1 KB** | |

## ▶ Running — toolchain and entry point

- **Toolchain:** Julia ≥ 1.9 — LinearAlgebra stdlib, Jacobi eigenvalue algorithm implemented in-file
- **Run:** `julia spinor38.jl [repo-root]`

## 🔬 Deep dive — what Test 38 establishes

Test 38 examines the **64 spinor structures of the Klein quartic**:
for each structure it computes the level-spacing statistics of its
spectrum and compares them against the GUE law, exactly as the main
suite does for the zeta zeros. The verified verdict — confirmed
independently by the full spinor64 experiment in `../../spinor64/` —
is that **all 64 structures are GUE-consistent**, with the PSL(2,7)
orbit decomposition 28/21/7/7/1 and exact isospectrality inside each
orbit at the ≈ 1e-14 level.

House rules for this port: it reads **only the frozen data files**
(`../../data/`) and its language's standard library — where the
language lacks a LAPACK binding, the Jacobi eigenvalue algorithm is
implemented in-file (the Julia port documents this explicitly). The
output format is shared across all ten languages so their verdict
lines can be diffed mechanically; any line that differs from the
validated C++ reference (`../../cpp/spinor38/spinor38.cpp`) marks a
port bug.

## Кратко (по-русски)

- Тест 38: статистика межуровневых расстояний всех 64 спинор-структур
  квартики Кляйна против GUE; итог — 64/64 согласованы, орбиты
  PSL(2,7) 28/21/7/7/1, изоспектральность ≈ 1e-14.
- Только замороженные данные и stdlib; формат вывода одинаков во всех
  десяти языках и сверяется с C++-эталоном.
