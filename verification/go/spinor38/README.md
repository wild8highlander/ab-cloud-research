# Test 38 -- 64 spinor structures of the Klein quartic (Go port)

Go port of the validated C++ reference `verification/cpp/spinor38/spinor38.cpp`.

The program uses ONLY the frozen data files and a self-implemented cyclic
Jacobi eigenvalue algorithm (no external packages, standard library only) to
verify:

1. the 28 odd (Arf=1) spinor structures of the Klein quartic are exactly
   isospectral (max pairwise spectral distance ~ 1e-14) -- no spinor structure
   is unique (corrects the v21 monograph claim about idx=38);
2. the spacing-ratio statistic `<r>` of the representative spectrum matches
   the reference value 0.4515710792825435.

## Build and run

    go run .
    # or build a binary first:
    go build -o spinor38 .
    ./spinor38

Optional first argument: path to the repository root. Without it the data
directory is located by walking up from the current working directory (up to
6 levels) looking for `verification/spinor64/data/spinor_classes.csv`:

    go run . /path/to/repo/root

Requires Go 1.16+ (standard library only, `go.mod` has no dependencies).
The program exits 0 on PASS / 1 on FAIL.

## Data files used

- `verification/spinor64/data/spinor_classes.csv` (64 classes, 84 signs each)
- `verification/spinor64/data/klein_graph_edges.csv` (84 edges of the Klein graph)
- `verification/spinor64/data/reference_stats.json` (reference statistics)

## Validated reference output

The C++ port is the validated reference; its output is:

    Test 38 - 64 spinor structures of the Klein quartic (C++ port)
    classes loaded: 64 | odd-orbit members: 28
    isospectrality within the odd orbit: max|dlambda| = 3.419e-14 -> PASS
    zero modes (representative): 2 (expected 2)
    <r> (representative): 0.4515710793 (reference 0.4515710793) -> PASS
    VERDICT: PASS

Note: this Go port was authored in an environment without a Go toolchain, so
it was verified by a line-by-line review against the C++ reference (and a
floating point cross-check of the identical algorithm), not by compilation in
place. It prints the same report with "(Go port)" in the header line.
