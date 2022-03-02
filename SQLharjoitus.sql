CREATE TABLE person (
    Id      SERIAL PRIMARY KEY,
    name    varchar(255) NOT NULL,
    age     int NOT NULL,
    student boolean
);

INSERT INTO person VALUES
    (1,'Olli', 32, true),
    (2,'Malli', 99, false);

INSERT INTO person (name,age,student) VALUES ('matti', 25, true);

TABLE person;

SELECT * FROM person;

SELECT name FROM person;

SELECT age,id FROM person;

SELECT age,id AS identifier FROM person;

SELECT * FROM person ORDER BY name;

SELECT * FROM person ORDER BY name ASC;

SELECT * FROM person ORDER BY name DESC;

SELECT sum(age) FROM person;

SELECT avg(age) FROM person;

UPDATE person SET   name = 'Eimatti',
                    age = 52,
                    student = false
    WHERE id = 4;

UPDATE person SET student = false;

DELETE FROM person WHERE id = 1;