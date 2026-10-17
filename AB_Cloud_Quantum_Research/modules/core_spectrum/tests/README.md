# tests/ — the pytest suite of the package

| File | Theorem/campaign | Source type |
|------|------------------|---------------|
| test_th1_passport.py | Th1 (hermiticity) | live recomputation |
| test_th2_selfadjoint.py | Th2 (self-adjointness) | live recomputation |
| test_th3_certificates.py | Th3 (certificates) | the V12 commit |
| test_th4_li.py | Th4 (the Li formula) | live recomputation (50k) |
| test_th5_block_reduction.py | Th5 (block reduction) | live recomputation |
| test_th6_trace_formula.py | Th6 (the trace formula) | live recomputation (20k) |
| test_blind_and_nulls.py | V1/V2 | committed verdicts |
| test_formal_blocked.py | V13 | the obligation machine |
| test_audit.py | V14 | the claims audit |
| test_repro.py | reproducibility | 15 campaigns + meta |
| test_v16_fullham.py | V16 | live recomputation |
| test_v17_electron.py | V17 | live recomputation (reduced) |
| test_v18_processor.py | V18 | live recomputation |
| test_v19_stitching.py | V19 | live recomputation |

Run: `python3 -m pytest tests/ -q` (~6 s, 42 tests). No test requires
network access or external toolchains.
