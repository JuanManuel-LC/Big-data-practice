# ── Setup: recrea ventas.csv y ventas.parquet si abres este ejercicio directo ──
from pathlib import Path

BASE = Path(__file__).parent / "files"
csv_file = BASE / "ventas.csv"
parquet_file = BASE / "ventas.parquet"
BASE.mkdir(parents=True, exist_ok=True)

import os as _os, csv as _csv, random as _random
import pandas as pd
if not _os.path.exists(csv_file) or not _os.path.exists(parquet_file):
    _random.seed(123)
    _rows = [(_i+1, _random.choice(["Laptop","Mouse","Teclado","Monitor","Webcam"]), round(_random.uniform(10,500),2), _random.choice(["Madrid","Barcelona","Valencia"]), f"2026-{_random.randint(1,12):02d}-{_random.randint(1,28):02d}") for _i in range(50_000)]
    with open(csv_file,"w",newline="") as _f:
        _w = _csv.writer(_f); _w.writerow(["id","producto","importe","ciudad","fecha"]); _w.writerows(_rows)
    pd.read_csv(csv_file).to_parquet(parquet_file)
# ─────────────────────────────────────────────────────────────────

import csv
import time

# --- Método 1: CSV (tiene que leer TODO el fichero) ---
# perf_counter es el cronómetro bueno: no le afectan los cambios de hora.
inicio = time.perf_counter()
total_csv = 0
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        total_csv += float(fila["importe"])
tiempo_csv = time.perf_counter() - inicio

# --- Método 2: Parquet (lee SOLO la columna "importe") ---
inicio = time.perf_counter()
# <- lee solo "importe" del Parquet y súmalo
#    Pista: pd.read_parquet(ruta, columns=[...]) y luego .sum()
df = pd.read_parquet(parquet_file, columns=["importe"])
total_pq = df["importe"].sum()       

tiempo_parquet = time.perf_counter() - inicio

# No toques
mismo = abs(total_csv - total_pq) < 0.01
# Los milisegundos NO se imprimen, y es a propósito: varían de una ejecución a
# otra en el mismo ordenador, así que compararlos con un texto fijo suspendería
# a quien lo hace bien. Lo que se comprueba es el veredicto: que sale el mismo
# total y que leer una sola columna gana.
print(f"CSV total:     {total_csv:>13,.2f}€")
print(f"Parquet total: {total_pq:>13,.2f}€")
print(f"Mismo resultado: {mismo}")
print(f"Parquet más rápido: {tiempo_parquet < tiempo_csv}")