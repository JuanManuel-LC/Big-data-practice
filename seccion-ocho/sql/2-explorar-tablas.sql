-- Ver todas las tablas disponibles
SHOW TABLES;

-- Ver la estructura de una tabla (columnas y tipos)
DESCRIBE clientes;

-- Tambien funciona con esta sintaxis:
DESCRIBE pedidos;


-- Línea por línea:

-- SHOW TABLES → comando de metadata que lista todas las tablas de la base de datos. Es tu primer paso al llegar a un entorno nuevo.
-- DESCRIBE clientes → muestra columnas, tipos de datos y restricciones de la tabla. Es como leer el "plano" antes de construir.
-- DESCRIBE pedidos → lo mismo para otra tabla.

-- Estos comandos no modifican datos — solo muestran información sobre la estructura. Son seguros de ejecutar en cualquier momento.