import json
import csv
from datetime import date, timedelta
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent / "files"
BASE.mkdir(parents=True, exist_ok=True)

# === EXTRACT: leer datos del origen ===
# (simulamos el JSON de pedidos del día)
pedidos_raw = [
    {"id": 1, "producto": "Mouse", "precio": 25.0, "cantidad": 2, "estado": "completado"},
    {"id": 2, "producto": "Teclado", "precio": 60.0, "cantidad": 1, "estado": "completado"},
    {"id": 3, "producto": "Mouse", "precio": 25.0, "cantidad": 1, "estado": "cancelado"},
    {"id": 4, "producto": "Monitor", "precio": 350.0, "cantidad": 1, "estado": "completado"},
    {"id": 5, "producto": "Teclado", "precio": 60.0, "cantidad": 3, "estado": "completado"},
    {"id": 6, "producto": "Webcam", "precio": 80.0, "cantidad": 1, "estado": "completado"},
]
print(f"EXTRACT: {len(pedidos_raw)} pedidos leídos")

# TRANSFORM: limpiar + enriquecer + agregar ===
# 1. Filtrar: solo pedidos completados
pedidos_validos = [p for p in pedidos_raw if p["estado"] == "completado"]
print(f"TRANSFORM: {len(pedidos_validos)} pedidos validos (sin cancelados)")

# 2. Enrrqiuecer: calcular importe total
for p in pedidos_validos:
    p["importe_total"] = p["cantidad"] * p["precio"]

# 3. Agregar: sumar por producto
ventas_por_producto = defaultdict(lambda: {"unidades": 0, "importe": 0})
for p in pedidos_validos:
    ventas_por_producto[p["producto"]]["unidades"] += p["cantidad"]
    ventas_por_producto[p["producto"]]["importe"] += p["importe_total"]
    
# LOAD: Guardar resultado 
hoy = date.today().isoformat()
with open(f"{BASE}/reporte_ventas_{hoy}.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["producto", "unidades_vendidas", "importe_total", "fecha"])
    for prod, datos in sorted(ventas_por_producto.items(), key=lambda x: -x[1]["importe"]):
        writer.writerow([prod, datos["unidades"], datos["importe"], hoy])
        
print(f"LOAD: reporte guardado como reporte_ventas_{hoy}.csv")
print("\n=== RESULTADO (lo que ve el equipo de compras) ===")
for prod, datos in sorted(ventas_por_producto.items(), key=lambda x: -x[1]["importe"]):
    print(f"  {prod:10} | {datos['unidades']} uds | {datos['importe']:>8.2f}€")