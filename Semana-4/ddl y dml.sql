USE practicas;
-- ahora procedemos a crear una tabla
CREATE TABLE tareas(
-- nombre datatype [ configuraciones adicionales]
id INT AUTO_INCREMENT PRIMARY KEY,
titulo varchar(100) UNIQUE,
descripcion TEXT,
usuario_id int,
-- Crear relacion entre tablas
-- Indico entre parentesis la columna de esta tabla y luego la tabla(columbna)
FOREIGN KEY (usuario_id) references usuarios(id)
);

-- sublenguajes de sql
-- DDL Data definition language, sirve para definir estructuras de datos
-- crear bd, crear tablas, eliminar tablas (create,alter,drop)
-- DML data manipulation language,sirve para definir info en tablas
-- insertar,actualizar,eliminar,leer (insert,select,update,delete)
insert into usuarios (nombre, dni) values ('Emily Galdos', '70809010');
insert into usuarios (id,nombre, dni) values (default,'Juan Perez', '50607080');
insert into usuarios (id,nombre, dni) values 
(default,'Ana Sanchez', '12309010'),
(default, 'Jose Muñoz','11112222'),
(default, 'Renata Gonzalez','11113333');
insert into tareas (id,titulo,descripcion,usuario_id) values
(default,'ir a la playa', 'ire a loa playa el fin de semana',1),
(default, 'ir a la piscina','ire a la piscina a mis clases de natacion', 2);
select * from usuarios;

insert into usuarios (id,nombre, dni) values 
(default,'Ana Sanchez', '65656565'),
(default, 'Jose Muñoz','12121212');

select * from usuarios where nombre='Ana Sanchez' and id=3;

select * from tareas where usuario_id=1;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES 
(DEFAULT, 'Ir a comer', 'Comer un sabroso pollito a la brasa', 1),
(DEFAULT, 'Comer pizza', 'Comer una sabrosa pizza con peperoni', 1);


