from collections import Counter

acciones = [
    "login", "ver_producto", "ver_producto", "añadir_carrito",
    "login", "ver_producto", "comprar", "login", "ver_producto",
    "añadir_carrito", "ver_producto", "login", "comprar",
    "ver_producto", "añadir_carrito", "login", "logout",
]

# Contar frecuencias (esto ya está hecho)
conteo = Counter(acciones)
print(conteo)

total_acciones = sum(conteo.values())          # <- la suma de todas las frecuencias
print(total_acciones)                                #    Pista: sum(conteo) suma las CLAVES (texto)
                                #    y revienta. Las frecuencias: conteo.values()
top_3 = conteo.most_common(3)   # <- deberían ser 3, no 1
print(top_3)


print("Top 3 acciones:")
for accion, frecuencia in top_3:
    porcentaje = (frecuencia / total_acciones) * 100
    print(f"  {accion}: {frecuencia} veces ({porcentaje:.1f}%)")
