# 1. SyntaxError — Escribiste mal el código (Python no puede ni leerlo)
# Causa: falta un ":", un paréntesis, indentación incorrecta
#if True
#    print("falta los dos puntos")  # SyntaxError: expected ':'

# 2. NameError — Usas una variable que no existe
# Causa: typo en el nombre, olvidaste definirla, scope incorrecto
print(total_ventas)  # NameError: name 'total_ventas' is not defined

# 3. TypeError — Mezclas tipos incompatibles
# Causa: sumar string + int, pasar argumento equivocado
edad = "25"
anio_nacimiento = 2024 - edad  # TypeError: unsupported operand type(s)

# 4. IndexError — Accedes a una posición que no existe
# Causa: lista más corta de lo esperado, off-by-one
filas = ["a", "b", "c"]
print(filas[5])  # IndexError: list index out of range

# 5. ValueError — El valor no es convertible al tipo esperado
# Causa: datos sucios en CSVs, campos vacíos, texto donde esperabas números
precio = float("N/A")  # ValueError: could not convert string to float