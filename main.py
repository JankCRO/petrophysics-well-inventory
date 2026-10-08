from pathlib import Path
from src.scanner import scan_wells_directory
from src.exporter import export_to_excel

def main():
    print("=" * 65)
    print("     GENERADOR DE INVENTARIO Y AUDITORÍA DE POZOS (PETROFÍSICA)     ")
    print("=" * 65)

    # Solicitar la ruta de la carpeta al usuario
    input_path = input("\nIngresa la ruta completa de la carpeta POZOS_VSM: ").strip('"').strip("'")
    output_file = "Inventario_Pozos_VSM.xlsx"

    try:
        print("\n1. Escaneando directorios y analizando archivos petrofísicos...")
        detailed, summary = scan_wells_directory(input_path)
        
        print(f"   -> Pozos procesados: {len(summary)}")
        print(f"   -> Total de archivos catalogados: {len(detailed)}")

        print("\n2. Generando reporte en Excel con formato...")
        export_to_excel(detailed, summary, output_file)
        
        print("\n¡Proceso completado con éxito! Revisa el archivo 'Inventario_Pozos_VSM.xlsx' generado.")

    except Exception as e:
        print(f"\n[Error]: Ocurrió un problema durante la ejecución: {e}")

if __name__ == "__main__":
    main()