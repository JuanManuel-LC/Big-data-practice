from pathlib import Path

BASE = Path(__file__).resolve().parent

logs_dir = BASE / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)

# Crear archivos de ejemplo (esto ya esta hecho)
for i in range(1, 4):
    with open(logs_dir / f"server_{i}.txt", "w") as f:
        for j in range(i * 10):
            f.write(f"[INFO] Evento {j} del servidor {i}\n")
            
archivos = sorted(logs_dir.glob("*.txt"))
print(f"Archivos encontrados: {len(archivos)}")

# Contar las lineas de cada uno
total_lienas = 0
for archivo in archivos:
    with open(archivo, "r") as f:
        lineas = len(f.readlines())
    print(f" {archivo.name}: {lineas} lineas")
    total_lienas += lineas
    
print()
print(f"Total de lineas de todos los logs: {total_lienas}")
