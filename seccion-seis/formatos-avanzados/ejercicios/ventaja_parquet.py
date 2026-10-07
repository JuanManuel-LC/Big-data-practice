"""La tabla 'pedidos' tiene 10 columnas: id, fecha, cliente, producto, importe, pais, metodo_pago, direccion, email, notas. Para cada pregunta, escribe SOLO las columnas imprescindibles."""

# La tabla "pedidos" está en Parquet con estas columnas:
#
#   id · fecha · cliente · producto · importe · pais · metodo_pago · direccion · email · notas
#
# Para cada pregunta, escribe la lista de columnas que hay que leer.
# Sólo las imprescindibles: cada columna de más es tiempo de más.

consultas = {
    "Total facturado por país":           ["pais", "importe"],
    "Cuántos pedidos por método de pago": ["metodo_pago"],
    "Ticket medio por mes":               ["fecha", "importe"],
    "Los 10 clientes que más gastan":     ["cliente", "importe"],
}

# --- No toques: la comprobación.
#     La clave va del revés para que no se lea de un vistazo.
#     El orden en que escribas las columnas da igual. ---
CLAVE = {
    "Total facturado por país":           "etropmi,siap",
    "Cuántos pedidos por método de pago": "ogap_odotem",
    "Ticket medio por mes":               "etropmi,ahcef",
    "Los 10 clientes que más gastan":     "etropmi,etneilc",
}
aciertos = 0
for pregunta, clave in CLAVE.items():
    buenas = set(clave[::-1].split(","))
    mias = set(consultas[pregunta])
    if mias == buenas:
        print(f"  OK    {pregunta}")
        aciertos += 1
    elif mias > buenas:
        print(f"  FALLO {pregunta}: lees columnas que no necesitas")
    else:
        print(f"  FALLO {pregunta}: te faltan columnas o no son ésas")
print(f"\nAciertos: {aciertos}/{len(CLAVE)}")
