import precios as p

#print(f"{pr.formatear_precio(49.9)}")

total = p.calcular_total(3, 120)
con_iva = p.aplicar_iva(total)
descuento = p.calcular_descuento(con_iva, 15)

print(f"Subtotal: {p.formatear_precio(total)}")
print(f"Con IVA: {p.formatear_precio(con_iva)}")
print(f"Total final: {p.formatear_precio(descuento)}")