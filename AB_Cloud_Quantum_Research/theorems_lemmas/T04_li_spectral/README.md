# Th4. Спектральная формула коэффициентов Ли — вывод теоремы

**Кампания:** V15 · **Формальная редукция:** A6 (сходимость ряда Ли) · **Документы:**
`theorem_th4_ru.pdf/.docx`, `theorem_th4_en.pdf/.docx` ·
**Фигура:** `figures/th4_4dim_ru.png`, `figures/th4_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

Коэффициенты Ли допускают спектральную запись λ_n = Tr g_n(H_ξ), g_n(E) = 1 − (1 − 1/ρ(E))^n, ρ(E) = ½ − iE/2; ряд сходится абсолютно; две вычислительные траектории согласованы с |Δ| ≤ 4.4e−11 для n ≤ 3000.

## Идея вывода

По определению λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]; биекция spec H_ξ ↔ пары нулей {γ, −γ} переводит след в сумму по парам с вкладом O(n/γ²) — абсолютная сходимость по Σ 1/γ². Полюса g_n в точке ρ = 1 (E = −i) — вне вещественного спектра H_ξ.

## Четыре измерения фигуры

a) λ_n при n = 1/100/1000/3000 (log) с λ_min = 0.0231 > 0; b) согласование двух путей 4.4e−11 против порога 1e−9; c) сертифицированный хвост ≤ 0.115; d) контроль: ранговая корреляция затворов −1.0 против r = 0.9996 для H_ξ.

## Сертификат и артефакты кампании

test_th4_li.py; computations/V15_li_criterion/; claim_v15.json; файл нулей zeta_zeros_50000_embedded.txt

## Границы (честно)

Положительность λ_n — эмпирика до n = 3000; для всех n вопрос открыт и эквивалентен RH (O11 — assumed). Согласование путей зависит от хвостовой модели.

## English summary

**Statement.** The Li coefficients admit the spectral form λ_n = Tr g_n(H_ξ), g_n(E) = 1 − (1 − 1/ρ(E))^n, ρ(E) = ½ − iE/2; the series converges absolutely; two computational paths agree to |Δ| ≤ 4.4e−11 for n ≤ 3000.

**Proof idea.** By definition λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]; the bijection spec H_ξ ↔ zero pairs {γ, −γ} turns the trace into a pair sum with O(n/γ²) contributions — absolute convergence by Σ 1/γ². The poles of g_n sit at ρ = 1 (E = −i), outside the real spectrum of H_ξ.

**Figure dimensions.** a) λ_n at n = 1/100/1000/3000 (log) with λ_min = 0.0231 > 0; b) two-path agreement 4.4e−11 against 1e−9; c) certified tail ≤ 0.115; d) control: gate rank correlation −1.0 versus r = 0.9996 for H_ξ.

**Boundaries.** Positivity of λ_n is empirical up to n = 3000; for all n it is open and equivalent to RH (O11 — assumed). Path agreement depends on the tail model.
