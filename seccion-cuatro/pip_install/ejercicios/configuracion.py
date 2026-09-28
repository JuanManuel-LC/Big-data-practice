"""Carga la configuración del pipeline con valores por defecto para las variables que no estén definidas. Los cuatro nombres de variable ya están escritos; pon el valor por defecto correcto en cada uno."""

import os
from pathlib import Path
from dotenv import load_dotenv

env_file = Path(__file__).parent.parent / ".env"

# La letra 'a' es de append, 'w' sobrescribe el contenido, 'a' agrega
with open(env_file, "a") as f:
    f.write("PIPELINE_NOMBRE=ventas-diarias\n")
    f.write("PIPELINE_UMBRAL=250\n")

load_dotenv(env_file)

# Simular un .env (normalmente usarías dotenv)
# os.environ["PIPELINE_NOMBRE"] = "ventas-diarias"
# os.environ["PIPELINE_UMBRAL"] = "250"
# PIPELINE_MODO y PIPELINE_REINTENTOS no están definidos → usarán su default

def cargar_config():
    """Lee las cuatro variables de entorno y devuelve el diccionario.
    Cada una con su valor por defecto: sin-nombre, 100, desarrollo, 3.
    Recuerda: os.getenv("VARIABLE", "por_defecto") y que todo llega como texto."""
    return {
        "nombre": os.getenv("PIPELINE_NOMBRE", "sin-nombre"), 
        "umbral": int(os.getenv("PIPELINE_UMBRAL", "100")), 
        "modo": os.getenv("PIPELINE_MODO", "desarrollo"), 
        "reintentos": int(os.getenv("PIPELINE_REINTENTOS", "3"))
    }

# No toques: prueba tu función
config = cargar_config()

print("Configuración del pipeline:")
for clave, valor in config.items():
    print(f"  {clave}: {valor}")
