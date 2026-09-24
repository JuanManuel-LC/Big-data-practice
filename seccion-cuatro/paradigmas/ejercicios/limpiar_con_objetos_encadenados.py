nombres_sucios = [
    "  ANA garcia",
    "LUIS   perez LOPEZ",
    "  maria   TORRES",
    "pedro\truiz",
    "  SARA   diaz martinez",
]

def limpiar(nombre):
    """Quita espacios de los extremos, colapsa los de dentro y pone
    la inicial de cada palabra en mayúscula, encadenando métodos.
    Pista: " ".join(... .strip().split()).title()"""
    return " ".join(nombre.strip().split()).title()

# No toques: prueba tu función con los cinco nombres
print("Nombres limpios:")
for n in nombres_sucios:
    print(f"  {limpiar(n)}")
