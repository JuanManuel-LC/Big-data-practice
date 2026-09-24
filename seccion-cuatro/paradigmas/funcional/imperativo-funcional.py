#Imperativo (modifica los datos originales)
precios = [100, 250, 50, 899, 1300]
precios.sort() #Modifica la lista original
print(precios)

#Funcional (crea datos nuevos, el original no se toca)
precios = [100, 250, 50, 899, 1300]
ordenados = sorted(precios)     # Crea una lista nueva
print(precios)      # [100, 250, 50, 899, 1300] — intacto!
print(ordenados)    # [50, 100, 250, 899, 1300] — copia ordenada

#List Comprehension = programa funcional que ya conoces
precios = [100, 250, 50, 899, 1300]
con_iva = [p * 1.21 for p in precios]   # Crea una nueva lista
caros = [p for p in precios if p > 200]     #Otra lista nueva
print()
print(f"Precios: {precios}")
print(f"Con IVA: {con_iva}")
print(f"Caros: {caros}")

#Ejemplo desglozando la list comprehension de la lista 'caros'
caros2 = []
for p in precios:
    if p > 200:
        caros2.append(p)

print(f"Caros2: {caros2}")