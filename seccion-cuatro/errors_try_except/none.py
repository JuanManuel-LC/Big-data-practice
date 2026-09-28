# None es el valer que significa "aqui no hay nada"

def buscar_precio(catalogo, producto):
    if producto in catalogo:
        return catalogo[producto]
    return None     # No lo he encontrado

precio = buscar_precio({"USB": 12.99}, "Monitor")
print(precio)       # None
print(precio is None)       # True --> Asi se comprueba, con 'is', no con ==