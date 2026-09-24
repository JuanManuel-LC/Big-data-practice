Aquí va una verdad incómoda del trabajo con datos: las cosas SIEMPRE fallan. El CSV viene con una fila corrupta. La API devuelve un error 500 a las 3 de la madrugada. El archivo que esperabas no existe porque alguien lo movió. Un campo que debería ser numérico tiene el texto "N/A". Si tu script no sabe manejar estas situaciones, muere silenciosamente o peor — produce datos incorrectos sin avisar.

try/except es tu red de seguridad. Le dice a Python: "intenta ejecutar este código, y si algo sale mal, no explotes — haz esto otro en su lugar". Es la diferencia entre un script de principiante que funciona solo con datos perfectos y un programa que aguanta datos de verdad.

## Anatomía de un error de Python

Antes de aprender a MANEJAR errores, necesitas saber LEERLOS. Cuando Python encuentra un problema, no simplemente dice "error" y se calla. Te imprime un traceback — un informe detallado de qué pasó, dónde pasó y por qué. El problema es que la mayoría de principiantes ven ese bloque de texto rojo y entran en pánico. No deberías. Un traceback es un MAPA que te lleva directamente al problema.

La regla de oro: lee el traceback DE ABAJO ARRIBA. La última línea es la más importante — te dice QUÉ falló. Las líneas de arriba te dicen DÓNDE (archivo, función, línea exacta). Un traceback tiene tres partes: la cadena de llamadas (cómo llegó Python hasta ahí), la línea exacta que falló (el código que causó el problema), y el tipo de error con su mensaje (qué salió mal y por qué).

## La técnica del print() detective

Los errores que hemos visto producen un crash — Python se detiene y te dice qué pasó. Pero hay otra categoría de bugs más peligrosa: los errores lógicos. Tu script no explota, termina sin errores... pero el resultado está MAL. Calculaste un promedio incorrecto, filtraste de más, o el informe salió vacío. Estos bugs no tienen traceback — tienes que cazarlos tú.

La técnica más simple y efectiva para depurar errores lógicos es el "print() detective": colocar prints estratégicos para inspeccionar el estado de tus variables en puntos clave del flujo. No es elegante, pero funciona. Incluso ingenieros senior con 15 años de experiencia usan print() para entender qué está pasando dentro de un programa.

## Tipos de excepciones comunes en datos

Python tiene muchos tipos de excepciones. Cada una indica un problema diferente. En datos, te encontrarás con estas constantemente:

▹ ValueError — Un valor no se puede convertir: float("N/A"), int("abc")
▹ KeyError — Buscas una clave que no existe en un diccionario: registro["campo_inexistente"]
▹ FileNotFoundError — El archivo que intentas leer no existe
▹ TypeError — Operas con tipos incompatibles: "texto" + 5
▹ ZeroDivisionError — Divides entre cero (frecuente al calcular promedios con datos vacíos)
▹ IndexError — Accedes a una posición que no existe en una lista
▹ json.JSONDecodeError — El JSON que intentas parsear está malformado
▹ UnicodeDecodeError — El archivo tiene una codificación diferente a la esperada

ejemplo --> Archivo "./ejemplo1.py"
