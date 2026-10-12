# Bridge Explorer (Streamlit)

Interactive v2.0 companion to the committed verdicts (plan item 9).

```bash
pip install streamlit
streamlit run explorer/streamlit_app.py
```

Three tabs:

1. **Live gate** — turn the handles (Nv, q, W, α, mass, δα, phase-coding β)
   → `eigvalsh` rebuilds the 576×576 resonator and re-measures the three
   projections of the H2 gap (rank r_H7, heat r_EF fluct, statistics class
   ⟨r⟩) against the internal zero cache, with the positive controls stated.
2. **Verdicts C9–C16** — the committed campaign verdicts (RU/EN) and metadata.
3. **Bridge map** — the v2.0 map: eight new campaigns, eight new theorems.

Honesty discipline is inherited from v1: the explorer replays committed
data; every live metric is the same protocol as the campaigns
(unfolded-vs-unfolded convention, internal mpmath zero cache, PC0′ = 1.000
for ispectral twins).
