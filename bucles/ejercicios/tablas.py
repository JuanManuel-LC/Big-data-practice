# Opcion 1 
numero = int(input("¿De que numero quieres la tabla?: "))

print(f"==== TABLA DEL {numero} ====")

while True:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    desicion = input("¿Desea ver otra tabla? (si/no): ")
    
    if desicion.lower() == "no":
        print("¡Gracias por usar el programa de tablas!")
        break
    
    numero = int(input("¿De que numero quieres la tabla?: "))
  
# ? Opcion 2
numero = int(input("¿De qué número quieres la tabla?: "))

print(f"==== TABLA DEL {numero} ====")

decision = ""

while decision != "no":
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    decision = input("¿Desea ver otra tabla? (si/no): ").strip().lower()

    if decision != "no":
        numero = int(input("¿De qué número quieres la tabla?: "))