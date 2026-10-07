import pyarrow.parquet as pq
from pathlib import Path
import os

# Path del archivo --- se debio ejecutar el archivo csv_parquet.py
file = Path(__file__).parent / "files" / "pedidos.parquet"

# --- Leer SOLO una columna de Parquet (column pruning) ---
# En CSV tendrias que leer TODO el archivo

tabla_parcial = pq.read_table(file, columns=["ciudad", "precio"])
print(f"Columnas leidas: {tabla_parcial.column_names}")
print(f"Filas: {len(tabla_parcial)}")
#print(f"Algunas filas {tabla_parcial[:20]}")

# Convertir a Python para trabajar
ciudades = tabla_parcial.column("ciudad").to_pylist()
precios = tabla_parcial.column("precio").to_pylist()


# Caulcular total por ciudad
ventas_ciudad = {}
for ciudad, precio in zip(ciudades, precios):
    ventas_ciudad[ciudad] = ventas_ciudad.get(ciudad, 0) + precio
    
print("\nVentas por ciudad")
for ciudad, total in sorted(ventas_ciudad.items(), key=lambda x: -x[1]):
    print(f" {ciudad:12} ---> {total:>12,.2f}€")
    
# --- Ver metadatos del archivo ---
metadata = pq.read_metadata(file)
print(f"\nMetadatos Parquet:")
print(f"  Filas totales: {metadata.num_rows:,}")
print(f"  Columnas: {metadata.num_columns}")
print(f"  Row groups: {metadata.num_row_groups}")