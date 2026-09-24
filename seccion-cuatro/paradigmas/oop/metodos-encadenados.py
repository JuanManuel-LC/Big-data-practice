"""
EL patron mas potente de OOP para datos es el ENCADENAMIENTO de metodos (method chaining). La idea: cada metodo
devuelve un objeto, y sobre ese objeto puedes llamar a otro metodo. Es como una cadena de montaje donde cada estacion
transforma el producto y lo pasa al siguiente.
"""

#Encadenamiento de metodos con string
nombre_sucio = "    ana GARCIA lopez    "

#Sin encadenar (verboso)

paso1 = nombre_sucio.strip()
paso2 = paso1.lower()
paso3 = paso2.title()
print(paso3) #'Ana Garcia Lopez'


#Encadenado (Una linea -- cada metodo devuelve un string nuevo)
nombre_limpio = nombre_sucio.strip().lower().title()
print(nombre_limpio)

# Asi se ve en Pandas (futuro):
# df.dropna().groupby("categoria")["importe"].sum().sort_values(ascending=False)
#    |          |                                |              |
#  quita NaN  agrupa                           suma          ordena
#
# Cada punto produce un objeto nuevo con mas metodos disponibles
