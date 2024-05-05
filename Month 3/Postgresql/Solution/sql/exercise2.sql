CREATE TABLE employee (id SERIAL PRIMARY KEY,name VARCHAR(100),city VARCHAR(100));

INSERT INTO employee (name, city) VALUES
('John', 'Hyderabad'),
('Alice', 'Ahmedabad'),
('Bob', 'Mumbai'),
('Charlie', 'Delhi'),
('David', 'Chennai'),
('Emma', 'Kochin'),
('Frank', 'Kolkata'),
('Grace', 'Pune'),
('Henry', 'Bangalore'),
('Sophia', 'Hyderabad'),
('James', 'Ahmedabad'),
('Olivia', 'Mumbai'),
('Michael', 'Delhi'),
('Elizabeth', 'Chennai'),
('William', 'Kochin'),
('Isabella', 'Kolkata'),
('Daniel', 'Pune'),
('Emily', 'Bangalore'),
('Alexander', 'Hyderabad'),
('Mia', 'Ahmedabad'),
('Ethan', 'Mumbai'),
('Ava', 'Delhi'),
('Matthew', 'Chennai'),
('Charlotte', 'Kochin'),
('Liam', 'Kolkata'),
('Amelia', 'Pune'),
('Benjamin', 'Bangalore'),
('Abigail', 'Ahmedabad'),
('Lucas', 'Mumbai');

select * from employee where city like '%abad'

select * from employee where city like '%under%'

SELECT * FROM employee WHERE SUBSTRING(city FROM LENGTH(city) - 2 FOR 1) = 'b';

select * from employee where city like 'A%'

select * from employee where substring(city from 2 for 1)='o';

select * from employee limit 10;

select * from employee where city='Mumbai' or city='Bangalore' limit 5

select * from employee where city='Mumbai' or city='Bangalore' offset 5 limit 5

select * from employee where city in ('Mumbai' , 'Bangalore') order by city

select * from employee order by id desc

INSERT INTO employee (name, city) VALUES('John Doe', NULL),('Alice Smith', NULL),('Bob Johnson', NULL);

select * from employee where city is Null

alter table employee add column join_date date	

INSERT INTO employee (name, city, join_date) VALUES ('Emma Watson', 'London', '2023-04-15'),('Michael Johnson', 'New York', '2022-10-20'),('Michael Johnson', 'New York', '2024-10-20');

select * from employee where date_part('year',join_date)=date_part('year',current_date)

select distinct * from employee;

alter table employee add column amount decimal(10,2)

INSERT INTO employee (name, city, join_date, amount)
VALUES
('John Doe', 'Paris', '2023-01-15', 2000.00),
('Alice Smith', 'London', '2024-02-10', 1800.50),
('Bob Johnson', 'New York', '2022-07-20', 2500.75);

select sum(amount) as total_amount from employee;

select city,sum(amount) as total_amount from employee group by city;

select city,avg(amount) as total_amount from employee group by city;

select max(amount) as max_amount from employee

select min(amount) as max_amount from employee

truncate table employee

