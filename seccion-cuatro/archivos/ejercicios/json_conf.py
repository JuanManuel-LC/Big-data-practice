import json

config = {
    "ruta_entrada": "data/ventas.csv",
    "ruta_salida": "data/resultado.json",
    "umbral_minimo": 100.00,
    "incluir_impuestos": True,
    "tasa_impuesto": 0.21,
}

# Guarda config en el fichero, en formato JSON
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)   # <- json.dump(config, f, indent=2, ensure_ascii=False)

# Lee la configuración DESDE EL FICHERO (no del diccionario de arriba)
with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)       # <- json.load(f)

# No toques: mira qué se ha guardado y con qué tipos
# type(x).__name__ dice de qué tipo es un valor ("float", "str", "bool"...)
print("--- config.json ---")
with open("config.json", "r", encoding="utf-8") as f:
    print(f.read())
print(f"umbral_minimo: {cfg['umbral_minimo']}  (tipo: {type(cfg['umbral_minimo']).__name__})")

ventas = [50.0, 120.0, 89.0, 200.0, 30.0, 150.0]
filtradas = [v for v in ventas if v >= cfg["umbral_minimo"]]
print(f"Ventas >= {cfg['umbral_minimo']}€: {filtradas}")