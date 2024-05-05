/*function1 for social media app*/
USE socialmediaapp

CREATE FUNCTION GetUserName(@UserId INT)
RETURNS NVARCHAR(50)
AS
BEGIN 
DECLARE @FullName NVARCHAR(50)
SELECT @FullName = FullName FROM Users WHERE UserID=@UserId
RETURN @FullName
END;

SELECT dbo.GetUserName(1) AS USERNAME

/*function2 for social media app*/
CREATE FUNCTION GetLikeCount(@PostId INT)
RETURNS INT
AS
BEGIN
DECLARE @Likes INT
SELECT @Likes=Likes FROM Posts WHERE PostID=@PostId
RETURN @Likes
END;

SELECT dbo.GetLikeCount(1) AS LIKES

/*function1 for library management*/
USE librarymanagement

CREATE FUNCTION GetAuthorFullName(@authorId INT)
RETURNS NVARCHAR(200)
AS
BEGIN
DECLARE @FullName NVARCHAR(200)
SELECT @FullName = CONCAT(firstName, ' ', lastName) FROM authors WHERE authorId = @authorId
RETURN @FullName
END;

SELECT dbo.GetAuthorFullName(1) AS AUTHORNAME

/*function2 for library management*/
CREATE FUNCTION GetMemberAge(@memberId INT)
RETURNS INT
AS
BEGIN
DECLARE @Age INT
SELECT @Age = DATEDIFF(YEAR, birthDate, GETDATE()) FROM members WHERE memberId = @memberId
RETURN @Age
END;

SELECT dbo.GetMemberAge(1) AS MemberAge

/*function1 for inventory module*/
USE INVENTORYMODULE

CREATE FUNCTION GetProductPrice(@productId INT)
RETURNS DECIMAL(10,2)
AS
BEGIN
DECLARE @Price DECIMAL(10,2)
SELECT @Price = price FROM products WHERE productId = @productId
RETURN @Price
END;

SELECT dbo.GetProductPrice(3) AS ProductPrice


/*function2 for inventory module*/
CREATE FUNCTION GetUserFullName (@userId INT)
RETURNS NVARCHAR(100)
AS
BEGIN
DECLARE @FullName NVARCHAR(100)
SELECT @FullName = CONCAT(firstName, ' ', lastName) FROM users WHERE userId = @userId
RETURN @FullName
END;

SELECT dbo.GetUserFullName(1) AS UserName
