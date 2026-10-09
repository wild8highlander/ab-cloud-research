#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_comp_readmes.py — генератор гигантских билингвальных README
папок вычислений C1–C8 (README.md на русском + README.en.md на английском).
Запуск: python3 scripts/make_comp_readmes.py"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

C = {}

C["C1_identity_function"] = {
"slug": "C1 · Функция тождеств и Γ-лестница",
"slug_en": "C1 · The identity function and the Γ-ladder",
"one": "Сборка функции тождеств Z_id(t) = e^{iθ(t)}ζ(½+it) из алгебраических "
       "замыканий Γ-каркаса; критерии K1–K4, K7; один честный отказ — "
       "неэлементарность отдельного модуля на линии.",
"one_en": "Assembling the identity function Z_id(t) = e^{iθ(t)}ζ(½+it) from "
          "the algebraic closures of the Γ-frame; criteria K1–K4, K7; one "
          "honest refutation — the single modulus on the line is not elementary.",
"question": [
 "Можно ли собрать на критической линии функцию, нули которой совпадают с "
 "нулями ζ, не обращаясь ни к каким данным о нулях — только к элементарным "
 "тождествам Γ-каркаса и самому ζ? Ответ этой кампании — да, и это "
 "составляет график всей серии: Z_id(t) = e^{iθ(t)}ζ(½+it). Но вместе с "
 "ответом фиксируется и граница: алгебраическая огибающая не порождает "
 "нули — она лишь упаковывает ζ в гладкую фазу. Всё, что верно для Z_id, "
 "верно в силу тождеств; всё, чего Z_id не может, не сможет ни одна "
 "перестройка фазы.",
],
"question_en": [
 "Can one assemble, on the critical line, a function whose zeros coincide "
 "with those of ζ without using any zero data — only elementary identities "
 "of the Γ-frame and ζ itself? This campaign answers yes, and that answer "
 "is the graph of the whole series: Z_id(t) = e^{iθ(t)}ζ(½+it). But the "
 "answer fixes the boundary as well: the algebraic envelope does not "
 "generate zeros — it merely wraps ζ in a smooth phase. Whatever is true "
 "of Z_id is true by identity; whatever Z_id cannot do, no rearrangement "
 "of the phase can do either.",
],
"results": [
 ("Замыкание |Γ(½+iu)|² = π/cosh πu", "невязка 2.59e-39 (dps 40)", "доказано"),
 ("Замыкание |Γ(iu)|² = π/(u·sinh πu)", "невязка 2.57e-39", "доказано"),
 ("Произведение |Γ(¼+iu)|·|Γ(¾+iu)| (Лежандр)", "невязка 1.27e-39", "доказано"),
 ("Кандидат-форма отдельного модуля", "структурное расхождение 0.765", "опровергнуто"),
 ("Вещественность Z_id (K2)", "max|Im Z_id| = 4.9e-29", "доказано"),
 ("Нули Z_id на [0,200] против mpmath (K3)", "79 нулей, max|Δγ| = 2.8e-14", "подтверждено"),
 ("Точки Грама (K7)", "220 точек, 4 нарушения (классика)", "воспроизведено"),
],
"results_en": [
 ("Closure |Γ(½+iu)|² = π/cosh πu", "residual 2.59e-39 (dps 40)", "proven"),
 ("Closure |Γ(iu)|² = π/(u·sinh πu)", "residual 2.57e-39", "proven"),
 ("Product |Γ(¼+iu)|·|Γ(¾+iu)| (Legendre)", "residual 1.27e-39", "proven"),
 ("Candidate form of the single modulus", "structural mismatch 0.765", "refuted"),
 ("Reality of Z_id (K2)", "max|Im Z_id| = 4.9e-29", "proven"),
 ("Z_id zeros on [0,200] vs mpmath (K3)", "79 zeros, max|Δγ| = 2.8e-14", "confirmed"),
 ("Gram points (K7)", "220 points, 4 violations (classical)", "reproduced"),
],
"how": [
 "Ядро кампании — hpbridge/identity.py: θ(t) через Im ln Γ(¼+it/2), сборка "
 "Z_id в двух арифметиках (float64 и mpmath dps 25–40), бисекция нулей по "
 "смене знака с 80 итерациями доуплотнения, точки Грама через findroot. "
 "Γ-замыкания проверяются на сетке 401 точки при dps = 40; невязка "
 "сравнивается с порогом 1e-30. Вся кампания детерминирована и исполняется "
 "примерно за две секунды.",
],
"how_en": [
 "The campaign core is hpbridge/identity.py: θ(t) via Im ln Γ(¼+it/2), the "
 "Z_id assembly in two arithmetics (float64 and mpmath dps 25–40), zero "
 "bisection on sign changes with 80 refinement steps, Gram points via "
 "findroot. The Γ-closures are verified on a 401-point grid at dps = 40 "
 "against the 1e-30 threshold. The whole campaign is deterministic and "
 "runs in about two seconds.",
],
"figs": ["fig01_zid", "fig02_gamma_ladder"],
"honest": [
 "Терминологическая гигиена: выражение «Riemann relations» в соседних "
 "проектах относится к билинейным соотношениям для матриц периодов, а не "
 "к гипотезе Римана. В этой серии оба предмета разведены явно.",
 "Опровержение K1 — не поражение, а калибровка: лестница замыкается "
 "элементарно только на краях полосы и произведением пары Лежандра. "
 "Именно это произведение входит в фазу θ(t).",
],
"honest_en": [
 "Terminological hygiene: Riemann relations in neighbouring projects "
 "refers to bilinear relations for period matrices, not to the Riemann "
 "Hypothesis. The series keeps the two subjects strictly apart.",
 "The K1 refutation is not a defeat but a calibration: the ladder closes "
 "elementarily only at the strip edges and through the Legendre pair "
 "product — exactly the product that enters the phase θ(t).",
],
}

