categorias = {}

gastos = [
    {"concepto":"Almuerzo","cantidad":12,"categoria":"Comida"},
    {"concepto":"Bus","cantidad":5,"categoria":"Transporte"},
    {"concepto":"Bicicleta","cantidad":10,"categoria":"Transporte"},
    {"concepto":"Jeringa","cantidad":20,"categoria":"Salud"}
]

# gastos = []

def agregar_gasto(gastos):
    """Agregar gasto """
    concepto = input("\n¿Que compraste?: ")
    cantidad = float(input("¿Cuanto costo?: "))
    print("Categorias: comida, transporte, ocio, hogar, otros ")
    categoria = input("Categoría: ")
    
    gasto = {
        "concepto": concepto,
        "cantidad": cantidad,
        "categoria": categoria
    }
    
    gastos.append(gasto)
    print(f"\nGasto registrado: {concepto} ({cantidad:.2f}€)")


def ver_gastos(gastos):
    """Funcion para imprimir todos los gastos"""   

    if len(gastos) == 0:
        print("\nNo hay gastos agregados")
        return
    
    print()
    print(f"{'#':<4} {'concepto':<20} {'cantidad':<12} {'categoría'}")
    print("-" * 50)
    
    total = 0
    for i in range(len(gastos)):
        g = gastos[i]
        print(f"{i+1:<4}{g['concepto']:<20}{g['cantidad']:<12.2f}{g['categoria']}")
        total = total + g['cantidad']
        
    print("-" * 50)
    print(f"\n TOTAL: {total:.2f}€ ({len(gastos)} gastos)")
    

def resumen_categoria(gastos):
    """Mostrará un resumen por categorias"""
    if len(gastos) == 0:
       print("No hay gastos guardados.")
       return
   
    categorias = {}
    for gasto in gastos:
        cat = gasto['categoria']
        if cat in categorias:
            categorias[cat] = categorias[cat] + gasto["cantidad"]
        else:
            categorias[cat] = gasto['cantidad']
            
    print()
    print("Resumen por categoria")
    
    total_ganeral = 0
    for cat in categorias:
        total_cat = categorias[cat]
        total_general = total_ganeral + total_cat
        print(f" {cat:<12} {total_cat:<8.2f}€")
        
    print(f" {'TOTAL:':<12} {total_general:<8.2f}€")

def buscar_gastoss(gastos):
    """Buscar gastos por categorias o importe minimo"""
    print("Buscar por: (1) categoría  (2) importe mínimo")
    tipo = input(" Opción: ")
    
    

while True:
    print("\n=== GASTOS ===")
    print("Elija una opcion: ")
    print("1. agregar un gasto")
    print("2. listar todos los gastos")
    print("3. resumen por categorias")
    print("4. salir del programa")
    
    eleccion = int(input("\n --> "))

    if eleccion == 1:
        agregar_gasto(gastos)
    elif eleccion == 2:
        ver_gastos(gastos)
    elif eleccion == 3:
        resumen_categoria(gastos)
    elif eleccion == 4:
        print("Gracias por usar.")
        break
    else:
        print("Opcion no valida")
        
        
# for gasto in gastos:
            # cat = gasto["categoria"]
            # if cat in categorias:
                # categorias[cat] = categorias[cat] + gasto["cantidad"]
            # else:
                # categorias[cat] = gasto["cantidad"]
                # print(categorias)
                # print(f"Agregando la nueva categoria: {categorias[cat]}")