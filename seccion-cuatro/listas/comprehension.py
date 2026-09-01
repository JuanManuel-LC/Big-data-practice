# Las listas comprehensions son la forma pythónica de crear listas a partir de otras listas.
precios_sin_iva = [100, 250, 49.99, 899, 1299.50]
print(f"Precios sin IVA: {precios_sin_iva}")

# Calcular precios sin IVA (21%)
# Forma sin List ComprehensionS

precios_con_iva = []
for precios in precios_sin_iva:
    precios_con_iva.append(precios * 1.21)
    
print(f"Precios con IVA (Sencillo): {precios_con_iva}")

# Lo mismo pero con List Comprenhension (1 linea)
precios_con_iva2 = [precio * 1.21 for precio in precios_sin_iva]
print(f"Precion con IVA pero con list comprenhension: {precios_con_iva2}")

# Filtrar: solo precios mayores a 200
caros = [p for p in precios_con_iva2 if p > 200]
print(f"Productos caros (>200): {caros}")

# Transformar: redondear a 2 decimales
redondeados = [round(p, 2) for p in precios_con_iva2]
print(f'Precios redondeados: {redondeados}')