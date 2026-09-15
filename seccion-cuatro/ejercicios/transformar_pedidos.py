# Ejercicio: transformar_pedidos.py
# Transforma una lista de pedidos aplicando descuentos y creando un resumen.

pedidos = [
    {"producto": "Camiseta", "cantidad": 3, "precio_unitario": 20.0},
    {"producto": "Pantalón", "cantidad": 1, "precio_unitario": 55.0},
    {"producto": "Zapatillas", "cantidad": 2, "precio_unitario": 80.0},
    {"producto": "Gorra", "cantidad": 4, "precio_unitario": 15.0},
]

# List comprehension que añade a cada pedido un campo "subtotal" (cantidad * precio_unitario)
# Pista: {**p, "subtotal": p["cantidad"] * p["precio_unitario"]}  -> {**p} copia el dict y luego
# añade/actualiza el campo "subtotal" sin modificar el original.
con_subtotal = [{**p, "subtotal": p["cantidad"] * p["precio_unitario"]} for p in pedidos]

# Pedidos con descuento: los que tengan subtotal >= 100€ se quedan, el resto se descarta.
# Pista: [p for p in con_subtotal if p["subtotal"] >= 100]
pedidos_con_descuento = [p for p in con_subtotal if p["subtotal"] >= 100]

# Total general sumando todos los subtotales. Pista: sum(p["subtotal"] for p in ...)
total_general = sum(p["subtotal"] for p in con_subtotal)

# No toques estas líneas: son las que muestran el resultado
print("PEDIDOS CON SUBTOTAL:")   # dos decimales en subtotal
for p in con_subtotal:
    print(f"  {p['producto']}: {p['cantidad']} ud x {p['precio_unitario']:.2f}€ = {p['subtotal']:.2f}€")
print("")
print("PEDIDOS QUE SE LLEVAN DESCUENTO (>=100€):")
for p in pedidos_con_descuento:
    print(f"  {p['producto']}: {p['subtotal']:.2f}€")
print("")
print(f"TOTAL FACTURADO: {total_general:.2f}€")
