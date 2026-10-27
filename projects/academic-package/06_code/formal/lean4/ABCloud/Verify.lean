/-
Copyright (c) 2026 Isaev Iskhak Khamzatovich.
Released under the Custom Research License (see ../../LICENSE).

# `abcloud-verify` — the Lean4 executable re-verification

`lake exe abcloud-verify` recomputes the frozen reference numbers of the
AB-Cloud verification suite — the b(N) ladder, the GUE spacing statistics
(KS D and Cramér–von Mises W²), the mean spacing ratio ⟨r⟩ and the log–log
decay fit — directly from the frozen dataset, and checks every value
against the committed reference block. It exits non-zero on any mismatch,
so it doubles as a CI gate.

Modes:

* default — load `verification/data/zeta_zeros_50000.txt` (5000 zeros)
  from the repository and check against `REF_MAIN`;
* `--embedded` — use the 256 embedded zeros and the `REF_EMBED` block
  (always available, even outside a full checkout);
* `--data PATH` / `--count N` — custom dataset and ladder depth.
-/

import ABCloud.Basic
import ABCloud.Zeta
import ABCloud.Embed

namespace ABCloud.Verify

open ABCloud.Zeta
open ABCloud.Embed

/-! ## Check bookkeeping -/

/-- One verification check and its outcome. -/
structure Check where
  name : String
  value : Float
  reference : Float
  tolerance : Float

/-- Outcome of one check. -/
structure Outcome where
  ok : Bool
  delta : Float

def Check.run (c : Check) : Outcome :=
  let d := Zeta.fabs (c.value - c.reference)
  ⟨d ≤ c.tolerance, d⟩

def Outcome.line (c : Check) (o : Outcome) : String :=
  let status := if o.ok then "PASS" else "FAIL"
  "  " ++ c.name ++ " = " ++ c.value.toString
    ++ "   ref " ++ c.reference.toString
    ++ "   Δ = " ++ o.delta.toString
    ++ "  (tol " ++ c.tolerance.toString ++ ")  " ++ status

/-! ## Minimal self-contained decimal parser -/

/-- Accumulate leading decimal digits into a `Float`. -/
private partial def parseDigits : Float → List Char → Float × List Char
  | acc, c :: rest =>
    if '0' ≤ c ∧ c ≤ '9' then
      parseDigits (acc * 10.0 + Float.ofNat (c.toNat - '0'.toNat)) rest
    else (acc, c :: rest)
  | acc, [] => (acc, [])

/-- Accumulate fractional digits: returns (value, scale, rest). -/
private partial def parseFrac : List Char → Float → Float → Float × Float × List Char
  | c :: rest, acc, scale =>
    if '0' ≤ c ∧ c ≤ '9' then
      parseFrac rest (acc * 10.0 + Float.ofNat (c.toNat - '0'.toNat)) (scale * 10.0)
    else (acc, scale, c :: rest)
  | [], acc, scale => (acc, scale, [])

/-- Accumulate a signed exponent. -/
private partial def parseExp : List Char → Int → Int → Int × List Char
  | c :: rest, sign, acc =>
    if '0' ≤ c ∧ c ≤ '9' then
      parseExp rest sign (acc * 10 + (c.toNat - '0'.toNat))
    else (sign * acc, c :: rest)
  | [], sign, acc => (sign * acc, [])

private def pow10 : Nat → Float
  | 0 => 1.0
  | n + 1 => 10.0 * pow10 n

private def applyExp (m : Float) : Int → Float
  | 0 => m
  | n => if n > 0 then pow10 (Int.toNat n) * m else m / pow10 (Int.toNat (-n))

