def procesar_ventas(registros):
    """Procesa ventas con tolerancia a fallos."""
    exitosos = []
    fallidos = []

    for i, reg in enumerate(registros):
        try:
            # Validamos campos requeridos
            if "producto" not in reg or "precio" not in reg:
                raise ValueError("Faltan campos requeridos")

            # Convertir y calcular
            precio = float(reg["precio"])
            cantidad = int(reg.get("cantidad", 1))
            
            if precio < 0:
                raise ValueError(f"Precio negativo: {precio}")

            reg["total"] = precio * cantidad
            exitosos.append(reg)
            
        except (ValueError, TypeError) as e:
            fallidos.append({"fila": i, "error": str(e), "registro": reg})
    
    return exitosos, fallidos

# Datos con problemas reales
ventas_sucias = [
    {"producto": "Laptop", "precio": "1299.99", "cantidad": "2"},
    {"producto": "Monitor", "precio": "N/A"},        # precio no numérico
    {"precio": "50.00"},                              # falta producto
    {"producto": "Teclado", "precio": "79.99", "cantidad": "3"},
    {"producto": "Cable", "precio": "-5.00"},         # precio negativo
]

ok, errores = procesar_ventas(ventas_sucias)
print(f"\n[OK] Procesados: {len(ok)}")
print(f"\n[FAIL] Con errores: {len(errores)}")
for err in errores:
    print(f"    Fila {err["fila"]} : {err['error']}")