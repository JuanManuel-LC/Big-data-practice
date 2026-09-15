# Ejercicio: inventario_actualizado.py
# Actualiza un inventario (dict) con las nuevas entregas y detecta agotados.

# Inventario actual: producto -> stock disponible
inventario = {
    "laptop": 4,
    "monitor": 7,
    "teclado": 12,
    "ratón": 0,
    "webcam": 3,
}

# Nuevas entregas que acaban de llegar
# (el ratón sigue sin recibir unidades, así que quedará agotado)
entregas = {
    "monitor": 5,
    "teclado": 10,
    "impresora": 2,
    "laptop": 3,
}

# Suma las entregas al inventario.
# Pista: recorre entregas.items() y haz inventario[prod] = inventario.get(prod, 0) + cantidad
# El .get(prod, 0) sirve para productos nuevos que aún no están en el inventario (como "impresora").
for prod, cantidad in entregas.items():
    inventario[prod] = inventario.get(prod, 0) + cantidad

# Lista de productos agotados (stock == 0). Pista: [prod for prod, stock in inventario.items() if stock == 0]
agotados = [prod for prod, stock in inventario.items() if stock == 0]

# No toques estas líneas: son las que muestran el resultado
print("INVENTARIO ACTUALIZADO:")
for prod, stock in sorted(inventario.items()):
    print(f"  {prod}: {stock} unidades")
print("")
if agotados:
    print("AGOTADOS:", ", ".join(agotados))
else:
    print("No hay productos agotados.")
