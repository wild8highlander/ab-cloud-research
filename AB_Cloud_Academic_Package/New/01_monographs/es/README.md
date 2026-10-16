<div align="center">

# El programa de investigación AB-Cloud: monografía unificada (resumen en español)

**AB-Cloud Research Programme · Unified Academic Package**

[返回主 README / back](../../README.md)

[Русский](../ru/README.md) · [English](../en/README.md) · [中文](../zh/README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [العربية](../ar/README.md)

</div>

---

> [!NOTE]
**La versión en español es un resumen.** El texto científico completo son los volúmenes en ruso e inglés: [`../ru/monograph_ru.pdf`](../ru/monograph_ru.pdf) y [`../en/monograph_en.pdf`](../en/monograph_en.pdf). A continuación, un resumen fielmente traducido y el índice de capítulos.

## Abstract / 摘要

Esta monografía es el relato unificado del programa de investigación AB-Cloud: un estudio desplegado en cuatro niveles y un estudio suplementario de espinores. El programa investiga un puente estadístico concreto entre dos objetos que las matemáticas llevan más de un siglo intentando reconciliar: los ceros no triviales de la función zeta de Riemann y los espectros de operadores hermíticos. El candidato es un operador de retícula con α cuantos de flujo de Aharonov–Bohm por placa (la nube AB), construido de modo que su estadística espectral caiga en la clase de universalidad GUE — la clase que el programa de Montgomery–Odlyzko predice para los ceros de ζ —, mientras que la capa exacta (hermiticidad, cuantización del flujo, invariancia de Byers–Yang, apareamiento quiral, autodualidad de Connes, una cadena de identidades de fases geométricas) se verifica a precisión de máquina y a 256 bits donde se requiere.

El relato consolida los tres laboratorios de investigación del programa. **Nivel I** — el núcleo espectral y el procesador AB: campañas V01–V20, teoremas Th1–Th6, la máquina de obligaciones V13, y el procesador con ISA de nube AB y compilación Givens–QR exacta (1−F ≤ 4.4·10⁻¹⁶). **Nivel II** — el esqueleto de Dirac: catorce pruebas D1–D14 que establecen que la retícula de flujo π *es* una ecuación de Dirac sin masa discretizada, y que el operador de Dirac decorado con ζ eleva la estadística del volumen de GOE a GUE (⟨r⟩ = 0.608 frente a 0.5992). **Nivel III** — el puente de Hilbert–Pólya: diecisiete campañas C1–C17 y dieciocho teoremas T1–T18; el veredicto del nivel — «el operador que casi existe». **Nivel IV** — verificación ciega: dieciocho veredictos preregistrados E01–E18, incluida la lectura ciega de los 649 ceros de ζ hasta T = 1000 por dos motores independientes con coincidencia bit-exacta, y el legado de la ejecución de referencia de 38 pruebas.

**El registro consolidado de veredictos: autoadjunción — **sí**; identidad espectral — **sí** (al nivel de los propios ceros; auditoría v2.0.7; la rama a nivel de bits queda abierta); clase GUE — **sí**; dinámica de Dirac — **sí**; primos en el operador — **sí** (por la escalera de convergencia; auditoría v2.0.8); la hipótesis de Riemann — **bloqueada** por construcción.** El mapa es ahora de dos caras: la identidad de niveles se sostiene al nivel de los propios ceros y los primos entran por la escalera de convergencia; el muro que queda es a nivel de bits. Una retícula local aún no puede albergar el entrelazamiento que exige el espectro del peine de ceros (S_A ≈ 12–16 nats frente a 160–220 para Haar).

## Índice de capítulos

| # | Chapter |
|---|---|
| 1 | Introducción |
| 2 | Trabajos relacionados |
| 3 | Arquitectura: niveles de una máquina |
| 4 | Nivel I: el núcleo espectral y el procesador AB |
| 5 | Nivel II: el esqueleto de Dirac |
| 6 | Nivel III: el puente de Hilbert–Pólya |
| 7 | Nivel IV: verificación ciega y legado |
| 8 | El estudio de espinores: la máquina sin memoria a largo plazo |
| 9 | Datos y reproducibilidad |
| 10 | El registro experimental consolidado |
| 11 | Resultados y veredictos |
| 12 | Discusión: el muro de localidad |
| 13 | Limitaciones y límites honestos |
| 14 | Conclusión |
| A | Apéndice A: registro de campañas |
| B | Apéndice B: mapa de fuentes |

## Cifras clave

| Resultado | Valor |
|---|---|
| Lectura ciega de ceros ζ hasta T=1000 (dos motores) | 649/649 + 639/639; entre motores 0.0 |
| Estadística decorada con ζ | ⟨r⟩ 0.608 vs teoría 0.5992 |
| Supertúnel de Klein | 0.978 vs 0.0010 (×977) |
| Gemelo no local | r_H7 = 1.000000 |
| Muro de localidad | S_A 12–16 nats vs Haar 160–220 |
| Estado de RH | bloqueada por construcción (V13) |

## Keywords

Palabras clave: función zeta de Riemann · Hilbert–Pólya · Aharonov–Bohm · operador de Dirac en retícula · matrices aleatorias · GUE · Montgomery–Odlyzko · Berry–Keating · Connes · verificación ciega · reproducibilidad
