import csv

#utf-8-sig se come la marca invisible; delimiter le dice cuál es el separador de verdad
with open("ventas_excel.csv", "w", encoding="utf-8-sig", newline="") as f:
    f.write("producto;cantidad;precio\n")
    f.write("Laptop;3;1299,99\n")
    f.write("Monitor;2;449,00\n")
    
with open("ventas_excel.csv", "r", encoding="utf-8-sig", newline="") as f:
    lector = csv.DictReader(f, delimiter=";")
    for fila in lector:
        #El decima, de coma a punto, antes de convertirlo a numero
        precio = float(fila["precio"].replace(",", "."))
        print(f"{fila["producto"]}: {precio:.2f}€")