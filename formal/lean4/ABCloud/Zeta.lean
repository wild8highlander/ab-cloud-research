/-
Copyright (c) 2026 Isaev Iskhak Khamzatovich.
Released under the Custom Research License (see ../../LICENSE).

# AB-Cloud numeric port — the verification pipeline in Lean 4

A dependency-free Float64 port of the algorithms of
`verification/python/ab_cloud_verify.py`:

* Lambert W (principal branch) by Newton iteration — same initial guess,
  same 50-iteration cap, same 1e-12 relative exit criterion;
* Gram points γ̃_k = 2πk / W(k/e);
* the b(N) = (1/N)·Σ_{k≤N} |γ_k − γ̃_k| convergence ladder;
* unfolded spacings s_k = (γ_{k+1} − γ_k)·log(γ_k/2π)/(2π);
* the GUE Wigner–Dyson CDF F(s) = 1 − e^{−πs²/4};
* the Kolmogorov–Smirnov D statistic and the Cramér–von Mises W²;
* the mean adjacent-spacing ratio ⟨r⟩;
* the log–log linear regression of b(N) (slope / intercept / R²).

The executable entry point (`ABCloud.Verify`) recomputes the frozen
reference numbers committed with the repository and checks each of them.
-/

namespace ABCloud.Zeta

/-! ## Float helpers -/

/-- Absolute value on `Float` (self-contained). -/
def fabs (x : Float) : Float := if x < 0.0 then -x else x

/-- Maximum on `Float` (self-contained). -/
def fmax (a b : Float) : Float := if a < b then b else a

/-- Minimum on `Float` (self-contained). -/
def fmin (a b : Float) : Float := if a < b then a else b

/-! ## Lambert W — principal branch, Newton iteration -/

/-- Newton loop for `w·e^w = x`. Mirrors the Python reference exactly:
skip the update when the derivative vanishes (`|f'| < 1e-30`), update,
then exit when `|Δw| < 1e-12·max(|w|,1)`; hard cap 50 iterations. -/
private partial def lambertLoop (x : Float) : Float → Nat → Float
  | w, i =>
    if 50 ≤ i then w
    else
      let ew := w.exp
      let f := w * ew - x
      let fp := ew * (w + 1.0)
      if fabs fp < 1.0e-30 then w
      else
        let w' := w - f / fp
        let delta := w - w'
        if fabs delta < 1.0e-12 * fmax (fabs w) 1.0 then w'
        else lambertLoop x w' (i + 1)

/-- Principal branch of the Lambert W function, `W₀(x)`: Newton iteration
from the logarithmic seed, with the small-`x` seed fallback `w = x`.
Port of `lambert_w` in the Python reference. -/
partial def lambertW (x : Float) : Float :=
  if x == 0.0 then 0.0
  else
    let w0 := (fmax x 1.0e-30).log
    let w1 := if w0 < 0.0 then x else w0
    lambertLoop x w1 0

/-- 2π at full Float64 precision. -/
def twoPi : Float := 6.283185307179586

/-- Euler's number e. -/
def euler : Float := 2.718281828459045

/-- Gram-point approximation `γ̃_k = 2πk / W(k/e)` — the same estimator the
10-language verification suite and the canonical Julia suite use. -/
def gramPoint (k : Nat) : Float :=
  twoPi * Float.ofNat k / lambertW (Float.ofNat k / euler)

/-! ## Objection 1 — the b(N) convergence ladder -/

private partial def bnGo (zeros : Array Float) (N : Nat) : Nat → Float → Float
  | k, acc =>
    if k > N then acc
    else bnGo zeros N (k + 1) (acc + fabs (zeros[k - 1]! - gramPoint k))

/-- `b(N) = (1/N)·Σ_{k=1..N} |γ_k − γ̃_k|`. Returns NaN when `N` is out of
range, mirroring the reference behaviour. -/
def computeBn (zeros : Array Float) (N : Nat) : Float :=
  if N = 0 ∨ N > zeros.size then (0.0 / 0.0)
  else bnGo zeros N 1 0.0 / Float.ofNat N

/-! ## Objection 2 — GUE spacing statistics -/

/-- GUE (Wigner–Dyson) CDF: `F(s) = 1 − e^{−πs²/4}`. -/
def gueCdf (s : Float) : Float :=
  1.0 - (-(3.141592653589793 * s * s / 4.0)).exp

/-- GUE (Wigner–Dyson) PDF: `p(s) = (πs/2)·e^{−πs²/4}`. -/
def guePdf (s : Float) : Float :=
  (3.141592653589793 * s / 2.0) * (-(3.141592653589793 * s * s / 4.0)).exp

