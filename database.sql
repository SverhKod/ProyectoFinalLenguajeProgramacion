CREATE DATABASE braillerproyectofinal;
use braillerproyectofinal;

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    email VARCHAR(100)
);
CREATE TABLE historial (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    texto_original TEXT,
    texto_braille TEXT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);
CREATE TABLE progreso (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    ejercicio VARCHAR(50),
    puntaje INT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

