"""Practica 1: leer y escribir un CSV.

Completa solamente las lineas marcadas con TODO. Ejecuta este archivo desde la
carpeta `ejercicios`; al terminar debe crear `salida_practica.csv`.
"""

import csv
from pathlib import Path 

ruta_carpeta = Path("archivos_practica1")
ruta_csv_entrada = ruta_carpeta / "entrada_practica.csv"
ruta_csv_salida = ruta_carpeta / "salida_practica.csv"

# Creamos el directorio
ruta_carpeta.mkdir(parents=True, exist_ok=True)

# Estos datos ya estan preparados para que puedas centrarte en la lectura y escritura.
with open(ruta_csv_entrada, "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["producto", "cantidad", "precio"])
    escritor.writerow(["Laptop", "3", "1299.99"])
    escritor.writerow(["Monitor", "5", "399.00"])
    escritor.writerow(["Teclado", "20", "69.99"])



with open(ruta_csv_entrada, "r", encoding="utf-8", newline="") as archivo:
    reader = csv.DictReader(archivo)
    ventas = list(reader)
    
filas = []
for venta in ventas:
    venta["total"] = int(venta["cantidad"]) * float(venta["precio"])
    print(venta)
    filas.append(venta)



campos = ["producto", "cantidad", "precio", "total"]
with open(ruta_csv_salida, "w", encoding="utf-8", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    writer.writerows(filas)
    
    
# Recuerda usar `newline=""` y un csv.DictWriter.




# No modifiques este bloque: te permite comprobar el resultado.
print("--- salida_practica.csv ---")
with open("salida_practica.csv", "r", encoding="utf-8") as archivo:
    print(archivo.read(), end="")
