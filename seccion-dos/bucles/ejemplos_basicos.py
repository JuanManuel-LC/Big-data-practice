# Ptron acumulador: sumar gastos
gastos = [12.50, 8.99, 45.00, 3.20, 22.15]

total = 0

for gasto in gastos:
    total += gasto
    print(f" + {gasto:.2f}€ → Acumulado: {total:.2f}€")
    
print(f"Total de gastos: {total:.2f}€")

# Otro ejemplo: contar cuántos aprobados hay
notas = [7.5, 4.2, 9.0, 3.8, 6.1, 8.4, 5.0]
aprobados = 0
suspensos = 0

for nota in notas:
    if nota >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1

print(f"Aprobados: {aprobados}, Suspensos: {suspensos}")