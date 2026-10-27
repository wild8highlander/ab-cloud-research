(* RPBasic.v — формальный скелет AB Research Program (Coq, Gallina).
   Компиляция — открытое обязательство O-coq. *)

Require Import Reals Lqa.
Open Scope R_scope.

(* Сумма квадратов неотрицательна *)
Lemma sumSq_nonneg : forall (n : nat) (v : nat -> R),
  0 <= sum_f_R (fun i => v i * v i) n.
Proof.
  intros. apply sum_f_R_nonneg. intros; apply Rle_0_sqr.
Qed.

(* Дефектные ядра пусты: сумма |v_i|^2 > 0 при ненулевом v *)
Lemma sumSq_pos : forall (n : nat) (v : nat -> R),
  (exists i, i < n /\ v i <> 0) -> 0 < sum_f_R (fun k => v k * v k) n.
Proof.
  intros n v [i [Hi Hv]].
  apply Rlt_le_trans with (v i * v i).
  - apply Rlt_0_sqr. apply not_0_imp_Rlt_or_Rgt_or_Rlt_0_0 in Hv.
    destruct Hv as [H | H]; [apply Rlt_R0_Rsqr | apply Rlt_R0_Rsqr]; auto.
  - apply sum_f_R_le. intros; apply Rle_0_sqr.
    pose proof (sum_f_R_ge_bound (fun k => v k * v k) n i Hi).
    lra.
Qed.

(* Tr(AB) = Tr(BA) для конечных матриц: перестановка сумм *)
Lemma trace_commute :
  forall (A B : nat -> nat -> R) (n : nat),
  sum_f_R (fun i => sum_f_R (fun j => A i j * B j i) n) n =
  sum_f_R (fun i => sum_f_R (fun j => B i j * A j i) n) n.
Proof.
  intros. apply sum_f_R_ext. intros.
  rewrite (sum_f_R_swap_correct).
  apply sum_f_R_ext. intros. ring.
Qed.
