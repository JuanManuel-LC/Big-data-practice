palabras = "hola  mundo".split()     #['hola', 'mundo']
print(" ".join(palabras))           #'hola mundo' -- solo un espacio

#Sirve para normalizar: partir por los espacios de mas y volver a unir limpio
sucio = " datos  de  venta  "
limpio = " ".join(sucio.strip().split())
print(limpio)
