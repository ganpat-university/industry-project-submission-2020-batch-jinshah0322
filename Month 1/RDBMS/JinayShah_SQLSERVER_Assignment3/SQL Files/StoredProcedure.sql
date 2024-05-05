/*Stored Procedures for Inventory module*/
USE INVENTORYMODULE

/*Stored procedure for select query*/
CREATE PROCEDURE SelectAllCategories
AS
BEGIN
    SELECT * FROM categories;
END;

EXEC SelectAllCategories


/*Stored procedure for insert query*/
CREATE PROCEDURE AddProduct
	@categoryId INT,
    @productName NVARCHAR(25),
    @price DECIMAL(10,2),
    @quantity INT,
    @createdDate DATE,
    @description VARCHAR(50)
AS
BEGIN
    INSERT INTO products (productName,categoryId, price, quantity, createdDate, description)
    VALUES (@productName,@categoryId, @price, @quantity, @createdDate, @description);
END;

EXEC AddProduct
    @productName = 'New Product',
	@categoryId = 2,
    @price = 19.99,
    @quantity = 100,
    @createdDate = '2024-01-25',
    @description = 'Description of the new product';


/*Stored procedure for update query*/
CREATE PROCEDURE UpdateSupplier
    @supplierId INT,
    @isActive BIT
AS
BEGIN
    UPDATE suppliers
    SET isActive = @isActive
    WHERE supplierId = @supplierId;
END;

EXEC UpdateSupplier
    @supplierId = 1,
    @isActive = 0;


/*Stored procedure for delete query*/
CREATE PROCEDURE DeleteUser
    @orderId INT
AS
BEGIN
    DELETE FROM orders
    WHERE orderId = @orderId;
END;

EXEC DeleteUser
    @orderId = 1;


/*Stored procedure for full*/
CREATE PROCEDURE FullOrderProcedure
    @orderId INT
AS
BEGIN
    SELECT
        o.orderId,
        o.orderDate,
        u.userId,
        u.firstName + ' ' + u.lastName AS userName,
        p.productId,
        p.productName,
        o.quantity,
        o.totalAmount,
        o.note,
        o.isDelivered
    FROM
        orders o
    JOIN
        users u ON o.userId = u.userId
    JOIN
        products p ON o.productId = p.productId
    WHERE
        o.orderId = @orderId;
END;

EXEC FullOrderProcedure
    @orderId = 3;



/*Stored Procedures for library management*/
USE librarymanagement

/*Stored procedure for select query*/
CREATE PROCEDURE SelectAllAuthors
AS
BEGIN
    SELECT * FROM authors;
END;

EXEC SelectAllAuthors;


/*Stored procedure for insert query*/
CREATE PROCEDURE AddMember
    @firstName NVARCHAR(100),
    @lastName NVARCHAR(100),
    @birthDate DATE,
    @contact VARCHAR(10),
    @memberType CHAR(1)
AS
BEGIN
    INSERT INTO members (firstName, lastName, birthDate, contact, memberType)
    VALUES (@firstName, @lastName, @birthDate, @contact, @memberType);
END;

EXEC AddMember
    @firstName = 'John',
    @lastName = 'Doe',
    @birthDate = '1990-01-01',
    @contact = '1234567890',
    @memberType = 'A';


/*Stored procedure for update query*/
CREATE PROCEDURE UpdateBook
    @bookId INT,
    @price DECIMAL(10,2)
AS
BEGIN
    UPDATE books
    SET price = @price
    WHERE bookId = @bookId;
END;

EXEC UpdateBook
    @bookId = 1,
    @price = 9.99


/*Stored procedure for delete query*/
CREATE PROCEDURE DeleteReview
    @reviewId INT
AS
BEGIN
    DELETE FROM reviews
    WHERE reviewId = @reviewId;
END;

EXEC DeleteReview
    @reviewId = 1;


/*Stored procedure for full*/
CREATE PROCEDURE FullProcedure
    @authorFirstName NVARCHAR(100)
AS
BEGIN
    SELECT a.*, b.*, m.*, r.*
    FROM authors a
    JOIN books b ON a.authorId = b.authorId
    JOIN reviews r ON b.bookId = r.bookId
    JOIN members m ON r.memberId = m.memberId
    WHERE a.firstName = @authorFirstName;
END;

EXEC FullProcedure
    @authorFirstName = 'Jane';



/*Stored Procedures for social media app*/
USE socialmediaapp


/*Stored procedure for select query*/
CREATE PROCEDURE SelectAllUsers
AS
BEGIN
    SELECT * FROM Users;
END;

EXEC SelectAllUsers;


/*stored procedure for insert query*/
CREATE PROCEDURE AddPost
    @UserID INT,
    @Caption NVARCHAR(255),
    @Image VARBINARY(MAX),
    @Likes INT,
    @IsPublic BIT
AS
BEGIN
	DECLARE @PostedDate DATETIME = GETDATE();
    INSERT INTO Posts (UserID, Caption, Image, PostedDate, Likes, IsPublic)
    VALUES (@UserID, @Caption, @Image, @PostedDate, @Likes, @IsPublic);
END;

EXEC AddPost
    @UserID = 1,
    @Caption = 'New Post',
    @Image = NULL,
    @Likes = 0,
    @IsPublic = 1;


/*Stored procedure for update query*/
CREATE PROCEDURE UpdateComment
    @CommentID INT,
    @CommentText NVARCHAR(MAX)
AS
BEGIN
    DECLARE @CommentDate DATETIME = GETDATE()
    UPDATE Comments
    SET CommentText = @CommentText, CommentDate = @CommentDate
    WHERE CommentID = @CommentID;
END;

EXEC UpdateComment
    @CommentID = 1,
    @CommentText = 'Updated Comment'


/*Stored procedure for delete query*/
CREATE PROCEDURE DeleteFriendship
    @FriendshipID INT
AS
BEGIN
    DELETE FROM Friendships
    WHERE FriendshipID = @FriendshipID;
END;

EXEC DeleteFriendship
    @FriendshipID = 1;



/*Stored procedure for full*/
CREATE PROCEDURE FullProcedure
    @UserName NVARCHAR(50)
AS
BEGIN
    SELECT u.*, p.*, c.*, f.*, m.*
    FROM Users u
    JOIN Posts p ON u.UserID = p.UserID
    JOIN Comments c ON p.PostID = c.PostID
    JOIN Friendships f ON u.UserID = f.UserID1 OR u.UserID = f.UserID2
    JOIN Messages m ON u.UserID = m.SenderID OR u.UserID = m.ReceiverID
    WHERE u.UserName = @UserName;
END;

EXEC FullProcedure
    @UserName = 'jane_smith';