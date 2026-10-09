# multilang/ — мультиязычные двойники ядра

Шесть портов одного и того же вычислительного зерна — «Γ-замыкание +
Λ-сито» — для перекрёстной проверки арифметики на разных языках и
рантаймах. Все порты пишут одинаковый управляющий блок
`verify_control.txt`:

```
gamma_closure_max_res = 5.855e-15   # max |  |Г(½+iu)| − √(π/cosh πu) | / ref, u ∈ {0.5, 1, 2, 3}
lambda_sum_check    = 1.4989125716  # Σ Λ(n)/n^{3/2}, n ≤ 1e5
n_sieve             = 100000
```

## Статусы портов (честно)

| Порт | Язык | Статус | Управляющий блок |
|------|------|--------|------------------|
| `c/verify_core.c` | C11 | **верифицирован в этой среде** | `c/verify_control.txt` (закоммичен) |
| `cpp/verify_core.cpp` | C++17 | **верифицирован в этой среде** | см. лог сборки ниже |
| `javascript/verify_core.js` | Node ≥ 18 | **верифицирован в этой среде** | см. лог сборки |
| `go/verify_core.go` | Go ≥ 1.21 | portable source | тулчейн недоступен в среде сборки |
| `rust/verify_core.rs` | Rust ≥ 1.70 | portable source | тулчейн недоступен в среде сборки |
| `julia/verify_core.jl` | Julia ≥ 1.9 | portable source | тулчейн недоступен в среде сборки |

Эталонные значения (Python, тот же алгоритм): gamma_closure_max_res =
5.9e-15 (пол двойной точности), lambda_sum_check = 1.4989125716.
Расхождение Λ-суммы между C и Python: 4.6e-11.

## Сборка и запуск

```bash
# C
cc -O2 multilang/c/verify_core.c -lm -o /tmp/hpb_c && /tmp/hpb_c multilang/c/verify_control.txt
# C++
g++ -O2 -o /tmp/hpb_cpp multilang/cpp/verify_core.cpp && /tmp/hpb_cpp /tmp/ctl_cpp.txt
# JavaScript
node multilang/javascript/verify_core.js /tmp/ctl_js.txt
# Go (где есть тулчейн)
go build -o /tmp/hpb_go multilang/go/verify_core.go && /tmp/hpb_go /tmp/ctl_go.txt
# Rust (где есть тулчейн)
rustc -O -o /tmp/hpb_rs multilang/rust/verify_core.rs && /tmp/hpb_rs /tmp/ctl_rs.txt
# Julia (где есть тулчейн)
julia multilang/julia/verify_core.jl /tmp/ctl_jl.txt
```

IVP10 (independent_verification/) сверяет закоммиченный C-блок с
пересчётом на Python; порты с «portable source» верифицируются той же
процедурой на машинах с их тулчейнами.
