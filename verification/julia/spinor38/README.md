# Test 38 -- 64 spinor structures of the Klein quartic (Julia port)

Julia port of the validated C++ reference `verification/cpp/spinor38/spinor38.cpp`.
Uses ONLY the frozen data files and the stdlib `LinearAlgebra`; the Jacobi
eigenvalue algorithm is implemented in-file (no LAPACK calls).

## Run

    julia spinor38.jl [repo-root]

## Validated reference output (C++ / JavaScript, this environment)

    isospectrality within the odd orbit: max|dlambda| = 3.419e-14 -> PASS
    zero modes (representative): 2 (expected 2)
    <r> (representative): 0.4515710793 (reference 0.4515710793) -> PASS
    VERDICT: PASS
