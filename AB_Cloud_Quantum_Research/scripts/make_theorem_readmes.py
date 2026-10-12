#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_theorem_readmes.py — 6 детальных README для папок теорем
(пакет AB Cloud Quantum Research). Русская основная часть + English summary."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

THM = [
 dict(no=1, dir="T01_hermiticity", key="Th1", camp="V4",
      title_ru="Эрмитовость и вещественность спектра",
      title_en="Hermiticity and the real spectrum",
      stmt_ru=("Для любого набора вихрей, W, α и границ оператор H_L "
               "удовлетворяет H_L = H_L†; следовательно spec(H_L) ⊂ ℝ. "
               "При α = ½ и W = 0 спектр симметричен: λ ∈ spec ⇒ −λ ∈ spec."),
      stmt_en=("For any set of vortices, W, α and boundaries the operator "
               "H_L satisfies H_L = H_L†; hence spec(H_L) ⊂ ℝ. At α = ½ and "
               "W = 0 the spectrum is symmetric: λ ∈ spec ⇒ −λ ∈ spec."),
      idea_ru=("Каждая связь вносится парой H[i,j] = −t·e^{iφ}, H[j,i] = "
               "−t·e^{−iφ} = conj(H[i,j]) — эрмитовость по построению; "
               "диагональ вещественна (вихревой потенциал, беспорядок, "
               "стэггерд-масса). Симметрия при W = 0 — двудольность "
               "решётки по чётности ix+iy: в этом базисе H = [[0, B], "
               "[B†, 0]], и спектр зеркалится относительно нуля."),
      idea_en=("Every bond is inserted as a pair H[i,j] = −t·e^{iφ}, "
               "H[j,i] = −t·e^{−iφ} = conj(H[i,j]) — hermiticity by "
               "construction; the diagonal is real. The W = 0 symmetry "
               "comes from bipartiteness in ix+iy parity: in that basis "
               "H = [[0, B], [B†, 0]] and the spectrum mirrors about zero."),
      dims_ru=("a) ‖H−H†‖ по затворам L = 12/16/24/32 — ровно 0.0 (log-шкала); "
               "b) невязка вещественности спектра по затворам — ≤ 8.8e−15; "
               "c) спаривание λ ↔ −λ — до 8.2e−15; d) остатки собственных пар "
               "— ≤ 8.8e−15. Порог ε = 1e−12 отмечен на каждой панели."),
      dims_en=("a) ‖H−H†‖ across gates L = 12/16/24/32 — exactly 0.0 (log "
               "scale); b) spectrum-realness residuals ≤ 8.8e−15; c) λ ↔ −λ "
               "pairing to 8.2e−15; d) eigenpair residuals ≤ 8.8e−15. The "
               "ε = 1e−12 threshold is marked on every panel."),
      bounds_ru=("Th1 ничего не говорит о соответствии спектра нулям ζ "
                 "(отрицательные вердикты V1, V3, V6, V16). Симметрия λ ↔ −λ "
                 "нарушается уже при W > 0 и не восстанавливается вихрями."),
      bounds_en=("Th1 says nothing about matching the spectrum to the ζ zeros "
                 "(negative verdicts V1, V3, V6, V16). The λ ↔ −λ symmetry "
                 "breaks at W > 0 and is not restored by vortices."),
      files=("test_th1_passport.py (сертификат, Nv = 16/64/256, сид 96); "
             "computations/V04_operator_passport/ (монографии, фигуры); "
             "verification/claim_audit/claims/claim_v04.json")),
 dict(no=2, dir="T02_self_adjointness", key="Th2", camp="V8",
      title_ru="Конечномерная самосопряжённость",
      title_en="Finite-dimensional self-adjointness",
      stmt_ru=("Симметричный оператор на ℂ^N существенно самосопряжён: "
               "дефектные индексы (0, 0); e^{−iHt} унитарен; "
               "Im⟨ψ, Hψ⟩ = 0."),
      stmt_en=("A symmetric operator on ℂ^N is essentially self-adjoint: "
               "defect indices (0, 0); e^{−iHt} is unitary; Im⟨ψ, Hψ⟩ = 0."),
      idea_ru=("На ℂ^N всякий симметричный ограниченный оператор "
               "самосопряжён. Ключевая оценка: ‖(H ∓ iI)ψ‖² = ‖Hψ‖² + "
               "‖ψ‖² ≥ ‖ψ‖² > 0 — кросс-член исчезает по симметрии H, "
               "поэтому ker(H* ∓ iI) пусты. Следствия: спектр вещественен, "
               "e^{−iHt} — унитарная группа, форма вещественна."),
      idea_en=("On ℂ^N every symmetric bounded operator is self-adjoint. "
               "Key estimate: ‖(H ∓ iI)ψ‖² = ‖Hψ‖² + ‖ψ‖² ≥ ‖ψ‖² > 0 — the "
               "cross term vanishes by symmetry, hence ker(H* ∓ iI) are "
               "empty. Consequences: real spectrum, unitary e^{−iHt}, real "
               "form."),
      dims_ru=("a) дефектные индексы n+/n− по L = 12/16/24/32 — все нули; "
               "b) min сингулярное число H−iI ≈ 1.0 по L; c) дрейф "
               "унитарности 2.2e−16 и Im⟨ψ,Hψ⟩ = 0 против порога 1e−12; "
               "d) сдвиги спектра при смене границ (открытые/тор, 4 твиста) "
               "для L12/L24 — конечны и убывают с L."),
      dims_en=("a) defect indices n+/n− across L = 12/16/24/32 — all zero; "
               "b) smallest singular value of H−iI ≈ 1.0 across L; c) "
               "unitarity drift 2.2e−16 and Im⟨ψ,Hψ⟩ = 0 against 1e−12; "
               "d) spectrum shifts under boundary change (open/torus, 4 "
               "twists) for L12/L24 — finite, decaying with L."),
      bounds_ru=("Теорема конечномерна; перенос на L → ∞ требует оценки "
                 "существенного спектра — открытое обязательство O03."),
      bounds_en=("The theorem is finite-dimensional; the L → ∞ transfer "
                 "requires essential-spectrum estimates — open obligation "
                 "O03."),
      files=("test_th2_selfadjoint.py (дефекты, унитарность, вещественность "
             "формы); computations/V08_self_adjoint/; claim_v08.json")),
 dict(no=3, dir="T03_certificates", key="Th3", camp="V12",
      title_ru="Сертификаты собственных значений",
      title_en="Eigenvalue certificates",
      stmt_ru=("Для эрмитовой H, вычисленного λ̃, единичного v с невязкой "
               "r = Hv − λ̃v, δ = ‖r‖ и зазором gap до ближайшего другого "
               "уровня существует λ̂ ∈ spec H с |λ̂ − λ̃| ≤ δ²/gap; весь "
               "спектр лежит в объединении рациональных интервалов "
               "Гершгорина."),
      stmt_en=("For Hermitian H, computed λ̃, unit v with residual "
               "r = Hv − λ̃v, δ = ‖r‖ and gap to the nearest other level, "
               "there is λ̂ ∈ spec H with |λ̂ − λ̃| ≤ δ²/gap; the whole "
               "spectrum lies in the union of rational Gershgorin "
               "intervals."),
      idea_ru=("Разложение v = c·u + w с u — нормированным собственным "
               "вектором даёт ‖w‖ ≤ δ/gap и квадратичную сверхсходимость "
               "|λ̂ − λ̃| ≤ δ²/gap. Гершгорин: радиусы R_i = Σ_{j≠i}|H_ij| "
               "в точной рациональной арифметике (fractions, "
               "limit_denominator 1e12) — интервалы без округлений."),
      idea_en=("Decomposing v = c·u + w with u a normalized eigenvector "
               "gives ‖w‖ ≤ δ/gap and quadratic superconvergence "
               "|λ̂ − λ̃| ≤ δ²/gap. Gershgorin: radii R_i = Σ_{j≠i}|H_ij| in "
               "exact rational arithmetic (fractions, limit_denominator "
               "1e12) — rounding-free intervals."),
      dims_ru=("a) невязка δ по пяти сертификатам (log); b) граница "
               "Каутского δ²/gap (log); c) ширины интервалов hi−lo — "
               "~1e−27 (mpmath dps 40); d) покрытие Гершгорина [−4.210, "
               "4.205] с 144 интервалами и положением λ̃."),
      dims_en=("a) residual δ across five certificates (log); b) Kato bound "
               "δ²/gap (log); c) interval widths hi−lo — ~1e−27 (mpmath "
               "dps 40); d) Gershgorin coverage [−4.210, 4.205] with 144 "
               "intervals and the λ̃ positions."),
      bounds_ru=("Оценка квадратична по δ — требует уже хорошо сошедшегося "
                 "λ̃; для близких уровней зазор мал и интервал расширяется; "
                 "рациональная арифметика медленна — слой применяется "
                 "точечно."),
      bounds_en=("The bound is quadratic in δ — a well-converged λ̃ is "
                 "required; close levels shrink the gap and widen the "
                 "interval; rational arithmetic is slow — applied pointwise."),
      files=("test_th3_certificates.py (попадание, покрытие, "
             "воспроизводимость); computations/V12_interval_certificates/; "
             "claim_v12.json")),
 dict(no=4, dir="T04_li_spectral", key="Th4", camp="V15",
      title_ru="Спектральная формула коэффициентов Ли",
      title_en="Spectral formula of the Li coefficients",
      stmt_ru=("Коэффициенты Ли допускают спектральную запись λ_n = "
               "Tr g_n(H_ξ), g_n(E) = 1 − (1 − 1/ρ(E))^n, ρ(E) = ½ − iE/2; "
               "ряд сходится абсолютно; две вычислительные траектории "
               "согласованы с |Δ| ≤ 4.4e−11 для n ≤ 3000."),
      stmt_en=("The Li coefficients admit the spectral form λ_n = "
               "Tr g_n(H_ξ), g_n(E) = 1 − (1 − 1/ρ(E))^n, ρ(E) = ½ − iE/2; "
               "the series converges absolutely; two computational paths "
               "agree to |Δ| ≤ 4.4e−11 for n ≤ 3000."),
      idea_ru=("По определению λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]; биекция "
               "spec H_ξ ↔ пары нулей {γ, −γ} переводит след в сумму по "
               "парам с вкладом O(n/γ²) — абсолютная сходимость по "
               "Σ 1/γ². Полюса g_n в точке ρ = 1 (E = −i) — вне "
               "вещественного спектра H_ξ."),
      idea_en=("By definition λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]; the bijection "
               "spec H_ξ ↔ zero pairs {γ, −γ} turns the trace into a pair "
               "sum with O(n/γ²) contributions — absolute convergence by "
               "Σ 1/γ². The poles of g_n sit at ρ = 1 (E = −i), outside "
               "the real spectrum of H_ξ."),
      dims_ru=("a) λ_n при n = 1/100/1000/3000 (log) с λ_min = 0.0231 > 0; "
               "b) согласование двух путей 4.4e−11 против порога 1e−9; "
               "c) сертифицированный хвост ≤ 0.115; d) контроль: ранговая "
               "корреляция затворов −1.0 против r = 0.9996 для H_ξ."),
      dims_en=("a) λ_n at n = 1/100/1000/3000 (log) with λ_min = 0.0231 > 0; "
               "b) two-path agreement 4.4e−11 against 1e−9; c) certified "
               "tail ≤ 0.115; d) control: gate rank correlation −1.0 "
               "versus r = 0.9996 for H_ξ."),
      bounds_ru=("Положительность λ_n — эмпирика до n = 3000; для всех n "
                 "вопрос открыт и эквивалентен RH (O11 — assumed). "
                 "Согласование путей зависит от хвостовой модели."),
      bounds_en=("Positivity of λ_n is empirical up to n = 3000; for all n "
                 "it is open and equivalent to RH (O11 — assumed). Path "
                 "agreement depends on the tail model."),
      files=("test_th4_li.py; computations/V15_li_criterion/; "
             "claim_v15.json; файл нулей zeta_zeros_50000_embedded.txt")),
 dict(no=5, dir="T05_block_reduction", key="Th5", camp="V9",
      title_ru="Блочная редукция по симметрии",
      title_en="Block reduction by symmetry",
      stmt_ru=("Если [H, A] = [H, B] = 0 для порождающих абелевой группы G "
               "магнитных трансляций, то H блочно-диагонален в разложении "
               "по характерам χ группы G и spec H = ⊔_χ spec(H|Π_χ Π_χ)."),
      stmt_en=("If [H, A] = [H, B] = 0 for the generators of an abelian "
               "group G of magnetic translations, then H is block-diagonal "
               "in the character decomposition and "
               "spec H = ⊔_χ spec(H|Π_χ Π_χ)."),
      idea_ru=("Коммутирующие унитарные A, B одновременно диагонализуются; "
               "совместные собственные значения — характеры χ: G → U(1); "
               "проекторы Π_χ (полиномы от A, B) коммутируют с H, каждое "
               "Π_χℂ^N инвариантно, H распадается в прямую сумму сужений. "
               "Следствие: спектр ищется в блоках ~L²/6 вместо L²."),
      idea_en=("Commuting unitaries A, B are simultaneously diagonalizable; "
               "joint eigenvalues are characters χ: G → U(1); projectors "
               "Π_χ (polynomials in A, B) commute with H, each Π_χℂ^N is "
               "invariant, and H splits into a direct sum of restrictions. "
               "Consequence: the spectrum is found in blocks of ~L²/6 "
               "instead of L²."),
      dims_ru=("a) коммутаторы чистой решётки ε_Ux/ε_Uy/ε_AB/внеблочные "
               "(log) — ~9e−15; b) ошибка объединения блоков 7.1e−15 против "
               "порога 1e−9; c) вихри: коммутаторы по 4 твистам — "
               "ε ~ O(1), симметрия сломана (отрицательный контроль); "
               "d) среднее r по твистам ≈ 0.6."),
      dims_en=("a) clean-lattice commutators ε_Ux/ε_Uy/ε_AB/off-block (log) "
               "— ~9e−15; b) block-union error 7.1e−15 against 1e−9; "
               "c) vortices: commutators over 4 twists — ε ~ O(1), symmetry "
               "broken (negative control); d) mean r over twists ≈ 0.6."),
      bounds_ru=("Для несимметричных вихревых размещений редукция "
                 "неприменима — это граница области действия, а не дефект; "
                 "частично-симметричные конфигурации дают приближённые "
                 "инвариантные подпространства (в пакет не включено)."),
      bounds_en=("For asymmetric vortex placements the reduction does not "
                 "apply — a scope boundary, not a defect; partially "
                 "symmetric configurations give approximate invariant "
                 "subspaces (not included)."),
      files=("test_th5_block_reduction.py; "
             "computations/V09_symmetry_reduction/; claim_v09.json")),
 dict(no=6, dir="T06_trace_formula", key="Th6", camp="V7",
      title_ru="Следовая формула Гуинанда–Вейля",
      title_en="Guinand–Weil trace formula",
      stmt_ru=("Q(a) = Σ_{γ>0} 2a/(a²+γ²) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) "
               "− ½ln π + ½ψ(¼+a/2) − B − C₀, где B = ½ln(4π) − 1 − γ/2, "
               "C₀ = −B; и K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a)·sin(ax) da."),
      stmt_en=("Q(a) = Σ_{γ>0} 2a/(a²+γ²) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) "
               "− ½ln π + ½ψ(¼+a/2) − B − C₀, with B = ½ln(4π) − 1 − γ/2, "
               "C₀ = −B; and K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a)·sin(ax) da."),
      idea_ru=("Логарифмическая производная произведения Адамара ξ(s) даёт "
               "сумму по нулям; явные полюсные члены (полюс ζ при s = 1, "
               "функциональное уравнение при s = ½, Γ-фактор через ψ) "
               "собираются в константы B и C₀ (выведены заново — эрратум "
               "родительского репозитория исправлен). Представление "
               "2a/(a²+γ²) = 2∫e^{−γt} sin(at) dt и смена порядка "
               "интегрирования дают K(x); при a > ½ ряд ζ′/ζ переносит вес "
               "Λ(n)/√n в след."),
      idea_en=("The logarithmic derivative of the Hadamard product of ξ(s) "
               "gives the zero sum; explicit pole terms (ζ pole at s = 1, "
               "functional equation at s = ½, Γ-factor via ψ) assemble into "
               "the constants B and C₀ (re-derived — parent-repo erratum "
               "fixed). The representation 2a/(a²+γ²) = 2∫e^{−γt}sin(at)dt "
               "and exchanging integration order give K(x); at a > ½ the "
               "series ζ′/ζ moves the Λ(n)/√n weight into the trace."),
      dims_ru=("a) арифметика констант: |B−C₀| = 2.5e−10 и M0(Q) "
               "(log); b) след H_ξ ↔ простые: r = 0.9996, невязка 0.027; "
               "c) решёточные затворы: r_EF по затворам (среднее 0.76); "
               "d) контраст H_ξ против решётки — гребёнка простых живёт "
               "только в следе H_ξ."),
      dims_en=("a) constants arithmetic: |B−C₀| = 2.5e−10 and M0(Q) (log); "
               "b) H_ξ trace ↔ primes: r = 0.9996, residual 0.027; "
               "c) lattice gates: r_EF per gate (mean 0.76); d) the H_ξ vs "
               "lattice contrast — the prime comb lives only in the H_ξ "
               "trace."),
      bounds_ru=("Эталон «работающего оператора» — ДА для H_ξ, НЕТ для "
                 "решёточных затворов (гипотеза A: класс A подтверждён, "
                 "архитектурная связь затворов с ζ — нет); константы "
                 "проверены асимптотикой a → 0+."),
      bounds_en=("The «working operator» reference holds for H_ξ, not for "
                 "the lattice gates (class A confirmed for the mathematical "
                 "construction; the architectural gate link to ζ — no); the "
                 "constants are verified by the a → 0+ asymptotics."),
      files=("test_th6_trace_formula.py; computations/V07_arithmetic_trace/; "
             "claim_v07.json")),
]

