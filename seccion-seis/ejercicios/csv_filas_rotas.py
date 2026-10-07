import csv
import io

csv_sucio = """id,nombre,email,edad
1,Ana,ana@mail.com,28
2,Pedro,pedro@mail.com
3,Lucía,lucia@mail.com,35,extra_campo
4,Carlos,carlos@mail.com,40
5,,sara@mail.com,22
6,Jorge,jorge@mail.com,treinta
"""

columnas_esperadas = 4
filas_ok = []
filas_error = []

# io.StringIO hace que un texto se comporte como si fuera un fichero
reader = csv.reader(io.StringIO(csv_sucio.strip()))
header = next(reader)          # next() consume la primera línea: la cabecera
print(header)

for i, fila in enumerate(reader, start=2):     # el header es la línea 1
    errores = []

    # Tres cosas que comprobar. La primera ya está hecha:
    if len(fila) != columnas_esperadas:
        errores.append(f"columnas: esperadas {columnas_esperadas}, tiene {len(fila)}")

    # <- ¿el nombre (columna 1) está vacío?  -> "nombre vacío"
    if len(fila) > 1 and fila[1].strip() == "":
        errores.append("Nombre vacio")

    # <- ¿la edad (columna 3) es un número?  -> f"edad no numérica: '{fila[3]}'"
    #    Ojo: si la fila viene corta, fila[3] no existe. Comprueba antes len(fila).
    if len(fila) >= 4:
        try:
            int(fila[3])
        except ValueError:
            errores.append(f"Edad no numerica: '{fila[3]}'")

    if errores:
        filas_error.append({"linea": i, "errores": errores})
    else:
        filas_ok.append(i)

# No toques
print(f"Filas válidas: {len(filas_ok)}")
print(f"Filas con error: {len(filas_error)}")
for e in filas_error:
    print(f"  Línea {e['linea']}: {e['errores']}")