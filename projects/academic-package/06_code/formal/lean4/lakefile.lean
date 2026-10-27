import Lake
open Lake DSL

/-
AB-Cloud formal verification — Lean4 project.

Zero external dependencies: the library builds on the Lean 4 core only
(no Mathlib, no Std), so `lake build` completes in well under a minute
and the formal CI job needs nothing but the pinned toolchain.
-/

package «abcloud» where
  version := v!"1.0.0"
  leanOptions := #[
    ⟨`autoImplicit, false⟩,
    ⟨`relaxedAutoImplicit, false⟩
  ]

/-- Machine-checked exact core + the numeric port of the verification suite. -/
@[default_target]
lean_lib «ABCloud» where
  -- root module: ABCloud.lean

/-- Executable re-verification: recomputes the frozen reference numbers of
the flagship run and checks them against the committed values. -/
@[default_target]
lean_exe «abcloud-verify» where
  root := `ABCloud.Verify
