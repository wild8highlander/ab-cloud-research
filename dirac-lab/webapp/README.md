# webapp/ — Interactive applications (self-contained HTML, no external assets)

## 1. Dirac Cone Explorer — [`dirac_cone_explorer.html`](dirac_cone_explorer.html)

- Live heatmap of the π-flux Bloch dispersion |E+(k)| over the full Brillouin zone; the four Dirac points circled.
- **Anisotropy/mass slider** δ: h(k) → 2t·cos(k_y)σ_z + 2t·cos(k_x+δ)σ_x — watch the E = 0 touching gap out
  (the mass-regularized C = 0 of parent test 20); the live gap readout quantifies it.
- Cross-section E(k_x) through the cone; Berry phase and v_F chips tie the app to tests D1/D3.
- **Hofstadter butterfly**: 627 rational fluxes α = p/q (q ≤ 45) computed on load from the same Harper
  Hamiltonian; the α = 1/2 line marks the Dirac touching.

## 2. Wave Packet Lab — [`wave_packet_lab.html`](wave_packet_lab.html)

Real-time exact spectral evolution (Jacobi-diagonalized 1D Dirac chain, complex coefficient space):

- **Klein tunneling tab**: Dirac packet vs **Schrödinger control** at the same smooth barrier; sliders for
  V₀, width d and mass m; live transmission readouts. At m = 0 the Dirac transmission approaches 1 through
  a classically forbidden barrier while the control stays exponentially suppressed — test D5 in your browser.
- **Zitterbewegung tab**: ⟨x(t)⟩ trembling at ω = 2E₁ (live theory readout) with a sublattice-mixing knob
  that suppresses the oscillation — the interband-coherence lesson of test D6, made hands-on.

Both apps are pure client-side HTML/JS — open the files directly in any browser, or serve the folder.
