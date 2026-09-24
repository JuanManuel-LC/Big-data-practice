import json

def cargar_config(ruta):
    """Cargamos la configuracion JSON con manejo robusto de errores"""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"[AVISO] {ruta} no existe. Usando configuracion por defecto.")
        config = {"umbral": 100, "formato_salida": "json"}
    except json.JSONDecodeError as e:
        print(f"[ERROR] {ruta} tiene JSON inválido: {e}")
    else:
        # Se ejecuta SOLO si no hubo excepcion
        print(f"[OK] Configuracion cargada desde {ruta}")
    finally:
        # Se ejecuta SIEMPRE (haya o no error)
        print(f" Config activa: {config}")
    
    return config

# Probar con archivo existente y no existente
config = cargar_config("config.json")
config2 = cargar_config("no_existe.json")