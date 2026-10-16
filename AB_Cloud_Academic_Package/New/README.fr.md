<div align="center">

<img src="08_assets/logos/logo_unified.svg" alt="AB-Cloud unified research logo" width="200"/>

# AB CLOUD RESEARCH — PAQUET ACADÉMIQUE UNIFIÉ

**Une étude sur quatre niveaux : l'architecture AB algébrique (Aharonov–Bohm) comme tissu de calcul, son squelette de Dirac, le pont de Hilbert–Pólya et l'appareil de vérification aveugle.**

*Édition unifiée · sans numéros de version · données ouvertes · limites honnêtes*

[![Campaigns](https://img.shields.io/badge/campaigns-44%2B_PASS-7FC8A8?style=for-the-badge)](02_data/processed/research_registry.json)
[![Theorems](https://img.shields.io/badge/theorems-27-E8DDB8?style=for-the-badge)](01_monographs/README.md)
[![RH](https://img.shields.io/badge/RH_status-BLOCKED-FFB74D?style=for-the-badge)](#honest)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21825394)

[Русский](README.ru.md) · [English](README.md) · [中文](README.zh.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md)

</div>

---

> [!IMPORTANT]
> **Limite honnête (Important).** Tout ce que contient ce paquet est une étude numérique et formelle d'un modèle mathématique. Il ne prouve **pas** l'hypothèse de Riemann : la machine d'obligations V13 maintient la conclusion RH **bloquée** tant que les prérequis analytiques restent des hypothèses. Les résultats négatifs sont publiés comme des citoyens de première classe : le mur de localité (T18), la zone nulle aux portes (T8), les échecs des correspondances ζ sur réseau (V1/V3/V6/V16).

---

## Ce que c'est

Ce dossier est l'édition académique unifiée de tout le programme de recherche AB-Cloud : un paquet autonome qui consolide les trois laboratoires de recherche du dépôt — AB_Cloud_Quantum_Research (noyau spectral et processeur AB), dirac-lab (le squelette de Dirac) et Hilbert_Polya (le pont de Hilbert–Pólya) — avec l'héritage de vérification du paquet de soumission précédent (l'exécution de référence de 38 tests et ses addenda). L'édition unifiée ne porte **aucun numéro de version** : c'est une structure académique vivante (00_meta … 10_notebooks), pas une version figée.

## Architecture : les niveaux d'une machine

| Niveau | Dossier source | Campagnes | Essence en une ligne |
|---|---|---|---|
| 🧠 **Noyau** | `AB_Cloud_Quantum_Research` | **V01–V19** | spectre aveugle, classe GUE, la trace porte Λ(n)/√n (r = 0.9996), la machine V13 bloque RH |
| ⚛️ **Processeur** | `AB_Cloud_Quantum_Research` | **V20** | ISA de nuage AB, compilation Givens–QR exacte (1−F ≤ 4.4·10⁻¹⁶), « lit, ne stocke pas », CHSH = 2√2 − 4.4·10⁻¹⁶ |
| ⚛️ **Squelette de Dirac** | `dirac-lab` | **D1–D14** | le réseau à flux π **est** une équation de Dirac sans masse discrétisée ; l'opérateur décoré par ζ élève GOE → GUE (⟨r⟩ 0.608 vs 0.5992) |
| 🌉 **Pont** | `Hilbert_Polya` | **C1–C17 · T1–T18** | l'opérateur qui existe presque : trace non locale exacte (r_H7 = 1.000), l'identité des niveaux au niveau des zéros eux-mêmes (G2 — OUI), les nombres premiers par l'échelle de convergence (G5 — OUI), le mur au niveau des bits = **localité** |
| 🔬 **Vérification** | `AB_Cloud_Quantum_Research` | **E01–E18** | lecture aveugle des zéros ζ 649/649 + 639/639 (entre moteurs 0.0), Riemann–Siegel indépendant, classe B gagnée ×59 000 |
| 🌀 **Spineur** | `AB_Cloud_Quantum_Research` | **ES1–ES5** | la machine sans mémoire à long terme : cycles fermés à N = 2k, pas O(1) vs Ω(t) |

## 📂 Structure du paquet

| Chemin | Contenu |
|---|---|
| [`00_meta/`](00_meta/README.md) | manifeste, provenance, listes de contrôle reproductibilité/FAIR/éthique |
| [`01_monographs/`](01_monographs/README.md) | la monographie unifiée : volumes complets RU/EN + résumés en cinq langues |
| [`02_data/`](02_data/README.md) | données, schémas, dictionnaire de données, codebook, sommes de contrôle |
| [`03_figures/`](03_figures/README.md) | figures statiques (600 dpi), diagrammes, palettes, légendes |
| [`04_reports/`](04_reports/README.md) | rapport unifié (MD/PDF/DOCX), résumés, communiqué de presse, diapositives |
| [`05_logs/`](05_logs/README.md) | journaux d'exécution/erreurs/audit, métriques, sessions |
| [`06_code/`](06_code/README.md) | CLI unifiée en six langues + contrat JSON partagé |
| [`07_web_lab/`](07_web_lab/README.md) | le laboratoire web interactif (hors ligne) |
| [`08_assets/`](08_assets/README.md) | avatars, badges, logos, neuf thèmes |
| [`09_tests/`](09_tests/README.md) | suite pytest d'intégrité du paquet |
| [`10_notebooks/`](10_notebooks/README.md) | notebooks d'exploration/analyse/rapport |

## 🚀 Démarrage rapide

```bash
./06_code/cli/run.sh --lang=fr --theme=neon   # CLI unifiée
python3 -m pytest 09_tests/python -q              # vérifications d'intégrité
```

## ⚖️ Registre des verdicts

| Thèse | Verdict | Base |
|---|---|---|
| Auto-adjonction | **OUI** | hermiticité au zéro machine, spectre réel |
| Identité spectrale | **NON** | 9–10 ordres (C3) ≈ 0.5 (C4) ; le mur = localité |
| Classe GUE | **OUI** | ⟨r⟩ = 0.60 ; toute la famille C5 dans la classe |
| Dynamique de Dirac | **OUI** | paquet cohérent 1·10⁻¹⁵ ; Klein ×977 ; ZB à ω = 2E |
| Nombres premiers dans l'opérateur | **NON** | dans les traces oui (r = 0.9996) ; dans les spectres de portes — zone nulle |
| RH | **BLOQUÉE** | machine d'obligations V13 ; prérequis supposés |

## 📜 Citation

```bibtex
@dataset{isaev_abcloud_unified,
  author  = {Isaev, Iskhak Khamzatovich},
  title   = {AB-Cloud Research Programme: Unified Academic Package},
  year    = {2026},
  doi     = {10.5281/zenodo.21825394},
  url     = {https://github.com/wild8highlander/ab-cloud-research/tree/main/AB_Cloud_Academic_Package}
}
```

---

*Ce paquet s'explique lui-même : chaque dossier porte son propre README, chaque nombre nomme sa campagne, chaque affirmation porte sa limite.* — **[Retour au README principal](README.md)**
