# Study W1 — Hyperbolic wave attractors

**Numerical reproduction of "Hyperbolic wave attractors" (Nature Physics,
2026, CUNY ASRC) inside the AB-Cloud Research repository.**

Waves launched into an odd-shaped cavity made of a hyperbolic
metamaterial skip chaotic scattering and self-organize into **robust,
chiral, broadband closed routes** — *hyperbolic wave attractors*, the
wave analogue of limit cycles in nonlinear dynamics. Study W1 rebuilds
the phenomenon at two levels (exact k-vector ray billiard + frequency-
domain anisotropic Helmholtz solver), cross-verifies the implementation
against an independent Julia port, and adds a companion reproduction of
the Aharonov–Bohm effect with water waves (Berry 1980; OIST 2026) — the
classical-fluid root of the AB-phase theme of this repository.

## Headline numbers

| Observable | Value |
|---|---|
| Attractor lock-in (hyperbolic vs isotropic control) | **1.00** vs **0.00** |
| Wavelength cascade per slope reflection | mean **×7.6**, max ×65 |
| Mirror-pair chirality sum C + C′ | **0.0** (machine precision) |
| Frequency invariance of the ray map (K = 1 ↔ 7) | **exact** (deviation 0.0) |
| Ray-density contrast on the route | **×5.47** |
| Python ↔ Julia trajectory identity (1200 bounce points) | **3.45·10⁻¹⁵** |
| Attractor window in u = s·√η (η = 9…400, E6) | **u₁ = 0.176 ± 0.041**, u₂ = 0.490 ± 0.084 |
| TD corridor capture, hyperbolic vs isotropic pulse (E7a) | **1.43×** |
| Peak capture growth from 32 → 192 unit cells (E7b) | **×10** |
| Python ↔ Julia TD-kernel identity (400 steps) | **2.4·10⁻¹⁵** |

## Mechanism

1. The indefinite dispersion `ky² − kx²/η = K²` confines the group
   velocity to a cone of half-angle `arctan(1/√η)` around the optical
   axis — waves propagate only along narrow prescribed directions.
2. Reflection from an inclined wall conserves the tangential wave-vector
   component; on the open hyperbola the reflected state is the *second*
   intersection (Vieta root) — non-specular, with |k| jumping along the
   contour: the **wavelength cascade**.
3. In a chamber combining vertical walls (specular) with shallow slopes
   (cascade), every ray funnels onto the same closed route. The route is
   chiral; its mirror image lives in the mirrored chamber; both
   circulation senses coexist as attractors in the symmetric case.
4. The cascade terminates at the finest resolved scale — the unit-cell
   cutoff of the experiment, the grid cutoff of the simulation.
5. **E6 (η-scan).** Both boundaries of the attractor window are universal
   in u = s·√η across two decades of anisotropy (u₁ = 0.18 ± 0.04,
   u₂ = 0.49 ± 0.08); the naive resonance s\* = 1/√η (u = 1) overestimates
   the window. Wave-level maps show
   the field channeling into vertical corridors as η grows (anisotropy
   H: 0.78 → 0.87 vs isotropic baseline 0.5).
6. **E7 (time domain).** A physically consistent TD model requires the
   Drude dispersion of the wire-mesh metamaterial, μ_y(ω) = 1 − ω_p²/ω²
   with ω_p = πc/a (a — unit cell); the naive nondispersive indefinite
   tensor blows up exponentially. At ω₀ = ω_p/√(η+1) the medium is
   exactly the η = 100 hyperbolic medium; the pulsed TD drive funnels
   onto the ray route (1.43× the isotropic control), the k-space cascade
   runs along the IFC hyperbola and piles up below the unit-cell fold
   |kₓ| ≈ ω_p/c; the capture grows ×10 from 32 to 192 cells
   (homogenisation convergence).

## Files and pipeline

The full pipeline, quick-start commands, result tables and
reproducibility notes live in
[`wave_attractors/README.md`](https://github.com/wild8highlander/ab-cloud-research/blob/main/wave_attractors/README.md).

Run everything with:

```bash
make wave-attractors        # full protocol
make wave-attractors-quick  # CI protocol
```

## Reproducibility

The study regenerates from repository sources alone (`make wave-attractors`,
`make wave-attractors-julia`, `make wave-attractors-docs`). A blind
cold-start audit (2026-10-01) reproduced 31/31 data files, 12/12 figures
bitwise, the 14-page report text identically and both monograph DOCX
contents bitwise — see `wave_attractors/REPRODUCING.md` and the certificate
`wave_attractors/data/REPRODUCIBILITY.json`.

```bash
make wave-attractors-verify CAND=/path/to/fresh/wave_attractors/data
```

## References

* *Hyperbolic wave attractors*, Nature Physics (2026),
  DOI 10.1038/s41567-026-03453-7.
* Naked Science, «В кривой камере волны сами выстроились в идеальную
  структуру», 30.09.2026.
* Maas & Lam, Phys. Rev. Lett. 74, 1040 (1995) — internal-wave attractors.
* Berry et al., Eur. J. Phys. 1, 154 (1980) — AB effect with water waves.
* OIST / Communications Physics (2026) — water-tank AB experiment.
