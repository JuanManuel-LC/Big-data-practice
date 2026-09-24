from datetime import datetime, timedelta
from collections import Counter, defaultdict


#datetime - fundamental para datos temporales
ahora = datetime.now()
ayer = ahora - timedelta(days=1)
print(f"Hoy: {ahora.strftime('%Y-%m-%d %H:%M')}")
print(f"Ayer: {ayer.strftime('%Y-%m-%d')}")

#Counter --- contar ocurrencias (perfecto para analisis)
categorias = ["electronica", "ropa", "electronica", "comida", "ropa", "ropa"]
conteo = Counter(categorias)
print(f"Conteo: {conteo}")
print(f"Mas común: {conteo.most_common(1)}")

#Defaultdict --- diccionario con valor por defecto
ventas_por_dia = defaultdict(list)
print(ventas_por_dia)
ventas_por_dia["lunes"].append(100)
ventas_por_dia["lunes"].append(200)
ventas_por_dia["martes"].append(150)
print(dict(ventas_por_dia))

#strptime: de texto a fecha (la "p" es de "parse")
fecha = datetime.strptime("2024-01-15", "%Y-%m-%d")
print(fecha)                # 2024-01-15 00:00:00

#Restar dos fechas de una duracion; .days son los dias enteros
hoy = datetime(2026, 8, 18)
diferencia = hoy - fecha
print(f"Han pasado {diferencia.days} dias")
