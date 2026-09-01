import sys
import os
import platform

version = sys.version   # <- esta ya esta hecha, como modelo
sistema = platform.system() + " " + platform.release() # <- platform.system() + " " + platform.release()
directorio = os.getcwd() # <- carpeta actual. Pista: os.getcwd()


print(f"Python: {version}")
print(f"Sistema: {sistema}")
print(f"Directorio: {directorio}")

version_ok = sys.version_info >= (3, 10)
print(f"Version 3.10? {version_ok}")
print(f"Version_info, {sys.version_info}")