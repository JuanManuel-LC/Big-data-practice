-- Archivo: init.sql (Se ejecuta automaticamente al crear la DB)

CREATE TABLE IF NOT EXISTE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT null,
    email VARCHAR(100) UNIQUE NOT null,
    ciudad VARCHAR(50),
    fecha_registro DATE DEFAULT CURRENT_DATE
)


INSERT INTO clientes (nombre, email, ciudad) VALUES
('Ana García', 'ana@ejemplo.com', 'Madrid'),
('Carlos López', 'carlos@ejemplo.com', 'Barcelona'),
('María Fernández', 'maria@ejemplo.com', 'Valencia');