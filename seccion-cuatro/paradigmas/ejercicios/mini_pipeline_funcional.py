"""Escribe tres funciones — una por etapa del pipeline — que filtren, transformen y acumulen con estilo funcional puro."""

from functools import reduce

clientes = [
    {"nombre": "Ana", "gasto": 1200},
    {"nombre": "Luis", "gasto": 89},
    {"nombre": "Maria", "gasto": 750},
    {"nombre": "Pedro", "gasto": 320},
    {"nombre": "Sara", "gasto": 2100},
    {"nombre": "Nuria", "gasto": 500},
]

IVA = 1.21
UMBRAL_VIP = 500

def filtrar_vips(clientes):
    """filter: solo los que gastan MÁS del umbral."""
    return list(filter(lambda c: c['gasto'] > UMBRAL_VIP, clientes))

def gastos_con_iva(vips):
    """map: de cada cliente, su gasto con el IVA aplicado."""
    return list(map(lambda c: c['gasto'] * IVA, vips))

def sumar(gastos):
    """reduce: acumula empezando en 0 y combina acum con cada x."""
    return reduce(lambda acum, x: acum + x, gastos, 0)

# No toques: encadena las tres funciones
vips = filtrar_vips(clientes)
total = sumar(gastos_con_iva(vips))
print(f"Clientes VIP: {len(vips)}")
print(f"Total VIP con IVA: {total:.2f}")
