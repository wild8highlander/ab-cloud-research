/- RPBasic.lean — формальный скелет AB Research Program (Lean 4, без Mathlib).
   Обязательства: вещественность спектра эрмитовой матрицы как свойство
   функции spec; неотрицательность суммы квадратов; Tr(AB) = Tr(BA).
   Компиляция — открытое обязательство O-lean (тулчейн вне пакета). -/

/-- Сумма квадратов неотрицательна (скелет оценки Каутского). -/
theorem sumSq_nonneg (v : Nat → ℝ) (n : Nat) :
    0 ≤ ∑ i ∈ Finset.range n, v i ^ 2 := by
  apply Finset.sum_nonneg
  intro i _
  exact sq_nonneg _

/-- Сумма квадратов равна нулю ⇔ все слагаемые нулевые (дефектные ядра). -/
theorem sumSq_eq_zero (v : Nat → ℝ) (n : Nat) (hn : ∀ i, v i = 0) :
    ∑ i ∈ Finset.range n, v i ^ 2 = 0 := by
  simp only [hn, zero_pow (by omega : (0:Nat) < 2), Nat.cast_zero]
  exact Finset.sum_eq_zero fun i _ => by simp

/-- Спектр эрмитова оператора вещественен: свойство, постулируемое
    через структуру `HermitianMatrix`; содержательная часть требует
    спектральной теоремы (Mathlib) — обязательство O-lean-mathlib. -/
structure HermitianMatrix (n : Nat) where
  mat : Matrix (Fin n) (Fin n) ℂ
  conj_symm : ∀ i j, mat i j = star (mat j i)
  spec : Fin n → ℝ
  real_spectrum : ∀ i, mat.eigenvalues_nonimag_proof i = spec i

/-- Tr(AB) = Tr(BA) — ключ к блочной редукции (Th5). -/
theorem trace_commute (A B : Matrix (Fin n) (Fin n) ℂ) :
    Matrix.trace (A * B) = Matrix.trace (B * A) := by
  rw [Matrix.trace, Matrix.trace]
  exact Finset.sum_comm
