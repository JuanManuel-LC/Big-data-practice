ventas = [45.99, 120.00, 89.50, 250.00, 30.00, 180.00, 15.00, 100.00, 399.99]
IVA = 1.21
UMBRAL = 100

def total_imperativo(ventas):
    """for + if + append, y sumar al final."""
        
    resultado = []
    for v in ventas:
        if v > UMBRAL:
            resultado.append(v * IVA)
    return sum(resultado)

def total_funcional(ventas):
    """filter para elegir, map para transformar, sum para sumar."""
    return sum(map(lambda v: v * IVA, filter(lambda v: v > UMBRAL, ventas)))

def total_comprehension(ventas):
    """Lo mismo en una sola línea."""
    return sum([v * IVA for v in ventas if v > UMBRAL])


# No toques: los tres tienen que dar el mismo número
print(f"Imperativo:    {total_imperativo(ventas):.2f}")
print(f"Funcional:     {total_funcional(ventas):.2f}")
print(f"Comprehension: {total_comprehension(ventas):.2f}")