# Ejercicio: contar_ventas_vendedor.py
# Cuenta cuántas ventas hizo cada vendedor y calcula su total facturado.

ventas = [
    {"vendedor": "Carmen", "importe": 250},
    {"vendedor": "David", "importe": 140},
    {"vendedor": "Carmen", "importe": 90},
    {"vendedor": "Elena", "importe": 600},
    {"vendedor": "David", "importe": 310},
    {"vendedor": "Carmen", "importe": 175},
    {"vendedor": "Elena", "importe": 120},
]

# Conteo de ventas por vendedor: dict vendedor -> número de ventas
num_ventas = {}
for venta in ventas:
    v = venta["vendedor"]
    num_ventas[v] = num_ventas.get(v, 0) + 1   # <- suma 1, y si no existe empieza en 0. Pista: .get(v, 0)

# Total facturado por vendedor: dict vendedor -> suma de importes
total_por_vendedor = {}
for venta in ventas:
    v = venta["vendedor"]
    # Pista: igual que arriba, pero sumando venta["importe"] en vez de 1
    total_por_vendedor[v] = total_por_vendedor.get(v, 0) + venta["importe"]

# No toques estas líneas: son las que muestran el resultado
print("VENTAS POR VENDEDOR")
for vendedor, num in num_ventas.items():
    print(f"  {vendedor}: {num} ventas, {total_por_vendedor[vendedor]:.2f}€")
