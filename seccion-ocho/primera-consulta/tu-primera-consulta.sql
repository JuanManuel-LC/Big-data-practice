-- Ver TODAS las columnas de la tabla clientes
SELECT * FROM clientes;

-- Ver solo nombre y ciudad (mejor practica)
SELECT nombre, ciudad FROM clientes;

-- Puedes renombrar columnas con AS (alias)
SELECT
    nombre AS cliente,
    email AS correo_electronico
FROM clientes;

-- FROM: Elegir tabla
-- Todos los productos
SELECT nombre, precio FROM productos;

-- Todas las categorias
SELECT * FROM categorias;

-- Todos los pedidos
SELECT id, cliente_id, importe, fecha FROM pedidos;

-- WHERE: Filtrar filas con condiciones
-- CLientes de Madrid
SELECT nombre, email
FROM clientes
WHERE ciudad = 'Madrid';

-- Productos que cuestan mas de 100
SELECT nombre, precio
FROM productos
WHERE precio > 100;

-- Pedidos completado
SELECT id, importe, fecha
FROM pedidos
WHERE estado = 'ompletado';