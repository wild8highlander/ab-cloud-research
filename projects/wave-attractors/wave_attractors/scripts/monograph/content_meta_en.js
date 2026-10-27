/** content_meta_en.js — metadata for the English W1 monograph. */
module.exports = {
  fileName: "AB_Cloud_Monograph_W1_EN.docx",
  docTitle: "Hyperbolic Wave Attractors: Ray and Wave Models",
  docSubject: "AB-Cloud study W1: hyperbolic wave attractors, anisotropy scan, and time-domain simulation with unit-cell truncation",
  headerTitle: "Hyperbolic wave attractors — study W1 (AB-Cloud)",
  cover: {
    schoolName: "AB-CLOUD RESEARCH",
    docType: "Monograph · Study W1",
    title: "Hyperbolic Wave Attractors",
    subtitle: "Ray and wave models, anisotropy scan,",
    subtitle2: "and time-domain simulation with unit-cell truncation",
    metaLines: [
      "Series: AB-Cloud repository monograph",
      "Object: hyperbolic billiard",
      "Methods: billiard, Helmholtz, ADE-FDTD, Julia",
      "Repository: github.com/wild8highlander",
      "Version: 1.0 (W1 + E6 + E7)",
    ],
    footerRight: "October 2026",
  },
  abstractTitle: "Abstract",
  abstract: [
    "This monograph systematises the results of study W1 of the AB-Cloud Research repository, devoted to the numerical reproduction of hyperbolic wave attractors — the self-organisation of waves into closed, chiral and broadband trajectories inside an anisotropic (hyperbolic) cavity. The work builds on «Hyperbolic wave attractors» (Nature Physics, 2026, CUNY ASRC) and extends the reproduction to a two-sided wave model: beyond the ray billiard and the frequency-domain Helmholtz equation it adds an anisotropy scan and a time-domain simulation with a physically consistent unit-cell truncation of the metamaterial.",
    "At the ray level (experiments E1–E5) the study confirms the wavelength cascade with a mean |k| growth of ×7.6 per slope bounce, full attractor lock-in (24 of 24 rays against 0 of 24 in the isotropic control), exact chiral complementarity of mirror pairs, and the frequency invariance of the route. The new experiments E6–E7 extend the picture. First, the attractor phase turns out to be a WINDOW whose both boundaries are universal in the variable u = s·√η (u₁ = 0.176 ± 0.041; u₂ = 0.490 ± 0.084 across two decades of η), while the naive resonance criterion s* = 1/√η overestimates this window. Second, the time-domain problem for the nondispersive indefinite tensor is shown to be ill-posed (exponential blow-up at the measured rate γ = 74.6 against the estimate 2/(Δx·√η)); the cure is the dispersive (Drude) model of the wire-mesh metamaterial μ_y(ω) = 1 − ω_p²/ω² with ω_p = πc/a set by the cell size. At the drive frequency ω₀ = ω_p/√(η+1) such a medium is EXACTLY the η = 100 hyperbolic medium of the ray model; a pulsed drive demonstrates the funneling onto the ray route in real time (corridor energy 1.43× the isotropic control), the k-space cascade locked onto the iso-frequency hyperbola and piling up below the fold |kₓ| ≈ ω_p/c, and the cell-count scan (32…192 cells) reveals the homogenisation convergence of the attractor: the peak corridor capture grows tenfold.",
    "Every key result is reproduced twice, independently, in two languages (Python and Julia): the agreement of short trajectories is 3.45·10⁻¹⁵ over bounce points and 2.4·10⁻¹⁵ over the TD-kernel field. The monograph is accompanied by a fully reproducible pipeline (Makefile, CI, primary CSV/JSON/NPZ data) and twelve publication-grade figures.",
  ],
  keywordsLabel: "Keywords:",
  keywords: "hyperbolic metamaterial; wave attractor; wavelength cascade; billiard; non-specular reflection; anisotropy; universal scaling; unit-cell truncation; Drude dispersion; ADE-FDTD; chirality; cross-verification",
  tocTitle: "Table of Contents",
  tocHint: "Note: this Table of Contents is generated via field codes. To ensure page-number accuracy after editing, right-click the TOC and select «Update Field».",
};
