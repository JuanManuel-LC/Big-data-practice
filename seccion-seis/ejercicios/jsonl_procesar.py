import json

# Un JSONL: un objeto JSON por línea. En producción serían millones.
jsonl_data = """{"tipo":"compra","importe":50.0,"usuario":"ana"}
{"tipo":"login","usuario":"pedro"}
{"tipo":"compra","importe":120.5,"usuario":"lucia"}
{"tipo":"compra","importe":30.0,"usuario":"ana"}
{"tipo":"logout","usuario":"pedro"}
{"tipo":"compra","importe":200.0,"usuario":"carlos"}
{"tipo":"login","usuario":"ana"}
{"tipo":"compra","importe":15.99,"usuario":"lucia"}
{"tipo":"compra","usuario":"marta"}
{"tipo":"error","codigo":500}
"""

total_eventos = 0
total_compras = 0
compras_con_importe = 0
suma_importes = 0
usuarios_unicos = set()    # un conjunto: no admite repetidos

for linea in jsonl_data.strip().split("\n"):
    evento = json.loads(linea)                  # <- convierte la línea en diccionario. Pista: json.loads
    total_eventos += 1

    if evento.get("tipo") == "compra":
        total_compras += 1
        suma_importes += evento.get("importe", 0)
        if "importe" in evento:
            compras_con_importe += 1
        # <- suma aquí el importe, sin que reviente si el evento no lo trae
        # <- cuenta aparte cuántas compras SÍ traen importe

    if "usuario" in evento:
        usuarios_unicos.add(evento["usuario"])
    # <- si el evento tiene "usuario", guárdalo. Pista: usuarios_unicos.add(...)

# No toques
print(f"Total eventos: {total_eventos}")
print(f"Compras: {total_compras}")
print(f"Facturación: {suma_importes:.2f}€")
print(f"Usuarios únicos: {len(usuarios_unicos)}")
print(f"Ticket medio: {suma_importes / total_compras:.2f}€   (sobre las {total_compras} compras)")
print(f"Ticket medio: {suma_importes / compras_con_importe:.2f}€   (sólo las {compras_con_importe} con importe)")