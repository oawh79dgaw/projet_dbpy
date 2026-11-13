CREATE SCHEMA IF NOT EXISTS braintraining;

USE braintraining;

CREATE TABLE IF NOT EXISTS excercices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    excercice_id INT NOT NULL,
    FOREIGN KEY (excercice_id)
    REFERENCES excercices(id),
    date DATETIME NOT NULL,
    duration TIME(3) NOT NULL,
    nb_try SMALLINT NOT NULL,
    nb_ok SMALLINT NOT NULL
);