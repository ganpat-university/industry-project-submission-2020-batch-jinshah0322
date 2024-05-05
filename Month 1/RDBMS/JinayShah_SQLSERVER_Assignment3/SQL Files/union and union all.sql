/*union and union all for social media app*/

use socialmediaapp

SELECT 'Post' AS ItemType,PostID AS ItemID,UserID,Caption AS Text,Image,PostedDate AS ItemDate FROM Posts
UNION
SELECT 'Comment' AS ItemType,CommentID AS ItemID,UserID,CommentText AS Text,NULL AS Image,CommentDate AS ItemDate FROM Comments

SELECT 'Post' AS ItemType,PostID AS ItemID,UserID,Caption AS Text,Image,PostedDate AS ItemDate FROM Posts
UNION ALL
SELECT 'Comment' AS ItemType,CommentID AS ItemID,UserID,CommentText AS Text,NULL AS Image,CommentDate AS ItemDate FROM Comments

/*union and union all for inventory module*/
use INVENTORYMODULE

SELECT 'Category' AS ItemType,categoryId AS ItemID,categoryName AS ItemName,NULL AS ProductName,NULL AS Price FROM categories
UNION
SELECT 'Product' AS ItemType,categoryId AS ItemID,NULL AS ItemName,productName AS ProductName,price AS Price FROM products

SELECT 'Category' AS ItemType,categoryId AS ItemID,categoryName AS ItemName,NULL AS ProductName,NULL AS Price FROM categories
UNION ALL
SELECT 'Product' AS ItemType,categoryId AS ItemID,NULL AS ItemName,productName AS ProductName,price AS Price FROM products

/*union and union all for library management*/
use librarymanagement

-- UNION Query combining data from authors and members without duplicates
SELECT 'Author' AS UserType,authorId AS UserID,firstName,lastName,birthdate AS UserBirthdate,nationality,awarded,awardDate FROM authors
UNION
SELECT 'Member' AS UserType,memberId AS UserID,firstName,lastName,birthDate AS UserBirthdate,NULL AS Nationality,NULL AS Awarded,NULL AS AwardDate FROM members

SELECT 'Author' AS UserType,authorId AS UserID,firstName,lastName,birthdate AS UserBirthdate,nationality,awarded,awardDate FROM authors
UNION ALL
SELECT 'Member' AS UserType,memberId AS UserID,firstName,lastName,birthDate AS UserBirthdate,NULL AS Nationality,NULL AS Awarded,NULL AS AwardDate FROM members

/*In above examples union and union all was no properly diffrentiated so below is a proper example*/
CREATE DATABASE unionDb

use unionDb

CREATE TABLE Finance_FirstHalf2023 (
    TransactionID INT PRIMARY KEY,
    TransactionDate DATE,
    Description NVARCHAR(255),
    Income DECIMAL(18, 2),
    Expenses DECIMAL(18, 2)
);
INSERT INTO Finance_FirstHalf2023 (TransactionID, TransactionDate, Description, Income, Expenses)
VALUES
    (1, '2023-01-15', 'Sales Income', 150000.00, 0.00),
    (2, '2023-02-05', 'Service Income', 75000.00, 0.00),
    (3, '2023-03-20', 'Product Purchase', 0.00, 30000.00),
	(4,'2023-03-20', 'Product Purchase', 0.00, 30000.00)

CREATE TABLE Finance_SecondHalf2023 (
    TransactionID INT PRIMARY KEY,
    TransactionDate DATE,
    Description NVARCHAR(255),
    Income DECIMAL(18, 2),
    Expenses DECIMAL(18, 2)
);

INSERT INTO Finance_SecondHalf2023 (TransactionID, TransactionDate, Description, Income, Expenses)
VALUES
	(4,'2023-03-20', 'Product Purchase', 0.00, 30000.00),
    (5, '2023-07-10', 'Sales Income', 120000.00, 0.00),
    (6, '2023-08-22', 'Consulting Fees', 50000.00, 0.00),
    (7, '2023-09-05', 'Equipment Purchase', 0.00, 45000.00)

/*union query*/
select * from Finance_FirstHalf2023 union select * from Finance_SecondHalf2023

/*union all*/
select * from Finance_FirstHalf2023 union all select * from Finance_SecondHalf2023