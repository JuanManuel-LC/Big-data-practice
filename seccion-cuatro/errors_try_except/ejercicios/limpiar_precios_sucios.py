"""Convierte los precios válidos a número y guarda los inválidos aparte. El except ValueError ya está puesto — escribe los cuerpos del try y el except."""

precios_raw = ["29.99", "N/A", "150.00", "", "89.50", "error", "45.00", "null"]

def clasificar_precios(precios):
    """Intenta convertir cada precio. Devuelve (validos, invalidos)."""
    validos = []
    invalidos = []
    for precio in precios:
        try:
            validos.append(float(precio))
        except ValueError:
            invalidos.append(precio)
    return validos, invalidos

# No toques: prueba tu función
validos, invalidos = clasificar_precios(precios_raw)
print(f"Válidos: {len(validos)} → Total: {sum(validos):.2f}€")
print(f"Inválidos: {len(invalidos)} → {invalidos}")