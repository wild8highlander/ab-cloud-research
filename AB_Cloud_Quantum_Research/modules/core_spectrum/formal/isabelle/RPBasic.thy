(* RPBasic.thy — the formal skeleton of the AB Research Program
   (Isabelle/HOL). Compilation is the open obligation O-isa. *)
theory RPBasic
  imports Complex_Main
begin

(* The sum of squares is nonnegative (defect-index skeleton) *)
lemma sumSq_nonneg:
  fixes v :: "nat \<Rightarrow> real"
  shows "0 \<le> (\<Sum>i<n. v i ^ 2)"
  by (simp add: sum_nonneg)

(* The spectral identity of traces: Tr(AB) = Tr(BA) *)
lemma trace_commute:
  fixes A B :: "complex^nat^nat"
  shows "trace (A ** B) = trace (B ** A)"
proof -
  have "trace (A ** B) = (\<Sum>i. \<Sum>j. A $ i $ j * B $ j $ i)"
    by (simp add: trace_def matrix_matrix_mult_def)
  also have "... = (\<Sum>j. \<Sum>i. A $ i $ j * B $ j $ i)"
    by (rule sum.swap)
  also have "... = trace (B ** A)"
    by (simp add: trace_def matrix_matrix_mult_def ac_simps)
  finally show ?thesis .
qed

(* A1 — the spectral theorem, hermitian case: the deep step is accepted
   explicitly as the named reduction axiom (the same reduction as
   RPTheorems.lean A1_real_spectrum / RPTheorems.v A1_real_spectrum_rc).
   The full derivation through Spectrum is tracked as the open
   obligation O-isa-herm. *)
axiomatization where
  A1_hermitian_real_eigenvalue:
    "\<And>(A::complex^nat^nat) (v::complex^nat^nat) (c::complex).
       v \<noteq> 0 \<Longrightarrow>
       (\<forall>i j. A $ i $ j = cnj (A $ j $ i)) \<Longrightarrow>
       A ** v = c *s v \<Longrightarrow> Im c = 0"

(* The hermitian case follows from the declared reduction axiom. *)
lemma herm_eigen_real:
  fixes A :: "complex^nat^nat" and v :: "complex^nat^nat" and c :: complex
  assumes "A ** v = c *s v" "v \<noteq> 0"
          "\<forall>i j. A $ i $ j = cnj (A $ j $ i)"
  shows "Im c = 0"
  using assms by blast

end
