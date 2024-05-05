/*Triggers on Social Media App*/
USE socialmediaapp

/*Before Trigger on delete*/
CREATE TRIGGER Users_InsteadOfDelete
ON Users
FOR DELETE
AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (SELECT 1 FROM Posts WHERE UserID IN (SELECT UserID FROM deleted))
    BEGIN
        THROW 50000, 'Cannot delete user with related posts.', 16;
        RETURN;
    END
    IF EXISTS (SELECT 1 FROM Comments WHERE UserID IN (SELECT UserID FROM deleted))
    BEGIN
        THROW 50000, 'Cannot delete user with posted comments.', 16;
        RETURN;
    END
    DELETE FROM Users WHERE UserID IN (SELECT UserID FROM deleted);
END;


/*After Trigger on delete*/
CREATE TRIGGER Users_AfterDelete
ON Users
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @DeletedUserID INT;
    SELECT @DeletedUserID = UserID FROM deleted;
    IF @@ROWCOUNT > 0
    BEGIN
        PRINT 'User with ID ' + CAST(@DeletedUserID AS NVARCHAR(10)) + ' is deleted.';
    END
END;

/*Before trigger on insert*/
CREATE TRIGGER trg_ForInsert_Posts
ON Posts
FOR INSERT
AS
BEGIN
    UPDATE Posts
    SET PostedDate = GETDATE()
    FROM Posts
    INNER JOIN inserted ON Posts.PostID = inserted.PostID;
END;

/*After trigger on insert*/
CREATE TRIGGER trg_AfterInsert_Posts
ON Posts
AFTER INSERT
AS
BEGIN
    UPDATE Posts
    SET PostedDate = GETDATE()
    WHERE PostID IN (SELECT PostID FROM inserted);
END;

/*Before trigger on update*/
CREATE TRIGGER trg_InsteadOfUpdate_Posts
ON Posts
INSTEAD OF UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE p
    SET
        p.Caption = i.Caption,
        p.Image = i.Image,
        p.Likes = CASE WHEN i.Likes IS NOT NULL THEN i.Likes ELSE p.Likes END,
        p.IsPublic = i.IsPublic
    FROM
        Posts p
        INNER JOIN inserted i ON p.PostID = i.PostID;
END;


/*After trigger on update*/
CREATE TRIGGER trg_AfterUpdate_Posts
ON Posts
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    PRINT 'Posts have been updated.';
END;



/*Triggers on Library Management*/
USE librarymanagement

/*Before Trigger on insert*/
CREATE TRIGGER Review_InsteadOfInsert
ON reviews
FOR INSERT
AS
BEGIN 
	SET NOCOUNT ON
	INSERT INTO reviews (memberId, bookId, rating, comment, reviewDate, reviewSentiment) 
	SELECT 
		memberId,
		bookId,
		CASE WHEN rating BETWEEN 1 AND 5 THEN rating else 3 END,
		comment,reviewDate,reviewSentiment
	FROM inserted
END;

/*After Trigger on insert*/
CREATE TRIGGER Review_AfterInsert
ON reviews
AFTER INSERT
AS
BEGIN
	SET NOCOUNT ON
	UPDATE r SET reviewSentiment=CASE WHEN i.rating>=3 THEN 1 ELSE 0 END
	FROM reviews r 
	INNER JOIN inserted i ON r.reviewID=i.reviewId;
END;

/*Before trigger on delete*/
-- FOR DELETE trigger for Books
CREATE TRIGGER trg_ForDelete_Books
ON Books
FOR DELETE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (SELECT 1 FROM Reviews WHERE BookID IN (SELECT BookID FROM deleted))
    BEGIN
        THROW 50000, 'Cannot delete book with associated reviews.', 16;
        RETURN;
    END

    DELETE FROM Books WHERE BookID IN (SELECT BookID FROM deleted);
END;
GO


/*After trigger on delete*/
CREATE TRIGGER trg_AfterDelete_Books
ON Books
AFTER DELETE
AS
BEGIN
    PRINT 'Book and associated reviews have been deleted.';
END;

/*Before trigger on update*/
CREATE TRIGGER trg_ForUpdate_Books
ON Books
FOR UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF UPDATE(publishDate)
    BEGIN
        UPDATE Reviews
        SET reviewDate = GETDATE()
        FROM Reviews
        INNER JOIN deleted ON Reviews.BookID = deleted.BookID
        INNER JOIN inserted ON Reviews.BookID = inserted.BookID;
    END
END;

/*After trigger on update*/
CREATE TRIGGER trg_AfterUpdate_Books
ON Books
AFTER UPDATE
AS
BEGIN
    PRINT 'Books have been updated.';
END;


/*Triggers on Inventory Module*/
USE INVENTORYMODULE

/*Before Trigger*/
CREATE TRIGGER Orders_InsteadOfUpdate
ON orders
FOR UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE o
    SET 
        orderDate = i.orderDate,
        userId = i.userId,
        productId = i.productId,
        quantity = i.quantity,
        totalAmount = o.totalAmount, 
        note = i.note,
        isDelivered = i.isDelivered
    FROM orders o
    INNER JOIN inserted i ON o.orderId = i.orderId;
END;

/*After Trigger*/
CREATE TRIGGER Orders_AfterUpdate
ON orders
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    PRINT 'Orders have been updated.';
END;

/*Before trigger on delete*/
CREATE TRIGGER trg_ForDelete_Users
ON Users
FOR DELETE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (SELECT 1 FROM Orders WHERE UserID IN (SELECT UserID FROM deleted))
    BEGIN
        THROW 50000, 'Cannot delete user with related orders.', 16;
        RETURN;
    END

    DELETE FROM Users WHERE UserID IN (SELECT UserID FROM deleted);
END;

/*After trigger on delete*/
CREATE TRIGGER trg_AfterDelete_Categories
ON Categories
AFTER DELETE
AS
BEGIN
    PRINT 'Category and associated products have been deleted.';
END;

/*Before trigger on update*/
CREATE TRIGGER trg_ForUpdate_Products
ON Products
FOR UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF UPDATE(Price)
    BEGIN
        UPDATE Orders
        SET OrderDate = GETDATE()
        FROM Orders
        INNER JOIN deleted ON Orders.ProductID = deleted.ProductID
        INNER JOIN inserted ON Orders.ProductID = inserted.ProductID;
    END
END;

/*After trigger on update*/
CREATE TRIGGER trg_AfterUpdate_Products
ON Products
AFTER UPDATE
AS
BEGIN
    PRINT 'Products have been updated.';
END;