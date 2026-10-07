# Un caracter ocupa 1 byte, y cada escalon multiplica por 1024

bytes_totales = 1000000 * 200       # Un millon de registros de 200 carcateres

print(bytes_totales / 1024)     # 195312.5 kb
print(bytes_totales / (1024 * 1024))        # 190.7 MB

# Division entera: se queda con la parte de abajo, sin decimales
print(7 / 2)        # 3.5   division normal
print(7 // 2)       # 3 division entera -- Util para repartir en partes iguales