<div align="center">

<img src="08_assets/logos/logo_unified.svg" alt="AB-Cloud unified research logo" width="200"/>

# AB CLOUD RESEARCH — PAQUETE ACADÉMICO UNIFICADO

**Un estudio en cuatro niveles: la arquitectura AB algebraica (Aharonov–Bohm) como tejido de cómputo, su esqueleto de Dirac, el puente de Hilbert–Pólya y el aparato de verificación ciega.**

*Edición unificada · sin números de versión · datos abiertos · límites honestos*

[![Campaigns](https://img.shields.io/badge/campaigns-44%2B_PASS-7FC8A8?style=for-the-badge)](02_data/processed/research_registry.json)
[![Theorems](https://img.shields.io/badge/theorems-27-E8DDB8?style=for-the-badge)](01_monographs/README.md)
[![RH](https://img.shields.io/badge/RH_status-BLOCKED-FFB74D?style=for-the-badge)](#honest)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21825394)

[Русский](README.ru.md) · [English](README.md) · [中文](README.zh.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md)

</div>

---

> [!IMPORTANT]
> **Límite honesto (Importante).** Todo en este paquete es un estudio numérico y formal de un modelo matemático. **No** demuestra la hipótesis de Riemann: la máquina de obligaciones V13 mantiene la conclusión de RH **bloqueada** mientras los prerrequisitos analíticos sigan siendo supuestos. Los resultados negativos se publican como ciudadanos de primera clase: el muro de localidad (T18), la zona nula en las compuertas (T8), los fallos de correspondencia ζ de retícula (V1/V3/V6/V16).

---

## Qué es esto

Esta carpeta es la edición académica unificada de todo el programa de investigación AB-Cloud: un paquete autosuficiente que consolida los tres laboratorios de investigación del repositorio — AB_Cloud_Quantum_Research (núcleo espectral y procesador AB), dirac-lab (el esqueleto de Dirac) y Hilbert_Polya (el puente de Hilbert–Pólya) — junto con el legado de verificación del paquete anterior (la ejecución de referencia de 38 pruebas y sus adenda). La edición unificada no lleva números de versión: es una estructura académica viva (00_meta … 10_notebooks), no un lanzamiento congelado.

## Arquitectura: niveles de una máquina

| Nivel | Carpeta fuente | Campañas | Esencia en una línea |
|---|---|---|---|
| 🧠 **Núcleo** | `AB_Cloud_Quantum_Research` | **V01–V19** | espectro ciego, clase GUE, la traza lleva Λ(n)/√n (r = 0.9996), la máquina V13 bloquea RH |
| ⚛️ **Procesador** | `AB_Cloud_Quantum_Research` | **V20** | ISA de nube AB, compilación Givens–QR exacta (1−F ≤ 4.4·10⁻¹⁶), «lee, no almacena», CHSH = 2√2 − 4.4·10⁻¹⁶ |
| ⚛️ **Esqueleto de Dirac** | `dirac-lab` | **D1–D14** | la retícula de flujo π **es** una ecuación de Dirac sin masa discretizada; el operador decorado con ζ eleva GOE → GUE (⟨r⟩ 0.608 vs 0.5992) |
| 🌉 **Puente** | `Hilbert_Polya` | **C1–C17 · T1–T18** | el operador que casi existe: traza no local exacta (r_H7 = 1.000), la identidad de niveles al nivel de los propios ceros (G2 — SÍ), los primos por la escalera de convergencia (G5 — SÍ), el muro a nivel de bits = **localidad** |
| 🔬 **Verificación** | `AB_Cloud_Quantum_Research` | **E01–E18** | lectura ciega de ceros ζ 649/649 + 639/639 (entre motores 0.0), Riemann–Siegel independiente, clase B ganada ×59.000 |
| 🌀 **Espinor** | `AB_Cloud_Quantum_Research` | **ES1–ES5** | la máquina sin memoria a largo plazo: ciclos que cierran en N = 2k, paso O(1) vs Ω(t) |

## 📂 Estructura del paquete

| Ruta | Contenido |
|---|---|
| [`00_meta/`](00_meta/README.md) | manifiesto, procedencia, listas de verificación de reproducibilidad/FAIR/ética |
| [`01_monographs/`](01_monographs/README.md) | la monografía unificada: volúmenes completos RU/EN + resúmenes en cinco idiomas |
| [`02_data/`](02_data/README.md) | datos, esquemas, diccionario de datos, libro de códigos, sumas de verificación |
| [`03_figures/`](03_figures/README.md) | figuras estáticas (600 dpi), diagramas, paletas, leyendas |
| [`04_reports/`](04_reports/README.md) | informe unificado (MD/PDF/DOCX), resúmenes, nota de prensa, diapositivas |
| [`05_logs/`](05_logs/README.md) | registros de ejecución/errores/auditoría, métricas, sesiones |
| [`06_code/`](06_code/README.md) | CLI unificado en seis idiomas + contrato JSON compartido |
| [`07_web_lab/`](07_web_lab/README.md) | el laboratorio web interactivo (sin conexión) |
| [`08_assets/`](08_assets/README.md) | avatares, insignias, logotipos, nueve temas |
| [`09_tests/`](09_tests/README.md) | suite pytest de integridad del paquete |
| [`10_notebooks/`](10_notebooks/README.md) | notebooks de exploración/análisis/informe |

## 🚀 Inicio rápido

```bash
./06_code/cli/run.sh --lang=es --theme=neon   # CLI unificado
python3 -m pytest 09_tests/python -q              # comprobaciones de integridad
```

## ⚖️ Registro de veredictos

| Tesis | Veredicto | Base |
|---|---|---|
| Autoadjunción | **SÍ** | hermiticidad de cero de máquina, espectro real |
| Identidad espectral | **NO** | 9–10 órdenes (C3) ≈ 0.5 (C4); el muro = localidad |
| Clase GUE | **SÍ** | ⟨r⟩ = 0.60; toda la familia C5 en la clase |
| Dinámica de Dirac | **SÍ** | paquete coherente 1·10⁻¹⁵; Klein ×977; ZB en ω = 2E |
| Primos en el operador | **NO** | en trazas sí (r = 0.9996); en espectros de compuertas — zona nula |
| RH | **BLOQUEADA** | máquina de obligaciones V13; prerrequisitos supuestos |

## 📜 Citación

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

*Este paquete se explica a sí mismo: cada carpeta lleva su propio README, cada número nombra su campaña, cada afirmación lleva su límite.* — **[Volver al README principal](README.md)**
