# Un registro de venta como diccionario
venta = {
    "id": "VNT-2024-001",
    "fecha": "2025-08-27",
    "cliente": "Juan Manuel Lame",
    "producto": "Monitor 4k",
    "cantidad": 2,
    "precio_unitario": 349.99,
    "impuesto": 0.21
}

# Acceder a valores por clave
print(venta["producto"])
print(venta["precio_unitario"])

print()
# Acceso seguro con .get() (no explota si la clave no existe)
descuento = venta.get("descuento", 0) # 0 si no existe
print(f"Descuento: {descuento}")

print()
# Añadir/modificar campos
venta["total"] = venta["cantidad"] * venta["precio_unitario"] * (1 + venta["impuesto"])
print(f"Total: {venta['total']:.2f}")