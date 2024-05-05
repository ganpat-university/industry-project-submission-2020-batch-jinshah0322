CREATE DATABASE INVENTORYMODULE;

USE INVENTORYMODULE;

create table categories(
	categoryId int primary key identity(1,1),
	categoryName nvarchar(25) not null,
	description varchar(100),
	createdDate datetime,
	isActive bit not null,
)

create table products(
	productId int primary key identity(1,1),
	categoryId int not null,
	productName nvarchar(25) not null,
	price decimal(10,2) not null,
	quantity int,
	createdDate date,
	description varchar(50)
	foreign key(categoryId) references categories(categoryId)
)

create table suppliers(
	supplierId int primary key identity(1,1),
	supplierName nvarchar(25) not null,
	contact varchar(10) not null,
	supplierEmail nvarchar(50),
	registrationDate datetime,
	isActive bit not null
)

create table users(
	userId int primary key identity(1,1),
	firstName nvarchar(50) not null,
	lastName nvarchar(50) not null,
	registrationDate date not null,
	contact varchar(10) not null,
	isAdmin bit default 0
)

create table orders(
	orderId int primary key identity(1,1),
	orderDate datetime ,
	userId int not null,
	productId int not null,
	quantity int not null,
	totalAmount decimal(10,2) not null,
	note varchar(100),
	isDelivered bit default 0 not null,
	foreign key(userId) references users(userId),
	foreign key(productId) references products(productId)
)

insert into categories(categoryName, description, createdDate, isActive)
values	('Category1', 'Description for Category1', '2022-01-01 08:00:00', 1),
		('Category2', 'Description for Category2', '2022-02-05 10:30:00', 1),
		('Category3', 'Description for Category3', '2022-03-20 12:45:00', 1),
		('Category4', 'Description for Category4', '2022-04-15 14:15:00', 1),
		('Category5', 'Description for Category5', '2022-05-25 16:30:00', 1)

select * from categories

insert into products(productName,categoryId, price, quantity, createdDate, description)
values	('Product1',1, 19.99, 50, '2022-01-15', 'Description for Product1'),
		('Product2',1, 29.99, 30, '2022-02-20', 'Description for Product2'),
		('Product3',2, 14.99, 80, '2022-03-10', 'Description for Product3'),
		('Product4',4, 39.99, 20, '2022-04-05', 'Description for Product4'),
		('Product5',2, 24.99, 60, '2022-05-12', 'Description for Product5')

select * from products


insert into suppliers(supplierName, contact, supplierEmail, registrationDate, isActive)
values	('Supplier1', '1234567890', 'supplier1@example.com', '2022-01-01 09:00:00', 1),
		('Supplier2', '9876543210', 'supplier2@example.com', '2022-02-10 11:30:00', 1),
		('Supplier3', '5678901234', 'supplier3@example.com', '2022-03-25 13:45:00', 1),
		('Supplier4', '3456789012', 'supplier4@example.com', '2022-04-15 15:15:00', 1),
		('Supplier5', '7890123456', 'supplier5@example.com', '2022-05-05 17:30:00', 1)

select * from suppliers


insert into users(firstName, lastName, registrationDate, contact, isAdmin)
values	('John', 'Doe', '2022-01-01', '1234567890', 1),
		('Jane', 'Smith', '2022-02-05', '9876543210', 0),
		('Mark', 'Johnson', '2022-03-20', '5678901234', 0),
		('Alice', 'Williams', '2022-04-15', '3456789012', 0),
		('Bob', 'Miller', '2022-05-25', '7890123456', 1)

select * from users



insert into orders(orderDate, userId, productId, quantity, totalAmount, note, isDelivered)
values	('2022-01-15 09:30:00', 1, 7, 10, 199.90, 'Order for Product1', 0),
		('2022-02-20 11:45:00', 2, 6, 5, 149.95, 'Order for Product2', 1),
		('2022-03-10 13:00:00', 3, 3, 15, 224.85, 'Order for Product3', 0),
		('2022-04-05 14:30:00', 4, 4, 8, 319.92, 'Order for Product4', 0),
		('2022-05-12 16:45:00', 5, 5, 12, 299.88, 'Order for Product5', 1)

select * from orders

/*Displaying products with Category1 write sub query*/
select * from products where categoryId = (select categoryId from categories where categoryName='Category1')

/*display orders where product price is more than 25 write sub query*/
select * from orders where productId in (select productId from products where price>25 )

/*display order of john write sub query*/
select * from orders where userId = (select userId from users where firstName='John')

/*Display products and their categories using inline query*/
select productName,(select categoryName from categories where categoryId=products.categoryId) category from products

/*display orders of user John using inline query*/
select *,(select orderId from orders where userId = users.userId) as 'user' from users where firstName='John'

/*Display orders of product 5 using inline query*/
select *,(select orderId from orders where productId=products.productId) as products from products where productName='Product5'


/*String functions*/
SELECT P.productName, P.price, P.quantity,C.categoryName,LEFT(C.description, 20) AS LeftDescription,RIGHT(C.description, 20) AS RightDescription FROM Products P INNER JOIN Categories C ON P.categoryId = C.categoryId

SELECT O.orderId, O.orderDate, CONCAT(U.firstName, ' ', U.lastName) AS FullName, P.productName, O.quantity, O.totalAmount FROM Orders O INNER JOIN Users U ON O.userId = U.userId INNER JOIN Products P ON O.productId = P.productId

SELECT O.orderId, O.orderDate,UPPER(U.firstName) AS UppercaseFirstName,U.lastName, P.productName, O.quantity, O.totalAmount FROM Orders O INNER JOIN Users U ON O.userId = U.userId INNER JOIN Products P ON O.productId = P.productId

/*Math Functions*/
SELECT O.orderId, O.orderDate, O.quantity, O.totalAmount,P.productName, P.price,ROUND(O.totalAmount, 0) AS RoundedTotalAmount FROM Orders O INNER JOIN Products P ON O.productId = P.productId

SELECT P.productName, P.price,C.categoryName,CEILING(P.price) AS RoundedPrice FROM Products P INNER JOIN Categories C ON P.categoryId = C.categoryId

SELECT O.orderId, O.orderDate, O.quantity, O.totalAmount,P.productName, P.price,FLOOR(O.totalAmount) AS FlooredTotalAmount FROM Orders O INNER JOIN Products P ON O.productId = P.productId

/*Advanced function*/
SELECT O.orderId, O.orderDate,COALESCE(U.firstName + ' ' + U.lastName, 'Unknown') AS FullName,O.quantity, O.totalAmount FROM Orders O INNER JOIN Users U ON O.userId = U.userId

SELECT P.productName, P.price, P.quantity,C.categoryName,NULLIF(C.categoryName, 'Category1') AS CleanedCategoryName FROM Products P INNER JOIN Categories C ON P.categoryId = C.categoryId

SELECT O.orderId, O.orderDate, P.productName,CAST(O.totalAmount AS VARCHAR(20)) + ' ' + P.productName AS TotalAmountWithProductName FROM Orders O INNER JOIN Products P ON O.productId = P.productId
