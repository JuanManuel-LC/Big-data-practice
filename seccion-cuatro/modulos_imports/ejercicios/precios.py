def formatear_precio(precio):
    return f"{precio:.2f}€"

def calcular_total(cantidad, precio_unitario):
    return cantidad * precio_unitario

def aplicar_iva(importe, tasa=0.21):
    return importe * (1 + tasa)

def calcular_descuento(importe, porcentaje):
    descuento = importe * (porcentaje / 100)
    importe -= descuento
    return importe