C["C2_argument_principle"] = {
"slug": "C2 · Аргументный принцип до T = 1000",
"slug_en": "C2 · The argument principle up to T = 1000",
"one": "Счёт нулей в критической полосе без таблиц: адаптивный шаг Тьюринга, "
       "калибровка полюса (лемма T3), мост арифметик 2.6e-26, RH верифицирована "
       "в полосе: 649 = 649.",
"one_en": "Counting zeros in the critical strip without tables: the adaptive "
          "Turing step, the pole calibration (lemma T3), the arithmetic bridge "
          "2.6e-26; RH verified in the strip: 649 = 649.",
"question": [
 "Сколько нулей дзеты лежит в критической полосе ниже высоты T, и все ли "
 "они на критической линии? Кампания отвечает аргументным принципом: "
 "контур (2,0)→(2,T)→(0,T)→(0,0) с обходом полюса s = 1 сверху даёт "
 "N(T) = Δarg ξ / 2π, и это число сравнивается с количеством нулей на "
 "линии, найденных независимо. Равенство N_полоса = N_линия на каждой "
 "высоте — операционализация гипотезы Римана; на тринадцати высотах до "
 "T ≈ 1000 оно подтверждено.",
],
"question_en": [
 "How many zeta zeros lie in the critical strip below a height T, and are "
 "they all on the critical line? The campaign answers via the argument "
 "principle: the contour (2,0)→(2,T)→(0,T)→(0,0) bypassing the pole s = 1 "
 "from above gives N(T) = Δarg ξ / 2π, compared with the number of on-line "
 "zeros found independently. The equality N_strip = N_line at each height "
 "operationalises the Riemann Hypothesis; at thirteen heights up to "
 "T ≈ 1000 it holds.",
],
"results": [
 ("Якоря N(T)", "0 / 3 / 10 / 29 / 79 / 138 / 202 / 269 / … / 649", "= n_линия"),
 ("Мост арифметик fp ↔ mpmath (T = 100.07)", "|ΔN| = 2.6e-26", "машинная строгость"),
 ("Остаток S(T) на [0, 1.13e6]", "максимум 1.7994 (в пределах ±1.8)", "классика воспроизведена"),
 ("Второй момент Σγ² (K6)", "отклонение от (T³/6π)(ln(T/2π)−1/3) = 8.8e-7", "формула точна"),
 ("Зазоры ниже T = 1000", "min 0.3104 · max 6.887 · средний 1.521", "Леман–Одлыжко"),
 ("Ловушка алиасинга 2π", "первая версия теряла обороты (N=5 вместо 10)", "найдена и исправлена"),
],
"results_en": [
 ("Anchors N(T)", "0 / 3 / 10 / 29 / 79 / 138 / 202 / 269 / … / 649", "= n_line"),
 ("Arithmetic bridge fp ↔ mpmath (T = 100.07)", "|ΔN| = 2.6e-26", "machine rigour"),
 ("Residual S(T) on [0, 1.13e6]", "maximum 1.7994 (within ±1.8)", "classics reproduced"),
 ("Second moment Σγ² (K6)", "deviation from (T³/6π)(ln(T/2π)−1/3) = 8.8e-7", "formula exact"),
 ("Gaps below T = 1000", "min 0.3104 · max 6.887 · mean 1.521", "Lehman–Odlyzko"),
 ("The 2π aliasing trap", "first version lost turns (N=5 instead of 10)", "found and fixed"),
],
"how": [
 "Двухуровневая реализация: numpy-ветвь с рекурсивно-адаптивным шагом "
 "(двойное условие листа: |wrap| ≤ 0.3 И длина ≤ h_safe из границ "
 "|ζ′/ζ|) и mpmath-ветвь dps = 26 для эталонных высот. Полюс обходится "
 "сверху малой полуокружностью; по лемме T3 добавка +1 НЕ делается — "
 "её отсутствие проверено кросс-чеком с S(T) и якорями файла нулей.",
],
"how_en": [
 "A two-tier implementation: a numpy branch with a recursively adaptive "
 "step (the double leaf condition: |wrap| ≤ 0.3 AND length ≤ h_safe from "
 "the |ζ′/ζ| bounds) and an mpmath branch at dps = 26 for reference "
 "heights. The pole is bypassed from above by a small semicircle; by "
 "lemma T3 the additive +1 is NOT applied — its absence is verified by "
 "the S(T) cross-check and the anchors of the zero file.",
],
"figs": ["fig03_argument", "fig04_gaps"],
"honest": [
 "Верификация в полосе до T = 1000 — не доказательство RH для всех высот; "
 "это честная граница, ниже которой счёт согласован покомпонентно.",
 "История K6 поучительна: первая версия формулы второго момента содержала "
 "ошибку множителя 4π³ ≈ 124, найденную расхождением с данными; итоговое "
 "согласие — свойство формулы, а не подгонки.",
],
"honest_en": [
 "Verification in the strip up to T = 1000 is not a proof of RH for all "
 "heights; it is the honest boundary below which the counting agrees "
 "component by component.",
 "The K6 story is instructive: the first version of the second-moment "
 "formula carried a factor error of 4π³ ≈ 124, found through the mismatch "
 "with the data; the final agreement is a property of the formula, not a fit.",
],
}

