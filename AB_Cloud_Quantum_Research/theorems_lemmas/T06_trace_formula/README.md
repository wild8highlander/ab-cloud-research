# Th6. Следовая формула Гуинанда–Вейля — вывод теоремы

**Кампания:** V7 · **Формальная редукция:** A3 (произведение Адамара) · **Документы:**
`theorem_th6_ru.pdf/.docx`, `theorem_th6_en.pdf/.docx` ·
**Фигура:** `figures/th6_4dim_ru.png`, `figures/th6_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

Q(a) = Σ_{γ>0} 2a/(a²+γ²) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½ln π + ½ψ(¼+a/2) − B − C₀, где B = ½ln(4π) − 1 − γ/2, C₀ = −B; и K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a)·sin(ax) da.

## Идея вывода

Логарифмическая производная произведения Адамара ξ(s) даёт сумму по нулям; явные полюсные члены (полюс ζ при s = 1, функциональное уравнение при s = ½, Γ-фактор через ψ) собираются в константы B и C₀ (выведены заново — эрратум родительского репозитория исправлен). Представление 2a/(a²+γ²) = 2∫e^{−γt} sin(at) dt и смена порядка интегрирования дают K(x); при a > ½ ряд ζ′/ζ переносит вес Λ(n)/√n в след.

## Четыре измерения фигуры

a) арифметика констант: |B−C₀| = 2.5e−10 и M0(Q) (log); b) след H_ξ ↔ простые: r = 0.9996, невязка 0.027; c) решёточные затворы: r_EF по затворам (среднее 0.76); d) контраст H_ξ против решётки — гребёнка простых живёт только в следе H_ξ.

## Сертификат и артефакты кампании

test_th6_trace_formula.py; computations/V07_arithmetic_trace/; claim_v07.json

## Границы (честно)

Эталон «работающего оператора» — ДА для H_ξ, НЕТ для решёточных затворов (гипотеза A: класс A подтверждён, архитектурная связь затворов с ζ — нет); константы проверены асимптотикой a → 0+.

## English summary

**Statement.** Q(a) = Σ_{γ>0} 2a/(a²+γ²) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½ln π + ½ψ(¼+a/2) − B − C₀, with B = ½ln(4π) − 1 − γ/2, C₀ = −B; and K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a)·sin(ax) da.

**Proof idea.** The logarithmic derivative of the Hadamard product of ξ(s) gives the zero sum; explicit pole terms (ζ pole at s = 1, functional equation at s = ½, Γ-factor via ψ) assemble into the constants B and C₀ (re-derived — parent-repo erratum fixed). The representation 2a/(a²+γ²) = 2∫e^{−γt}sin(at)dt and exchanging integration order give K(x); at a > ½ the series ζ′/ζ moves the Λ(n)/√n weight into the trace.

**Figure dimensions.** a) constants arithmetic: |B−C₀| = 2.5e−10 and M0(Q) (log); b) H_ξ trace ↔ primes: r = 0.9996, residual 0.027; c) lattice gates: r_EF per gate (mean 0.76); d) the H_ξ vs lattice contrast — the prime comb lives only in the H_ξ trace.

**Boundaries.** The «working operator» reference holds for H_ξ, not for the lattice gates (class A confirmed for the mathematical construction; the architectural gate link to ζ — no); the constants are verified by the a → 0+ asymptotics.
