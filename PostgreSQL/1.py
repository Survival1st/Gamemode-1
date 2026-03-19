CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20)
);
SELECT * FROM phonebook;
INSERT INTO phonebook (first_name, phone) VALUES ('Alice', '123-456-7890');
