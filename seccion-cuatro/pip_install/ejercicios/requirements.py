"""Genera un requirements.txt con las dependencias del proyecto. El formato de cada línea es: paquete==version  # comentario (ojo: dos espacios antes de la almohadilla)."""

from pathlib import Path

archivo = Path(__file__).parent / "requirements.txt"

# Define las dependencias de tu proyecto
dependencias = [
    ("pandas", "2.1.4", "Manipulación de datos tabulares"),
    ("requests", "2.31.0", "Llamadas HTTP a APIs"),
    ("python-dotenv", "1.0.0", "Variables de entorno desde .env"),
    ("pytest", "7.4.3", "Testing automatizado"),
]

def linea_requirement(nombre, version, descripcion):
    """Devuelve la línea del requirements.txt, con salto al final.
    Formato: paquete==version + DOS espacios + # descripción +\n"""
    return f"{nombre}=={version}  # {descripcion}\n"

# No toques: genera el fichero y lo muestra
with open(archivo, "w") as f:
    f.write("# Dependencias del proyecto pipeline-ventas\n")
    for nombre, version, descripcion in dependencias:
        f.write(linea_requirement(nombre, version, descripcion))

with open(archivo, "r") as f:
    print(f.read())
