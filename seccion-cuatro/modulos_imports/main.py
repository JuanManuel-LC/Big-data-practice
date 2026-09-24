"""Script pprincipal que usa el modulo de calculos"""

#Importar el modulo completo, tambien podemos asignarles alias con "as"
import calculos as calc

#Importar funciones especificas (cuando usas mucho una funcio)
# from calculos import aplicar_iva, calcular_total

#Nunca hacer esto (import TODO sin prefijo - contamina tu namespace)
#from calculos import * -->> MALO: no sabes de donde vienen las funciones

#Usamos las funciones de calculos
total = calc.calcular_total(3, 299.99)
con_iva = calc.aplicar_iva(total)
final = calc.calcular_descuento(con_iva, 10)

print(f"Subtotal: {total:.2f}€")
print(f"Con IVA: {con_iva:.2f}€")
print(f"Con descuento 10%: {final:.2f}€")