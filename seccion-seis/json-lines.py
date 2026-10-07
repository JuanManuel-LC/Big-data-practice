import json

#JSON clasico (todo en un array)
# Problema: necesita cargar TODO en memoria

json_clasico = '[{"id":1, "nombre":Ana}, {"id":2, "nonbre":"Pedro"}]'
todos = json.loads(json_clasico)

# --- JSON Lines (un objeto por línea) ---
# Ventaja: puedes leer línea a línea
jsonl_contenido = """{"id":1,"nombre":"Ana"}
{"id":2,"nombre":"Pedro"}
{"id":3,"nombre":"Lucía"}
"""

# Leer línea a línea (eficiente en memoria)
for linea in jsonl_contenido.strip().split("\n"):
    registro = json.loads(linea)
    print(f"  Procesando: {registro['nombre']}")
    
# En un archivo real:
# with open('datos.jsonl') as f:
#     for linea in f:
#         registro = json.loads(linea)
#         procesar(registro)