importe = float(input("Importe de la compra (€): "))
es_vip = input("¿Tiene tarjeta VIP? (si/no): ")

    
if importe >= 200:
    descuento_base = 0.20
elif importe >= 100 and importe < 200:
    descuento_base = 0.10
elif importe < 100:
    descuento_base = 0.05
    

if es_vip.lower() == "si":
    descuento_total = descuento_base + 0.05
else:
    descuento_total = descuento_base
    
importe_final = importe * (1 - descuento_total)
    
print(f"Precio original: {importe} €")
print(f"Descuento aplicado: {descuento_total * 100}%")
print(f"Importe final: {importe_final} €")
