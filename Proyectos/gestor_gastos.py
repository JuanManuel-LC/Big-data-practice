# 1. El programa muestra un MENÚ con opciones (bucle while — se repite hasta que el usuario elija salir).
# 2. EL usuario puede AÑADIR un gasto (input + variables + almacenamiento en lista)
# 3. El usuario puede VER todos los gastos (bucle for para recorrer la lista).
# 4. El usuario puede ver un RESUMEN por categoría (bucle + condicional + acumulador).
# 5. Cada operación es una FUNCIÓN separada (organización y reutilización).


# Primero vamos a crear el Menu
def mostrar_menu():
    """Muestra las opciones disponibles"""
    print("")
    print("=" * 35)
    print("  💰 GESTOR DE GASTOS PERSONALES")
    print("=" * 35)
    print("  1. Añadir gasto")
    print("  2. Ver todos los gastos")
    print("  3. Resumen por categoría")
    print("  4. Buscar gastos")
    print("  5. Salir")
    print("-" * 35)

# Funcion de agregar gasto
def agregar_gasto(gastos):
    """Pide un gasto al usuario y añade un gasto a la lista"""
    print("")
    concepto = input("¿Que compraste?: ")
    cantidad = int(input("¿Cuanto costo? (€):"))
    print("Categorias: comida, transporte, ocio, hogar, otros")
    categoria = input("Categoria: ").lower()
    
    gasto = {
        "concepto": concepto,
        "cantidad": cantidad,
        "categoria": categoria
    }
    
    gastos.append(gasto)
    print(f"✓ Gasto registrado: {concepto} ({cantidad:.2f}€)")

# Función de ver los gastos
def ver_gastos(gastos):
    """Muestra todos los gastos registrados"""
    if len(gastos) == 0:
        print("No hay gastos registrados todavia.")
        return

    print("")
    print(f" {'#':<4}{'Concepto':<20}{'Cantidad':<12}{'Categoría'}")
    print(" " + "-" * 50)
    
    total = 0
    for i in range(len(gastos)):
        g = gastos[i]
        print(f" {i+1:<4}{g['concepto']:<20}{g['cantidad']:<12.2f}{g['categoria']}")
        total = total + g['cantidad']
        
    print(" " + "-" * 50)
    print(f" TOTAL: {total:.2f}€ ({len(gastos)} gastos)")

# Función para tener un resumen de categorias
def resumen_categorias(gastos):
    """Muestra el total gastado por categoría."""
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
    
    # Acumular por categoria
    categorias = {}
    for gasto in gastos:
        cat = gasto["categoria"]
        if cat in categorias:
            categorias[cat] = categorias[cat] + gasto["cantidad"]
        else:
            categorias[cat] = gasto["cantidad"]

    # Mostrar un resumen
    print("")
    print(" === RESUMEN POR CATEGORÍA ===")
    total_general = 0
    for cat in categorias:
        total_cat = categorias[cat]
        total_general = total_general + total_cat
        print(f" {cat:<15} {total_cat:<8.2f}€")
        
    print(f"  {'TOTAL':<15} {total_general:>8.2f}€")
    

def buscar_gastos(gastos):
    """Busca gastos por categoria o por importe mínimo."""
    print(" Buscar por: (1) categoría  (2) importe mínimo")
    tipo = input(" Opción: ")
    
    encontrados = {}
    if tipo == "1":
        cat = input("   ¿Que categoría?   ").lower()
        for gasto in gastos:
            if gasto["categoria"] == cat:
                encontrados.append(gasto)
    
    elif tipo == "2":
        minimo = float(input("   ¿Importe mínimo? (€):   "))
        for gasto in gastos:
            if gasto["cantidad"] >= minimo:
                encontrados.append(gasto)

    if len(encontrados) == 0:
        print("  No se encontraron gastos con esos criterios.   ")
    else:
        print(f" Encontrados: {len(encontrados)} gastos  ")
        for g in encontrados:
            print(f"    - {g['concepto']}: {g['cantidad']:.2f}€ ({g['categoria']})")


gastos = []


while True:
    mostrar_menu()
    opcion = input(" Tu elección (1-5): ")

    if opcion == "1":
        agregar_gasto(gastos)
    elif opcion == "2":
        ver_gastos(gastos)
    elif opcion == "3":
        resumen_categorias(gastos)
    elif opcion == "4":
        buscar_gastos(gastos)
    elif opcion == "5":
        print("")
        print("¡Hasta luego! Tus gastos NO se guardan al cerrar.")
        print(" (En la Skill 3 aprenderás a guardar en archivo)")
        break
    else:
        print("❌ Opción no válida. Elige entre 1 y 5.")
    