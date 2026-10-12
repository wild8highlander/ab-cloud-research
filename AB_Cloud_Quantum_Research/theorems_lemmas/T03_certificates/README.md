# Th3. Сертификаты собственных значений — вывод теоремы

**Кампания:** V12 · **Формальная редукция:** A4 (Като–Темпл), A5 (Гершгорин) · **Документы:**
`theorem_th3_ru.pdf/.docx`, `theorem_th3_en.pdf/.docx` ·
**Фигура:** `figures/th3_4dim_ru.png`, `figures/th3_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

Для эрмитовой H, вычисленного λ̃, единичного v с невязкой r = Hv − λ̃v, δ = ‖r‖ и зазором gap до ближайшего другого уровня существует λ̂ ∈ spec H с |λ̂ − λ̃| ≤ δ²/gap; весь спектр лежит в объединении рациональных интервалов Гершгорина.

## Идея вывода

Разложение v = c·u + w с u — нормированным собственным вектором даёт ‖w‖ ≤ δ/gap и квадратичную сверхсходимость |λ̂ − λ̃| ≤ δ²/gap. Гершгорин: радиусы R_i = Σ_{j≠i}|H_ij| в точной рациональной арифметике (fractions, limit_denominator 1e12) — интервалы без округлений.

## Четыре измерения фигуры

a) невязка δ по пяти сертификатам (log); b) граница Каутского δ²/gap (log); c) ширины интервалов hi−lo — ~1e−27 (mpmath dps 40); d) покрытие Гершгорина [−4.210, 4.205] с 144 интервалами и положением λ̃.

## Сертификат и артефакты кампании

test_th3_certificates.py (попадание, покрытие, воспроизводимость); computations/V12_interval_certificates/; claim_v12.json

## Границы (честно)

Оценка квадратична по δ — требует уже хорошо сошедшегося λ̃; для близких уровней зазор мал и интервал расширяется; рациональная арифметика медленна — слой применяется точечно.

## English summary

**Statement.** For Hermitian H, computed λ̃, unit v with residual r = Hv − λ̃v, δ = ‖r‖ and gap to the nearest other level, there is λ̂ ∈ spec H with |λ̂ − λ̃| ≤ δ²/gap; the whole spectrum lies in the union of rational Gershgorin intervals.

**Proof idea.** Decomposing v = c·u + w with u a normalized eigenvector gives ‖w‖ ≤ δ/gap and quadratic superconvergence |λ̂ − λ̃| ≤ δ²/gap. Gershgorin: radii R_i = Σ_{j≠i}|H_ij| in exact rational arithmetic (fractions, limit_denominator 1e12) — rounding-free intervals.

**Figure dimensions.** a) residual δ across five certificates (log); b) Kato bound δ²/gap (log); c) interval widths hi−lo — ~1e−27 (mpmath dps 40); d) Gershgorin coverage [−4.210, 4.205] with 144 intervals and the λ̃ positions.

**Boundaries.** The bound is quadratic in δ — a well-converged λ̃ is required; close levels shrink the gap and widen the interval; rational arithmetic is slow — applied pointwise.
