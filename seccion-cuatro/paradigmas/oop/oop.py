#Todo en Python es un objeto con metodos
texto = " datos de venta del lunes "

#El objeto String sabe transformarce
print(texto.strip())    #quita espacios
print(texto.upper())    #mayusculas
print(texto.split())    #divide palabras
print(texto.replace("lunes", "martes"))     #sustituye
print()

# EL objetp lista sabe gestionarse 
ventas = [120.5, 89.0, 245.0, 67.3]
ventas.append(180.0)    # Añade
ventas.sort()           # Se ordena a si misma
print(ventas)           # [67.3, 89.0, 120.5, 180.0, 245.0]
print()

#El objeto diccionario SABE consultarse
cliente = {"nombre": "Ana", "plan": "premium"}
print(cliente.keys())        # sabe sus claves
print(cliente.values())         # sabe sus valores
print(cliente.get("edad", 0))       #sabe buscar de forma segura
cliente.update({"edad": 28})

print(cliente)