TPL_RU = """# {key}. {title_ru} — вывод теоремы

**Кампания:** {camp} · **Формальная редукция:** {ax} · **Документы:**
`theorem_{lk}_ru.pdf/.docx`, `theorem_{lk}_en.pdf/.docx` ·
**Фигура:** `figures/{stem}_4dim_ru.png`, `figures/{stem}_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

{stmt_ru}

## Идея вывода

{idea_ru}

## Четыре измерения фигуры

{dims_ru}

## Сертификат и артефакты кампании

{files}

## Границы (честно)

{bounds_ru}

## English summary

**Statement.** {stmt_en}

**Proof idea.** {idea_en}

**Figure dimensions.** {dims_en}

**Boundaries.** {bounds_en}
"""

AX = {1: "A1 (спектральная теорема)", 2: "A2b (распадение дефектной нормы)",
      3: "A4 (Като–Темпл), A5 (Гершгорин)", 4: "A6 (сходимость ряда Ли)",
      5: "A2 (одновременная диагонализация)", 6: "A3 (произведение Адамара)"}


def main():
    for t in THM:
        d = os.path.join(ROOT, "theorems_lemmas", t["dir"])
        os.makedirs(d, exist_ok=True)
        text = TPL_RU.format(
            key=t["key"], title_ru=t["title_ru"], camp=t["camp"],
            ax=AX[t["no"]], lk=t["key"].lower(), stem=f"th{t['no']}",
            stmt_ru=t["stmt_ru"], idea_ru=t["idea_ru"],
            dims_ru=t["dims_ru"], files=t["files"], bounds_ru=t["bounds_ru"],
            stmt_en=t["stmt_en"], idea_en=t["idea_en"],
            dims_en=t["dims_en"], bounds_en=t["bounds_en"])
        with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
            f.write(text)
        print("OK", t["dir"])


if __name__ == "__main__":
    main()
