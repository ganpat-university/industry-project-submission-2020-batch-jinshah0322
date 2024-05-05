use OrderManagement

CREATE TABLE Customer (
    CustomerId INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100),
    Email NVARCHAR(100),
    Address NVARCHAR(255)
);

ALTER TABLE Customer
ADD isDeleted BIT DEFAULT 0;

select * from Customer

CREATE TABLE Product (
    ProductId INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100),
    Description NVARCHAR(MAX),
    Price DECIMAL(10, 2),
    StockQuantity INT
);

ALTER TABLE Product
ADD isDeleted BIT DEFAULT 0;

select * from Product

CREATE TABLE [Order] (
    OrderId INT PRIMARY KEY IDENTITY(1,1),
    CustomerId INT,
    OrderDate DATETIME,
    TotalAmount DECIMAL(10, 2),
    Status NVARCHAR(50),
    FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId)
);

ALTER TABLE [Order]
ADD isDeleted BIT DEFAULT 0;

update [Order]
SET TotalAmount=0 

SELECT * FROM [ORDER]
delete from [Order]

CREATE TABLE OrderItem (
    OrderItemId INT PRIMARY KEY IDENTITY(1,1),
    OrderId INT,
    ProductId INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    FOREIGN KEY (OrderId) REFERENCES [Order](OrderId),
    FOREIGN KEY (ProductId) REFERENCES Product(ProductId)
);	

ALTER TABLE OrderItem
ADD isDeleted BIT DEFAULT 0;

select * from OrderItem

update OrderItem set isDeleted=0

delete from OrderItem