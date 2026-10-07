# El CSV perfecto: funciona bien
csv_perfecto = """nombre,ciudad,edad
Ana López,Madrid,28
Carlos Ruiz,Barcelona,35
"""

# El CSV del INFIERNO: problemas reales
csv_infernal = """nombre,direccion,importe
Ana López,"Calle Mayor, 5",29.99
"Pedro ""El Grande""",Av. Diagonal 100,150.00
María\nGarcía,Sin dirección,
"""

# Problemas:
# 1. Comas dentro del campo → requiere comillas
# 2. Comillas dentro del campo → requiere escape (doble comilla)
# 3. Saltos de línea dentro del campo → rompe el parseo naive
# 4. Campo vacío al final → ¿es None o string vacío?

print("CSV parece simple... hasta que no lo es")