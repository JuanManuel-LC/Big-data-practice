"""Genera un CSV con 50.000 registros de ventas, conviértelo a Parquet con pandas y muestra la diferencia de tamaño."""

import csv
import os
import random
import pandas as pd
from pathlib import Path

folder = Path(__file__).parent / 'files'
csv_file = folder / "ventas.csv"
parquet_file = folder / "ventas.parquet"
folder.mkdir(parents=True, exist_ok=True)

random.seed(123)

# Generar CSV con 50.000 ventas
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "producto", "importe", "ciudad", "fecha"])
    for i in range(50_000):
        writer.writerow([
            i+1,
            random.choice(["Laptop", "Mouse", "Teclado", "Monitor", "Webcam"]),
            round(random.uniform(10, 500), 2),
            random.choice(["Madrid", "Barcelona", "Valencia"]),
            f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
        ])

df = pd.read_csv(csv_file)     # <- lee el CSV con pandas. Pista: pd.read_csv("ventas.csv")
# <- y guárdalo como Parquet. Pista: df.to_parquet("ventas.parquet")
parquet = df.to_parquet(parquet_file)

# No toques: compara los dos ficheros
tam_csv = os.path.getsize(csv_file) / 1024
tam_pq = os.path.getsize(parquet_file) / 1024 if os.path.exists(parquet_file) else 0
# En MB y con UN decimal a propósito: el tamaño exacto del Parquet depende de
# la versión de la librería que lo escribe, y así la comparación aguanta esa
# variación en vez de suspenderte por unos KB de diferencia.
print(f"CSV:     {tam_csv/1024:.1f} MB")
print(f"Parquet: {tam_pq/1024:.1f} MB")   # si sale 0.0, el fichero aún no existe
print(f"Parquet ocupa menos de la mitad: {0 < tam_pq < tam_csv / 2}")