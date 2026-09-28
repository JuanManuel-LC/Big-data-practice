La biblioteca estándar de Python es potente, pero el verdadero superpoder está en la comunidad. Hay más de 500,000 paquetes disponibles en PyPI (Python Package Index) — librerías que otros desarrolladores han escrito, probado y publicado para que tú no tengas que reinventar la rueda. Pandas, requests, pytest, black, pyspark... todo se instala con pip.

Piensa en pip como la app store de Python. ¿Necesitas manipular tablas de datos? pip install pandas. ¿Necesitas llamar a una API? pip install requests. ¿Necesitas testear tu código? pip install pytest. En 10 segundos tienes herramientas que costaron miles de horas construir.

## Pero antes de instalar nada: ¿dónde van las librerías?

Antes de lanzarte a hacer pip install, necesitas entender un problema fundamental. Imagina que tienes dos proyectos en tu ordenador. El proyecto A necesita la librería "requests" versión 2.28. El proyecto B necesita "requests" versión 2.31. Si ambos usan la misma instalación de Python, están condenados a pelear por la versión. Alguien pierde.

Este es el equivalente a tener una cocina compartida donde dos chefs necesitan aceite de oliva — pero uno necesita virgen extra y el otro de girasol, y solo hay un hueco en la estantería. Si metes uno, el otro desaparece. La solución es que cada chef tenga SU propia despensa. En Python, esa despensa privada se llama entorno virtual (venv).

## Entornos virtuales: tu burbuja aislada

Un entorno virtual (venv) es una copia aislada de Python dentro de tu proyecto. Cada proyecto tiene su propio venv con sus propias librerías. Lo que instales en un venv no afecta a nada fuera de él. Es como tener un taller limpio para cada proyecto, sin que las herramientas de uno se mezclen con las del otro.

Ahora que ya sabes qué son los módulos (lección 6) y cómo funcionan los imports, esto te hará sentido completo: un venv es básicamente un directorio con una copia de Python y una carpeta vacía donde pip instalará las librerías. Cuando activas el venv, tu terminal "redirige" los comandos python y pip para que apunten a esa copia local en vez de a la instalación global del sistema.

## Crear y activar el venv

Crear un venv es un comando. Activarlo es otro. El proceso es casi idéntico en ambos sistemas, con una diferencia clave: el comando de activación. A partir de ahora, ANTES de instalar cualquier librería con pip, siempre crearás y activarás un venv.

## 1. Crea una carpeta para tu proyecto

mkdir mi-proyecto-datos
cd mi-proyecto-datos

## 2. Crea el entorno virtual

python3 -m venv .venv

## 3. Actívalo

source .venv/bin/activate

## 4. Tu prompt cambia:

## (.venv) usuario@mac mi-proyecto-datos %

## 5. Verifica que python apunta al venv

python --version

## Python 3.12.4

La carpeta .venv NO se sube a Git. Añade ".venv/" a tu archivo .gitignore. La carpeta contiene binarios específicos de tu sistema operativo y puede pesar cientos de MB. Lo que SÍ se sube es el archivo requirements.txt con la lista de dependencias (lo verás en unos minutos).

## ¿Qué es pip y cómo funciona?

pip es el gestor de paquetes de Python. Viene incluido con Python desde la versión 3.4. Su trabajo es: descargar paquetes de internet (de PyPI por defecto), instalarlos en tu entorno y gestionar las dependencias entre paquetes.

# Ejemplos

pip install requests
pip install pandas

# (Dentro del venv, "pip" funciona igual en ambos sistemas)

# Instalar una versión específica

pip install requests==2.31.0

# Instalar versión mínima

pip install "requests>=2.28"

# Ver qué tienes instalado

pip list

# Ver detalles de un paquete

pip show requests

##

## ¿Y conda? ¿Y uv? Cuándo usar cada uno

pip no es la única forma de instalar librerías, y es normal cruzarte con otras dos. La diferencia de fondo es qué gestiona cada una. pip instala paquetes de Python (desde PyPI) y para aislar proyectos lo combinas con venv, como acabas de ver: son dos herramientas que se usan juntas. conda es distinto: es a la vez gestor de paquetes Y de entornos, y no se limita a Python — también instala dependencias del sistema (compiladores, librerías de C, versiones concretas de CUDA...). Por eso es habitual en ciencia de datos y machine learning, donde algunos paquetes son difíciles de compilar y conda te los trae ya listos. La contrapartida: es más pesado y sus entornos ocupan bastante más.

La regla práctica: para trabajo general de datos e ingeniería —lo que verás en esta plataforma— pip + venv es el estándar y con lo que debes quedarte. Considera conda si acabas en un equipo que ya lo usa, o si peleas con paquetes científicos que no compilan bien con pip. Y hay una tercera opción cada vez más popular, uv: hace lo mismo que pip + venv pero mucho más rápido y con los mismos comandos (uv venv, uv pip install), así que lo que aprendes aquí te sirve igual. No mezcles pip y conda en el mismo entorno sin necesidad: elige uno por proyecto y sé consistente.

## requirements.txt: la receta de tu proyecto

Cuando compartes tu proyecto con alguien (o contigo mismo en otro ordenador), esa persona necesita instalar las mismas librerías. El archivo requirements.txt es la lista de ingredientes — le dice a pip exactamente qué instalar y en qué versión.

# Generar requirements.txt con lo que tienes instalado

pip freeze > requirements.txt

# El archivo contiene algo como:

# requests==2.31.0

# pandas==2.1.4

# numpy==1.26.2

# Instalar todo desde requirements.txt (otro dev, otro PC)

pip install -r requirements.txt

pip freeze captura TODAS las dependencias, incluidas las transitivas (las que se instalaron automáticamente). Para proyectos serios, considera escribir requirements.txt manualmente solo con tus dependencias directas. Así controlas qué usas y evitas sorpresas.

Los números de versión de los ejemplos de esta lección son los que había cuando se escribió: sirven para ver la forma que tiene el fichero, no para copiarlos. Cuando montes el tuyo, pon las versiones que instales tú — y para eso está pip freeze, que las escribe solas.

## Resolver problemas de instalación

▹ Windows — Si pip falla con permisos, asegúrate de que PowerShell NO es administrador cuando trabajas con venvs.
▹ Mac — Si pip install falla con errores de compilación, instala Xcode Command Line Tools: xcode-select --install
▹ Ambos — "Could not find a version that satisfies": el paquete no existe o escribiste mal el nombre. Búscalo en pypi.org.
▹ Ambos — Si tu venv se corrompe: bórralo y crea uno nuevo. rm -rf .venv (Mac) o Remove-Item -Recurse .venv (Windows), luego recrea.
▹ Ambos — Actualizar pip: python -m pip install --upgrade pip
