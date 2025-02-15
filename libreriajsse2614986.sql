/*
 * @autor: Jhon Sebastian Serna
 * @fecha: 2023/11/17
 * @descripción: Creación de una base de datos
 *               para una librería.
*/

-- Eliminar la base de datos si existe.
-- Nota: Se debe cambiar xxxx por las iniciales de los nombres y apellidos
DROP SCHEMA IF EXISTS libreriajsse2614986;

-- Crear la base de datos si existe
-- Nota: Se debe cambiar xxxx por las iniciales de los nombres y apellidos
CREATE SCHEMA libreriajsse2614986;

-- Activar la base de datos
-- Nota: Se debe cambiar xxxx por las iniciales de los nombres y apellidos
USE libreriajsse2614986;

-- ************************** CREACIÓN DE LAS TABLAS **************************

-- Creación de la tabla 'clientes'
CREATE TABLE clientes (
    id_cliente INT NOT NULL AUTO_INCREMENT,
    identificacion VARCHAR(11) NOT NULL,
    nombres VARCHAR(25) NOT NULL,
    apellidos VARCHAR(25) NOT NULL,
    telefono VARCHAR(12) NOT NULL,
    direccion VARCHAR(100),
    correo_electronico VARCHAR(100) NOT NULL,
    estado VARCHAR(10) NOT NULL DEFAULT 'ACTIVO',
    PRIMARY KEY (id_cliente)
);

-- Creación de la tabla 'autores'
CREATE TABLE autores (
    id_autor INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(25) NOT NULL,
    apellidos VARCHAR(25) NOT NULL,
    estado VARCHAR(10) NOT NULL DEFAULT 'ACTIVO',
    PRIMARY KEY (id_autor)
);

-- Creación de la tabla 'categorias'
CREATE TABLE categorias (
    id_categoria INT NOT NULL AUTO_INCREMENT,
    categoria VARCHAR(40) NOT NULL,
    estado VARCHAR(10) NOT NULL DEFAULT 'ACTIVO',
    PRIMARY KEY (id_categoria)
);

-- Creación de la tabla 'libros'
CREATE TABLE libros (
    isbn INT NOT NULL,
    titulo VARCHAR(125) NOT NULL,
    fecha_pub DATE NOT NULL,
    categoria INT NOT NULL,
    precio INT NOT NULL,
    portada VARCHAR(128),
    cantidad_stock INT NOT NULL CHECK(cantidad_stock >= 0),
    estado VARCHAR(10) NOT NULL DEFAULT 'ACTIVO',
    PRIMARY KEY (isbn),
    FOREIGN KEY (categoria) REFERENCES categorias(id_categoria)
);

-- Creación de la tabla 'libro_por_autor'
CREATE TABLE libro_por_autor (
    id_autor INT NOT NULL,
    isbn INT NOT NULL,
    estado VARCHAR(10) NOT NULL DEFAULT 'ACTIVO',
    PRIMARY KEY (id_autor, isbn),
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY (isbn) REFERENCES libros(isbn)
);

-- Creación de la tabla 'pedido_cliente'
CREATE TABLE tbl_pedido_cliente (
    id_pedido INT NOT NULL AUTO_INCREMENT,
    nro_pedido INT NOT NULL,
    id_cliente INT NOT NULL,
    isbn INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    subtotal INT NOT NULL,
    estado VARCHAR(10) NOT NULL DEFAULT 'ACTIVO',
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (isbn) REFERENCES libros(isbn)
);

-- Creación de la tabla 'usuario' --
CREATE TABLE usuarios(
id_usuario INT NOT NULL AUTO_INCREMENT,
usuario VARCHAR(50) NOT NULL,
contrasena VARCHAR(50) NOT NULL,
PRIMARY KEY (id_usuario)
);
-- ************************ FIN CREACIÓN DE LAS TABLAS ************************
-- **************************** INSERCIÓN DE DATOS *****************************

-- Inserción de datos en la tabla 'usuarios'
INSERT INTO usuarios (usuario,contrasena) VALUES ('sebas','123');
-- Inserción de datos en la tabla 'clientes' --
INSERT INTO clientes (identificacion, nombres, apellidos, telefono, direccion, correo_electronico)
    VALUES ('98582870', 'Harol Mauricio', 'Gómez Zapata', '3043385981', NULL, 'hmgomezz@sena.edu.co');
    
INSERT INTO tbl_pedido_cliente (nro_pedido,id_cliente, isbn, fecha_pedido, cantidad, subtotal) VALUES (1,1,3725,"2023-12-01",5,500000);

ALTER TABLE tbl_pedido_cliente;

