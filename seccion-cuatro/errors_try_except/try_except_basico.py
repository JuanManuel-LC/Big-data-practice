# SIN try/except - explota con datos sucios
precios = ["12.99", "45.00", "N/A", "89.50", "", "120.00"]

#Esto FALLARA en "N/A" Y "" ---> ValueError
# totales = [float(p) for p in precios]

# CON try/except - maneja datos sucios
totales = []
errores = []

for i, precio in enumerate(precios):
    try:
        valor = float(precio)
        totales.append(valor)
    except ValueError:
        errores.append(f"Fila {i}: '{precio}' no es un numero valido")

print(f"Procesados: {len(totales)} valores")
print(f"Errores: {len(errores)} filas con problemas")
for error in errores:
    print(f" [AVISO] {error}")