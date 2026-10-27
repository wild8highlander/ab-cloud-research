# FAQ

**Q1. Does this package prove the Riemann hypothesis?**
No. The V13 obligation machine is unlocked: the RH conclusion is `certified`
(0 assumptions on the path — O12 classical; O08/O09/O11 certified numerically);
RH as a theorem still requires O11 for all n. The Lean/Coq formalization guarantees
this blocking. What the package *does* offer is the most precise map the
programme has produced of where such a proof would have to pass — and where
it hits walls (locality, T18).

**Q2. What is "reads, does not carry"?**
The AB-processor result (V23 preview): the machine reproduces 12/12 ζ zeros
from six formula constants with storage = 0 — it reads mathematics in real
time and retains nothing. The spinor study (ES1–ES5) formalizes the memory
model this implies.

**Q3. Why are there negative results on the front page?**
Because they are the map. The locality wall (T18), the null zone at gates
(T8) and the failed lattice ζ-correspondences (V1/V3/V6/V16) tell any future
positive construction exactly what cannot work. Burying them would be
scientific malpractice; the package treats them as first-class citizens.

**Q4. Why no version numbers?**
The unified edition is a living academic structure (numbered sections
`00_meta` … `10_notebooks`), not a release train. Editorial history is kept
in `CHANGELOG.md`. The legacy "v23/v34" identity of the submission package is
retired; its content survives as heritage records in `00_meta/`.

**Q5. Which languages does the package speak?**
READMEs: RU, EN, ZH, DE, ES, FR, AR. Monograph: full RU + EN volumes; the
other five languages get faithful abstracts. CLI: RU + EN message catalogues.
Web lab: RU + EN with a seven-language UI map. Glossary: RU, EN, ZH.

**Q6. How do I run the verification?**
`reproduce.sh` at the root, or `python3 -m pytest 09_tests/python -q` for the
package integrity suite. To re-run the research campaigns themselves, use the
source laboratories (their READMEs are the entry points) — this package
consolidates their records and adds the unified CLI for structure-level
operations.

**Q7. What is the relationship to the three source folders?**
Consolidation, not replacement. The sources remain the canonical homes of
their code and run data; this package is the unified academic edition of
their *content*: one monograph, one report, one registry, one honesty layer.

**Q8. Can I use the figures in my paper?**
Yes — CC BY 4.0 for the figure files, with the recommended credit line from
`LICENSE-TEXT`. Keep the honest boundary statements when you quote results.

**Q9. Where is the actual evidence?**
`02_data/` (curated datasets + registry), `05_logs/metrics.json` (numbers
with campaign attributions), and the per-campaign folders of the source
laboratories for the raw run archives.

**Q10. Why do two sources sometimes quote slightly different ⟨r⟩ values?**
Conventions differ (e.g. the bulk-window boundary convention documented in
note 2 of the Dirac cross-verification). The package quotes numbers verbatim
from their verdict files and shows both when they disagree — see
`CHANGELOG.md` editorial decisions.
