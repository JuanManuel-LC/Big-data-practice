import csv

# Escribir un CSV problemático para practicar
with open('ventas_problemas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['producto', 'descripcion', 'precio', 'stock'])
    writer.writerow(['Camiseta', 'Algodón, talla M', '29.99', '150'])
    writer.writerow(['Pantalón', 'Vaquero "slim fit"', '59.90', ''])
    writer.writerow(['Chaqueta', 'Impermeable\nlarga', '120.00', '45'])

# Leer manejando problemas
with open('ventas_problemas.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        # Convertir precio a float (viene como texto)
        precio = float(fila['precio'])
        # Manejar stock vacío como 0
        stock = int(fila['stock']) if fila['stock'] else 0
        print(f"  {fila['producto']:12} | {precio:>7.2f}€ | stock: {stock}")