/-- Minimal decimal parser: `[+-]? d+ [. d*] [ (e|E) [+-]? d+ ]`.
Round-off differs from platform `strtod` by at most 1 ulp, which the
check tolerances absorb. -/
partial def parseFloat? (s : String) : Option Float :=
  match s.data with
  | [] => none
  | '-' :: rest => (parseFloat? (String.mk rest)).map (· * -1.0)
  | '+' :: rest => parseFloat? (String.mk rest)
  | cs =>
    let (intPart, cs2) := parseDigits 0.0 cs
    if intPart == 0.0 ∧ cs.all (fun c => ¬c.isDigit) then none
    else
      let (fracNum, fracScale, cs3) :=
        match cs2 with
        | '.' :: rest => parseFrac rest 0.0 1.0
        | _ => (0.0, 1.0, cs2)
      let (exponent, cs4) :=
        match cs3 with
        | 'e' :: rest => parseExp rest 1 0
        | 'E' :: rest => parseExp rest 1 0
        | _ => (0, cs3)
      if cs4.length > 1 ∨ (cs4.any fun c => c.isDigit) then none
      else
        let mant := intPart + fracNum / fracScale
        some (applyExp mant exponent)
where
  applyExp (m : Float) : Int → Float
    | 0 => m
    | n => if n > 0 then pow10 (Int.toNat n) * m else m / pow10 (Int.toNat (-n))

/-! ## Dataset loading -/

private def dataCandidates : List String :=
  ["../../verification/data/zeta_zeros_50000.txt",
   "../verification/data/zeta_zeros_50000.txt",
   "verification/data/zeta_zeros_50000.txt"]

/-- Parse a frozen ζ-zero file: one value per line, `#` comments and blank
lines skipped — the same loader contract as the 10-language suite. -/
def parseZeroLines (lines : Array String) : Array Float :=
  (lines.filterMap fun line =>
      let s := line.trim
      if s.isEmpty ∨ s.startsWith "#" then none
      else parseFloat? s)
  |>.qsort (fun a b => decide (a < b))

private def loadFileAt (path : String) : IO (Option (Array Float)) := do
  if ← System.FilePath.pathExists path then do
    let lines ← IO.FS.lines path
    let zeros := parseZeroLines lines
    if zeros.size > 0 then
      IO.println s!"  data: {path}  ({zeros.size} zeros parsed)"
      return some zeros
  return none

/-- Try the candidate dataset paths and return the first that parses. -/
def loadDataset : IO (Option (Array Float)) := do
  for path in dataCandidates do
    match ← loadFileAt path with
    | some zs => return some zs
    | none => continue
  return none

private def getNextAfter (args : List String) (flag : String) : Option String :=
  match args with
  | a :: rest => if a == flag then rest.head? else getNextAfter rest flag
  | [] => none

/-! ## The check batteries -/

/-- The b(N) ladder checks for one mode. -/
def ladderChecks (zeros : Array Float) (refs : List (Nat × Float)) : List Check :=
  refs.filterMap fun (N, ref) =>
    some ⟨s!"b({N})", Zeta.computeBn zeros N, ref, 1.0e-6⟩

/-- The full check battery for one dataset + reference block. -/
def battery (zeros : Array Float) (ladder : List Nat)
    (bRefs : List (Nat × Float)) (dRef w2Ref slopeRef r2Ref : Float) :
    IO (List Check) := do
  let bs := ladderChecks zeros bRefs
  let sp := Zeta.spacings zeros
  let d := Zeta.ksStatistic sp Zeta.gueCdf
  let w2 := Zeta.cvmStatistic sp Zeta.gueCdf
  let xs := ladder.toArray.filterMap
    fun N => if N ≤ zeros.size then some (Float.ofNat N).log else none
  let ys := ladder.toArray.filterMap
    fun N => if N ≤ zeros.size then some (Zeta.computeBn zeros N).log else none
  let fit := Zeta.linFit xs ys
  IO.println s!"  unfolded spacings: {sp.size}  ·  ⟨r⟩ = {(Zeta.meanRatio zeros).toString}  (GUE 0.5997, informational)"
  pure (bs
    ++ [⟨"KS D", d, dRef, 5.0e-4⟩,
        ⟨"CvM W²", w2, w2Ref, 5.0e-3⟩,
        ⟨"decay slope", fit.slope, slopeRef, 1.0e-3⟩,
        ⟨"decay R²", fit.r2, r2Ref, 1.0e-3⟩])