INSERT INTO employee (name, city, join_date, amount)
VALUES
('Sarah Johnson', 'Los Angeles', '2023-05-10', 2200.75),
('David Lee', 'Chicago', '2022-09-15', 1900.25),
('Emily Brown', 'San Francisco', '2023-02-20', 2800.50),
('Michael Davis', 'Seattle', '2024-07-05', 2100.00),
('Jessica Martinez', 'Dallas', '2023-11-10', 2600.00),
('Daniel Anderson', 'Houston', '2022-03-15', 2400.75),
('Emma Rodriguez', 'Miami', '2023-08-20', 2300.50),
('William Taylor', 'Atlanta', '2024-01-25', 2700.25),
('Olivia Wilson', 'Boston', '2022-06-30', 2000.00),
('James Thomas', 'Phoenix', '2023-10-05', 2500.00),
('Sophia White', 'Denver', '2022-04-10', 2900.00),
('Alexander Jackson', 'Philadelphia', '2023-09-15', 2200.75),
('Isabella Harris', 'Detroit', '2024-02-20', 1900.25),
('Benjamin Martin', 'San Diego', '2023-05-25', 2800.50),
('Mia Thompson', 'Minneapolis', '2022-11-30', 2100.00),
('Ethan Garcia', 'Portland', '2023-04-05', 2600.00),
('Charlotte Martinez', 'Las Vegas', '2022-08-10', 2400.75),
('Liam Robinson', 'Salt Lake City', '2023-01-15', 2300.50),
('Amelia Hall', 'Orlando', '2024-06-20', 2700.25),
('Jacob Allen', 'Tampa', '2022-12-25', 2000.00),
('Ava Young', 'Washington, D.C.', '2023-07-30', 2500.00),
('Michael Scott', 'New Orleans', '2022-02-05', 2900.00),
('Jennifer King', 'Austin', '2023-11-10', 2200.75),
('John Wright', 'San Antonio', '2024-04-15', 1900.25),
('Abigail Lewis', 'Nashville', '2023-09-20', 2800.50),
('Noah Hill', 'Memphis', '2022-05-25', 2100.00),
('Grace Baker', 'Charlotte', '2023-10-30', 2600.00),
('Chloe Perez', 'Raleigh', '2022-03-05', 2400.75),
('Daniel Wood', 'Indianapolis', '2024-08-10', 2300.50);

select name,join_date,extract(quarter from join_date) as quarter from employee;

select *,extract(year from join_date) as year from employee;

select *,to_char(join_date,'day') as weekday from employee;

select id,name,case when extract(year from join_date)=extract(year from current_date) then 'new admission' 
					else 'old admission' 
					end as admission_status from employee
					
ALTER TABLE employee
ADD CONSTRAINT pk_employee PRIMARY KEY (id);

drop table employee;

create table city (id serial primary key,name varchar(100) not null )

create table employee (id serial primary key,name varchar(100) not null,city_id int not null,foreign key (city_id)
					   references city(id))
					   
alter table employee alter column name set not null

alter table city add column code varchar(10)

alter table city add constraint unique_code unique(code)

CREATE TABLE Company (id SERIAL PRIMARY KEY);

ALTER TABLE city ADD COLUMN company_id INT, ADD CONSTRAINT fk_company FOREIGN KEY (company_id) REFERENCES Company(id);

alter table city add constraint unique_cmp_code unique(company_id,code)

alter table city drop constraint unique_code

alter table employee add column join_date date

alter table employee add constraint check_date check(join_date>=date '2010-01-01')

create index index_name on 	city(name)

select * from employee

create index emp_index on employee(city_id,join_date)

create index emp_nameindex on employee(name)

create index cmp_name on company(id)

drop index cmp_name

create table new_table(id serial ,primary key (id))

create SEQUENCE start1000 start 1000

create table new_table1 (id int default nextval('start1000') primary key)

create SEQUENCE start500 start 500

create table new_table2 (id int default nextval('start500') primary key)

drop SEQUENCE start1000

INSERT INTO new_table1 (id) VALUES
(nextval('start1000')),
(nextval('start1000'));

SELECT e.id AS employee_id, e.name AS employee_name, c.name AS city_name 
FROM employee AS e INNER JOIN city AS c ON e.city_id = c.id;

select e.id as employee_id,e.name as employee_name,c.name as city_name,cp.id as company_id from employee as e inner join 
city as c on e.city_id = c.id inner join company as cp on c.company_id = cp.id

create view emp_city_cmp as select e.id as employee_id,e.name as employee_name,c.name as city_name,cp.id as company_id 
from employee as e inner join city as c on e.city_id = c.id inner join company as cp on c.company_id = cp.id

drop view emp_city_cmp

select * from employee