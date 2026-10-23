<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ core_spectrum/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
# multilang/ — multilanguage twins of the computational kernel

Six ports of one protocol: the **Γ-closure** |Γ(½+iu)|² = π/cosh(πu)
(complex Lanczos g=7, n=9) at u ∈ {0.5, 1, 2, 3} and the **Λ-sieve** up
to 10⁵ with the sum Σ Λ(n)/n^{3/2}. Each port prints (and writes on
request) a single control block `verify_control.txt`.

| Port | Status in this environment | gamma_closure_max_res | lambda_sum_check |
|------|---------------------|-----------------------|------------------|
| c (C11) | verified (cc -O2) | 1.13e-14 | 1.4989125716 |
| cpp (C++17) | verified (g++ -O2) | 1.24e-14 | 1.4989125716 |
| javascript (Node ≥ 18) | verified | 9.41e-15 | 1.4989125716 |
| go (≥ 1.21) | portable source (toolchain unavailable) | — | — |
| rust (≥ 1.70) | portable source (toolchain unavailable) | — | — |
| julia (≥ 1.9) | portable source (toolchain unavailable) | — | — |

The Python reference: gamma ≤ 1e-12 (the mpmath reference 1e-39 at dps 40),
lambda_sum = **1.4989125716** — agreement with the ports to 10 digits
(the C↔Python Λ discrepancy ≤ 1e-11).

## Build

```bash
cc  -O2 c/verify_core.c -lm && ./a.out c/verify_control.txt
g++ -O2 -std=c++17 cpp/verify_core.cpp -o vc && ./vc cpp/verify_control.txt
node javascript/verify_core.js javascript/verify_control.txt
go build -o vg go/verify_core.go && ./vg go/verify_control.txt
rustc -O rust/verify_core.rs -o vr && ./vr rust/verify_control.txt
julia julia/verify_core.jl julia/verify_control.txt
```

The control block of the C port is checked by the IVP10 protocol
(independent_verification/); the reference Hilbert Polya Bridge series
gives 5.9e-15 / 4.6e-11 — the same level.

## V19 · branch stitching (stitch twins, the R3 regression)

Since v1.2.0 the ports carry a second twin — `stitch_core`: stitching
the branches of the algebraic function (the θ-ladder, sign coherence,
the phase law ζ^{ra+sb} on the torus (Z/15)²). θ(t) is the Stirling
asymptotics (the principal branch; the Lanczos log does not guarantee
the Im branch — checked against mpmath). The first 64 ζ zeros are
embedded; the control block is `stitch_control.txt`.

| Port | Status | conc | coherence | phase_law_max_res |
|------|--------|------|-----------|-------------------|
| c (C11) | verified (cc -O2) | 0.967741935484 | 1.000000000000 | 1.21e-14 |
| javascript (Node ≥ 18) | verified | 0.967741935484 | 1.000000000000 | 1.23e-14 |

The Python reference (rpbridge.stitching on the same 64 zeros): conc
0.967741935484, coherence 1.0 — agreement to 1e-12; the phase law of
the double port 1.2e-14 (threshold 1e-9). Verdict: ALGEBRAIC_CERTIFICATE.

```bash
cc -O2 c/stitch_core.c -lm && ./a.out c/stitch_control.txt
node javascript/stitch_core.js javascript/stitch_control.txt
diff c/stitch_control.txt javascript/stitch_control.txt   # conc/coherence bit-for-bit
```

<div align="center">

<img src="../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