/-- Unfolded spacings `s_k = (γ_{k+1} − γ_k)·log(γ_k/2π)/(2π)`,
skipping nonpositive ordinates exactly like the reference loader. -/
def spacings (zeros : Array Float) : Array Float :=
  (Array.range (zeros.size - 1)).filterMap fun k =>
    let gk := zeros[k]!
    if gk ≤ 0.0 then none
    else some ((zeros[k + 1]! - gk) * (gk / twoPi).log / twoPi)

private partial def ksLoop (sorted : Array Float) (cdf : Float → Float)
    (n : Float) : Nat → Float → Float → Float
  | i, dPlus, dMinus =>
    if i ≥ sorted.size then fmax dPlus dMinus
    else
      let fx := cdf sorted[i]!
      let dp := fmax dPlus (Float.ofNat (i + 1) / n - fx)
      let dm := fmax dMinus (fx - (Float.ofNat i / n))
      ksLoop sorted cdf n (i + 1) dp dm

/-- Kolmogorov–Smirnov distance between the empirical distribution of the
sample and a reference CDF: `D = max(D⁺, D⁻)`. -/
def ksStatistic (sample : Array Float) (cdf : Float → Float) : Float :=
  if sample.size = 0 then 0.0
  else
    let sorted := sample.qsort (fun a b => decide (a < b))
    let n := Float.ofNat sorted.size
    ksLoop sorted cdf n 0 0.0 0.0

private partial def cvmLoop (sorted : Array Float) (cdf : Float → Float)
    (n : Float) : Nat → Float → Float
  | i, acc =>
    if i ≥ sorted.size then acc
    else
      let fx := cdf sorted[i]!
      let t := 2.0 * Float.ofNat (i + 1) - 1.0
      let t := t / (2.0 * n) - fx
      cvmLoop sorted cdf n (i + 1) (acc + t * t)

/-- Cramér–von Mises statistic
`W² = 1/(12n) + Σᵢ [(2i−1)/(2n) − F(xᵢ)]²`. -/
def cvmStatistic (sample : Array Float) (cdf : Float → Float) : Float :=
  if sample.size = 0 then 0.0
  else
    let sorted := sample.qsort (fun a b => decide (a < b))
    let n := Float.ofNat sorted.size
    cvmLoop sorted cdf n 0 (1.0 / (12.0 * n))

private partial def ratioLoop (ds : Array Float) : Nat → Float → Float
  | k, acc =>
    if k + 1 ≥ ds.size then acc
    else
      let a := ds[k]!
      let b := ds[k + 1]!
      ratioLoop ds (k + 1) (acc + fmin a b / fmax a b)

/-- Mean adjacent-spacing ratio ⟨r⟩ — the self-unfolding GUE statistic
(analytic GUE reference 0.5997, Poisson 0.3863). -/
def meanRatio (zeros : Array Float) : Float :=
  let ds := (Array.range (zeros.size - 1)).filterMap fun k =>
    let d := zeros[k + 1]! - zeros[k]!
    if d > 0.0 then some d else none
  if ds.size < 2 then 0.0
  else ratioLoop ds 0 0.0 / Float.ofNat (ds.size - 1)

/-! ## Objection 3 — the log–log decay fit -/

/-- Result of the linear fit `log b(N) = slope·log N + intercept`. -/
structure Fit where
  slope : Float
  intercept : Float
  r2 : Float

/-- Ordinary least squares in log–log space with the R² of the fit —
port of `_linear_regression` in the Python reference. -/
def linFit (xs ys : Array Float) : Fit :=
  let n := xs.size
  if n < 2 ∨ ys.size ≠ n then ⟨0.0, 0.0, 0.0⟩
  else
    let nf := Float.ofNat n
    let sx := xs.foldl (· + ·) 0.0
    let sy := ys.foldl (· + ·) 0.0
    let sxx := xs.foldl (fun acc x => acc + x * x) 0.0
    let sxy := (Array.zip xs ys).foldl (fun acc p => acc + p.1 * p.2) 0.0
    let den := nf * sxx - sx * sx
    let slope := (nf * sxy - sx * sy) / den
    let intercept := (sy - slope * sx) / nf
    let yMean := sy / nf
    let ssRes := (Array.zip xs ys).foldl
      (fun acc p => let d := p.2 - (slope * p.1 + intercept); acc + d * d) 0.0
    let ssTot := ys.foldl (fun acc y => let d := y - yMean; acc + d * d) 0.0
    let r2 := 1.0 - ssRes / ssTot
    ⟨slope, intercept, r2⟩

end ABCloud.Zeta
