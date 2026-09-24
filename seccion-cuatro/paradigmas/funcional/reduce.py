from functools import reduce

precios = [100, 250, 50]

# reduce lleva un acumulador que empieza en 0
# y en cada paso lo combina con el siguiente

total = reduce(lambda acum, p: acum + p, precios, 0)
print(f'Precios: {total}')
