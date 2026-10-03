#Primero creamos el archivo .env con configuracion
# (Este archivo NO se sube a git - cintiene secretos)
import os
from pathlib import Path

archivo = Path(__file__).parent / ".env"
archivo.parent.mkdir(parents=True, exist_ok=True)

# Simular un .env escribiendolo
with open(archivo, "w") as f:
    f.write("RUTA_DATOS=data/ventas.csv\n")
    f.write("UMBRAL_VIP=500\n")
    f.write("MODO=desarrollo\n")


#Ahora usar dotenv para cargar esas variables
from dotenv import load_dotenv

load_dotenv()   # Carga las variables

ruta = os.getenv("RUTA_DATOS")
umbral = int(os.getenv("UMBRA_VIP", "100"))     # 100 es el default
modo = os.getenv("MODO")

print(f"Ruta de datos: {ruta}")
print(f"Umbra VIP: {umbral}")
print(f"Modo: {modo}")

if modo == "desarrollo":
    print("[AVISO] Ejecutando el modo desarrollo")
