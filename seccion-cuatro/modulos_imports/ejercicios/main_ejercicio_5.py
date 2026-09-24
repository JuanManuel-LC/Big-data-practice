import precios as p

total = p.calcular_total(4, 15.0)
con_iva = p.aplicar_iva(total)
formateado = p.formatear_precio(con_iva)

print(f"El total serian: {formateado}€")