import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Tuple
from src.config import PETRO_EXTENSIONS, TARGET_SUBFOLDERS, get_file_category

def scan_wells_directory(base_path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Recorre la carpeta raíz de pozos y genera dos listas:
    1. Registros detallados (1 fila por archivo)
    2. Resumen horizontal agrupado (1 fila por pozo)
    """
    root_dir = Path(base_path)
    
    if not root_dir.exists() or not root_dir.is_dir():
        raise FileNotFoundError(f"La ruta no existe o no es válida: {base_path}")

    detailed_files = []
    well_summaries = []

    # Obtener carpetas de nivel 1 (los Pozos)
    well_folders = [f for f in root_dir.iterdir() if f.is_dir()]

    for well_folder in well_folders:
        well_name = well_folder.name
        detected_subfolders = set()
        
        # Estructura inicial para el resumen por pozo
        well_summary = {
            "POZO": well_name,
            "SUBCARPETAS_ENCONTRADAS": "",
            "TOTAL_ARCHIVOS_POZO": 0,
            "TOTAL_REGISTROS_PETRO": 0,
            "DATA_#_Archivos": 0,
            "DATA_#_PETRO": 0,
            "DATA_Lista_Archivos": [],
            "DATA_EDIT_#_Archivos": 0,
            "DATA_EDIT_#_PETRO": 0,
            "DATA_EDIT_Lista_Archivos": [],
            "DATA_COMP_#_Archivos": 0,
            "DATA_COMP_#_PETRO": 0,
            "DATA_COMP_Lista_Archivos": [],
            "IMG_#_Archivos": 0,
            "IMG_Lista_Archivos": [],
            "INF_#_Archivos": 0,
            "INF_Lista_Archivos": [],
            "OTRAS_SUBCARPETAS": []
        }

        # Recorrido recursivo dentro de la carpeta del pozo
        for root, _, files in os.walk(well_folder):
            current_path = Path(root)
            relative_path = current_path.relative_to(well_folder)
            
            # Identificar el nombre de la subcarpeta principal
            subfolder_name = relative_path.parts[0] if relative_path.parts else "Raiz"

            if subfolder_name != "Raiz":
                detected_subfolders.add(subfolder_name)
                if subfolder_name not in TARGET_SUBFOLDERS and subfolder_name not in well_summary["OTRAS_SUBCARPETAS"]:
                    well_summary["OTRAS_SUBCARPETAS"].append(subfolder_name)

            for file_name in files:
                file_path = current_path / file_name
                extension = file_path.suffix.lower()
                category = get_file_category(extension)
                is_petro = extension in PETRO_EXTENSIONS
                
                # Obtener tamaño y fecha
                try:
                    stats = file_path.stat()
                    size_mb = round(stats.st_size / (1024 * 1024), 3)
                    mod_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
                except Exception:
                    size_mb = 0.0
                    mod_time = "N/A"

                # 1. Guardar metadatos en lista detallada
                detailed_files.append({
                    "Pozo": well_name,
                    "Subcarpeta": str(relative_path),
                    "Nombre_Archivo": file_name,
                    "Extension": extension,
                    "Categoria": category,
                    "Tamano_MB": size_mb,
                    "Fecha_Modificacion": mod_time,
                    "Ruta_Completa": str(file_path)
                })

                # 2. Acumular conteos en el resumen del pozo
                well_summary["TOTAL_ARCHIVOS_POZO"] += 1
                if is_petro:
                    well_summary["TOTAL_REGISTROS_PETRO"] += 1

                # Mapear a carpetas objetivo
                if subfolder_name in TARGET_SUBFOLDERS:
                    well_summary[f"{subfolder_name}_#_Archivos"] += 1
                    
                    if subfolder_name in ['DATA', 'DATA_EDIT', 'DATA_COMP'] and is_petro:
                        well_summary[f"{subfolder_name}_#_PETRO"] += 1
                    
                    well_summary[f"{subfolder_name}_Lista_Archivos"].append(file_name)

        # Formatear listas a texto para que encajen bien en la celda de Excel
        well_summary["SUBCARPETAS_ENCONTRADAS"] = " | ".join(sorted(detected_subfolders))
        well_summary["OTRAS_SUBCARPETAS"] = ", ".join(well_summary["OTRAS_SUBCARPETAS"])
        
        for key in ["DATA_Lista_Archivos", "DATA_EDIT_Lista_Archivos", "DATA_COMP_Lista_Archivos", "IMG_Lista_Archivos", "INF_Lista_Archivos"]:
            well_summary[key] = "\n".join(well_summary[key]) if well_summary[key] else "Sin archivos"

        well_summaries.append(well_summary)

    return detailed_files, well_summaries