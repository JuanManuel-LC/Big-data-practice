#Convertir JSON semiestructurado --> tabla estructurada
import json

#Datos de una API (semiestructurado)
respuesta_api = [
    {"id": 1, "nombre": "Ana", "direccion": {"ciudad": "Madrid", "cp": "28001"}},
    {"id": 2, "nombre": "Pedro", "direccion": {"ciudad": "Barcelona", "cp": "08001"}},
    {"id": 3, "nombre": "Lucia", "direccion": None}
]


#Aplanar: extraer campos anidades a nivel plao
tabla = []

for registro in respuesta_api:
    fila = {
        "id": registro["id"],
        "nombre": registro["nombre"],
        "ciudad": registro["direccion"]["ciudad"] if registro["direccion"] else None,
        "cp": registro["direccion"]["cp"] if registro["direccion"] else None
    }
    tabla.append(fila)

for fila in tabla:
    print(fila)