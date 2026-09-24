# Lo que tu ya sabes hacer HOY (Python puro)
ventas = [
    {"producto": "Laptop", "categoria": "tech", "importe": 1299},
    {"producto": "Camiseta", "categoria": "ropa", "importe": 25},
    {"producto": "Monitor", "categoria": "tech", "importe": 449},
    {"producto": "Pantalon", "categoria": "ropa", "importe": 60},
]

# Estilo funcional (filter + transform con comprehension)
tech_grandes = [
    v['producto']
    for v in ventas
    if v['categoria'] == 'tech' and v['importe'] > 200
]

print(f'Productos caros: {tech_grandes}')

# En pandas seria:
# df[df['categoria] == 'tech'][df['importe'] > 200]['producto]

# En PySpark (datos masivos) seria:
# df.filter((col('categoria') == 'tech') & (col('importe') > 200)).select('producto')

