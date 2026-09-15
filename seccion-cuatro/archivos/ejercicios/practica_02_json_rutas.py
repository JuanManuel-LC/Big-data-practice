"""Practica 2: configuracion JSON y rutas con Path.

Completa solamente las lineas marcadas con TODO. Ejecuta este archivo desde la
carpeta `ejercicios`; al terminar debe existir la carpeta `datos_practica` y el
fichero `config_practica.json`.
"""

import json
from pathlib import Path


config = {
    "ruta_entrada": "datos_practica/ventas.csv",
    "ruta_salida": "datos_practica/resumen.json",
    "umbral_minimo": 100.00,
    "incluir_impuestos": True,
}

ruta_carpeta = Path("archivos_practica2")
ruta_json_config = ruta_carpeta / "config_practica.json"


ruta_carpeta.mkdir(parents=True, exist_ok=True)

# Pista: usa indent=2 y ensure_ascii=False para que el JSON sea legible.
with open(ruta_json_config, "w", encoding="utf-8") as archivo_json:
    json.dump(config, archivo_json, indent=2, ensure_ascii=False)

with open(ruta_json_config, "r", encoding="utf-8") as f:
    cfg = json.load(f)


cfg["umbral_minimo"] = 150.00


with open(ruta_json_config, "w", encoding="utf-8") as nuevo_json:
    json.dump(cfg, nuevo_json, indent=2, ensure_ascii=False)
    
ruta_entrada = ruta_carpeta / cfg["ruta_entrada"]
ruta_salida = ruta_carpeta / cfg["ruta_salida"] 

ruta_entrada.parent.mkdir(parents=True, exist_ok=True)

if ruta_entrada.exists():
    print(f"El archivo {ruta_entrada.name} existe")
else:
    print(f"El archivo {ruta_entrada.name} no existe")


print("Archivos CSV encontrados:")
for archivo_csv in ruta_entrada.parent.glob("*.csv"):
    print(archivo_csv.name)


# Cuando termines los TODO, descomenta este bloque para revisar el JSON guardado.
with open(ruta_json_config, "r", encoding="utf-8") as archivo:
    print(archivo.read())
