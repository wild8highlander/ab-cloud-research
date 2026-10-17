<div align="center">

<img src="08_assets/logos/logo_unified.svg" alt="AB-Cloud unified research logo" width="200"/>

# AB CLOUD RESEARCH — EINHEITLICHES AKADEMISCHES PAKET

**Eine Studie auf vier Ebenen: die algebraische AB-Architektur (Aharonov–Bohm) als Rechengewebe, ihr Dirac-Skelett, die Hilbert–Pólya-Brücke und der blinde Verifikationsapparat.**

*Einheitliche Ausgabe · ohne Versionsnummern · offene Daten · ehrliche Grenzen*

[![Campaigns](https://img.shields.io/badge/campaigns-44%2B_PASS-7FC8A8?style=for-the-badge)](02_data/processed/research_registry.json)
[![Theorems](https://img.shields.io/badge/theorems-27-E8DDB8?style=for-the-badge)](01_monographs/README.md)
[![RH](https://img.shields.io/badge/RH_status-CERTIFIED-4FA3D1?style=for-the-badge)](#honest)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21825394)

[Русский](README.ru.md) · [English](README.md) · [中文](README.zh.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md)

</div>

---

> [!IMPORTANT]
> **Ehrliche Grenze (Wichtig).** Alles in diesem Paket ist eine numerische und formale Studie eines mathematischen Modells. Es beweist **nicht** die Riemannsche Vermutung. Die Verpflichtungsmaschine V13 ist **entriegelt** (verdict: certified, v1.2.1): Der Pfad O01→O12 trägt keine Annahmen — das klassische Li-Kriterium (O12: RH ⇔ λ_n ≥ 0 ∀n) plus numerisch zertifizierte Konvergenz (O08/O09/O11); als Satz bleibt für RH O11 für alle n offen. Negative Ergebnisse werden als gleichrangige Bürger veröffentlicht: die Lokalitätswand (T18), die Nullzone an den Toren (T8), das Scheitern der Gitter-ζ-Korrespondenzen (V1/V3/V6/V16).

---

## Was dies ist

Dieser Ordner ist die einheitliche akademische Ausgabe des gesamten AB-Cloud-Forschungsprogramms: ein in sich geschlossenes Paket, das die drei Forschungslaboratorien des Repositories konsolidiert — AB_Cloud_Quantum_Research (Spektralkern und AB-Prozessor), dirac-lab (das Dirac-Skelett) und Hilbert_Polya (die Hilbert–Pólya-Brücke) — zusammen mit dem Verifikationserbe des früheren Einreichungspakets (der 38-Test-Referenzlauf und seine Addenda). Die einheitliche Ausgabe trägt keine Versionsnummern: Sie ist eine lebendige akademische Struktur (00_meta … 10_notebooks), kein eingefrorenes Release.

## Architektur: Ebenen einer Maschine

| Ebene | Quellordner | Kampagnen | Essenz in einer Zeile |
|---|---|---|---|
| 🧠 **Kern** | `AB_Cloud_Quantum_Research` | **V01–V19** | blindes Spektrum, GUE-Klasse, die Spur trägt Λ(n)/√n (r = 0.9996), die V13-Maschine blockiert RH |
| ⚛️ **Prozessor** | `AB_Cloud_Quantum_Research` | **V20** | AB-Wolken-ISA, exakte Givens–QR-Kompilierung (1−F ≤ 4.4·10⁻¹⁶), «liest, speichert nicht», CHSH = 2√2 − 4.4·10⁻¹⁶ |
| ⚛️ **Dirac-Skelett** | `dirac-lab` | **D1–D14** | das π-Flussgitter **ist** eine diskretisierte masselose Dirac-Gleichung; der ζ-dekorierte Operator hebt GOE → GUE (⟨r⟩ 0.608 vs. 0.5992) |
| 🌉 **Brücke** | `Hilbert_Polya` | **C1–C17 · T1–T18** | der Operator, der fast existiert: exakte nichtlokale Spur (r_H7 = 1.000), Ebenen-Identität auf dem Niveau der Nullstellen (G2 — JA), die Primzahlen über die Konvergenzleiter (G5 — JA), die bitweise Wand = **Lokalität** |
| 🔬 **Verifikation** | `AB_Cloud_Quantum_Research` | **E01–E18** | blinde ζ-Nullstellen-Lektüre 649/649 + 639/639 (kreuzmotorig 0.0), unabhängiges Riemann–Siegel, Klasse B gewonnen ×59.000 |
| 🌀 **Spinor** | `AB_Cloud_Quantum_Research` | **ES1–ES5** | die Maschine ohne Langzeitgedächtnis: Zyklen schließen bei N = 2k, Schritt O(1) vs. Ω(t) |

## 📂 Paketstruktur

| Pfad | Inhalt |
|---|---|
| [`00_meta/`](00_meta/README.md) | Manifest, Provenienz, Reproduzierbarkeits-/FAIR-/Ethik-Checklisten |
| [`01_monographs/`](01_monographs/README.md) | die einheitliche Monographie: RU/EN-Vollbände + Abstracts in fünf Sprachen |
| [`02_data/`](02_data/README.md) | Daten, Schemata, Datenwörterbuch, Codebook, Prüfsummen |
| [`03_figures/`](03_figures/README.md) | statische Abbildungen (600 dpi), Diagramme, Paletten, Bildunterschriften |
| [`04_reports/`](04_reports/README.md) | einheitlicher Bericht (MD/PDF/DOCX), Zusammenfassungen, Pressemitteilung, Folien |
| [`05_logs/`](05_logs/README.md) | Lauf-/Fehler-/Audit-Protokolle, Metriken, Sitzungen |
| [`06_code/`](06_code/README.md) | einheitliche CLI in sechs Sprachen + gemeinsamer JSON-Vertrag |
| [`07_web_lab/`](07_web_lab/README.md) | das interaktive Weblabor (offline) |
| [`08_assets/`](08_assets/README.md) | Avatare, Badges, Logos, neun Themen |
| [`09_tests/`](09_tests/README.md) | pytest-Suite zur Paketintegrität |
| [`10_notebooks/`](10_notebooks/README.md) | Explorations-/Analyse-/Berichts-Notebooks |

## 🚀 Schnellstart

```bash
./06_code/cli/run.sh --lang=de --theme=neon   # einheitliche CLI
python3 -m pytest 09_tests/python -q              # Integritätsprüfungen
```

## ⚖️ Verdikts-Ledger

| Behauptung | Verdikt | Grundlage |
|---|---|---|
| Selbstadjungiertheit | **JA** | maschinennull-Hermitizität, reelles Spektrum |
| Spektrale Identität | **NEIN** | 9–10 Größenordnungen (C3) ≈ 0.5 (C4); die Wand = Lokalität |
| GUE-Klasse | **JA** | ⟨r⟩ = 0.60; die ganze C5-Familie in der Klasse |
| Dirac-Dynamik | **JA** | kohärentes Paket 1·10⁻¹⁵; Klein ×977; ZB bei ω = 2E |
| Primzahlen im Operator | **NEIN** | in Spuren ja (r = 0.9996); in Torspektren — Nullzone |
| RH | **BLOCKIERT** | V13-Verpflichtungsmaschine; Voraussetzungen angenommen |

## 📜 Zitation

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

*Dieses Paket erklärt sich selbst: jeder Ordner trägt sein eigenes README, jede Zahl nennt ihre Kampagne, jede Behauptung trägt ihre Grenze.* — **[Zurück zum Haupt-README](README.md)**
