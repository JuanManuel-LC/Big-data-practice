"""Escribe los cuerpos de los tres bloques: el try abre y devuelve el JSON; cada except avisa y devuelve lo que dice el docstring ({} o None)."""

import json

def leer_json_seguro(ruta):
    """Lee un JSON de forma segura.
    Devuelve dict si OK, {} si no existe, None si JSON inválido.
    """
    try:
        with open(ruta, "r", encoding='utf-8') as f:
            return json.load(f) # <- sustituye pass: abre ruta y devuelve json.load(f)
    except FileNotFoundError:
        print(f"   [AVISO] Archivo no encontrado: {ruta}")
        return {}
    except json.JSONDecodeError as e:
        print(f"   [ERROR] JSON inválido en {ruta} ({type(e).__name__})")
        return None

# ═══════════════════════════════════════════════════════════
# NO MODIFIQUES nada debajo de esta línea.
# ═══════════════════════════════════════════════════════════
print("1. Archivo que no existe:")
resultado = leer_json_seguro("no_existe.json")
print(f"   Resultado: {resultado}")

with open("test_ok.json", "w") as f:
    json.dump({"status": "ok"}, f)

print("")
print("2. Archivo válido:")
resultado = leer_json_seguro("test_ok.json")
print(f"   Resultado: {resultado}")

with open("test_bad.json", "w") as f:
    f.write("{esto no es json}")

print("")
print("3. JSON inválido:")
resultado = leer_json_seguro("test_bad.json")
print(f"   Resultado: {resultado}")
