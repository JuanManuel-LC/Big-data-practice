productos = [
    {"nombre": "Laptop", "categoria": "electrónica", "precio": 1299},
    {"nombre": "Camiseta", "categoria": "ropa", "precio": 25},
    {"nombre": "Monitor", "categoria": "electrónica", "precio": 399},
    {"nombre": "Pantalón", "categoria": "ropa", "precio": 55},
    {"nombre": "Teclado", "categoria": "electrónica", "precio": 89},
    {"nombre": "Zapatos", "categoria": "ropa", "precio": 120},
]

por_categoria = {}

for producto in productos:
    cat = producto["categoria"]
    if cat not in por_categoria:
        por_categoria[cat] = []
    por_categoria[cat].append(producto)
    
for cat, prod in por_categoria.items():
    nombres= [p["nombre"] for p in prod]
    print(f"{cat}: {nombres}")