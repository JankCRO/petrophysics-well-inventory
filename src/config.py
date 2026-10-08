from pathlib import Path

# 1. Extensiones de registros petrofísicos principales
PETRO_EXTENSIONS = {'.las', '.lis', '.dlis'}

# 2. Extensiones de imágenes
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp'}

# 3. Nombres de subcarpetas clave que analizaremos en cada pozo
TARGET_SUBFOLDERS = ['DATA', 'DATA_EDIT', 'DATA_COMP', 'IMG', 'INF']

def get_file_category(extension: str) -> str:
    """
    Retorna la categoría del archivo según su extensión.
    """
    ext = extension.lower()
    if ext in PETRO_EXTENSIONS:
        return "Registro Petrofísico"
    elif ext == '.pdf':
        return "Documento PDF"
    elif ext in IMAGE_EXTENSIONS:
        return "Imagen"
    else:
        return "Otro"