# Journal Recommendations — Interdisciplinary Venues for the AB-Cloud v23 Submission Package

*Подготовлено: 19 сентября 2026 · для пакета `AB_Cloud_v23_Full_Package_Academic_v34.zip`*

---

## Краткая сводка (RU)

Для вашей работы — междисциплинарного вычислительного исследования (решётчатый оператор
Ааронова–Бома против нулей дзеты Римана, 38-тестовый верификационный протокол, GUE-статистика,
полный код и данные на GitHub + Zenodo DOI) — профиль лучше всего дают журналы трёх групп:
широкие междисциплинарные OA, математическая физика и вычислительная математика.

**Топ-3 рекомендации на 2026 год:**

1. **Royal Society Open Science** — междисциплинарный OA-журнал Лондонского королевского
   общества (математика + физические науки). В 2026 году действует модель Subscribe to Open:
   **APC для авторов отсутствует (waiver автоматический)**. Сильная политика открытых данных
   и кода — репозиторий GitHub и Zenodo DOI указываются прямо в рукописи. Регистрация:
   аккаунт на сайте журнала + ORCID. Лучшее сочетание «престиж / стоимость / открытость».
2. **Scientific Reports** (Springer Nature) — крупнейший междисциплинарный OA-журнал,
   IF ≈ 4.9, принимает воспроизводимые и верификационные исследования без требования
   новизны («scientifically sound»), что идеально для 38-тестового протокола. APC ≈
   £2,190 / $2,890 (проверить на сайте при подаче). Обязательны statements о доступности
   данных и кода — ссылка на `github.com/wild8highlander/ab-cloud-research` встраивается
   в раздел «Data availability».
3. **PLOS ONE** — междисциплинарный мега-журнал с моделью «sound science» и жёсткой
   политикой шеринга кода/данных (с 2026 г. шеринг кода обязателен). APC ≈ $2,477.
   Формат «Collection of results» позволяет подать верификационную работу целиком.

**Специализированные (если сузить материал до статьи):** SIGMA (без APC, мат. физика),
Experimental Mathematics (T&F — вычислительные эксперименты в математике), Random Matrices:
Theory and Applications (World Scientific — если акцент на GUE/RMT-статистику), Mathematics
and Computers in Simulation (Elsevier — верификационный протокол как методология), J. Phys. A
(IOP, гибридный OA). Быстрый широкий вариант: Open Mathematics (De Gruyter) или Mathematics
(MDPI, ≈ CHF 2,700, быстро, но проверьте репутационные дискуссии по MDPI в вашем поле).

**Бонус — журнал для самого кода:** Journal of Open Source Software (JOSS) — бесплатный,
рецензирование через GitHub, принимает «свободно стоящий» программный артефакт
(`ab_cloud_v23.jl` + python_clone) со ссылкой на научную статью. Можно публиковать
параллельно: JOSS-пейпер для кода + основная статья в одном из журналов выше.

**Чего избегать:** Heliyon (Clarivate приостанавливал журнал в 2024, сотни ретракций 2025 —
репутационный риск возвращается, хотя «on hold» снят в 2026); издательства типа Peertechz
(«Annals of Mathematics and Physics», APC $2,589) — признаки хищнической модели.

---

## Detailed notes (EN)

### 1. Royal Society Open Science — *first recommendation, 2026 window*

- **Scope fit.** Covers the full range of science and mathematics, explicitly including
  mathematical physics, statistical mechanics and computational science. A verification
  study combining lattice Hamiltonians, random-matrix statistics and number-theory
  reference data is squarely in scope as a cross-disciplinary contribution.
