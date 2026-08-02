# Mini cajero automático con bucle
saldo = 1000.00
print("=== CAJERO BIGDATABANK ===")
print(f"Saldo actual: {saldo:.2f}€")

opcion = ""
while opcion != "salir":
    print("")
    print("Opciones: consultar / retirar / ingresar / salir")
    opcion = input("¿Qué deseas hacer? ")

    if opcion == "consultar":
        print(f"Tu saldo es: {saldo:.2f}€")
    elif opcion == "retirar":
        cantidad = float(input("¿Cuánto quieres retirar? "))
        if cantidad > saldo:
            print("¡Saldo insuficiente!")
        else:
            saldo = saldo - cantidad
            print(f"Retirados {cantidad:.2f}€. Nuevo saldo: {saldo:.2f}€")
    elif opcion == "ingresar":
        cantidad = float(input("¿Cuánto quieres ingresar? "))
        saldo = saldo + cantidad
        print(f"Ingresados {cantidad:.2f}€. Nuevo saldo: {saldo:.2f}€")
    elif opcion == "salir":
        print("¡Hasta luego! Recoge tu tarjeta.")
    else:
        print("Opción no reconocida. Intenta de nuevo.")