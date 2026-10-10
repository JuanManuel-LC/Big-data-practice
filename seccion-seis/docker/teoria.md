## Las instrucciones fundamentales del Dockerfile
▹ FROM: "Empieza con esta imagen base". Siempre es la primera línea. Define los cimientos de tu imagen.
▹ WORKDIR: "Trabaja dentro de este directorio". Crea el directorio si no existe y se posiciona ahí. Es como hacer cd pero dentro de la imagen.
▹ COPY: "Copia archivos de tu ordenador al contenedor". COPY <origen-en-tu-PC> <destino-en-la-imagen>.
▹ RUN: "Ejecuta este comando DURANTE la construcción de la imagen". Para instalar dependencias, crear directorios, etc.
▹ CMD: "Ejecuta este comando CUANDO el contenedor arranque". Es el comando por defecto al hacer docker run.
▹ ENV: "Define una variable de entorno". Disponible tanto durante la build como en runtime.
▹ EXPOSE: "Documenta que este contenedor escucha en este puerto". Es informativo — no abre el puerto realmente.

El orden de las instrucciones en un Dockerfile IMPORTA MUCHO para el rendimiento. Regla de oro: pon las cosas que cambian MENOS frecuentemente arriba (instalar dependencias del sistema, pip install) y las que cambian MÁS frecuentemente abajo (copiar tu código). Así maximizas el cache.