DELETE FROM clientes WHERE id_cliente = 2;

SELECT * FROM clientes;

SELECT * FROM libros;

ALTER TABLE tbl_pedido_cliente MODIFY fecha_pedido VARCHAR(25) NOT NULL;

ALTER TABLE libros MODIFY fecha_pub VARCHAR(25) NOT NULL;

ALTER TABLE cuentas ADD COLUMN id_usuario INT NOT NULL REFERENCES usuarios(id_usuario);

SELECT * FROM tbl_pedido_cliente;

SELECT id_pedido,nro_pedido,id_cliente,isbn, fecha_pedido,cantidad,subtotal,estado FROM tbl_pedido_cliente;

ALTER TABLE libros
MODIFY categoria VARCHAR(255) NOT NULL;  


-- Inserción de datos en la tabla 'autores'
INSERT INTO autores (nombres, apellidos) VALUES
    ('Marc', 'Cerasini'),               --  1
    ('Julio', 'Verne'),                 --  2
    ('Edgar', 'Allan Poe'), 	        --  3		
    ('Mary', 'Wollstonecraft Shelley'), --  4
    ('Ben', 'Mezrich'),                 --  5  
    ('Bram', 'Stoker'),                 --  6
    ('Bruno', 'Nievas'),                --  7
    ('César', 'García Muñoz'),          --  8
    ('Armando', 'Rodera'),              --  9
    ('Jane', 'Austen'),                 -- 10
    ('Emily', 'Bronte'),                -- 11
    ('Alejandro', 'Dumas'),             -- 12
    ('Gabriel', 'García Márquez'),      -- 13
    ('Nikos', 'Kazantzakis'),           -- 14
    ('Raymond', 'Carver'),              -- 15
    ('Umberto', 'Eco'),                 -- 16
    ('Ernest', 'Hemingway'),            -- 17
    ('Toni', 'Morrison'),               -- 18
    ('Haruki', 'Murakami'),             -- 19
    ('J.K.', 'Rowling'),                -- 20
    ('George', 'Orwell'),               -- 21
    ('William', 'Shakespeare'),         -- 22
    ('Charlotte', 'Bronte'),            -- 23
    ('Agatha', 'Christie'),             -- 24
    ('Charles', 'Dickens'),             -- 25
    ('Leo', 'Tolstoy'),                 -- 26
    ('Jose', 'Saramago'),               -- 27
    ('Jorge Luis', 'Borges'),           -- 28
    ('Albert', 'Camus'),                -- 29
    ('Ernesto', 'Sábato'),              -- 30
    ('Héctor Abad', 'Faciolince'),      -- 31
    ('Julio', 'Cortázar'),              -- 32
    ('Stephen', 'King'),                -- 33
    ('Mario', 'Vargas Llosa'),          -- 34
    ('Carlos', 'Ruiz Zafón');           -- 35


-- Inserción de datos en la tabla 'categorias'
INSERT INTO categorias (categoria) VALUES
    ('Acción y Aventura'), --  1
    ('Terror'),            --  2
    ('Ficción Moderna'),   --  3
    ('Suspenso'),          --  4
    ('Romance'),           --  5
    ('Narrativa'),         --  6
    ('Novela'),            --  7
    ('Poesía'),            --  8 
    ('Fantasía'),          --  9 
    ('Ficción');           -- 10 


