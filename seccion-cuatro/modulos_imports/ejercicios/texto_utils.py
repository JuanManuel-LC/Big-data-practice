def limpiar_nombre(nombre):
    return nombre.strip()

def tiene_dominio(email):
    return "." in email.split("@")[-1]

def validar_email(email):
    return "@" in email and tiene_dominio(email)