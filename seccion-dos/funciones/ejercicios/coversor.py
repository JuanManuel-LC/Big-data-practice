# Conversor de monedas
# Tasa de cambio

TASA_DOLAR = 1.08
TASA_LIBRA = 0.86
TASA_YEN = 161

def euros_a_dolares(euros):
    """Convierte euros a dolares americanos."""
    return euros * TASA_DOLAR

def euros_a_libras(euros):
    """Convierte euros a libras esterlinas."""
    return euros * TASA_LIBRA

def euros_a_yenes(euros):
    """Convierte euros a Yenes japonenes."""
    return euros * TASA_YEN

def mostrar_conversion(euros):
    """Muestra todas las conversiones desde euros"""
    print(f"")
    print(f"=== CONVERSIÓN DE {euros:.2f}€ ===")
    print(f"  --> {euros_a_dolares(euros):.2f} USD")
    print(f"  --> {euros_a_libras(euros):.2f} GBP")
    print(f"  --> {euros_a_yenes(euros):.2f} JPY")
    
euros = float(input("Ingrese la cantidad de Euros: "))
mostrar_conversion(euros)