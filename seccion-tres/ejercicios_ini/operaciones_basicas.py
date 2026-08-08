# Ventas del dia
ventas_dia = [45.99, 123.50, 67.00, 89.99, 234.50, 12.00, 178.90]

# La primera ya está hecha, como modelo
total = sum(ventas_dia)

promedio = total / len(ventas_dia)    # <- el total dividido entre cuántas ventas hay
maxima = max(ventas_dia)      # <- la venta más alta. Pista: max(...)
minima = min(ventas_dia)      # <- la venta más baja

print(f"Total: {total:.2f}€")
print(f"Promedio: {promedio:.2f}€")
print(f"Máxima: {maxima:.2f}€")
print(f"Mínima: {minima:.2f}€")