"""Genera un reporte JSON con el desglose por categoría: número de productos, total vendido y porcentaje sobre el total general."""

import csv
import json
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent / "csv" / "ventas_cat.csv"
BASE.parent.mkdir(parents=True, exist_ok=True)

# Generar datos
with open(BASE, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["producto", "categoria", "total"])
    w.writerow(["Laptop", "electrónica", "1299.99"])
    w.writerow(["Camiseta", "ropa", "24.99"])
    w.writerow(["Monitor", "electrónica", "449.00"])
    w.writerow(["Pantalón", "ropa", "59.99"])
    w.writerow(["Teclado", "electrónica", "89.99"])
    w.writerow(["Zapatillas", "calzado", "129.99"])
    w.writerow(["Botas", "calzado", "189.00"])

with open(BASE, "r", encoding="utf-8") as f:
    ventas = list(csv.DictReader(f))

def agrupar(ventas):
    """cat -> {"productos": cuántos, "total": suma}."""
    agrupado = defaultdict(lambda: {"productos": 0, "total": 0.0})

    for v in ventas:
        cat = v["categoria"]
        agrupado[cat]["productos"] += 1
        agrupado[cat]["total"] += float(v["total"])
        
    return dict(agrupado)

def construir_reporte(agrupado):
    """Añade a cada categoría su "porcentaje" sobre el total general,
    redondeado a 1 decimal. Los totales, redondeados a 2."""
    
    total_general = sum(datos["total"] for datos in agrupado.values())
    
    for categoria, datos in agrupado.items():
        datos["total"] = round(datos["total"], 2)
        datos["porcentaje"] = round(
            datos["total"] / total_general * 100,
            1
        )
    
    return agrupado

# No toques
with open("reporte_categorias.json", "w", encoding="utf-8") as f:
    json.dump(construir_reporte(agrupar(ventas)), f, indent=2, ensure_ascii=False)

print(json.dumps(construir_reporte(agrupar(ventas)), indent=2, ensure_ascii=False))