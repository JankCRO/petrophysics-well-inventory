# Petrophysical Well Inventory & Audit Tool

Herramienta automatizada en Python para auditar, clasificar y catalogar volúmenes masivos de datos técnicos de pozos petroleros (`.LAS`, `.LIS`, `.DLIS`, `.PDF` e imágenes).

## Contexto del Proyecto
En la industria de E&P, la información técnica suele estar dispersa en cientos de carpetas con nomenclaturas heterogéneas. Esta herramienta automatiza el recorrido dinámico de directorios para generar una **matriz consolidada** y un **inventario detallado** en Excel, permitiendo identificar rápidamente la disponibilidad de registros petrofísicos por pozo.

> **Métrica de rendimiento:** Probado exitosamente con **473 pozos** y más de **29,600 archivos** catalogados en tiempo récord.

## Características
- **Recorrido Dinámico Recursivo:** Inspecciona carpetas de pozos con subestructuras variables sin interrumpir la ejecución.
- **Detección Petrofísica Dedicada:** Clasifica y contabiliza de forma independiente archivos `.LAS`, `.LIS` y `.DLIS`.
- **Estructura Multicapa en Excel:**
  - `Matriz_Resumen_Pozos`: Vista ejecutiva horizontal (1 fila por pozo) con conteos por subcarpeta (`DATA`, `DATA_EDIT`, `DATA_COMP`, `IMG`, `INF`).
  - `Detalle_General_Archivos`: Traza individual de cada archivo con peso (MB), extensión y fecha de modificación.

## 🛠️ Tecnologías Utilizadas
- **Python 3.x**
- **Pandas** (Procesamiento y estructuración de datos)
- **OpenPyXL** (Generación y estilización del reporte Excel)

## 🔧 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/petrophysics-well-inventory.git](https://github.com/TU_USUARIO/petrophysics-well-inventory.git)
   cd petrophysics-well-inventory