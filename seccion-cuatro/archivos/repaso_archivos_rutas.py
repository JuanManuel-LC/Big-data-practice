"""Repaso de archivos y rutas visto en esta seccion.

Ejecuta este archivo desde la carpeta `archivos` para crear una carpeta
`repaso_generado` con los ficheros usados en los ejemplos.
"""

import csv
import json
from pathlib import Path


# Path permite construir rutas que funcionan tanto en Windows como en Linux/macOS.
ruta_carpeta = Path("repaso_generado")
ruta_texto = ruta_carpeta / "productos.txt"
ruta_csv = ruta_carpeta / "ventas.csv"
ruta_csv_excel = ruta_carpeta / "ventas_excel.csv"
ruta_json = ruta_carpeta / "resumen.json"

# `parents=True` crea tambien las carpetas padre que falten.
# `exist_ok=True` evita un error si la carpeta ya existe.
ruta_carpeta.mkdir(parents=True, exist_ok=True)


# -----------------------------------------------------------------------------
# ARCHIVOS DE TEXTO
# -----------------------------------------------------------------------------

# `with` cierra el fichero automaticamente, incluso si ocurre un error.
# `w` crea el fichero o reemplaza su contenido. `encoding` indica la codificacion.
with open(ruta_texto, "w", encoding="utf-8") as archivo:
    archivo.write("producto,cantidad,precio\n")
    archivo.write("Laptop,3,1299.99\n")
    archivo.write("Monitor,2,449.00\n")

# `read()` obtiene todo el contenido como un unico texto.
with open(ruta_texto, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("--- Lectura completa del texto ---")
print(contenido, end="")

# Recorrer el fichero linea por linea evita cargarlo entero en memoria.
print("\n--- Lectura linea por linea ---")
with open(ruta_texto, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # `strip()` quita el salto de linea final y otros espacios de los extremos.
        print(linea.strip())

# `readlines()` devuelve una lista: una posicion por cada linea del fichero.
with open(ruta_texto, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

print(f"\nEl fichero de texto tiene {len(lineas)} lineas.")


# -----------------------------------------------------------------------------
# CSV NORMAL: COMAS COMO SEPARADOR Y PUNTO EN LOS DECIMALES
# -----------------------------------------------------------------------------

# `newline=""` evita lineas vacias extra al trabajar con csv, especialmente en Windows.
with open(ruta_csv, "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["fecha", "producto", "cantidad", "precio"])
    escritor.writerow(["2024-01-15", "Laptop", 2, 1299.99])
    escritor.writerow(["2024-01-16", "Monitor", 1, 449.00])

# DictReader usa la primera fila como nombres de columnas y devuelve diccionarios.
with open(ruta_csv, "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    ventas = list(lector)

print("\n--- CSV leido con DictReader ---")
for venta in ventas:
    # Los valores leidos de un CSV siempre son texto; por eso se convierten.
    total = int(venta["cantidad"]) * float(venta["precio"])
    print(f"{venta['producto']}: {total:.2f}")

# DictWriter hace el proceso inverso: escribe diccionarios en un CSV.
filas_resumen = [
    {"producto": "Laptop", "total": "2599.98"},
    {"producto": "Monitor", "total": "449.00"},
]
ruta_salida_csv = ruta_carpeta / "totales.csv"

with open(ruta_salida_csv, "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["producto", "total"])
    escritor.writeheader()
    escritor.writerows(filas_resumen)


# -----------------------------------------------------------------------------
# CSV EXPORTADO DESDE EXCEL EN ESPANOL
# -----------------------------------------------------------------------------

# En este formato es habitual usar ; como separador y , para los decimales.
# `utf-8-sig` escribe/lee correctamente la marca que puede incluir Excel al inicio.
with open(ruta_csv_excel, "w", encoding="utf-8-sig", newline="") as archivo:
    archivo.write("producto;cantidad;precio\n")
    archivo.write("Laptop;3;1299,99\n")
    archivo.write("Monitor;2;449,00\n")

print("\n--- CSV de Excel en espanol ---")
with open(ruta_csv_excel, "r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo, delimiter=";")
    for fila in lector:
        # Antes de convertir a float, la coma decimal debe convertirse en punto.
        precio = float(fila["precio"].replace(",", "."))
        print(f"{fila['producto']}: {precio:.2f}")


# -----------------------------------------------------------------------------
# JSON
# -----------------------------------------------------------------------------

resumen = {
    "fecha": "2024-01-16",
    "total_ventas": 3048.98,
    "num_transacciones": 3,
    "productos_top": ["Laptop", "Monitor"],
    "meta_alcanzada": True,
}

# `dump()` guarda un diccionario Python en un fichero JSON.
# `indent=2` lo hace legible y `ensure_ascii=False` conserva acentos.
with open(ruta_json, "w", encoding="utf-8") as archivo:
    json.dump(resumen, archivo, indent=2, ensure_ascii=False)

# `load()` recupera el contenido JSON como un diccionario Python.
with open(ruta_json, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("\n--- JSON cargado ---")
print(f"Fecha: {datos['fecha']}")
print(f"Total: {datos['total_ventas']}")


# -----------------------------------------------------------------------------
# COMPROBACIONES Y LISTADO DE RUTAS
# -----------------------------------------------------------------------------

if ruta_csv.exists():
    print(f"\n{ruta_csv.name} existe y mide {ruta_csv.stat().st_size} bytes.")
else:
    print(f"\n{ruta_csv.name} no existe.")

# `glob("*.csv")` busca los archivos CSV dentro de la carpeta indicada.
print("CSV encontrados:")
for archivo_csv in ruta_carpeta.glob("*.csv"):
    print(f"- {archivo_csv.name}")
