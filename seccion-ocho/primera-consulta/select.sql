-- Ver todas las columnas de la tabla clientes
SELECT * FROM clientes;

-- Ver solo nombre y ciudad (mejor practica)
SELECT nombre, ciudad FROM clientes;

-- Puedes renombrar columnas con  AS (alias)
SELECT
    nombre AS cliente,
    email AS correo_electronico
FROM clientes;