# Funciones como argumentos (funciones de orden superior)
productos = ['laptop', 'a', 'monitor 4K', 'teclado mecanico']

# Ordenar por longitud de nombre
por_longitud = sorted(productos, key=len)
print(por_longitud)

# Ordenar registros por un campo
ventas = [
    {'producto': 'Laptop', 'importe': 1299},
    {'producto': 'Raton', 'importe': 30},
    {'producto': 'Monitor', 'importe': 449},
]

por_importe = sorted(ventas, key=lambda v: v['importe'], reverse=True)
for v in por_importe:
    print(f'    {v['producto']}: {v['importe']}e')

# max/min tambien aceptan key:
mas_caro = max(ventas, key=lambda v: v['importe'])
print(f'Mas caro: {mas_caro['producto']}')

