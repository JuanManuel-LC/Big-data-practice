eleccion = ""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Division por cero no puede ser resuelta."
    return a / b

def mostrar_resultado(operacion, resultado):
    print(f"\nResultado de {operacion}: {resultado}")

def mostrar_menu():
    print("=== Calculadora Básica ===")
    print("\nElija la operación.")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("0. salir")

while eleccion != "n":

    mostrar_menu()

    eleccion = int(input("\nElija la operacion a realizar: "))
    

    if eleccion == 0:
        print("¡Gracias por usar!")
        break
    
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
        
    if eleccion == 1:
        resultado = sumar(num1, num2)
        mostrar_resultado("suma", resultado)
    elif eleccion == 2:
        resultado = restar(num1, num2)
        mostrar_resultado("resta", resultado)
    elif eleccion == 3:
        resultado = multiplicar(num1, num2)
        mostrar_resultado("multiplicacion", resultado)
    elif eleccion == 4:
        resultado = dividir(num1, num2)
        mostrar_resultado("division", resultado)
    
    else:
        resultado = "Opción no válida"
        
    # print(f"\n Resultado: {resultado}")
    
    
    eleccion = input("\nDesea volver a intentarlo? (s/n): ").lower()