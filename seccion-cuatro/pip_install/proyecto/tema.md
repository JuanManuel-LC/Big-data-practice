# Proyecto: script que procesa un CSV de ventas

Ha llegado el momento de unir todo lo que has aprendido en un proyecto real. Imagina este escenario: trabajas en el equipo de datos de una tienda online. Cada día a las 7:00 de la mañana, el sistema de ventas genera un archivo CSV con todas las transacciones del día anterior. Tu trabajo es procesar ese archivo y generar un resumen ejecutivo que el CEO revisa antes de la reunión de las 9:00.

El CSV viene "sucio" — tiene filas con datos faltantes, precios con formato incorrecto, fechas inconsistentes. Tu script tiene que ser robusto: no puede explotar porque una fila entre miles esté mal. Tiene que limpiar, calcular y reportar. Es tu primer programa completo que lee datos, los transforma y deja el resultado escrito.

## El problema de negocio

▹ ENTRADA: CSV con ventas del día (fecha, producto, categoría, cantidad, precio_unitario, cliente)
▹ PROCESO: Limpiar datos sucios, calcular totales, agrupar por categoría
▹ SALIDA: Archivo JSON con el resumen ejecutivo del día
▹ RESTRICCIÓN: El script debe reportar errores sin detenerse (tolerancia a fallos)
