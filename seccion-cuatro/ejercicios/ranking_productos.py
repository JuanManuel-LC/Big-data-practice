# Ejercicio: ranking_productos.py
# Ordena una lista de productos por precio y saca el top 3.

productos = [
    {"nombre": "Laptop", "precio": 1299},
    {"nombre": "Ratón", "precio": 19},
    {"nombre": "Monitor", "precio": 399},
    {"nombre": "Teclado", "precio": 89},
    {"nombre": "Webcam", "precio": 55},
    {"nombre": "Auriculares", "precio": 120},
    {"nombre": "Micrófono", "precio": 210},
]

# Ordena los productos por precio de MAYOR a menor (usa sorted con key= y reverse)
# Pista: sorted(productos, key=lambda p: ..., reverse=True)
# La "key" le dice a sorted con qué campo comparar: usa "precio".
ranking = sorted(productos, key= lambda p: p["precio"], reverse=True)

# Saca los 3 productos más caros (los tres primeros del ranking)
top3 = ranking[:3]

# Saca el producto más barato. Pista: min(productos, key=...)
mas_barato = min(productos, key= lambda p: p["precio"])

# No toques estas líneas: son las que muestran el resultado
print("RANKING DE PRECIOS (más caro primero):")
for i, prod in enumerate(ranking, start=1):
    print(f"  {i}. {prod['nombre']}: {prod['precio']}€")
print("")
print("TOP 3 MÁS CAROS:")
for prod in top3:
    print(f"  {prod['nombre']}: {prod['precio']}€")
print("")
print(f"El más barato es {mas_barato['nombre']} ({mas_barato['precio']}€)")
