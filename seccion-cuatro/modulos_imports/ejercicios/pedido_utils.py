import precios as p

def limpiar_texto(texto):
    return texto.strip()

def es_email_valido(email):
    return "@" in email and "." in email.split("@")[-1]

def resumen_pedido(cliente, email, cantidad, precio_unitario):
    cliente = limpiar_texto(cliente)
    email = limpiar_texto(email)
    total = p.calcular_total(cantidad, precio_unitario)
    
    print(f"Cliente: {cliente} | Email válido: {es_email_valido(email)} | Total {p.formatear_precio(total)}")
    

cliente = input("Ingrese el nombre: ")
email = input("Ingrese un email valido: ")
cantidad = int(input("Ingrese la cantidad: "))
precio_unitario= float(input("Ingrese el precio unitario: "))

resumen_pedido(cliente, email, cantidad, precio_unitario)