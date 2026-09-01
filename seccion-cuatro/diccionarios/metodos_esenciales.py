cliente = {
    "nombre": "Carlos Lopez",
    "email": "carlos@empresa.com",
    "plan": "premium",
    "gasto_mensual": 450.00,
}

# Obtener todas las claves y valores
print(list(cliente.keys()))
print(list(cliente.values()))

print()
# Iterar sobre clave-valor (Muy comun en datos) - la funcion es para poder reutilizarlo
def imprimir():    
    for campo, valor in cliente.items():
        print(f"{campo}: {valor}")
    
print()
print("--- Actualizacion de campos de golpe ---")
# Actualizar multiples campos de golpe
cliente.update({"plan": "enterprise", "gasto_mensual": 890.00})
imprimir()


print()
print("--- Eliminar clave ---")
# Eliminar una clave
del cliente["email"]
imprimir()


# Copiar (cuidado = NO copia, crea una referencia)
cliente_copia = cliente.copy()
