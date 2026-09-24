# Bug: el total de ventas da 0, pero el CSV tiene datos
ventas = []
with open("ventas.csv") as f:
    for linea in f:
        campos = linea.strip().split(",")
        # print() detective: ver que hay en campos
        print(f"DEBUG campos: {campos}")  # <-- inspeccionar
        
        precio = campos[2]
        # print() detective: ver el tipo y valor
        print(f"DEBUG precio: {repr(precio)}, tipo: {type(precio)}")  # <-- inspeccionar
        
        ventas.append(precio)  # BUG: es string, no float!

# El print revela: precio es "45.99" (string), no 45.99 (float)
# Solucion: ventas.append(float(precio))

total = sum(ventas)  # TypeError si son strings, o 0 si la lista esta vacia
print(f"DEBUG total: {total}, len(ventas): {len(ventas)}")  # <-- verificar resultado