- **Cost.** Under the Royal Society's Subscribe-to-Open model, **no APC is charged** for
  2026 publications (waivers are automatic for the Society's open-access journals).
- **Open science.** Data and code availability are expected; the manuscript cites the
  GitHub repository (`github.com/wild8highlander/ab-cloud-research`) and the Zenodo
  archive (DOI 10.5281/zenodo.21825394) directly.
- **Registration & submission.** Register at the journal's submission site (link "Submit
  an article" on royalsocietypublishing.org), attach ORCID 0009-0003-7299-0701, upload
  the manuscript (the Academic Essence preprint, ~50 pp., is the natural submission
  unit), the cover letter (`cover_letter.pdf` in this package), the full run archive as
  supplementary material or via Zenodo, and suggest reviewers.
- **Cautions.** Selective editorial triage; format the submission as a standard article
  (the monograph's full apparatus ships as supplementary data, not as the manuscript).

### 2. Scientific Reports (Springer Nature)

- **Scope fit.** Interdisciplinary; peer review of scientific soundness rather than
  novelty — a good match for a rigorous verification protocol whose value is in the
  completeness of the record (38 tests, 127 sub-checks, cross-language reproduction).
- **Cost.** APC ≈ £2,190 / $2,890 (2026; confirm on the journal's APC page; institutional
  agreements may cover it).
- **Open science.** Mandatory data and code availability statements; deposit reusable
  outputs (Zenodo DOI already in place; GitHub repository linked in the statement).
- **Registration & submission.** Register at the Nature Portfolio submission system
  (via nature.com/srep → "Submit manuscript"), ORCID linkage, upload manuscript +
  cover letter, fill the data-availability section with the GitHub and Zenodo links.
- **Cautions.** Page/figure limits are generous but the 31k-line source listing belongs
  in supplementary material or the repository, not the manuscript body.

### 3. PLOS ONE

- **Scope fit.** All-discipline mega-journal judging technical soundness; publishes
  replication and verification studies explicitly. The Test 34 addendum chain
  (pre-registration → re-run → forensics) matches PLOS ONE's registered-replication
  culture well.
- **Cost.** APC $2,477 (2026 standard research article); partial/fee waivers available
  on request.
- **Open science.** From 2026 code sharing is mandatory for applicable submissions —
  the GitHub repository and Zenodo DOI satisfy this directly.
- **Registration & submission.** Register at journals.plos.org (PLOS Editorial Manager),
  ORCID, upload the manuscript (Essence preprint adapted to the PLOS template), cover
  letter, and complete the data-availability questionnaire with the repository links.

### 4. Specialized alternatives (condense the material into a standard-length article)

| Journal | Publisher | Fit angle | Fees (2026) |
|---|---|---|---|
| **SIGMA** (Symmetry, Integrability and Geometry) | Scuola Normale Superiore | Mathematical physics; GUE statistics of a lattice operator vs ζ zeros | **No APC** (fully no-fee OA) |
| **Experimental Mathematics** | Taylor & Francis | Computational experiments suggesting formal results; the Test 34 confrontation as an experiment | Hybrid OA (APC optional; subscription route free) |
| **Random Matrices: Theory and Applications** | World Scientific | The GUE classification, unfolding and RMT statistics machinery | Subscription/hybrid |
| **Mathematics and Computers in Simulation** | Elsevier | The 38-test verification suite and reproducibility apparatus as simulation methodology | Hybrid OA |
| **Journal of Physics A: Mathematical and Theoretical** | IOP | Mathematical/theoretical physics; supports open access | Hybrid OA |
| **Open Mathematics** | De Gruyter | Broad mathematics journal, number theory among core areas | APC (moderate; check current) |
| **Mathematics** | MDPI | Fast broad OA incl. mathematical physics and number theory | ≈ CHF 2,700 (verify) |

### 5. Code-oriented companion: Journal of Open Source Software (JOSS)

A short "software paper" describing `ab_cloud_v23.jl` (the suite) and the standalone
laboratory can be submitted **via GitHub** (the submission itself is a pull request);
review is free, fast, and the published artifact links back to
`github.com/wild8highlander/ab-cloud-research`. Pairing a JOSS paper with a main article
in one of the venues above is a common and effective pattern.

### 6. Venues to avoid

- **Heliyon** (Cell Press): Clarivate "on hold" (2024), ~392 retractions in 2025; the hold
  was lifted in 2026, but the reputation risk persists.
- **Peertechz "Annals of Mathematics and Physics"** and similar APC-first outlets
  (persistent solicitation, minimal review) — predatory-pattern indicators.

### 7. Practical submission checklist (package mapping)

1. Choose the venue tier: broad OA (RSOS / Sci Rep / PLOS ONE) or specialized (SIGMA /
   Exp. Math. / RMT&A / MATCOM).
2. Manuscript unit: `preprint2/academic_essence_preprint.pdf` (53 pp.) for broad venues;
   a condensed Test-34-plus-framework article for the specialized ones.
3. Attach: `cover_letter.pdf` (update the journal name), `submission_forms.pdf`
   (CRediT, declarations, data availability), `journal_recommendations.md` (this file)
   for your own reference.
4. Link artefacts: GitHub repo + Zenodo DOI in the Data/Code Availability statement;
   cite the run archives (`run_20260914_234626`, `run_20260917_080329_m2`,
   `run_20260919_085734_m2`) as evidence objects with their own DOIs if desired.
5. Register: author account on the journal platform + ORCID 0009-0003-7299-0701;
   complete the author metadata exactly as in the monograph's title page.
6. Supplementary: the monograph PDF and/or the run-data archive via the journal's
   supplementary system or Zenodo (preferred for size).

*All fee figures verified against September 2026 search results; confirm on the journal
sites at submission time — APCs change.*
