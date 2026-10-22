## ¿Qué es DuckDB y por qué lo usamos aquí?
DuckDB es un motor de base de datos analítico creado en 2019 en el CWI (Centrum Wiskunde & Informatica) de Ámsterdam. A diferencia de PostgreSQL o MySQL — que necesitan un servidor corriendo, puertos abiertos, usuarios configurados — DuckDB es embebido: se ejecuta dentro de tu proceso. Cero configuración, cero servidor, cero dolores de cabeza. En esta plataforma, se ejecuta directamente en tu navegador gracias a WebAssembly.

¿Por qué no empezamos con PostgreSQL, como hace todo el mundo? Porque PostgreSQL es un motor transaccional (OLTP): está optimizado para que un cajero registre una venta, no para que un analista procese millones de filas. DuckDB es un motor analítico (OLAP): está optimizado exactamente para lo que tú vas a hacer — explorar datos, agregar, filtrar, cruzar tablas. Y habla el mismo SQL. Lo que aprendas aquí funciona casi igual en PostgreSQL, BigQuery, Redshift o cualquier otro motor — y cuando haya una diferencia que importa, te avisaré.


# Consejo de SENIOR!!

Consejo de senior: SELECT * es para explorar. En código que va a producción, siempre lista las columnas explícitamente. He visto pipelines romperse porque alguien añadió una columna de 10MB y el SELECT * empezó a devolver gigas de datos inesperados.

# Consejo de SENIOR!!

Error típico que verás al principio: poner comillas dobles en un texto ("Madrid" en vez de 'Madrid'). SQL interpreta las dobles como un nombre de columna, y el mensaje de error empieza por «Referenced column "Madrid"». En cuanto veas tu texto entre comillas dentro de un mensaje que habla de columnas, ya sabes: cambia las dobles por simples. Aprovecha además la línea de debajo: cuando el error ocurre dentro de un WHERE, DuckDB añade «Candidate bindings:» y te lista las columnas que SÍ existen en la tabla. Esa línea te va a sacar de casi todos los errores de nombre que cometas de aquí en adelante, no solo de éste.

## ¿Qué es una base de datos relacional?

Una base de datos relacional organiza la información en tablas. Cada tabla tiene columnas (los campos — nombre, email, edad) y filas (los registros — cada cliente individual). Las tablas se relacionan entre sí mediante claves. Piénsalo como un Excel con superpoderes: cada pestaña es una tabla, cada columna tiene un tipo fijo (texto, número, fecha) y puedes cruzar pestañas instantáneamente.

01. Tabla: una colección de datos sobre un tema (clientes, pedidos, productos).
02. Fila (registro): un elemento individual. Un cliente concreto, un pedido concreto.
03. Columna (campo): una propiedad. El nombre del cliente, la fecha del pedido.
04. Clave primaria (PK): el identificador único de cada fila. Nunca se repite.
05. Clave foránea (FK): una columna que apunta a la PK de otra tabla. Es el enlace entre tablas.

## Anatomía de una consulta SQL

▹ SELECT — lista las columnas que quieres ver en el resultado. Puedes poner * para "todas".
▹ FROM — indica de qué tabla lees los datos. Solo una tabla por ahora (luego veremos JOINs).
▹ WHERE — filtra filas que cumplen una condición. Es opcional: sin WHERE, obtienes TODAS las filas.
▹ El punto y coma (;) al final indica que la consulta terminó.