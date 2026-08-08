# Funciones incorporadas en python
ventas_hoy = [120.50, 89.99, 245.00, 67.30, 150.00]

total = sum(ventas_hoy)
promedio = total / len(ventas_hoy)
venta_maxima = max(ventas_hoy)

print(f"Venta del dia: {total:.2f}€")
print(f"Ticket medio: {promedio:.2f}€")
print(f"Venta mas alta: {venta_maxima:.2f}€")

# type() --> Obtiene el tipo de elemento
precio = 1299.99
print(type(precio))

# str() --> Convierte cualquier tipo a cadena de texto
precio_texto = str(precio)
print(type(precio_texto), precio_texto)

# int() y float() --> Convierten el texto a número
edad = int("25")
altura = float("1.78")
print(f"edad: | {edad + 1} | y altura: | {altura} |")
print(type(edad), type(altura))