-- Las primeras 5 filas de la tabla clientes
SELECT * FROM clientes LIMIT 5;

-- Las primeras 5 filas de pedidos
SELECT * FROM pedidos LIMIT 5;

-- Solo columnas especificas
SELECT nombre, ciudad, es_vip
FROM clientes
LIMIT 10

-- Cuantas filas tiene una tabla?
SELECT COUNT(*) AS total_filas FROM pedidos;


-- Línea por línea:

-- SELECT * FROM clientes LIMIT 5 → trae TODAS las columnas (*) pero solo 5 filas. Ideal para ver la "forma" de los datos sin descargar miles de filas.
-- SELECT * FROM pedidos LIMIT 5 → lo mismo para la tabla de pedidos. Compara estructuras rápidamente.
-- SELECT nombre, ciudad, es_vip FROM clientes LIMIT 10 → pide solo 3 columnas. Más eficiente y enfocado que *.
-- COUNT(*) → cuenta TODAS las filas de la tabla, sin importar si tienen NULLs. Es tu forma de medir el volumen de datos antes de lanzarte a explorar.

-- LIMIT es tu red de seguridad al explorar: sin él, una tabla con millones de filas inundaría tu pantalla (y tu memoria).