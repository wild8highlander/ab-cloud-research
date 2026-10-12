# multilang/ — мультиязычные двойники вычислительного зерна

Шесть портов одного протокола: **Γ-замыкание** |Γ(½+iu)|² = π/cosh(πu)
(комплексный Lanczos g=7, n=9) на u ∈ {0.5, 1, 2, 3} и **Λ-сито** до
10⁵ с суммой Σ Λ(n)/n^{3/2}. Каждый порт печатает (и пишет по запросу)
единый управляющий блок `verify_control.txt`.

| Порт | Статус в этой среде | gamma_closure_max_res | lambda_sum_check |
|------|---------------------|-----------------------|------------------|
| c (C11) | верифицирован (cc -O2) | 1.13e-14 | 1.4989125716 |
| cpp (C++17) | верифицирован (g++ -O2) | 1.24e-14 | 1.4989125716 |
| javascript (Node ≥ 18) | верифицирован | 9.41e-15 | 1.4989125716 |
| go (≥ 1.21) | portable source (тулчейн недоступен) | — | — |
| rust (≥ 1.70) | portable source (тулчейн недоступен) | — | — |
| julia (≥ 1.9) | portable source (тулчейн недоступен) | — | — |

Эталоны Python: gamma ≤ 1e-12 (mpmath-эталон 1e-39 при dps 40),
lambda_sum = **1.4989125716** — совпадение с портами до 10 знаков
(расхождение Λ C↔Python ≤ 1e-11).

## Сборка

```bash
cc  -O2 c/verify_core.c -lm && ./a.out c/verify_control.txt
g++ -O2 -std=c++17 cpp/verify_core.cpp -o vc && ./vc cpp/verify_control.txt
node javascript/verify_core.js javascript/verify_control.txt
go build -o vg go/verify_core.go && ./vg go/verify_control.txt
rustc -O rust/verify_core.rs -o vr && ./vr rust/verify_control.txt
julia julia/verify_core.jl julia/verify_control.txt
```

Управляющий блок C-порта сверяется протоколом IVP10
(independent_verification/); эталонная серия Hilbert Polya Bridge даёт
5.9e-15 / 4.6e-11 — уровень тот же.

## V19 · сшивка ветвей (stitch-двойники, регрессия R3)

Начиная с v1.2.0 порты содержат второй двойник — `stitch_core`: сшивка
ветвей алгебраической функции (θ-лестница, знаковая когерентность,
фазовый закон ζ^{ra+sb} на торе (Z/15)²). θ(t) — асимптотика Стирлинга
(главная ветвь; Ланцош-лог не гарантирует ветку Im — проверено против
mpmath). Встроены первые 64 нуля ζ; контрольный блок
`stitch_control.txt`.

| Порт | Статус | conc | coherence | phase_law_max_res |
|------|--------|------|-----------|-------------------|
| c (C11) | верифицирован (cc -O2) | 0.967741935484 | 1.000000000000 | 1.21e-14 |
| javascript (Node ≥ 18) | верифицирован | 0.967741935484 | 1.000000000000 | 1.23e-14 |

Python-эталон (rpbridge.stitching на тех же 64 нулях): conc
0.967741935484, coherence 1.0 — совпадение до 1e-12; фазовый закон
double-порта 1.2e-14 (порог 1e-9). Вердикт: ALGEBRAIC_CERTIFICATE.

```bash
cc -O2 c/stitch_core.c -lm && ./a.out c/stitch_control.txt
node javascript/stitch_core.js javascript/stitch_control.txt
diff c/stitch_control.txt javascript/stitch_control.txt   # conc/coherence бит-в-бит
```
