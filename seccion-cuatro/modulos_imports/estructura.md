# Estructura de un proyecto de datos

La carpeta crece con el proyecto, y hay tres formas de organizarla segun en que punto estes. Lo que no cambia nunca es lo primero: los datos que entran, separados de los datos que has generado tu. Cuando exploras, es la carpeta tipica de la seccion 2: data/raw, data/processed, netebooks para probar cosas, scripts para lo que ya funciona. Cuando el codigo se estabiliza, aparecen src/ y test/. Y cuando el proceso se automatiza y corre solo, los modulos acaban con nombres como extractors, transformers, loaders --- a ese patron se le llama ETL (Extract - Transform - Load), y es el plan de cada dia de un ingeniero de datos. Si vas por analisis, no lo montaras tú, pero vas a oirlo cada semana y conviene que sepas que hay dentro.

mi-proyecto/
├── data/
│ ├── raw/ # Datos originales (entrada)
│ └── processed/ # Datos procesados (salida)
├── src/
│ ├── **init**.py # Marca src como paquete
│ ├── extractors.py # Funciones para leer datos
│ ├── transformers.py # Funciones para transformar
│ └── loaders.py # Funciones para escribir resultados
├── main.py # Script principal (orquesta todo)
├── config.json # Configuración del proyecto
├── requirements.txt # Dependencias (pip install -r)
└── .gitignore # Archivos que no se suben a git

- data/raw/ → datos originales sin modificar. La "fuente de verdad" que nunca se toca.
- data/processed/ → datos ya transformados, listos para consumir.
- src/**init**.py → archivo vacío que marca la carpeta como un paquete Python importable.
- src/extractors.py, transformers.py, loaders.py → patrón ETL: cada archivo tiene una responsabilidad.
- main.py → orquestador: importa los módulos y ejecuta el flujo completo.
- config.json → parámetros externos (rutas, umbrales) separados del código.
- requirements.txt → lista de dependencias para que otro desarrollador pueda recrear tu entorno (lo verás en la lección de pip install).

Esta estructura escala desde un script de 3 archivos hasta un proyecto empresarial de 50 módulos.
