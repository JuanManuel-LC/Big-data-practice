# ── Setup: recrea ventas.parquet si abres este ejercicio directo ──
import os as _os, csv as _csv, random as _random
import pandas as _pd
if not _os.path.exists("ventas.parquet"):
    _random.seed(123)
    _rows = [(_i+1, _random.choice(["Laptop","Mouse","Teclado","Monitor","Webcam"]), round(_random.uniform(10,500),2), _random.choice(["Madrid","Barcelona","Valencia"]), f"2026-{_random.randint(1,12):02d}-{_random.randint(1,28):02d}") for _i in range(50_000)]
    with open("ventas.csv","w",newline="") as _f:
        _w = _csv.writer(_f); _w.writerow(["id","producto","importe","ciudad","fecha"]); _w.writerows(_rows)
    _pd.read_csv("ventas.csv").to_parquet("ventas.parquet")
# ─────────────────────────────────────────────────────────────────

import pyarrow.parquet as pq

metadata = pq.read_metadata("ventas.parquet")

filas = metadata.num_rows       # <- Pista: metadata.num_rows
columnas = metadata.num_columns     # <- Pista: metadata.num_columns

# No toques
print("=== Información del archivo Parquet ===")
print(f"Filas: {filas:,}")
print(f"Columnas: {columnas}")
print(f"Row groups: {metadata.num_row_groups}")

schema = pq.read_schema("ventas.parquet")
print("\n=== Esquema (tipos de cada columna) ===")
for i in range(len(schema)):
    print(f"  {schema.field(i).name:15} → {schema.field(i).type}")