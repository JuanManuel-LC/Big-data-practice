# Tipos de datos en Python
# Guarda estos datos, cada uno en su tipo correcto:
#   producto "Laptop Gaming" · cantidad 15 · precio 1299.99
#   en_stock sí · categorías: electrónica, gaming, portátiles

producto = "Laptop Gaming"      # <- un texto (str)
cantidad = int("15")      # <- un número entero (int)
precio = float("1299.99")        # <- un número con decimales (float)
en_stock = bool("True")      # <- un booleano (bool): True o False
categorias = ['electrónica', 'gaming', 'portátiles']    # <- una lista con las tres categorías

# Conversión: pasa el precio a texto. Pista: str(precio)
precio_texto = str(precio)   # <- sustituye esto

# No toques estas líneas: muestran cada variable y su tipo
print(f"{producto} -> {type(producto)}")
print(f"{cantidad} -> {type(cantidad)}")
print(f"{precio} -> {type(precio)}")
print(f"{en_stock} -> {type(en_stock)}")
print(f"{categorias} -> {type(categorias)}")
print(f"Precio como texto: {precio_texto} -> {type(precio_texto)}")