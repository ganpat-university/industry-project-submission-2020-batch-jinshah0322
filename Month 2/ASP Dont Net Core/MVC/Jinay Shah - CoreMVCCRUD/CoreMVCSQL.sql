use CoreMVC

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    HireDate DATE NOT NULL
);

INSERT INTO Employee (FirstName, LastName, Email, Salary, HireDate)
VALUES ('John', 'Doe', 'john.doe@example.com', 50000.00, '2023-01-15'),
       ('Jane', 'Smith', 'jane.smith@example.com', 60000.00, '2022-07-20'),
       ('Michael', 'Johnson', 'michael.johnson@example.com', 55000.00, '2023-03-10'),
       ('Emily', 'Brown', 'emily.brown@example.com', 62000.00, '2021-11-05'),
       ('David', 'Wilson', 'david.wilson@example.com', 58000.00, '2022-09-25');


CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY IDENTITY(1,1),
    DepartmentName VARCHAR(100) NOT NULL,
    DepartmentHead VARCHAR(100) NOT NULL,
    Budget DECIMAL(18, 2) NOT NULL,
    CreationDate DATE NOT NULL,
    IsActive BIT NOT NULL
);

INSERT INTO Department (DepartmentName, DepartmentHead, Budget, CreationDate, IsActive) VALUES
('Marketing', 'John Doe', 10000.00, '2024-02-22', 1),
('Finance', 'Jane Smith', 15000.00, '2024-02-22', 1),
('HR', 'Michael Johnson', 12000.00, '2024-02-22', 1),
('IT', 'Emily Brown', 20000.00, '2024-02-22', 1),
('Operations', 'David Wilson', 18000.00, '2024-02-22', 1);