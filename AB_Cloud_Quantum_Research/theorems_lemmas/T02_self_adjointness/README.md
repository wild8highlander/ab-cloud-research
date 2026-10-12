# Th2. Конечномерная самосопряжённость — вывод теоремы

**Кампания:** V8 · **Формальная редукция:** A2b (распадение дефектной нормы) · **Документы:**
`theorem_th2_ru.pdf/.docx`, `theorem_th2_en.pdf/.docx` ·
**Фигура:** `figures/th2_4dim_ru.png`, `figures/th2_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

Симметричный оператор на ℂ^N существенно самосопряжён: дефектные индексы (0, 0); e^{−iHt} унитарен; Im⟨ψ, Hψ⟩ = 0.

## Идея вывода

На ℂ^N всякий симметричный ограниченный оператор самосопряжён. Ключевая оценка: ‖(H ∓ iI)ψ‖² = ‖Hψ‖² + ‖ψ‖² ≥ ‖ψ‖² > 0 — кросс-член исчезает по симметрии H, поэтому ker(H* ∓ iI) пусты. Следствия: спектр вещественен, e^{−iHt} — унитарная группа, форма вещественна.

## Четыре измерения фигуры

a) дефектные индексы n+/n− по L = 12/16/24/32 — все нули; b) min сингулярное число H−iI ≈ 1.0 по L; c) дрейф унитарности 2.2e−16 и Im⟨ψ,Hψ⟩ = 0 против порога 1e−12; d) сдвиги спектра при смене границ (открытые/тор, 4 твиста) для L12/L24 — конечны и убывают с L.

## Сертификат и артефакты кампании

test_th2_selfadjoint.py (дефекты, унитарность, вещественность формы); computations/V08_self_adjoint/; claim_v08.json

## Границы (честно)

Теорема конечномерна; перенос на L → ∞ требует оценки существенного спектра — открытое обязательство O03.

## English summary

**Statement.** A symmetric operator on ℂ^N is essentially self-adjoint: defect indices (0, 0); e^{−iHt} is unitary; Im⟨ψ, Hψ⟩ = 0.

**Proof idea.** On ℂ^N every symmetric bounded operator is self-adjoint. Key estimate: ‖(H ∓ iI)ψ‖² = ‖Hψ‖² + ‖ψ‖² ≥ ‖ψ‖² > 0 — the cross term vanishes by symmetry, hence ker(H* ∓ iI) are empty. Consequences: real spectrum, unitary e^{−iHt}, real form.

**Figure dimensions.** a) defect indices n+/n− across L = 12/16/24/32 — all zero; b) smallest singular value of H−iI ≈ 1.0 across L; c) unitarity drift 2.2e−16 and Im⟨ψ,Hψ⟩ = 0 against 1e−12; d) spectrum shifts under boundary change (open/torus, 4 twists) for L12/L24 — finite, decaying with L.

**Boundaries.** The theorem is finite-dimensional; the L → ∞ transfer requires essential-spectrum estimates — open obligation O03.