/-! ## Entry point -/

def usage : String :=
"usage: lake exe abcloud-verify [--embedded] [--data PATH] [--count N] [--help]"

/-- The main verification program. -/
def runVerify (args : List String) : IO UInt32 := do
  let embedded := args.contains "--embedded"
  let countArg :=
    match getNextAfter args "--count" with
    | some s => s.toNat?
    | none => none
  let customData := getNextAfter args "--data"

  if args.contains "--help" ∨ args.contains "-h" then
    IO.println usage
    return (0 : UInt32)

  IO.println "══════════════════════════════════════════════════════════════"
  IO.println " AB-Cloud formal verification — Lean 4 (core-only, no Mathlib)"
  IO.println " re-derives the frozen reference numbers of the flagship run"
  IO.println "══════════════════════════════════════════════════════════════"

  let zeros ←
    if embedded then
      pure (some Embed.embeddedZeros)
    else
      match customData with
      | some path => loadFileAt path
      | none => loadDataset

  let zerosOpt :=
    match zeros with
    | some zs => if zs.isEmpty then none else some zs
    | none => none

  match zerosOpt with
  | none =>
      IO.println "  no dataset found — falling back to the embedded 256 zeros"
      IO.println "  (run with --data PATH to point at the frozen dataset)"
  | some _ => pure ()

  let zeros := zerosOpt.getD Embed.embeddedZeros
  let count := countArg.getD 5000
  let useEmbedded := embedded ∨ count > zeros.size
  let zeros := if useEmbedded then Embed.embeddedZeros else zeros.take count

  let ladder := if useEmbedded then Embed.REF_EMBEDLadder else Embed.REF_MAINLadder
  let (bRefs, dRef, w2Ref, slopeRef, r2Ref) :=
    if useEmbedded then
      (Embed.REF_EMBEDbRefs, Embed.REF_EMBEDD, Embed.REF_EMBEDW2,
       Embed.REF_EMBEDSlope, Embed.REF_EMBEDR2)
    else
      (Embed.REF_MAINbRefs, Embed.REF_MAIND, Embed.REF_MAINW2,
       Embed.REF_MAINSlope, Embed.REF_MAINR2)
  let mode := if useEmbedded then "EMBEDDED (256 zeros)"
    else s!"DATASET ({zeros.size} zeros)"
  let tmin := zeros[0]!
  let tmax := zeros[zeros.size - 1]!

  IO.println ""
  IO.println s!"  mode: {mode}  ·  zeros: {zeros.size}  ·  T ∈ [{tmin.toString}, {tmax.toString}]"
  IO.println ""
  IO.println " Objection 1 — b(N) convergence ladder"
  IO.println " Objection 2 — GUE spacing statistics (KS + Cramér–von Mises)"
  IO.println " Objection 3 — large-T decay fit (log–log regression)"
  IO.println ""

  let checks ← battery zeros ladder bRefs dRef w2Ref slopeRef r2Ref
  let outcomes := checks.map (fun c => (c, c.run))

  IO.println " ─────────────────────────────────────────────────────────────"
  for (c, o) in outcomes do
    IO.println (o.line c)
  IO.println " ─────────────────────────────────────────────────────────────"

  let total := outcomes.length
  let passed := (outcomes.filter (fun p => p.2.ok)).length
  let allOk := passed == total
  if allOk then
    IO.println s!" RESULT: {passed}/{total} checks PASS — Lean 4 re-derives the frozen numbers"
    IO.println " of the AB-Cloud verification suite to the committed tolerances."
  else
    IO.println s!" RESULT: {passed}/{total} checks PASS, {total - passed} FAIL — see the lines above."
  IO.println "══════════════════════════════════════════════════════════════"
  return if allOk then (0 : UInt32) else (1 : UInt32)

/-- The `lake exe` entry point. -/
def main (args : List String) : IO UInt32 :=
  runVerify args

end ABCloud.Verify

/-- Top-level `main` expected by the `lake exe` linker. -/
def main (args : List String) : IO UInt32 := ABCloud.Verify.main args
