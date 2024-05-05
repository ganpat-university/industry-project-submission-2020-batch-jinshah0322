/*Joins on Social Media App*/
USE socialmediaapp

/*Inner Join*/
SELECT *
FROM Posts p
INNER JOIN Users u ON p.UserID = u.UserID;

/*Left Outer Joni*/
SELECT *
FROM Comments C
LEFT OUTER JOIN Users u ON C.UserID = u.UserID;

/*Right Outer Join*/
SELECT *
FROM Users u
RIGHT OUTER JOIN Friendships f ON u.UserID = f.UserID1
RIGHT OUTER JOIN Friendships f1 ON u.UserID=f1.UserID2;

/*Full Outer Join*/
SELECT *
FROM Users u
FULL OUTER JOIN Messages m ON m.SenderID = u.UserID
FULL OUTER JOIN Messages m1 ON m.ReceiverID=u.UserID;


/*Joins on Library Management*/
USE librarymanagement

/*Inner Join*/
SELECT *
FROM authors a
INNER JOIN books b ON a.authorId = b.authorId;

/*Left Outer Joni*/
SELECT *
FROM publisher p
LEFT OUTER JOIN books b ON p.publisherId = b.publisherId;

/*Right Outer Join*/
SELECT *
FROM publisher P
RIGHT OUTER JOIN books b ON p.publisherId = b.publisherId;

/*Full Outer Join*/
SELECT *
FROM books b
FULL OUTER JOIN authors a ON b.authorId = a.authorId
FULL OUTER JOIN reviews r ON b.bookId = r.bookId
FULL OUTER JOIN members m ON r.memberId = m.memberId;


/*Joins on Inventory Module*/
USE INVENTORYMODULE

/*Inner Join*/
SELECT *
FROM orders o
INNER JOIN users u ON o.userId = u.userId
INNER JOIN products p ON o.productId = p.productId;


/*Left Outer Joni*/
SELECT *
FROM products p
LEFT OUTER JOIN categories c ON p.categoryId= c.categoryId;


/*Right Outer Join*/
SELECT *
FROM users u
RIGHT OUTER JOIN orders o ON u.userId = o.userId


/*Full Outer Join*/
SELECT *
FROM categories c
FULL OUTER JOIN products p ON c.categoryId = p.categoryId;