C["C3_gate_family"] = {
"slug": "C3 · Семейство затворов H7",
"slug_en": "C3 · The H7 gate family",
"one": "52 затвора (Nv × q × W × α) на решётке 24×24 с π-флаксом; вопрос "
       "спектрального тождества Г2; перестановочные нули; позитивные контроли "
       "PC1/PC2; вердикт: тождества нет, разрыв 9–10 порядков.",
"one_en": "52 gates (Nv × q × W × α) on a 24×24 lattice with π flux; the "
          "spectral-identity question H2; permutation nulls; positive controls "
          "PC1/PC2; verdict: no identity, a 9–10 order gap.",
"question": [
 "Существует ли затвор — конфигурация вихревого облака, — спектр которого "
 "тождественен спектру нулей ζ по соответствию «уровень n ↔ нуль n»? "
 "Тождество спектра сильнее совпадения статистики: оно требует корреляции "
 "+1 между развёрнутыми последовательностями. Кампания строит нулевые "
 "распределения (сдвиги нулей, GUE-матрицы) и два позитивных контроля, "
 "на которых метод обязан видеть тождество: изоспектральные близнецы "
 "spinor64 и график Z_id против файла.",
],
"question_en": [
 "Does a gate exist — a vortex-cloud configuration — whose spectrum is "
 "identical to the zeta zero spectrum under the correspondence level n ↔ "
 "zero n? Spectral identity is stronger than a statistics match: it "
 "requires correlation +1 between the unfolded sequences. The campaign "
 "builds null distributions (zero-list shifts, GUE matrices) and two "
 "positive controls on which the method must see identity: the spinor64 "
 "isospectral twins and the Z_id graph against the file.",
],
"results": [
 ("Семейство", "52 уникальные конфигурации, мастер-сид 96", "протокол C3"),
 ("Лучший r_H7", "0.226 (p = 0.169, Bonferroni 0.80)", "тождества нет"),
 ("Декуи / GUE-нуль", "0.026±0.140 / −0.014±0.127", "нулевые зоны"),
 ("PC1 близнецы spinor64", "r = 1.000000000, D_nn = 2.7e-14", "метод видит тождество"),
 ("PC2 график ↔ файл", "r = 1.000000000000, D_nn = 1.2e-10", "метод видит тождество"),
 ("Разрыв график ↔ оператор", "9–10 порядков по D_nn", "масштаб серии"),
],
"results_en": [
 ("Family", "52 unique configurations, master seed 96", "protocol C3"),
 ("Best r_H7", "0.226 (p = 0.169, Bonferroni 0.80)", "no identity"),
 ("Decoys / GUE null", "0.026±0.140 / −0.014±0.127", "null zones"),
 ("PC1 spinor64 twins", "r = 1.000000000, D_nn = 2.7e-14", "method sees identity"),
 ("PC2 graph ↔ file", "r = 1.000000000000, D_nn = 1.2e-10", "method sees identity"),
 ("Graph ↔ operator gap", "9–10 orders in D_nn", "the series scale"),
],
"how": [
 "Конвейер: vortex-конфигурация (центры ячеек, нейтральные заряды) → "
 "эрмитов гамильтониан (engine/hamiltonian.py) → eigvalsh → центральная "
 "полоса 0.6 (344 уровня) → полиномиальная развёртка степени 6 → окно "
 "200 уровней. Нулевая сторона — гладкий счёт Римана–фон Мангольдта. "
 "Статистики: r_H7 (рампы исключены), D_nn со сдвиг-оптимумом, KS_sp. "
 "Кластеризация ⟨r⟩ = 0.32 чистой решётки — эффект локализации, а не "
 "родства с ζ.",
],
"how_en": [
 "The pipeline: vortex configuration (cell centres, neutral charges) → "
 "Hermitian Hamiltonian (engine/hamiltonian.py) → eigvalsh → central band "
 "0.6 (344 levels) → degree-6 polynomial unfolding → 200-level window. "
 "The zero side is the smooth Riemann–von Mangoldt count. Statistics: "
 "r_H7 (ramps removed), D_nn with a shift optimum, KS_sp. The ⟨r⟩ = 0.32 "
 "clustering of the clean lattice is a localization effect, not kinship "
 "with ζ.",
],
"figs": ["fig05_gates"],
"honest": [
 "Г2 — отрицательный вердикт, но метод допущен к нему только после "
 "позитивных контролей: PC1/PC2 показывают, что конвейер видит тождество "
 "на уровне 1e-14, когда оно есть.",
 "Термин «затвор» — конструкция серии; он означает параметризованное "
 "семейство эрмитовых гамильтонианов, а не физический прибор.",
],
"honest_en": [
 "H2 is a negative verdict, but the method earned it only after the "
 "positive controls: PC1/PC2 show the pipeline sees identity at the 1e-14 "
 "level when it exists.",
 "The term gate is a construct of this series; it denotes a parametrised "
 "family of Hermitian Hamiltonians, not a physical device.",
],
}

