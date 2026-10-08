# Tres tablas. Las dos primeras tienen su id propio (clave primaria).
clientes = [{"id": 1, "nombre": "Ana"}]
productos = [{"id": 7, "nombre": "Teclado", "precio": 49.9}]

# La tercera las RELACIONA guardando sus ids (claves ajenas)
pedidos = [{"id": 100, "cliente_id": 1, "producto_id": 7}]

# "Que compro Ana?" se responde saltando de tabla en tabla por el id
pedido = pedidos[0]
producto = [p for p in productos if p["id"] == pedido["producto_id"]][0]
print(producto["nombre"])       # Teclado