-- DDL (Data Definition Lenguage): crear una tabla con 3 columnas
CREATE TABLE paises (
    id INTEGER PRIMARY KEY,     -- Identificador unico de cada fila
    nombre VARCHAR,             -- Texto de longitud variable
    continente VARCHAR
)

-- DML (Data Manipulation Lenguage): insertar varias filas de una vez
INSERT INTO paises (id, nombre, continente) VALUES
    (1, 'España', 'Europa'),
    (2, 'Portugal', 'Europa'),
    (3, 'Mexico', 'America');

-- Comprobar que los datos esten ahi
SELECT * FROM paises;


-- Línea por línea:

-- CREATE TABLE paises (...) → crea una tabla vacía con las columnas indicadas. Cada columna lleva un nombre y un tipo (INTEGER, VARCHAR).
-- PRIMARY KEY → garantiza que el id es único y no puede repetirse. Es la "matrícula" de cada fila.
-- INSERT INTO ... VALUES → introduce datos. La sintaxis multi-fila (fila1), (fila2), (fila3) es más limpia y más eficiente que tres INSERTs separados.
-- Los textos siempre van entre comillas simples (' '). Las dobles (" ") son para identificadores (nombres de tabla o columna), no para valores.
-- SELECT * FROM paises → comprueba el resultado. Es tu forma de verificar que el INSERT funcionó.