C["C4_trace_formula"] = {
"slug": "C4 · Следовая формула: Tr e^{−uH} против явной формулы",
"slug_en": "C4 · The trace formula: Tr e^{−uH} versus the explicit formula",
"one": "Вывод тождества Q(a) из произведения Адамара; следовая формула "
       "K(x) = (1/π)∫Q sin с весом простых Λ(n)/√n; калибровка 1.7e-12; "
       "H_ξ верифицирован до 1.2e-5; затворы — в нулевой зоне (разрыв ≈0.5 порядка).",
"one_en": "Deriving the Q(a) identity from the Hadamard product; the trace "
          "formula K(x) = (1/π)∫Q sin with the prime weight Λ(n)/√n; "
          "calibration 1.7e-12; H_ξ verified to 1.2e-5; gates in the null "
          "zone (residual gap ≈0.5 order).",
"question": [
 "Если бы оператор Гильберта–Пойа существовал, его тепловой след обязан "
 "был бы нести вес простых: Tr e^{−xH} = гладкие Γ-члены − ΣΛ(n)/√n·"
 "x/(x²+ln²n). Кампания выводит это строго (теорема T6), верифицирует "
 "для оператора H_ξ = diag(±γ_n) и затем меряет, что остаётся у решёточных "
 "затворов. Это третья проекция разрыва Г2 — после ранговой корреляции "
 "(C3) и ψ-лестницы (C6).",
],
"question_en": [
 "If a Hilbert–Pólya operator existed, its heat trace would have to carry "
 "the prime weight: Tr e^{−xH} = smooth Γ-terms − ΣΛ(n)/√n·x/(x²+ln²n). "
 "The campaign derives this rigorously (theorem T6), verifies it for the "
 "operator H_ξ = diag(±γ_n), and then measures what survives for the "
 "lattice gates. This is the third projection of the H2 gap — after the "
 "rank correlation (C3) and the ψ-ladder (C6).",
],
"results": [
 ("M0: тождество Q(a)", "|ΔQ| ≤ 1.7e-12 на сетке a ∈ [0.1, 3]", "калибровано"),
 ("Встроенный контроль B = −C₀", "0.023095708966 — 12 цифр", "классическое тождество подтверждено"),
 ("M1: следовая формула H_ξ", "|ΔK| ≤ 1.2e-5 (абс.), 1e-6…1e-4 относ. при x ≤ 0.35", "T6 верифицирована"),
 ("PC0: окно нулей против гребёнки", "r = +0.9998, относ. остаток 2.1%", "метод видит вес простых"),
 ("M2: 52 затвора", "r_EF −0.93…+1.00, нулевые облака", "веса простых нет"),
 ("Разрыв в следовой метрике", "≈ 0.5 порядка по невязке (лучший остаток 6.7% против 2.1%)", "Г2 — НЕТ, измерено"),
 ("Воспроизведение протокола C3", "|Δ mean_spacing| = 1.45e-16", "бит-в-бит"),
],
"results_en": [
 ("M0: the Q(a) identity", "|ΔQ| ≤ 1.7e-12 on the grid a ∈ [0.1, 3]", "calibrated"),
 ("Built-in control B = −C₀", "0.023095708966 — 12 digits", "classical identity confirmed"),
 ("M1: trace formula for H_ξ", "|ΔK| ≤ 1.2e-5 (abs), 1e-6…1e-4 rel. at x ≤ 0.35", "T6 verified"),
 ("PC0: zeros window vs the comb", "r = +0.9998, relative residual 2.1%", "method sees the prime weight"),
 ("M2: 52 gates", "r_EF −0.93…+1.00, null clouds", "no prime weight"),
 ("Gap in the trace metric", "≈ 0.5 orders by residual (best 6.7% vs 2.1%)", "H2 — NO, measured"),
 ("C3 protocol reproduction", "|Δ mean_spacing| = 1.45e-16", "bit-for-bit"),
],
"how": [
 "Вывод: произведение Адамара ξ'/ξ = B + Σ_ρ[1/(s−ρ)+1/ρ] → спаривание "
 "ρ ↔ ρ̄ → Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀. "
 "След: 2a/(a²+γ²) = 2∫e^{−γt}sin(at)dt → K(x) = (1/π)∫Q(a)sin(ax)da. "
 "При a > ½ ряд ζ'/ζ = −ΣΛ(n)/n^{½+a} — простая часть T2 вычисляется "
 "точным преобразованием ряда; гладкая часть T3 — замкнутыми формами "
 "Si/Ci (полюс, ψ с разложением, константы); Γ-часть T1 — на [0, 1.5] "
 "по сплайну mpmath-сетки. Метрика затворов: флуктуация развёрнутого "
 "теплового следа против гребёнки P(u) при фиксированном масштабе "
 "(оптимизация масштаба исключена как источник завышения r).",
],
"how_en": [
 "Derivation: Hadamard ξ'/ξ = B + Σ_ρ[1/(s−ρ)+1/ρ] → pairing ρ ↔ ρ̄ → "
 "Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀. "
 "Trace: 2a/(a²+γ²) = 2∫e^{−γt}sin(at)dt → K(x) = (1/π)∫Q(a)sin(ax)da. "
 "For a > ½ the series ζ'/ζ = −ΣΛ(n)/n^{½+a} — the prime part T2 is "
 "computed by the exact series transform; the smooth part T3 by closed "
 "Si/Ci forms (pole, ψ expansion, constants); the Γ-part T1 on [0, 1.5] "
 "through the spline of the mpmath grid. The gate metric: the fluctuation "
 "of the unfolded heat trace against the comb P(u) at fixed scale "
 "(scale optimisation is excluded as a source of r-inflation).",
],
"figs": ["fig06_trace", "fig07_parts", "fig08_rEF"],
"honest": [
 "Пол 1.2e-5 — численный пол квадратуры, а не предел точности тождества: "
 "при x ≥ 1 сам K(x) порядка 1e-6, и относительная метрика теряет смысл; "
 "в содержательной зоне согласие 1e-6…1e-4.",
 "Файл нулей нужен только для свежих пересчётов; закоммиченный вердикт "
 "самодостаточен.",
],
"honest_en": [
 "The 1.2e-5 floor is the quadrature floor, not the precision limit of "
 "the identity: for x ≥ 1 the value of K(x) itself is ~1e-6 and the "
 "relative metric loses meaning; in the informative range the agreement "
 "is 1e-6…1e-4.",
 "The zero file is needed only for fresh recomputations; the committed "
 "verdict is self-contained.",
],
}

