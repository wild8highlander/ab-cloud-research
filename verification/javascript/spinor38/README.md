# Test 38 -- 64 spinor structures of the Klein quartic (JAVASCRIPT port)

JAVASCRIPT port of the validated C++ reference `verification/cpp/spinor38/spinor38.cpp`.

The program uses ONLY the frozen data files and a self-implemented cyclic
Jacobi eigenvalue algorithm (no BLAS/LAPACK built-ins, standard library only)
to verify:

1. the 28 odd (Arf=1) spinor structures of the Klein quartic are exactly
   isospectral (max pairwise spectral distance ~ 1e-14) -- no spinor structure
   is unique (corrects the v21 monograph claim about idx=38);
2. the spacing-ratio statistic `<r>` of the representative spectrum matches
   the reference value 0.4515710792825435.

## Data (frozen, deterministic)

- verification/spinor64/data/spinor_classes.csv -- 64 signings, orbit ids, Arf
- verification/spinor64/data/klein_graph_edges.csv -- the {3,7} Klein graph (84 edges)
- verification/spinor64/data/reference_stats.json -- reference values

## Build and run

    node spinor38.js [repo-root]     (Node >= 18, std only)

## Validated reference output (C++ / JavaScript, this environment)

    isospectrality within the odd orbit: max|dlambda| = 3.419e-14 -> PASS
    zero modes (representative): 2 (expected 2)
    <r> (representative): 0.4515710793 (reference 0.4515710793) -> PASS
    VERDICT: PASS
