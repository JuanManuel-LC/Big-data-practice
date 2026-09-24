"""
Python tiene tres funciones built-in que representan la esencia de la programación funcional: map() transforma cada elemento, filter() selecciona elementos por condición, y lambda crea funciones anónimas de una línea. Las list comprehensions que ya conoces son la versión "pytónica" de map y filter — pero entender las versiones puras te prepara para PySpark, donde se usan constantemente.
"""

#lambda: funcion anonima de una linea
def aplicar_iva(precio):
    return precio * 1.21

#Lo mismo con lambda:
aplicar_iva_fn = lambda precio: precio * 1.21
print(aplicar_iva_fn(100))

print()
print("Con IVA")
# map(): aplica una funcion a CADA elemento
precios = [100, 250, 50, 899]
con_iva = list(map(lambda p: p * 1.21, precios))
print(con_iva)

#Equivalente con list comprehension (mas pythonico):
con_iva = [p * 1.21 for p in precios]

print()
print("Caros")
# filter(): selecciona elementos que cumplen una condicion
caros = list(filter(lambda p: p > 200, precios))
print(caros)

# Equivalente con list comprehension
caros = [p for p in precios if p > 200]

#Encadenar map + filter (Estilo funcional puro):
resultado = list(map(
    lambda p: round(p * 1.21, 2),
    filter(lambda p: p > 200, precios)
))
print(f"Resultados: {resultado}")

