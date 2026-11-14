# Thin CLI runner (CANON_SPEC v3.0) — all math in ab_cloud_verify.jl.
# main() parses ARGS (--zeros/--source/--objection/--lang/--data-dir) and
# exits 1 when a frozen self-check anchor fails; run_suite() with no kwargs
# would silently drop every CLI flag.
include("ab_cloud_verify.jl")
main()
