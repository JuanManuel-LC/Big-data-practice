# Capturar excepciones especificas (RECOMENDADO)

try:
    with open("datos.csv", "r", encoding="utf-8") as f:
        contenido = f.read()
    
except FileNotFoundError:
    print("EL archivo no existe. ¿Se movió o se renombró?")
except PermissionError:
    print("No tienes permisos para leer este archivo")
except UnicodeDecodeError:
    print("El archivo no esta en UTF-8. Prueba con encoding='latin-1'.")
    
# Captura CUALQUIER excepcion (usar con cuidado)
print()
# try:
#     resultado = operacion_arriesgada()
# except Exception as e:
#     print(f"Error inesperado: {type(e).__name__}: {e}")