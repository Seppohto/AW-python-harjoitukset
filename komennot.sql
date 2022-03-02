CREATE TABLE certificates (
    Id      SERIAL PRIMARY KEY,
    name    varchar(255) NOT NULL,
    person_id     int,
    CONSTRAINT fk_person
        FOREIGN KEY(person_id)
            REFERENCES person(id)
);

INSERT INTO person (name,age,student) VALUES ('Olli', 32, true);

SELECT * FROM person;

INSERT INTO certificates (name,person_id) VALUES ('Scrum', 6);

INSERT INTO certificates (name,person_id) VALUES ('Scrum', 4);

INSERT INTO certificates (name,person_id) VALUES ('GCP', 5);

INSERT INTO certificates (name,person_id) VALUES ('AZ-104', 3);

SELECT person.name as person, certificates.name as cert FROM person, certificates WHERE certificates.name = "Scrum" ;

