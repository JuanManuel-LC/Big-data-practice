## Las instrucciones fundamentales del Dockerfile
▹ FROM: "Empieza con esta imagen base". Siempre es la primera línea. Define los cimientos de tu imagen.
▹ WORKDIR: "Trabaja dentro de este directorio". Crea el directorio si no existe y se posiciona ahí. Es como hacer cd pero dentro de la imagen.
▹ COPY: "Copia archivos de tu ordenador al contenedor". COPY <origen-en-tu-PC> <destino-en-la-imagen>.
▹ RUN: "Ejecuta este comando DURANTE la construcción de la imagen". Para instalar dependencias, crear directorios, etc.
▹ CMD: "Ejecuta este comando CUANDO el contenedor arranque". Es el comando por defecto al hacer docker run.
▹ ENV: "Define una variable de entorno". Disponible tanto durante la build como en runtime.
▹ EXPOSE: "Documenta que este contenedor escucha en este puerto". Es informativo — no abre el puerto realmente.

El orden de las instrucciones en un Dockerfile IMPORTA MUCHO para el rendimiento. Regla de oro: pon las cosas que cambian MENOS frecuentemente arriba (instalar dependencias del sistema, pip install) y las que cambian MÁS frecuentemente abajo (copiar tu código). Así maximizas el cache.

## Multi-stage builds: imágenes limpias de producción
A veces necesitas herramientas pesadas para CONSTRUIR tu aplicación (compiladores, cabeceras de desarrollo, gcc) pero no las necesitas para EJECUTARLA. Un multi-stage build usa dos etapas: una para construir, otra para ejecutar. Solo la segunda acaba en la imagen final.

# Comandos
# Listar todos los volúmenes
docker volume ls

# Inspeccionar un volumen (ver dónde está en tu disco)
docker volume inspect pgdata

# Borrar un volumen específico
docker volume rm pgdata

# Borrar TODOS los volúmenes no usados (¡cuidado!)
docker volume prune

# Volumenes

# 1. Ver si se aplico la configuracion de los volumenes
docker compose config --volumes

# 2. Ver cuánto hay por limpiar
docker system df

# 3. Listar volúmenes (ventas_data tiene datos que NO puedes perder)
docker volume ls

# 4. Borrar los contenedores parados (retienen las imágenes)
docker container prune -f

# 5. Borrar las imágenes que ya no usa nadie
docker image prune -a -f

# OJO: NO uses 'docker volume prune -a' — ese borraría ventas_data.
# Comprueba que sigue:
docker volume ls


## Receta 1: PostgreSQL listo para SQL
PostgreSQL es la base de datos que usarás en la skill de SQL. Aquí tienes el docker-compose.yml definitivo que usarás durante todo el track: {docker-para-datos/postgres-sql.yml}

El truco del /docker-entrypoint-initdb.d/ es brillante: cualquier archivo .sql que pongas en esa carpeta se ejecuta AUTOMÁTICAMENTE la primera vez que PostgreSQL arranca. Perfecto para crear tablas y cargar datos de ejemplo sin esfuerzo manual.

CUIDADO: PostgreSQL SOLO ejecuta los scripts de initdb.d cuando el volumen de datos está vacío (primera vez). Si ya tenías el contenedor corriendo de lecciones anteriores, el pgdata ya existe y el init.sql se ignora silenciosamente. Solución: ejecuta "docker compose down -v" para borrar el volumen y empezar limpio. La -v es clave — sin ella solo para el contenedor pero mantiene los datos.