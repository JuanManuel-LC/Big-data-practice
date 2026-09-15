from pathlib import Path

# Pathlib funciona funciona igual en Windows y en Mac
ruta_datos = Path("data") / "raw" / "ventas.cvs"
print(ruta_datos) # data/raw/ventas.csv (Mac) o data\raw\ventas.csv (Win)

# Crear directorios si no existen
ruta_datos.parent.mkdir(parents=True, exist_ok=True)


# Verificar si existe
if ruta_datos.exists():
    print(f"Tamaño: {ruta_datos.stat().st_size} bytes")
    # Esto es para imprimir el tamaño del archivo
else:
    print("El archivo no existe")


# Listar archivos de un directorio
for archivo in Path("data").glob("*.csv"):
    print(f"Encontrado: {archivo.name}")