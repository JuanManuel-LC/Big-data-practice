from datetime import datetime

fechas_str = ["2024-01-15", "2024-03-22", "2024-02-08", "2024-04-01"]

#Fecha de referencia fija, para que el resultado no cambie cada dia
hoy = datetime(2024, 6, 1)

#Convierte cada texto en una fecha de verdad
#Pista: datetime.strptime(f, "%Y-%m-%d")
fechas = [datetime.strptime(f, "%Y-%m-%d") for f in fechas_str]

#Calcula los dias que han pasado desde cada fecha
# Pista: al restar dos fechas, .days te da los dias
for i, fecha in enumerate(fechas):
    dias = (hoy - fecha).days
    print(f"{fechas_str[i]} --> hace {dias} días")
    
    
#La fecha mas reciente de la lista
mas_reciente = max(fechas)
print("")
print(f"Mas reciente: {mas_reciente.strftime('%Y-%m-%d')}")
