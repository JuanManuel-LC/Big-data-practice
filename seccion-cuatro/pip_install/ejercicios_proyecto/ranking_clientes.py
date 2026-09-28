"""El CEO quiere saber quiénes son los top 3 clientes que más han gastado. Lee las ventas, agrupa por cliente, calcula el gasto total de cada uno y muestra el ranking.

Pista para ordenar: sorted(gastos.items(), key=lambda x: x[1], reverse=True). gastos.items() te da pares (cliente, gasto). lambda x: x[1] es una función de usar y tirar que, dado un par, devuelve su segundo elemento — el gasto. Y reverse=True los pone de mayor a menor. Es la primera vez que ves lambda: una función sin nombre, escrita en la misma línea donde se usa.

"""

import csv
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent / "csv" / "ventas_clientes.csv"
BASE.parent.mkdir(parents=True, exist_ok=True)

# Generar datos (no tocar)
with open(BASE, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["cliente", "producto", "total"])
    w.writerow(["Ana García", "Laptop", "1299.99"])
    w.writerow(["Luis Pérez", "Monitor", "449.00"])
    w.writerow(["Ana García", "Teclado", "89.99"])
    w.writerow(["María López", "Laptop", "1299.99"])
    w.writerow(["Luis Pérez", "Ratón", "49.99"])
    w.writerow(["Ana García", "Auriculares", "199.00"])
    w.writerow(["Pedro Ruiz", "Monitor", "449.00"])
    w.writerow(["María López", "Cable", "15.99"])

with open(BASE, "r", encoding="utf-8") as f:
    ventas = list(csv.DictReader(f))

def gasto_por_cliente(ventas):
    """Devuelve un diccionario cliente -> gasto total acumulado."""
    gastos = defaultdict(float)
    for v in ventas:
        gastos[v["cliente"]] += float(v["total"])
    return dict(gastos)   # <- de momento, todos a cero

def top_n(gastos, n):
    """Devuelve los n pares (cliente, gasto) con MÁS gasto, de mayor a menor."""
    return sorted(gastos.items(), key=lambda x: x[1], reverse=True)[:n]               # <- ahora mismo no ordena

# No toques: el arnés que prueba tus funciones
ranking = top_n(gasto_por_cliente(ventas), 3)
print("TOP 3 CLIENTES:")
for i, (cliente, gasto) in enumerate(ranking, 1):
    print(f"  {i}. {cliente}: {gasto:.2f}€")