C["C5_gates_extended"] = {
"slug": "C5 · Расширенное семейство затворов",
"slug_en": "C5 · The extended gate family",
"one": "35 новых затворов + 2 декуя по шести новым ручкам: твисты, "
       "анизотропия, флакс-сдвиг, стэггерд-масса, профиль вихря, знаки и "
       "границы. Вердикт: разрыв Г2 устойчив — GUE-класс (⟨r⟩ = 0.500±0.001) "
       "и нулевая зона (|r_H7| ≤ 0.043) у всех.",
"one_en": "35 new gates + 2 decoys across six new handles: twists, "
          "anisotropy, flux shift, staggered mass, vortex profile, signs and "
          "boundaries. Verdict: the H2 gap is stable — the GUE class and the "
          "null zone for everyone.",
"question": [
 "Может быть, тождество достигается не на протокольных ручках C3, а на "
 "какой-нибудь другой? Кампания расширяет пространство ручек шестью "
 "измерениями и проверяет, выведет ли хоть одна из них затвор из нулевой "
 "зоны. Регрессионный контроль: эталонный затвор протокола воспроизводит "
 "средний интервал CSV C3 бит-в-бит (1.4e-16).",
],
"question_en": [
 "Perhaps identity is reached not on the C3 protocol handles but on some "
 "others? The campaign extends the handle space by six dimensions and "
 "checks whether any of them moves a gate out of the null zone. The "
 "regression control: the protocol reference gate reproduces the mean "
 "spacing of the C3 CSV bit-for-bit (1.4e-16).",
],
"results": [
 ("Твисты (φx, φy)", "3 класса спин-структур", "|r_H7| ≤ 0.033"),
 ("Анизотропия t_x/t_y", "0.8; 1.25", "|r_H7| ≤ 0.030"),
 ("Флакс-сдвиг δα", "±0.02; ±1/24 на торусе", "|r_H7| ≤ 0.034"),
 ("Стэггерд-масса m", "0.15; 0.35", "|r_H7| ≤ 0.032"),
 ("Профиль вихря", "site | midpoint", "|r_H7| ≤ 0.033"),
 ("Знаки и границы", "neutral/all_plus/random · open/torus", "|r_H7| ≤ 0.044"),
 ("Семейство в целом", "⟨r⟩ = 0.498–0.502 (0.500±0.001)", "GUE-класс у всех"),
],
"results_en": [
 ("Twists (φx, φy)", "3 spin-structure classes", "|r_H7| ≤ 0.033"),
 ("Anisotropy t_x/t_y", "0.8; 1.25", "|r_H7| ≤ 0.030"),
 ("Flux shift δα", "±0.02; ±1/24 on the torus", "|r_H7| ≤ 0.034"),
 ("Staggered mass m", "0.15; 0.35", "|r_H7| ≤ 0.032"),
 ("Vortex profile", "site | midpoint", "|r_H7| ≤ 0.033"),
 ("Signs and boundaries", "neutral/all_plus/random · open/torus", "|r_H7| ≤ 0.044"),
 ("Family overall", "⟨r⟩ = 0.498–0.502 (0.500±0.001)", "GUE class for all"),
],
"how": [
 "Все ручки реализованы в engine/hamiltonian.py: твисты — фазы на "
 "wrap-связях торуса (спин-структуры C8); анизотропия — t_x = t/aniso; "
 "флакс-сдвиг — α_eff = α + δα (на торусе только разрешённые ±1/24); "
 "масса — стэггерд-потенциал (−1)^{ix+iy}; профиль midpoint — угол "
 "вихря из середины связи (ядро конечного радиуса); знаки — нейтральный "
 "(протокол), все плюс, случайные; границы — открытые или торус. "
 "Вырожденный угол W = 0 + midpoint заменён на W = 0.1 с пометкой.",
],
"how_en": [
 "All handles are implemented in engine/hamiltonian.py: twists — phases "
 "on the torus wrap links (the C8 spin structures); anisotropy — "
 "t_x = t/aniso; flux shift — α_eff = α + δα (on the torus only the "
 "admissible ±1/24); mass — the staggered potential (−1)^{ix+iy}; the "
 "midpoint profile — the vortex angle taken from the link midpoint (a "
 "finite-radius core); signs — neutral (protocol), all-plus, random; "
 "boundaries — open or torus. The degenerate corner W = 0 + midpoint is "
 "replaced by W = 0.1 with a note.",
],
"figs": ["fig09_handles", "fig10_gue_ext"],
"honest": [
 "Максимум |r_H7| по семейству достигается на декуе со случайными "
 "знаками — ожидаемый шумовой максимум, а не сигнал.",
 "Утверждение «разрыв устойчив» — измерение на 37 конфигурациях, а не "
 "теорема о всех возможных ручках.",
],
"honest_en": [
 "The family maximum of |r_H7| is reached on a random-sign decoy — the "
 "expected noise maximum, not a signal.",
 "The statement the gap is stable is a measurement over 37 configurations, "
 "not a theorem about all possible handles.",
],
}

