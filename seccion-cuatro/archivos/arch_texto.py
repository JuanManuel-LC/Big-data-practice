with open("datos_ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("producto,cantidad,precio\n")
    f.write("Laptop,5,1299.99\n")
    f.write("Monitor,12,349.50\n")
    f.write("Teclado,30,79.99\n")

print("Archivo creado.")

print()
# Leer el archivo completo
with open("datos_ejemplo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)

print()
# Leer linea por linea (Mejor para archivos grandes)
with open("datos_ejemplo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip()) # strip() le quita el "\n" al final de cada linea
        
print()
print("Adicional...")
# Para contar lineas sin recorrerlas una a una como en el caso anterior, "readlines()" te devuelve la lista entera de golpe. Mejor para archivos de menos de un millon de lineas
with open("datos_ejemplo.txt", "r", encoding="utf-8") as f:
    lineas = f.readline() #Lista con una entrada por linea
    print(lineas)
    print()
    print(f"El fichero tiene {len(lineas)} lineas")