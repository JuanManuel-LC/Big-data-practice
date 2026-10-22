-- IMPERATIVO (pseudocódigo Python):
-- resultado = []
-- for fila in clientes:
--     if fila.ciudad == 'Madrid':
--         resultado.append(fila.nombre)

-- DECLARATIVO (SQL):
SELECT nombre
FROM clientes
WHERE ciudad = 'Madrid'


-- Comparación directa entre paradigmas:

-- Imperativo (Python): defines cada paso — crear lista vacía, iterar, comprobar condición, añadir al resultado. Tú controlas el CÓMO.
-- Declarativo (SQL): SELECT nombre → qué columnas. FROM clientes → de qué tabla. WHERE ciudad = 'Madrid' → qué condición.

-- El motor SQL decide internamente cómo buscar (¿índice? ¿escaneo completo? ¿paralelismo?). Tú solo dices QUÉ quieres. Es más conciso y el optimizador suele ser más eficiente que un bucle manual.