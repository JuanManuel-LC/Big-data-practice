def calcular_iva(precio, porcentaje_iva=21):
    """Calcular el precio con IVA incluido"""
    iva = precio * (porcentaje_iva / 100)
    total = precio + iva
    return total

precio_final = calcular_iva(100)
print(f"100€ + IVA = {precio_final}€")