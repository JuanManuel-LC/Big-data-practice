import os
import shutil

# No toques: limpia carpetas de funciones anteriores
for c in ['data', 'src', 'tests']:
    shutil.rmtree(c, ignore_errors=True)

# Carpetas que necesitamos crear
carpetas = [
    "data/raw",
    "data/processed",
    "src",
    "tests"
]

existentes = 0

for carpeta in carpetas:
    os.makedirs(carpeta, exist_ok=True)
    
    if os.path.isdir(carpeta):
        existentes =+ 1
        print(f" Creada: {carpeta}")
    else:
        print(f" Falta: {carpeta}")

print()
print(f"{existentes} de {len(carpetas)} carpetas listas.")