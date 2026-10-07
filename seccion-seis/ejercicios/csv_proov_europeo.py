import csv
import io

# El CSV que manda el proveedor europeo. Fíjate en dos cosas: cómo separa
# las columnas y cómo escribe los decimales.
csv_texto = """producto;precio;cantidad
Jamón ibérico;45,90;10
Queso manchego;12,50;25
Aceite de oliva;8,99;50
Vino Rioja;15,00;30
"""

SEPARADOR = ";"      # <- ¿de verdad este CSV separa por comas?

reader = csv.DictReader(io.StringIO(csv_texto), delimiter=SEPARADOR)

# No toques: enseña qué columnas ha entendido el lector con ese separador
print("Columnas detectadas:", reader.fieldnames)
print("")

total = 0
registros = []
for fila in reader:
    precio = float(fila["precio"].replace(",", "."))     # <- pasa fila["precio"] a número. Ojo: viene como "45,90"
    cantidad = int(fila["cantidad"])     # <- pasa fila["cantidad"] a entero
    subtotal = precio * cantidad
    total += subtotal
    registros.append({"producto": fila.get("producto", "???"), "subtotal": subtotal})

# No toques
for r in registros:
    print(f"  {r['producto']:20} → {r['subtotal']:.2f}€")
print(f"\nTOTAL: {total:.2f}€")