C["C6_prime_flow"] = {
"slug": "C6 · Поток простых, ядро ко-локации и ψ-лестница",
"slug_en": "C6 · The prime flow, the co-location kernel and the ψ-ladder",
"one": "Φ_p = ½ln p; точная ко-локация (Φ_p,Φ_q) ≡ Φ_pq (1.35e-14); ядро "
       "разрешения δ(d) с ξ_mult ≈ 2–3 ячейки; ψ-лестница: corr = 0.972 у "
       "нулей, нулевая зона у затворов; универсальность стирает кодировки.",
"one_en": "Φ_p = ½ln p; exact co-location (Φ_p,Φ_q) ≡ Φ_pq (1.35e-14); the "
          "resolution kernel δ(d) with ξ_mult ≈ 2–3 cells; the ψ-ladder: "
          "corr = 0.972 for zeros, null zone for gates; universality washes "
          "the codings out.",
"question": [
 "Живёт ли арифметика простых в фазовом слое вихревого облака? Три "
 "вопроса: композит ли поток (M1); кодирует ли лестница ψ(x) нулевую "
 "структуру ζ (M2); видит ли спектр кодировки, или универсальность GUE "
 "стирает всё (M3). Ответы: поток композитит точно, лестница согласована "
 "с нулями, спектр — нет.",
],
"question_en": [
 "Does the arithmetic of primes live in the phase layer of the vortex "
 "cloud? Three questions: is the flow compositive (M1); does the ladder "
 "ψ(x) encode the zero structure of ζ (M2); does the spectrum see the "
 "codings, or does GUE universality wash them out (M3). The answers: the "
 "flow composites exactly, the ladder matches the zeros, the spectrum "
 "does not.",
],
"results": [
 ("Ко-локация (Φ_p,Φ_q) ≡ Φ_pq (T4)", "max|ΔE| = 1.35e-14", "доказано+измерено"),
 ("Ядро разрешения δ(d) (T5)", "0 → 3.2e-3 → 1.5e-2 → ~2e-2 (d≈4–6)", "ξ_mult ≈ 2–3 ячейки"),
 ("Аддитивность 1-го порядка", "не выполняется (~1e-2)", "отклик нелинеен"),
 ("ψ-лестница: эталон 200 нулей", "corr = +0.972, max err 4.2", "вес простых у нулей"),
 ("ψ-лестница: затворы", "+0.24/+0.13/+0.09/−0.12", "нулевая зона (Г5 — НЕТ)"),
 ("M3: 4 кодировки потока", "⟨r⟩ = 0.585–0.611, разброс 0.026", "один GUE-класс"),
],
"results_en": [
 ("Co-location (Φ_p,Φ_q) ≡ Φ_pq (T4)", "max|ΔE| = 1.35e-14", "proven+measured"),
 ("Resolution kernel δ(d) (T5)", "0 → 3.2e-3 → 1.5e-2 → ~2e-2 (d≈4–6)", "ξ_mult ≈ 2–3 cells"),
 ("First-order additivity", "fails (~1e-2)", "the response is nonlinear"),
 ("ψ-ladder: 200-zero reference", "corr = +0.972, max err 4.2", "the prime weight of the zeros"),
 ("ψ-ladder: gates", "+0.24/+0.13/+0.09/−0.12", "null zone (H5 — NO)"),
 ("M3: 4 flow codings", "⟨r⟩ = 0.585–0.611, spread 0.026", "one GUE class"),
],
"how": [
 "Поток: Φ_p = ½ln p на решёточных фазах; ко-локация — совпадение узла "
 "(p,q) с узлом pq в фазовом слое. Ядро δ(d) — отклик композитного узла "
 "на расстояние d между сомножителями. ψ-лестница: эталон по первым 200 "
 "нулям ψ_ζ(x) = x − √x·Σe^{iγ ln x}/(½+iγ) − ln2π − ½ln(1−x⁻²) против "
 "сита фон Мангольдта до 10⁶; методический урок — окно на γ~500 даёт "
 "corr 0.48, эталон обязан быть на тех же высотах. Кодировки M3 — "
 "случайная, 1/√p, ln p, D10 — при фиксированных позициях.",
],
"how_en": [
 "Flow: Φ_p = ½ln p on the lattice phases; co-location — the coincidence "
 "of the (p,q) node with the pq node in the phase layer. The kernel δ(d) "
 "— the response of a composite node to the distance d between factors. "
 "The ψ-ladder: the reference over the first 200 zeros ψ_ζ(x) = x − "
 "√x·Σe^{iγ ln x}/(½+iγ) − ln2π − ½ln(1−x⁻²) against the von Mangoldt "
 "sieve up to 10⁶; the methodological lesson — a window at γ~500 gives "
 "corr 0.48, the reference must live at the same heights. The M3 codings "
 "— random, 1/√p, ln p, D10 — at fixed positions.",
],
"figs": ["fig11_coloc", "fig12_psi"],
"honest": [
 "Г5 — отрицательный вердикт с позитивным контролем:corr 0.972 у нулей "
 "показывает, что метод видит вес простых, когда он есть.",
 "Кодировки в спектре (M3) — универсальный механизм без "
 "RH-доказательной силы; честная кодировка предъявляет себя в потоке "
 "(T4) и лестнице (M2).",
],
"honest_en": [
 "H5 is a negative verdict with a positive control: the 0.972 correlation "
 "for the zeros shows the method sees the prime weight when it exists.",
 "Spectral codings (M3) are a universal mechanism without RH-proving "
 "force; an honest coding presents itself in the flow (T4) and the "
 "ladder (M2).",
],
}

C["C7_wave_dynamics"] = {
"slug": "C7 · Динамика волнового пакета",
"slug_en": "C7 · Wave-packet dynamics",
"one": "Когерентное распространение, отражение и рассеяние на L=96; "
       "сохранение энергии до 1e-15; ζ-облако прозрачнее случайного в 16 раз "
       "в дальнем крыле — динамическое лицо парных корреляций Монтгомери.",
"one_en": "Coherent propagation, reflection and scattering on L=96; energy "
          "conserved to 1e-15; the ζ-cloud is 16× more transparent than "
          "random in the far wing — the dynamical face of the Montgomery "
          "pair correlations.",
"question": [
 "Если решёточный резонатор — «электрон на флакс-решётке», то пакет "
 "должен двигаться: распространяться когерентно, отражаться от границ, "
 "рассеиваться на вихрях. И если структура ζ-фаз физична, ζ-облако "
 "обязано вести себя иначе, чем случайное той же плотности. Так и "
 "происходит — в трёх измеренных эффектах.",
],
"question_en": [
 "If the lattice resonator is an electron on a flux lattice, the packet "
 "must move: propagate coherently, reflect from boundaries, scatter on "
 "vortices. And if the ζ-phase structure is physical, the ζ-cloud must "
 "behave differently from a random cloud of the same density. It does — "
 "in three measured effects.",
],
"results": [
 ("Сохранение энергии", "1e-15 на всех траекториях", "динамика честная"),
 ("Когерентность (чистая решётка)", "⟨x⟩: 24 → 4.3 (отражение, t≈14.5) → 44", "бильярдная траектория"),
 ("Рассеяние на вихрях", "Nv=16: почти прозрачно; Nv=64: R=0.39; Nv=256: R=0.47", "монотонный тормозящий эффект"),
 ("Поперечное отклонение (ζ Nv=256)", "⟨y⟩: 48 → 38; случайные: без отклонения", "фазы направляют"),
 ("Транспорт P(x ≥ 90)", "ζ-облако 0.0032 против случайного 0.0002 (×16)", "эффект D10 воспроизведён"),
],
"results_en": [
 ("Energy conservation", "1e-15 on every trajectory", "honest dynamics"),
 ("Coherence (clean lattice)", "⟨x⟩: 24 → 4.3 (reflection, t≈14.5) → 44", "billiard trajectory"),
 ("Vortex scattering", "Nv=16: nearly transparent; Nv=64: R=0.39; Nv=256: R=0.47", "a monotone braking effect"),
 ("Transverse drift (ζ Nv=256)", "⟨y⟩: 48 → 38; random: none", "the phases steer"),
 ("Transport P(x ≥ 90)", "ζ-cloud 0.0032 vs random 0.0002 (×16)", "the D10 effect reproduced"),
],
"how": [
 "Разреженный гамильтониан 96×96 (open bc), шаг dt = 0.1, горизонт T = 40, "
 "пакет по конвенции D10. Вся динамика живёт на самодуальной линии α = ½, "
 "где π-флакс превращает решётку в дискретизированное безмассовое "
 "уравнение Дирака — критерий Г4.",
],
"how_en": [
 "A sparse 96×96 Hamiltonian (open bc), step dt = 0.1, horizon T = 40, "
 "the packet by the D10 convention. All the dynamics lives on the "
 "self-dual line α = ½, where the π flux turns the lattice into a "
 "discretised massless Dirac equation — criterion H4.",
],
"figs": ["fig13_dynamics"],
"honest": [
 "Отождествление самодуальной линии α = ½ с Re(s) = ½ — конъектурный "
 "мост: статистическая поддержка есть (D7/D10), тождества нет.",
 "«Движение электрона» подтверждено в динамическом смысле; это не "
 "утверждение о спектре (см. C3–C5).",
],
"honest_en": [
 "The identification of the self-dual line α = ½ with Re(s) = ½ is a "
 "conjectural bridge: statistical support exists (D7/D10), identity does not.",
 "The electron motion is confirmed in the dynamical sense; it is not a "
 "statement about the spectrum (see C3–C5).",
],
}

