def tiene_longitud_minima(password):
    """Determinar la longitud"""
    return len(password) >= 8

def tiene_numero(password):
    for caracter in password:
        if caracter.isdigit():
            return True
    return False

def tiene_mayusculas(password):
    for caracter in password:
        if caracter.isupper():
            return True
    return False

def es_password_segura(password):
    """Averiguamos que este segura con las funciones anteriores"""
    return tiene_longitud_minima(password) and tiene_numero(password) and tiene_mayusculas(password)

pw = input("Ingrese la contraseña: ")
print("")

if es_password_segura(pw):
    print("✅ ¡Contraseña segura!")
else:
    print("❌ Contraseña insegura. Problemas:")
    if not tiene_longitud_minima(pw):
        print(f"  - Muy corta ({len(pw)} chars, mínimo 8)")
    if not tiene_numero(pw):
        print("  - Falta al menos un número")
    if not tiene_mayusculas(pw):
        print("  - Falta al menos una mayúcula")