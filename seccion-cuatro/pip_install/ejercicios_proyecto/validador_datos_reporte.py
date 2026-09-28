"""Escribe una función que valide un CSV completo: verifica que no hay campos vacíos, que los numéricos son válidos y que las fechas tienen formato correcto. Genera un reporte de calidad."""

import csv
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent / "csv" / "datos_sucios.csv"
BASE.parent.mkdir(parents=True, exist_ok=True)

# Generar CSV con problemas
with open(BASE, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["fecha", "producto", "cantidad", "precio"])
    w.writerow(["2024-01-15", "Laptop", "2", "1299.99"])  # OK
    w.writerow(["2024-01-15", "", "1", "449.00"])          # producto vacío
    w.writerow(["15/01/2024", "Teclado", "3", "89.99"])    # fecha mal
    w.writerow(["2024-01-16", "Monitor", "abc", "399.00"]) # cantidad inválida
    w.writerow(["2024-01-16", "Ratón", "5", "N/A"])        # precio inválido
    w.writerow(["2024-01-16", "Cable", "10", "9.99"])      # OK

def validar_fila(fila):
    """Devuelve la lista de errores de la fila (vacía si está bien).
    Comprueba: producto no vacío · fecha con formato YYYY-MM-DD ·
    cantidad entera · precio decimal.
    Pista: datetime.strptime(texto, "%Y-%m-%d") lanza ValueError si no encaja."""
    
    errores = []
    
    if not fila.get("producto", "").strip():
        errores.append("Producto vacío")
    
    try:
        datetime.strptime(fila["fecha"], "Y%-%m-%d")
    except ValueError:
        errores.append(f"Fecha inválida: {fila['fecha']}")
    
    try:
        int(fila["cantidad"])
    except ValueError:
        errores.append(f"Cantidad inválida: {fila['cantidad']}")
    
    try:
        float(fila["precio"])
    except ValueError:
        errores.append(f"Precio inválido: {fila['precio']}")

    return errores

# No toques: el arnés que genera el reporte
with open(BASE, "r", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

print("REPORTE DE CALIDAD DE DATOS")
print("=" * 40)
total_errores = 0
filas_ok = 0
for i, fila in enumerate(filas, 2):
    errores = validar_fila(fila)
    if errores:
        total_errores += len(errores)
        print(f"  Fila {i}: {errores}")
    else:
        filas_ok += 1

print(f"\nFilas válidas: {filas_ok}/{len(filas)}")
print(f"Total errores: {total_errores}")