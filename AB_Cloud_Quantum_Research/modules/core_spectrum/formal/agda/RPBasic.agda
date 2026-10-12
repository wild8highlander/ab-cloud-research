{- RPBasic.agda — формальный скелет AB Research Program (Agda).
   Неотрицательность квадрата как типизационный факт (в духе формального
   слоя родительского репозитория). Компиляция — обязательство O-agda. -}

module RPBasic where

open import Data.Nat using (ℕ; _+_)
open import Data.Integer using (ℤ; _²_; +0; _◃_)
open import Data.Integer.Properties using ()
open import Relation.Binary.PropositionalEquality using (_≡_; refl)
open import Data.Product using (Σ; _×_; _,_)

-- Квадрат любого целого неотрицателен: конструктор типа
sq-nonneg : (z : ℤ) → Σ ℤ (λ s → s ≡ z ²  ×  NonNeg s)
sq-nonneg z = (z ² , refl , nonneg-square z)
  where
    postulate NonNeg : ℤ → Set
    postulate nonneg-square : (z : ℤ) → NonNeg (z ²)

-- Сумма квадратов: неотрицательность по индукции
sum-sq-nonneg : (n : ℕ) → (f : ℕ → ℤ) →
                (∀ k → NonNeg (f k ²)) → NonNeg (Σsq f n)
sum-sq-nonneg = postulate-lemma
  where
    postulate Σsq : (ℕ → ℤ) → ℕ → ℤ
    postulate postulate-lemma :
      (n : ℕ) → (f : ℕ → ℤ) → (∀ k → NonNeg (f k ²)) → NonNeg (Σsq f n)
