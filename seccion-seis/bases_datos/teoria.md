## Bases de datos NoSQL: cuando las tablas no son suficientes

Relacional no es la única opción. En los años 2000, con la explosión de internet, surgieron necesidades que las bases de datos relacionales manejaban con dificultad: almacenar documentos con estructura variable (como perfiles de usuario donde cada uno tiene campos diferentes), manejar millones de lecturas por segundo (como un feed de red social) o almacenar relaciones complejas (como "amigos de amigos de amigos"). Así nacieron las bases de datos NoSQL — "No Solo SQL".

▹Documentos (MongoDB, CouchDB): almacenan documentos JSON. Cada documento puede tener estructura diferente. Ideal para catálogos con atributos variables.
▹Clave-valor (Redis, DynamoDB): como un diccionario gigante. Ultra rápidas para lecturas simples. Ideal para caché y sesiones.
▹Columnar (Cassandra, HBase): optimizadas para escribir y leer enormes cantidades de datos distribuidos. Ideal para series temporales y logs.
▹Grafos (Neo4j): almacenan nodos y relaciones. Ideales para redes sociales, recomendaciones, detección de fraude.

## Relacional vs NoSQL: no es una competencia

El error más común es pensar que tienes que elegir. La realidad es que la mayoría de empresas usan AMBOS: una base relacional para los datos transaccionales del negocio (clientes, pedidos, facturas — donde la consistencia es crítica) y una o varias NoSQL para casos específicos (caché en Redis para velocidad, MongoDB para un catálogo con atributos variables, etc.). Son herramientas complementarias, no competidoras.

Consejo de senior: si estás empezando un proyecto y no sabes qué base elegir, elige relacional (PostgreSQL). Cubre el 90% de los casos. Solo elige NoSQL cuando tengas un problema concreto que relacional no resuelve bien. He visto equipos elegir MongoDB "porque es moderno" y luego sufrir porque necesitaban JOINs y transacciones que MongoDB no ofrecía bien. Elige la herramienta para el problema, no al revés.

## La base de datos como servidor: el modelo cliente-servidor

A diferencia de un archivo (que simplemente está en tu disco), una base de datos es un PROGRAMA que está corriendo constantemente, esperando peticiones. Es como un restaurante: el cocinero (la base de datos) está siempre listo en la cocina, y los camareros (tu código Python, la app web, etc.) le pasan comandas. Tú (cliente) envías una petición ("dame los pedidos de enero"), la base de datos la procesa y te devuelve el resultado. Este modelo permite que 1000 clientes pregunten al mismo tiempo sin problema.

En este curso practicarás SQL directamente en el navegador con DuckDB, que es una base de datos ligera diseñada para análisis. Pero conceptualmente, ya entiendes la idea: una base de datos es un programa especializado en gestionar datos, no un archivo pasivo. Las empresas usan servidores de bases de datos (PostgreSQL, MySQL, etc.) que están encendidos 24/7 atendiendo consultas.

Error que veo en juniors todo el tiempo: usar la base de datos como vertedero. "Guardemos todo por si acaso". Una base de datos tiene un coste: espacio, mantenimiento, backups, migraciones. Cada tabla que creas es una tabla que alguien tendrá que mantener durante años. Antes de crear una tabla, pregúntate: "¿quién la va a usar y para qué?". Si no tienes respuesta clara, no la crees.

## Las zonas de los datos: raw, procesado y listo

En un sistema profesional, los datos no saltan directamente del origen al reporte. Pasan por zonas, como estaciones en un tren. La idea es simple: mantener el dato original intacto (por si necesitas reprocesar) y tener versiones cada vez más limpias y útiles.

▹ Zona Raw (bruto): el dato tal cual llega del origen. Sin tocar. El JSON original, el CSV del proveedor. Es tu seguro: si algo sale mal en la transformación, siempre puedes volver aquí.
▹ Zona Procesada (limpio): el dato ya limpio, validado y en formato estándar. Has quitado duplicados, convertido tipos, validado rangos. Listo para transformar.
▹ Zona Final (listo para uso): el dato agregado, enriquecido y en el formato que el consumidor necesita. El reporte, la tabla del dashboard, el archivo para el equipo de compras.
En el proyecto que cerró Python desde cero (el script que procesaba un CSV de ventas) ya hiciste esto intuitivamente: leíste el archivo original (raw), lo limpiaste (procesado) y generaste un resultado (final). En sistemas profesionales, estas zonas son carpetas en un disco, carpetas en la nube o tablas diferentes en una base de datos. La idea es idéntica.

Regla de oro que aprendí por las malas: NUNCA borres los datos raw. Jamás. Aunque sean feos, estén sucios y parezcan inútiles. Son tu fuente de verdad. Si descubres un bug en tu transformación dentro de 6 meses, necesitarás los datos originales para reprocesar. Si los borraste, estás perdido.

## Cuándo corren los pipelines: batch vs continuo

Hay dos grandes modos de ejecutar pipelines. El modo BATCH (lote) significa que el pipeline se ejecuta a intervalos: cada hora, cada día, cada semana. Es como el correo postal: se acumula durante el día y se reparte una vez. El modo CONTINUO (streaming) significa que los datos se procesan según llegan, en tiempo real o casi real. Es como los mensajes de WhatsApp: instantáneos.

El 90% de los pipelines en la industria son batch. El reporte de ventas diario, la carga de datos del proveedor semanal, la actualización del dashboard cada hora. Streaming se usa cuando necesitas reaccionar en segundos: detección de fraude, alertas de temperatura, actualizaciones de ubicación de repartidores. Empezarás con batch — es más simple, más predecible y suficiente para la mayoría de casos.

## ¿Qué puede salir mal? (spoiler: todo)

Los pipelines parecen simples en teoría: leer, transformar, guardar. ¿Qué puede fallar? TODO. Y lo hará. A las 3 de la mañana de un domingo:

▹ El origen no responde: la API del proveedor está caída, el archivo no llegó, el servidor está lleno.
▹ Los datos cambiaron de formato: el proveedor añadió una columna nueva sin avisarte, o cambió "precio" por "price".
▹ Datos corruptos: una fila tiene caracteres extraños, un número es negativo cuando no debería, un campo fecha tiene formato incorrecto.
▹ El destino está lleno: el disco se llenó, la base de datos no acepta más conexiones.
▹ Error parcial: procesaste 999.000 de 1.000.000 registros y el 999.001 falló. ¿Guardas los 999.000 o tiras todo?
▹ Duplicados: el pipeline se ejecutó dos veces (porque alguien lo relanzó sin querer). ¿Datos duplicados en el destino?

El error más caro que he visto: un pipeline que falló silenciosamente durante 3 semanas. No dio error — simplemente dejó de procesar datos nuevos porque el archivo del origen cambió de nombre. Nadie se dio cuenta hasta que el director financiero preguntó por qué las ventas del mes parecían bajas. Lección: pon alertas desde el día 1. Si tu pipeline no procesa datos, TIENES que enterarte.
