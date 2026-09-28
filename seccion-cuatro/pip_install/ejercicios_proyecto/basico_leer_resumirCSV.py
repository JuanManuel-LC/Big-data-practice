"""Lee el CSV de ventas, filtra las ventas de electrónica y calcula el total facturado en esa categoría. Escribe el resultado como JSON."""

import csv
import json
from pathlib import Path

archivo_ventas = Path(__file__).parent / "csv" /"ventas.csv"
archivo_ventas.parent.mkdir(parents=True, exist_ok=True)

input_categoria = input("Introduzca la categoria ('electrónica', 'ropa'): ").lower().strip()

# Generar CSV de prueba (no tocar)
with open(archivo_ventas, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["producto", "categoria", "precio"])
    w.writerow(["Laptop", "electrónica", "1299.99"])
    w.writerow(["Camiseta", "ropa", "24.99"])
    w.writerow(["Monitor", "electrónica", "449.00"])
    w.writerow(["Pantalón", "ropa", "59.99"])
    w.writerow(["Teclado", "electrónica", "89.99"])

def leer_ventas(ruta):
    """Lee el CSV y devuelve la lista de ventas (una por fila)."""
    with open(ruta, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))                       # Pista: list(csv.DictReader(f))

def filtrar_categoria(ventas, categoria):
    """Devuelve solo las ventas de esa categoría."""
    # Pista: con DictReader cada venta es un DICCIONARIO, así que se
    #        accede por nombre: v["categoria"]. Si usas csv.reader en
    #        vez de DictReader, cada fila es una lista y v["categoria"]
    #        falla con "list indices must be integers".
    return [v for v in ventas if v["categoria"] == categoria]

def calcular_total(ventas):
    """Suma los precios. Ojo: DictReader devuelve TEXTO."""
    # Pista: sum() necesita números y v["precio"] es texto -> float(...)
    return sum(float(v["precio"]) for v in ventas)

# No toques: el arnés del pipeline
categoria = filtrar_categoria(leer_ventas(archivo_ventas), input_categoria)
print(f"[CHECK] variable categoria es: {categoria}")
total = calcular_total(categoria)
resultado = {"categoria": input_categoria, "num_productos": len(categoria), "total": round(total, 2)}
with open("resultado.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=2, ensure_ascii=False)

print(f"{input_categoria}: {len(categoria)} productos, {total:.2f}€ total")
with open("resultado.json", "r", encoding="utf-8") as f:
    print(f.read())