C["C8_stats_ladder"] = {
"slug": "C8 · Статистическая лестница и спин-структуры",
"slug_en": "C8 · The statistics ladder and spin structures",
"one": "Пуассон/GOE/GUE под управлением симметрии (T10); GSE структурно "
       "недостижима (T²=+1); spinor64: 64 спин-структуры → 4 гамильтониана "
       "(T8) с изоспектральностью 1.1e-14.",
"one_en": "Poisson/GOE/GUE governed by symmetry (T10); GSE is structurally "
          "unreachable (T²=+1); spinor64: 64 spin structures → 4 Hamiltonians "
          "(T8) with isospectrality 1.1e-14.",
"question": [
 "Какие классы случайных матриц реализует решётка и что ими управляет? "
 "И что кодируют дискретные фазовые структуры — есть ли среди них "
 "«скрытая переменная» арифметики? Ответы: класс задаётся симметрией "
 "(тройственность Дайсона); дискретные кодировки точны, но их ёмкость "
 "определяется симметрией фаз, а не числом структур.",
],
"question_en": [
 "Which random-matrix classes does the lattice realise, and what governs "
 "them? And what do discrete phase structures encode — is there a hidden "
 "variable of arithmetic among them? The answers: the class is set by "
 "symmetry (the Dyson triplet); discrete codings are exact, but their "
 "capacity is set by phase symmetry, not by the number of structures.",
],
"results": [
 ("Чистая решётка", "⟨r⟩ = 0.324–0.386", "Пуассон/кластеризация"),
 ("Вещественный беспорядок w = 1–4", "⟨r⟩ = 0.520–0.538", "GOE-плато"),
 ("Сильный беспорядок w = 16–32", "⟨r⟩ = 0.387", "Пуассон (локализация)"),
 ("Комплексные вихри Nv ≥ 8", "⟨r⟩ = 0.597–0.612", "GUE"),
 ("GSE", "T² = +1 → недостижима", "архитектурное ограничение"),
 ("spinor64 E1", "64 класса/84 ребра; орбиты 28/21/7/7/1; Арф 28/36", "бит-в-бит с эталоном"),
 ("spinor64 E2 (T8)", "ровно 4 уникальных ⟨r⟩: 0.59348/0.59682/0.60054/0.60271", "64 → 4 по парам (φx,φy)"),
 ("Изоспектральность орбит", "max|Δλ| = 1.02e-14", "машинная точность"),
],
"results_en": [
 ("Clean lattice", "⟨r⟩ = 0.324–0.386", "Poisson/clustering"),
 ("Real disorder w = 1–4", "⟨r⟩ = 0.520–0.538", "GOE plateau"),
 ("Strong disorder w = 16–32", "⟨r⟩ = 0.387", "Poisson (localization)"),
 ("Complex vortices Nv ≥ 8", "⟨r⟩ = 0.597–0.612", "GUE"),
 ("GSE", "T² = +1 → unreachable", "architectural constraint"),
 ("spinor64 E1", "64 classes/84 edges; orbits 28/21/7/7/1; Arf 28/36", "bit-for-bit vs reference"),
 ("spinor64 E2 (T8)", "exactly 4 unique ⟨r⟩: 0.59348/0.59682/0.60054/0.60271", "64 → 4 by (φx,φy) pairs"),
 ("Orbit isospectrality", "max|Δλ| = 1.02e-14", "machine precision"),
],
"how": [
 "Лестница из 11 каналов (n_real до 5, n_spacings до 1715): Nv, "
 "дополнительный беспорядок w, границы; классификация по ⟨r⟩ и KS к "
 "трём эталонам. spinor64: 64 класса спин-структур квартики Клайна "
 "(φx = π(e1+e3+e5), φy = π(e2+e4+e6) mod 2π) — редукция к 2×2 = 4 "
 "классам; изоспектральность проверяется внутри орбит.",
],
"how_en": [
 "An 11-channel ladder (n_real up to 5, n_spacings up to 1715): Nv, "
 "extra disorder w, boundaries; classification by ⟨r⟩ and KS against "
 "three references. spinor64: the 64 spin-structure classes of the Klein "
 "quartic (φx = π(e1+e3+e5), φy = π(e2+e4+e6) mod 2π) — the reduction to "
 "2×2 = 4 classes; isospectrality is checked within orbits.",
],
"figs": ["fig14_ladder", "fig15_spinor"],
"honest": [
 "Универсальность — аттрактор: она не может быть свидетелем арифметики, "
 "потому что стирает всё, кроме симметрии.",
 "«Все статистики» подтверждены в объёме тройственности Дайсона; GSE — "
 "закрыта архитектурно, а не численно.",
],
"honest_en": [
 "Universality is an attractor: it cannot witness arithmetic, because it "
 "erases everything but symmetry.",
 "All statistics is confirmed within the Dyson triplet; GSE is closed "
 "architecturally, not numerically.",
],
}


