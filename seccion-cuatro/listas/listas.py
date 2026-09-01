ventas_semana = [1250.00, 980.50, 1100.75, 1430.20, 890.00, 1560.80, 2100.00]

# Acceder por indicie (Empieza en cero)
print(ventas_semana[0])
print(ventas_semana[-1])

# Slicing: obtener un rango
entre_semana = ventas_semana[0:5] # lunes a viernes
fin_semana = ventas_semana[5:] # sabado y domingo

print(f"Entre semana: {entre_semana}")
print(f"Fin semana: {fin_semana}")