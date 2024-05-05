CREATE TABLE department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(255),
    manager_name VARCHAR(100)
);

INSERT INTO department (department_name, location, manager_name)
VALUES 
  ('Sales', 'New York', 'John Smith'),
  ('Marketing', 'Los Angeles', 'Alice Johnson'),
  ('Finance', 'Chicago', 'Michael Brown'),
  ('Engineering', 'San Francisco', 'David Lee'),
  ('Human Resources', 'Boston', 'Emily Wilson'),
  ('IT', 'Seattle', 'Daniel Miller'),
  ('Operations', 'Dallas', 'Sophia Taylor'),
  ('Customer Service', 'Houston', 'Matthew Martinez'),
  ('Research and Development', 'Atlanta', 'Olivia Thomas'),
  ('Legal', 'Washington D.C.', 'William Anderson');
  
UPDATE department
SET location='India'
WHERE department_name='IT';

DELETE FROM department
WHERE department_name='Sales';
