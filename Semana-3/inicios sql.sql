-- Asi se crea una base de datos
CREATE DATABASE IF NOT EXISTS practicas;
USE practicas;
-- ahora procedemos a crear una tabla
CREATE TABLE usuarios(
-- nombre datatype [ configuraciones adicionales]
id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
nombre TEXT NOT NULL,
dni CHAR(8) INT 
);