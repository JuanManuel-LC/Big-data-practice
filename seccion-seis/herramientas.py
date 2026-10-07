#Dos herramientas para campos que pueden no existir
evento = {"tipo": "login", "usuario": 42}

print(evento.get("importe", 0))
print("importe" in evento)


import io

# io.StringIO: hace que un texto se comporte como un fichero abierto.
# Util para probar sin crear archivos de verdad.

texto = "a,b,c\n1,2,3"
fichero_falso = io.StringIO(texto)
print(fichero_falso.readline())         # "a,b,c\n"

# set: un conjunto que no admite repetidos.
usuarios = set()
usuarios.add("ana")
usuarios.add("ana")       # esta no entra: ya estaba
usuarios.add("pedro")
print(len(usuarios))      # 2