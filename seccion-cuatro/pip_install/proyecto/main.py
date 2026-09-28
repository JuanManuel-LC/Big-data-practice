import pipeline_ventas as pl

# ═══ MAIN: orquestar el pipeline ══════════════════════════════
def main():
    """Punto de entrada del pipeline"""
    print("=" * 50)
    print(" PIPELINE DE VENTAS DIARIAS")
    print("=" * 50)

    # Configuracion
    
    ruta_entrada = "data/ventas_dia.csv"
    ruta_salida = "data/resumen_dia.json"
    ruta_errores = "data/errores_dia.json"

    # 1. EXTRACT
    print("\n[1/4] Extrayendo datos...")
    ventas_raw = pl.extraer_ventas(ruta_entrada)
    print(f"    Leídos: {len(ventas_raw)} registros")

    # 2. TRANSFORM
    print("\n[2/4] Limpiando y transformando ...")
    ventas_limpias, errores = pl.transformar_ventas(ventas_raw)
    tasa_exito = len(ventas_limpias) / len(ventas_raw) * 100
    print(f"     Válidos: {len(ventas_limpias)} ({tasa_exito}%)")
    print(f"     Errores: {len(errores)}")

    # 3. ANALYZE
    print("[3/4] Generando resumen ejecutivi ...")
    resumen = pl.generar_resumen(ventas_limpias)
    print(f"    Total facturado: {resumen['total_facturado']}€")
    
    # 4. LOAD
    print("[4/4] Guardando resultado ...")
    pl.guardar_resultado(resumen, errores, ruta_salida, ruta_errores)
    print(f"    Resumen: {ruta_salida}")
    if errores:
        print(f"    Errores: {ruta_errores}")
        
if __name__ == "__main__":
    main()