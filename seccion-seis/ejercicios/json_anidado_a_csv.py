import json
import csv

productos_json = [
    {"nombre": "MacBook Pro", "precio": 2499, "specs": {"ram": 16, "disco": 512}, "tags": ["portátil", "pro"]},
    {"nombre": "iPad Air", "precio": 699, "specs": {"ram": 8, "disco": 256}, "tags": ["tablet"]},
    {"nombre": "AirPods Pro", "precio": 279, "specs": {"ram": None, "disco": None}, "tags": ["audio", "wireless"]},
    {"nombre": "Funda iPad", "precio": 59, "specs": {"ram": None, "disco": 0}, "tags": []},
]

# Aplana cada producto y escríbelo como fila del CSV.
# Ojo: el CSV no tiene "null". Donde no haya dato, escribe "".
# Y más ojo aún: un 0 SÍ es un dato. No lo confundas con "no hay dato".
# Pista: "is not None" distingue los dos; "if x" los confunde.
with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["nombre", "precio", "ram_gb", "disco_gb", "tag_principal"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()

    for prod in productos_json:
        fila = {
            "nombre": prod["nombre"],
            "precio": prod["precio"],
            "ram_gb": prod["specs"]["ram"] if prod["specs"]["ram"] is not None else "",
            "disco_gb": prod["specs"]["disco"] if prod["specs"]["disco"] is not None else "",
            "tag_principal": prod["tags"][0] if prod["tags"] else "",
        }
        writer.writerow(fila)

# No toques: vuelve a abrir el fichero para ver qué has escrito de verdad
with open("productos.csv", "r", encoding="utf-8") as f:
    print(f.read(), end="")