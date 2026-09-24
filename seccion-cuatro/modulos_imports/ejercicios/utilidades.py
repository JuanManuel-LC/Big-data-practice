# --- imagina que esto es data_utils.py ---

def limpiar_texto(texto):
    return texto.strip()

def validar_email(email):
    return "@" in email and "." in email.split("@")[-1]

def formatear_precio(precio):
    return f"{precio:.2f}€"


print(limpiar_texto("  Hola mundo  "))
print(validar_email("user@email.com"))
print(validar_email("invalido"))
print(validar_email("sin.punto@dominio"))
print(formatear_precio(1299.567))