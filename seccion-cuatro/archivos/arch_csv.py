import csv

# Creamos un CSV  de ejemplo                    newline=Evita que windows añada lineas bacias entre filas
with open("ventas.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["fecha", "producto", "cantidad", "precio"])
    writer.writerow(["2024-01-15", "Laptop Pro", 2, 1299.99])
    writer.writerow(["2024-01-15", "Monitor 4K", 1, 449.00])
    writer.writerow(["2024-01-16", "Teclado mecánico", 5, 89.99])
    writer.writerow(["2024-01-16", "Ratón argónomico", 3, 59.99])

# Leemos el CSV como lista de diccionarios (DictReader)
with open("ventas.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # print(f"Reader: {reader}")
    ventas = list(reader)
    # print(f"Ventas: {ventas}")
    
for venta in ventas:
    total = int(venta["cantidad"]) * float(venta["precio"])
    print(f"{venta["fecha"]} | {venta["producto"]:20s} | {total:.2f}")
    
    
print()
print("Inversa")
# La libreria CSV tambien tiene la funcion contraria, pasar de una lista de diccionarios a un CSV (DictWriter)
filas = [
    {"producto": "Laptop", "total": "3899.97" },
    {"producto": "Monitor", "total": "1995.00" }
]

with open("salida.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["producto", "total"])
    writer.writeheader() #Escriber la fila de nombre (Encabezados)
    writer.writerows(filas)
    
with open("salida.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ventas2 = list(reader)
    print(ventas2)