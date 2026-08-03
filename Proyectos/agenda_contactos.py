contactos = []

def mostrar_menu():
    print("")
    print("  📱 AGENDA DE CONTACTOS")
    print("  1. Añadir contacto")
    print("  2. Buscar por nombre")
    print("  3. Listar todos")
    print("  4. Eliminar contacto")
    print("  5. Salir")

def agregar_contacto():
    """Pedir nombre, telefono, email y agregarlo a la lista"""
    print("")
    nombre = input("Nombre: ")
    email = input("Email: ")
    indicativo = input("Indicativo: ")
    telefono = int(input("Telefono: "))
    
    contacto = {
        "nombre": nombre,
        "email": email,
        "indicativo": indicativo,
        "telefono": telefono
    }
    
    contactos.append(contacto)
    print(f" {nombre}, ha sido creado exitosamente")

def buscar_contacto(contactos):
    """Busca por nombre (parcial) y muestra coincidencias"""
    busqueda = input(" Buscar nombre: ").lower()
    encontrados = []
    for c in contactos:
        if busqueda in c['nombre'].lower():
            encontrados.append(c)
    if len(encontrados) == 0:
        print("  No se encontraron contactos.")
    else:
        for c in encontrados:
            print(f"  📌 {c['nombre']} | {c['indicativo']} | {c['telefono']} | {c['email']}")
    
    
def listar_contactos(contactos):
    """Muestra todos los contactos"""
    if len(contactos) == 0:
        print("No hay contactos guardados.")
        return
    
    for i in range(len(contactos)):
        c = contactos[i]
        print(f" {i + 1}. {c['nombre']} - {c['telefono']}")
        
        
def elimiar_contacto(contactos):
    if len(contactos) == 0:
        print("No hay contactos para eliminar.")
        return
    
    print(f"{'-' * 5} Contactos guardados {'-' * 5}")
    listar_contactos(contactos)
    
    numero = int(input("Número a eliminar: ")) - 1
    
    if 0 <= numero < len(contactos):
        eliminado = contactos.pop(numero)
        print(f"  ✓ {eliminado['nombre']} eliminados")
        
    else:
        print("Numero no valido.")
    
    
    
    
decision = ""

while True:
    mostrar_menu()
    
    decision = input("Elección: ")
    
    if decision == "1":
        agregar_contacto()
    elif decision == "2":
        buscar_contacto(contactos)
    elif decision == "3":
        listar_contactos(contactos)
    elif decision == "4":
        elimiar_contacto(contactos)
    elif decision == "5":
            print("Gracias por usar.")
            break
    else:
        print("Opción no valida.")