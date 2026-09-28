"""Procesa registros de empleados. Las validaciones ya están escritas — falta la conversión del salario a número. El except ya está puesto."""

registros = [
    {"nombre": "Ana", "salario": "45000", "departamento": "Datos"},
    {"nombre": "Luis", "salario": "N/A", "departamento": "Ventas"},
    {"nombre": "María", "departamento": "Marketing"},
    {"nombre": "Pedro", "salario": "52000", "departamento": "Datos"},
    {"nombre": "", "salario": "38000", "departamento": "Soporte"},
]

def validar_registro(reg):
    """Devuelve el salario como número si el registro es válido.
    Si no lo es, lanza ValueError con el motivo:
      nombre vacío · falta el campo salario · salario no numérico."""
    
    if not reg.get("nombre"):
        raise ValueError("Nombre vacio")
    if "salario" not in reg:
        raise ValueError("Falta campo salario")
    
    salario = float(reg["salario"])
    reg["salario_num"] = salario
    return reg

# No toques: el arnés que prueba tu función
exitosos = []
fallidos = []
for i, reg in enumerate(registros):
    try:
        exitosos.append(validar_registro(reg))
    except (ValueError, TypeError) as e:
        fallidos.append({"fila": i, "error": str(e)})

print(f"Procesados: {len(exitosos)}/{len(registros)}")
if fallidos:
    print("Errores:")
    for f in fallidos:
        print(f"  Fila {f['fila']}: {f['error']}")
