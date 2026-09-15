import csv

# Crear el CSV de entrada (esto ya está hecho)
with open("entrada.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["producto", "cantidad", "precio"])
    writer.writerow(["Laptop", "3", "1299.99"])
    writer.writerow(["Monitor", "5", "399.00"])
    writer.writerow(["Teclado", "20", "69.99"])

# Leer y calcular el total de cada fila
with open("entrada.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    filas = []
    for row in reader:
        # DictReader devuelve TEXTO: hay que convertir antes de multiplicar.
        # Pista: f"{int(row['cantidad']) * float(row['precio']):.2f}"
        row["total"] = int(row['cantidad']) * float(row['precio'])
        filas.append(row)

# Escribir el CSV de salida con la columna total
with open("salida.csv", "w", encoding="utf-8", newline="") as f:
    campos = ["producto", "cantidad", "precio", "total"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(filas)  # <- escribe todas las filas. Pista: writer.writerows(filas)

# No toques: vuelve a abrir el fichero para ver qué has escrito
print("--- salida.csv ---")
with open("salida.csv", "r", encoding="utf-8") as f:
    print(f.read(), end="")