def badge(lang):
    if lang == "ru":
        return ("![version](https://img.shields.io/badge/версия-1.0.0-298bbc) "
                "![](https://img.shields.io/badge/серия-C1--C8-3b4f58) "
                "![](https://img.shields.io/badge/статусы-честные-3a6b4f)")
    return ("![version](https://img.shields.io/badge/version-1.0.0-298bbc) "
            "![](https://img.shields.io/badge/series-C1--C8-3b4f58) "
            "![](https://img.shields.io/badge/statuses-honest-3a6b4f)")


def render(comp, key, lang):
    d = comp
    suf = "" if lang == "ru" else "_en"
    L = {
        "ru": {"back": "← Назад к главному README", "toc": "Содержание",
               "q": "Вопрос кампании", "r": "Результаты", "how": "Метод",
               "mon": "Монографии", "figs": "Рисунки", "data": "Данные",
               "rep": "Воспроизведение", "hon": "Честные замечания",
               "ver": "Вердикт", "th": ["Величина", "Значение", "Статус"]},
        "en": {"back": "← Back to the main README", "toc": "Contents",
               "q": "The campaign question", "r": "Results", "how": "Method",
               "mon": "Monographs", "figs": "Figures", "data": "Data",
               "rep": "Reproduction", "hon": "Honest notes",
               "ver": "Verdict", "th": ["Quantity", "Value", "Status"]},
    }[lang]
    num = key.split("_")[0]
    mons = (f"`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · "
            f"`monograph_en.pdf`")
    figs = "\n".join(
        f"| `{f}{suf}.png` | 600 dpi — `figures_hires/{lang}/{f}{suf}.png`; "
        f"экран — `figures/{lang}/` |"
        for f in d["figs"])
    figs = ("| Файл | Где |\n|---|---|\n" if lang == "ru" else
            "| File | Where |\n|---|---|\n") + figs
    rows = d["results"] if lang == "ru" else d["results_en"]
    tbl = "| " + " | ".join(L["th"]) + " |\n|---|---|---|\n" + "\n".join(
        "| " + " | ".join(r) + " |" for r in rows)
    paras = d["question"] if lang == "ru" else d["question_en"]
    how = d["how"] if lang == "ru" else d["how_en"]
    hon = d["honest"] if lang == "ru" else d["honest_en"]
    hon_md = "\n".join(f"> {h}" for h in hon)
    title = d["slug"] if lang == "ru" else d["slug_en"]
    one = d["one"] if lang == "ru" else d["one_en"]
    verdict = {"ru": {"C1": "композитный вердикт K1–K4, K7: PASS (одно опровержение опубликовано)",
                      "C2": "RH верифицирована в полосе до T = 1000 (649 = 649)",
                      "C3": "Г2 — НЕТ (тождества нет), измерено с PC1/PC2",
                      "C4": "T6 верифицирована; разрыв Г2 ≈ 1 порядок в тепловой метрике",
                      "C5": "разрыв Г2 устойчив ко всем шести новым ручкам",
                      "C6": "T4 доказана; Г5 — НЕТ, измерено; универсальность стирает кодировки",
                      "C7": "Г4 — ДА (динамика честная); мост к Re(s)=½ — конъектура",
                      "C8": "Г3 — ДА; T8, T10"}[num],
               "en": {"C1": "composite verdict K1–K4, K7: PASS (one refutation published)",
                      "C2": "RH verified in the strip up to T = 1000 (649 = 649)",
                      "C3": "H2 — NO (no identity), measured with PC1/PC2",
                      "C4": "T6 verified; the H2 gap ≈ 1 order in the trace metric",
                      "C5": "the H2 gap is stable across all six new handles",
                      "C6": "T4 proven; H5 — NO, measured; universality washes the codings out",
                      "C7": "H4 — YES (honest dynamics); the bridge to Re(s)=½ is a conjecture",
                      "C8": "H3 — YES; T8, T10"}[num]}
    return f"""# {title}

{badge(lang)}

> **{one}**

[{L['back']}](../..{'/README.ru.md' if lang == 'ru' else '/README.md'})

## {L['toc']}

1. [{L['q']}](#{L['q'].lower().replace(' ', '-')})
2. [{L['r']}](#{L['r'].lower()})
3. [{L['how']}](#{L['how'].lower()})
4. [{L['figs']}](#{L['figs'].lower()})
5. [{L['mon']}](#{L['mon'].lower()})
6. [{L['data']}](#{L['data'].lower()})
7. [{L['rep']}](#{L['rep'].lower()})
8. [{L['hon']}](#{L['hon'].lower()})
9. [{L['ver']}](#{L['ver'].lower()})

---

## {L['q']}

{paras[0]}

## {L['r']}

{tbl}

## {L['how']}

{how[0]}

## {L['figs']}

{figs}

## {L['mon']}

{mons}

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.
""" + ("" if lang == "ru" else "") + f"""
## {L['data']}

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/{key.split('_')[0].lower()}_*.json` | дубликат вердикта в общем реестре |

## {L['rep']}

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_{num.lower()}_{'identity' if num=='C1' else 'argument' if num=='C2' else 'gates' if num=='C3' else 'trace_formula' if num=='C4' else 'gates_ext' if num=='C5' else 'primes' if num=='C6' else 'dynamics' if num=='C7' else 'stats_ladder'}.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## {L['hon']}

{hon_md}

## {L['ver']}

**{verdict}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · {title}*
"""


def main():
    for key, comp in C.items():
        d = os.path.join(ROOT, "computations", key)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "README.md"), "w").write(render(comp, key, "ru"))
        open(os.path.join(d, "README.en.md"), "w").write(render(comp, key, "en"))
        print(f"{key}: README.md + README.en.md")


if __name__ == "__main__":
    main()
