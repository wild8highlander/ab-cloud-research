# infographics/ — Visual summaries

| File | Content |
|---|---|
| [`dirac_lab_map.png`](dirac_lab_map.png) (+ [`lab_map.html`](lab_map.html) source) | Lab map, **five tracks**: (I) the clean Dirac identity D1–D6 · (II) the ζ bridge D7–D8 · (III) §8 programme D9–D11 · (IV) JR-ready vortex physics · (V) beyond §8 D12–D14 + cross-verification — per-test cards with headline metrics and the skeleton↔phases bridge diagram |
| `results_dashboard.png` | Results dashboard, **6 rows / 20 panels**: verdict ledger (14/14 · 96 checks), E₁·L convergence, ⟨r⟩ GUE-shift bars, Klein T(θ), Landau ladders, ZB traces, D9 restoration contrast, D10 pair correlation + transport hierarchy, D11 BK residual + Dirichlet comb + drive form factor, D12 delta train + extensive protection, D13 pinned wall + generator band, D14 form factors of three zero bands, and the "what each version adds" panels |

The dashboard is rendered by matplotlib code in the generation scripts
(`make figures` lists the outputs); the lab map is a self-contained HTML file
rendered to PNG at 2× scale via Playwright. Both embed the canonical run
numbers from [`../results/run_20261006_full_v13/`](../results/run_20261006_full_v13/).
