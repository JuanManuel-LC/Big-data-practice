# Lista de módulos que necesitamos
modulos_requeridos = [
    ("json", "Serialización JSON"),
    ("csv", "Lectura de CSVs"),
    ("os", "Sistema operativo"),
    ("pandas", "DataFrames"),       # Puede no estar
    ("requests", "HTTP client"),    # Puede no estar
    ("datetime", "Fechas"),
]

print("Verificación de dependencias:")
print("=" * 45)

disponibles = 0
faltantes = 0

for modulo, descripcion in modulos_requeridos:
    try:
        __import__(modulo)    # <- importa el módulo cuyo nombre está en la variable
                #    No puedes escribir "import modulo" (importaría uno llamado "modulo").
                #    Pista: __import__(modulo)
        print(f"  [OK] {modulo:15s} — {descripcion}")
        disponibles = disponibles + 1
    except ImportError:
        print(f"  [ERROR] {modulo:15s} — FALTA ({descripcion})")
        faltantes = faltantes + 1

print("")
print(f"Resultado: {disponibles} disponibles, {faltantes} faltantes")
