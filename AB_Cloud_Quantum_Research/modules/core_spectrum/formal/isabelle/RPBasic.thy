(* RPBasic.thy — формальный скелет AB Research Program (Isabelle/HOL).
   Компиляция — открытое обязательство O-isa. *)
theory RPBasic
  imports Complex_Main
begin

(* Сумма квадратов неотрицательна (скелет дефектных индексов) *)
lemma sumSq_nonneg:
  fixes v :: "nat ⇒ real"
  shows "0 ≤ (∑i<n. v i ^ 2)"
  by (simp add: sum_nonneg)

(* Спектральное тождество следов: Tr(AB) = Tr(BA) *)
lemma trace_commute:
  fixes A B :: "complex^nat^nat"
  shows "trace (A ** B) = trace (B ** A)"
proof -
  have "trace (A ** B) = (∑i. ∑j. A $ i $ j * B $ j $ i)"
    by (simp add: trace_def matrix_matrix_mult_def)
  also have "... = (∑j. ∑i. A $ i $ j * B $ j $ i)"
    by (rule sum.swap)
  also have "... = trace (B ** A)"
    by (simp add: trace_def matrix_matrix_mult_def ac_simps)
  finally show ?thesis .
qed

(* Вещественность собственного значения эрмитовой матрицы (набросок:
   полная версия требует Spectrum.thy из HOL-Analysis) *)
lemma herm_eigen_real_sketch:
  fixes A :: "complex^nat^nat"
  assumes "A ** v = c *s v" "v ≠ 0"
          "∀i j. A $ i $ j = cnj (A $ j $ i)"
  shows "Im c = 0"
  oops (* обязательство O-isa-herm: полный вывод через Spectrum *)

end
