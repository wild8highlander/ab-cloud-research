# Th5. Блочная редукция по симметрии — вывод теоремы

**Кампания:** V9 · **Формальная редукция:** A2 (одновременная диагонализация) · **Документы:**
`theorem_th5_ru.pdf/.docx`, `theorem_th5_en.pdf/.docx` ·
**Фигура:** `figures/th5_4dim_ru.png`, `figures/th5_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

Если [H, A] = [H, B] = 0 для порождающих абелевой группы G магнитных трансляций, то H блочно-диагонален в разложении по характерам χ группы G и spec H = ⊔_χ spec(H|Π_χ Π_χ).

## Идея вывода

Коммутирующие унитарные A, B одновременно диагонализуются; совместные собственные значения — характеры χ: G → U(1); проекторы Π_χ (полиномы от A, B) коммутируют с H, каждое Π_χℂ^N инвариантно, H распадается в прямую сумму сужений. Следствие: спектр ищется в блоках ~L²/6 вместо L².

## Четыре измерения фигуры

a) коммутаторы чистой решётки ε_Ux/ε_Uy/ε_AB/внеблочные (log) — ~9e−15; b) ошибка объединения блоков 7.1e−15 против порога 1e−9; c) вихри: коммутаторы по 4 твистам — ε ~ O(1), симметрия сломана (отрицательный контроль); d) среднее r по твистам ≈ 0.6.

## Сертификат и артефакты кампании

test_th5_block_reduction.py; computations/V09_symmetry_reduction/; claim_v09.json

## Границы (честно)

Для несимметричных вихревых размещений редукция неприменима — это граница области действия, а не дефект; частично-симметричные конфигурации дают приближённые инвариантные подпространства (в пакет не включено).

## English summary

**Statement.** If [H, A] = [H, B] = 0 for the generators of an abelian group G of magnetic translations, then H is block-diagonal in the character decomposition and spec H = ⊔_χ spec(H|Π_χ Π_χ).

**Proof idea.** Commuting unitaries A, B are simultaneously diagonalizable; joint eigenvalues are characters χ: G → U(1); projectors Π_χ (polynomials in A, B) commute with H, each Π_χℂ^N is invariant, and H splits into a direct sum of restrictions. Consequence: the spectrum is found in blocks of ~L²/6 instead of L².

**Figure dimensions.** a) clean-lattice commutators ε_Ux/ε_Uy/ε_AB/off-block (log) — ~9e−15; b) block-union error 7.1e−15 against 1e−9; c) vortices: commutators over 4 twists — ε ~ O(1), symmetry broken (negative control); d) mean r over twists ≈ 0.6.

**Boundaries.** For asymmetric vortex placements the reduction does not apply — a scope boundary, not a defect; partially symmetric configurations give approximate invariant subspaces (not included).