-- Inserción de datos en la tabla 'libros'
INSERT INTO libros (isbn, titulo, fecha_pub, categoria, precio, portada, cantidad_stock) VALUES
    (3725, 'Operation Hell Gate', '2005-09-27',  1, 48000, 'no_portada.png', 100),          -- 3275,  1
    (7515, 'Godzilla 2000', '1997-11-11', 3, 65000, 'no_portada.png', 2),                   -- 7515,  1
    (3281, 'Miguel Strogoff', '2001-12-10',  1,  25000, 'no_portada.png', 100),             -- 3281,  2
    (5831, 'Viaje al centro de la Tierra', '1864-11-25', 7, 20000, 'no_portada.png', 1),    -- 5831,  2
    (3277, 'La vuelta al mundo en ochenta dias', '2003-05-22', 1, 32000, 'no_portada.png', 50),-- 3277,  2
    (4683, 'El Gato Negro', '1997-10-12', 2, 44000, 'no_portada.png', 100),                 -- 4683,  3
    (9781, 'Un sueño en un sueño', '1849-03-31', 8, 25000, 'no_portada.png', 5),            -- 9781,  3
    (7269, 'El corazón delator', '1999-08-15', 2, 48000, 'no_portada.png', 35),             -- 7269,  3 
    (4986, 'Frankenstein', '1990-03-01', 2, 55500, 'no_portada.png', 100),                  -- 4986,  4
    (6186, 'Mathilda', '1959-01-01', 3, 70000, 'no_portada.png', 9),                        -- 6186,  4
    (3852, 'Sexo en la Luna', '2011-06-01', 3, 29500, 'no_portada.png', 100),               -- 3852,  5
    (8000, 'The Antisocial Network', '2021-09-07', 6, 85000, 'no_portada.png', 10),         -- 8000,  5
    (4634, 'The midnight ride', '2022-03-22', 4, 35500, 'no_portada.png', 35),              -- 4634,  5
    (4159, 'Drácula', '1999-04-10', 2, 46800, 'no_portada.png', 100),                       -- 4159,  6
    (2266, 'La joya de las siete estrellas', '1903-01-01', 2, 50000, 'no_portada.png', 3),  -- 2266,  6
    (8991, 'La dama del sudario', '1995-12-07', 2, 40000, 'no_portada.png', 45),            -- 8991,  6
    (4287, 'Realidad Aumentada', '2001-03-13', 4, 35200, 'no_portada.png', 100),            -- 4287,  7
    (2185, 'Lo que el hielo atrapa', '2015-01-01', 1, 61000, 'no_portada.png', 0),          -- 2185,  7
    (4428, 'Juicio Final, Sangre en el Cielo', '2009-05-30', 4, 40000, 'no_portada.png', 100),  -- 4428,  8
    (2168, 'Herederos del Cielo', '2021-03-19', 3, 20000, 'no_portada.png', 3),             -- 2168,  8
    (4660, 'El Enigma de los Vencidos', '2000-11-25', 4, 38500, 'no_portada.png', 100),     -- 4660,  9
    (1713, 'El Aroma Del Miedo', '2017-09-05', 4, 35000, 'no_portada.png', 4),              -- 1713,  9
    (5784, 'Orgullo y Prejuicio', '2003-09-25', 5, 36100, 'no_portada.png', 100),           -- 5784, 10
    (3069, 'Darcy and Elizabeth', '1813-12-12', 5, 54500, 'no_portada.png', 15),            -- 3069, 10
    (1331, 'Lady Susan', '2000-01-28', 7, 38000, 'no_portada.png', 25),                     -- 1331, 10
    (6039, 'Cumbres Borrascosas', '1998-11-25', 5, 60800, 'no_portada.png', 100),           -- 6039, 11
    (6154, 'No coward soul is mine', '1990-10-12', 8, 48000, 'no_portada.png', 22),         -- 6154, 11
    (6182, 'La Dama de las Camelias', '1995-07-28', 5, 57600, 'no_portada.png', 100),       -- 6182, 12
    (6073, 'Black', '1858-12-01', 7, 25000, 'no_portada.png', 13),                          -- 6073, 12
    (2190, 'Los tres mosqueteros', '1997-08-04', 1, 66000, 'no_portada.png', 55),           -- 2190, 12
    (7297, 'Cien Años de Soledad', '1990-04-27', 6, 39500, 'no_portada.png', 100),          -- 7297, 13
    (2437, 'Crónica de Una Muerte Anunciada', '2016-07-15', 6, 48000, 'no_portada.png', 100),  -- 2437, 13
    (1280, 'Alexis Zorba, El Griego', '2010-11-25', 6, 38500, 'no_portada.png', 100),       -- 1280, 14
    (7211, 'Libertad o muerte', '1953-12-31', 7, 10000, 'no_portada.png', 20),              -- 7211, 14
    (2875, 'Cathedral', '2004-08-15', 6, 25700, 'no_portada.png', 100),                     -- 2875, 15
	(6240, 'De qué hablamos cuando hablamos de amor', '2000-11-18', 10, 37000, 'no_portada.png', 45), -- 6240, 15
    (9788, 'Si me necesitas, llámame', '2000-01-31', 8, 29000, 'no_portada.png', 10),       -- 9788, 15
    (8807, 'El Nombre de la Rosa', '2011-05-24', 7, 68000, 'no_portada.png', 100),          -- 8807, 16
    (5118, 'El cementerio de Praga', '2010-10-25', 7, 70000, 'no_portada.png', 32),         -- 5118, 16
    (5170, 'Historia de la belleza', '2004-10-06', 5, 85000, 'no_portada.png', 19),         -- 5170, 16
    (5963, 'El viejo y el mar', '1952-12-31', 7, 45000, 'no_portada.png', 0),               -- 5963, 17 
    (8900, 'Fiesta', '1926-10-22', 7, 70500, 'no_portada.png', 20),                         -- 8900, 17
    (1400, 'Sula', '1973-11-30', 1, 80000, 'no_portada.png', 10),                           -- 1400, 18
    (9778, 'Volver', '2012-05-08', 5, 30000, 'no_portada.png', 3),                          -- 9778, 18
    (2022, 'After Dark', '2004-09-30', 3, 65000, 'no_portada.png', 6),                      -- 2022, 19
    (5264, 'Kafka en la orilla', '2002-09-12', 7, 50000, 'no_portada.png', 0),              -- 5264, 19
    (8468, 'Romeo y Julieta', '1597-12-01', 5, 55500, 'no_portada.png', 30),                -- 8468, 22
    (5335, 'El sueño de una noche de verano', '1605-01-01', 7, 30500, 'no_portada.png', 10),-- 5335, 22
    (5437, 'El asesinato de Roger Ackroyd', '1926-06-06', 3, 90000, 'no_portada.png', 2),   -- 5437, 24
    (1378, 'El misterioso caso de Styles', '1867-12-31', 6, 10000, 'no_portada.png', 8),    -- 1378, 24
    (2473, 'A Tale of Two Cities', '2007-10-31', 7, 20000, 'no_portada.png', 4),            -- 2473, 25
    (4979, 'Calle sin salida', '1867-12-31', 6, 10000, 'no_portada.png', 5),                -- 4979, 25
    (4812, 'Guerra y paz', '1869-12-12', 7, 100000, 'no_portada.png', 5),                   -- 4812, 25
    (7419, 'Las tres preguntas', '1903-01-31', 1, 60000, 'no_portada.png', 22),             -- 7419, 26
    (2511, 'Ensayo sobre la ceguera', '1995-04-20', 7, 50000, 'no_portada.png', 43),        -- 2511, 27
    (5486, 'Intermitencias de la muerte', '2005-06-09', 7, 55000, 'no_portada.png', 25),    -- 5486, 24
    (2478, 'La biblioteca de Babel', '2001-07-19', 10, 35000, 'no_portada.png', 45),        -- 2478, 28
    (2560, 'El inmortal', '2002-09-29', 10, 40000, 'no_portada.png', 55),                   -- 2560, 28
    (9784, 'El extanjero', '1995-04-19', 7, 60000, 'no_portada.png', 33),		    -- 9784, 29
    (2239, 'La caída', '1998-06-14', 7, 66000, 'no_portada.png', 45),                       -- 2239, 29
    (8432, 'El túnel', '2001-01-21', 7, 58000, 'no_portada.png', 30),                       -- 8432, 30
    (9286, 'Sobre héroes y tumbas' , '2003-04-12', 7, 55000, 'no_portada.png', 35),         -- 9286, 30
    (7357, 'La oculta', '2014-09-16', 10, 45000, 'no_portada.png', 45),                     -- 7357, 31
    (4124, 'Angosta', '2003-11-06', 10, 48000, 'no_portada.png', 25),                       -- 4121, 31
    (4572, 'Rayuela', '1990-06-28', 7, 40500, 'no_portada.png', 20),                        -- 4572, 32
    (6691, 'Final del juego', '1995-09-30', 10, 44500, 'no_portada.png', 53),               -- 6691, 32
    (6439, 'La cúpula', '2009-10-10', 7, 66500, 'no_portada.png', 60),                      -- 6439, 33
    (1236, 'Doctor sueño', '2013-09-24', 2, 60500, 'no_portada.png', 36),                   -- 1236, 33
    (9959, '1984', '2000-07-27', 10, 57500, 'no_portada.png', 56),                          -- 9959, 34       
    (8897, 'Subir por aire', '1990-05-07', 10, 43000, 'no_portada.png', 60),                -- 8897, 34
    (8185, 'La fiesta del chivo', '2000-07-17', 7, 35000, 'no_portada.png', 28),            -- 8185, 35
    (5455, 'El héroe discreto', '2013-09-02', 10, 32500, 'no_portada.png', 38),             -- 5455, 35
    (2595, 'La sombra del viento', '2001-05-12', 4, 44000, 'no_portada.png', 22),           -- 2595, 36
    (5552, 'El juego del ángel', '2008-04-17', 7, 28500, 'no_portada.png', 20);          -- 5552, 36


-- ************************** FIN INSERCIÓN DE DATOS ***************************


SELECT isbn,titulo,fecha_pub,b.categoria,precio,portada,cantidad_stock,a.estado FROM libros a
inner join categorias b on a.categoria = b.id_categoria

CREATE DATABASE login_registerdb 