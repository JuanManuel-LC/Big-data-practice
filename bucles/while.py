password_correcta = "secreto123"
intentos = 0

password = input("Ingrese la contraseña: ")

while password != password_correcta:
    intentos += 1
    if intentos >= 3:
        print("¡Demasiados intentos! Cuenta bloqueada.")
        break
    print("Contraseña incorrecta. Intente nuevamente.")
    password = input("Ingrese la contraseña: ")
    
if password == password_correcta:
    print("¡Contraseña correcta! Acceso concedido.")