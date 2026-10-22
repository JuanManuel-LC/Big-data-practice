-- SQL como calculadora
SELECT 1 + 1 AS resultado;

-- Manipular texto
SELECT 'Hola' || ' ' || 'mundo' AS saludo;

-- Fecha actual
SELECT CURRENT_DATE AS hoy;

-- Expresiones complejas
SELECT
    42 * 3.14 AS pi_por_42,
    ROUND(100.0 / 3, 2) AS un_tercio,
    LENGTH('BigDataStack') AS longitud;


-- Línea por línea:

-- SELECT 1 + 1 AS resultado → aritmética básica. AS da un nombre legible a la columna resultante.
-- SELECT 'Hola' || ' ' || 'mundo' → el operador || concatena textos en SQL estándar (equivalente al + de strings en Python).
-- CURRENT_DATE → función del sistema que devuelve la fecha actual sin hora.
-- 42 * 3.14 → aritmética con decimales.
-- ROUND(100.0 / 3, 2) → divide y redondea a 2 decimales. Nota: 100.0 (con decimal) fuerza división no-entera.
-- LENGTH('BigDataStack') → cuenta los caracteres del texto.

-- Ninguno usa FROM porque no estamos leyendo datos de una tabla — solo calculando expresiones.