/*view1 of socialmediaapp*/
use socialmediaapp

CREATE VIEW UserPostsView AS
SELECT
    U.UserID,
    U.UserName,
    U.FullName,
    U.Email,
    U.Birthdate,
    U.ProfileImage,
    U.IsActive,
    P.PostID,
    P.Caption,
    P.Image AS PostImage,
    P.PostedDate,
    P.Likes,
    P.IsPublic
FROM
    Users U
JOIN
    Posts P ON U.UserID = P.UserID

select * from UserPostsView

/*view2 of socialmediaapp*/
CREATE VIEW UserPostCommentView AS
SELECT
    U.UserID,
    U.UserName,
    U.FullName,
    U.Email,
    U.Birthdate,
    U.ProfileImage,
    U.IsActive,
    P.PostID,
    P.Caption,
    P.Image AS PostImage,
    P.PostedDate AS PostDate,
    P.Likes,
    P.IsPublic,
    C.CommentID,
    C.CommentText,
    C.CommentDate
FROM
    Users U
JOIN
    Posts P ON U.UserID = P.UserID
JOIN
    Comments C ON P.PostID = C.PostID

select * from UserPostCommentView

/*view1 of librarymanagement*/
use librarymanagement

CREATE VIEW BookAuthorPublisherView AS
SELECT
    B.bookId,
    B.title,
    B.genre,
    B.publishDate AS BookPublishDate,
    B.copiesAvailable,
    B.shelfLocation,
    B.price,
    B.isEook,
    A.authorId,
    A.firstName + ' ' + A.lastName AS AuthorName,
    A.birthdate AS AuthorBirthdate,
    A.nationality AS AuthorNationality,
    A.awarded AS AuthorAwarded,
    A.awardDate AS AuthorAwardDate,
    P.publisherId,
    P.publisherName,
    P.publishDate AS PublisherPublishDate,
    P.publisherContact
FROM
    books B
JOIN
    authors A ON B.authorId = A.authorId
JOIN
    publisher P ON B.publisherId = P.publisherId

select * from BookAuthorPublisherView

/*view2 of librarymanagement*/
CREATE VIEW BookReviewView AS
SELECT
    B.bookId,
    B.title,
    B.genre,
    B.publishDate AS BookPublishDate,
    B.copiesAvailable,
    B.shelfLocation,
    B.price,
    B.isEook,
    R.reviewId,
    R.memberId,
    R.rating,
    R.comment,
    R.reviewDate,
    R.reviewSentiment
FROM
    books B
JOIN
    reviews R ON B.bookId = R.bookId

select * from BookReviewView

/*view1 of inventorymodule*/
use INVENTORYMODULE

CREATE VIEW ProductCategoryView AS
SELECT
    P.productId,
    P.productName,
    P.price,
    P.quantity,
    P.createdDate AS ProductCreatedDate,
    P.description AS ProductDescription,
    C.categoryId,
    C.categoryName,
    C.description AS CategoryDescription,
    C.createdDate AS CategoryCreatedDate,
    C.isActive AS CategoryIsActive
FROM
    products P
JOIN
    categories C ON P.categoryId = C.categoryId

select * from ProductCategoryView

/*view2 of inventorymodule*/
CREATE VIEW UserOrderProductView AS
SELECT
    O.orderId,
    O.orderDate,
    U.userId,
    U.firstName + ' ' + U.lastName AS UserName,
    U.registrationDate AS UserRegistrationDate,
    U.contact AS UserContact,
    U.isAdmin AS IsAdmin,
    P.productId,
    P.productName,
    P.price,
    P.quantity AS ProductQuantity,
    P.createdDate AS ProductCreatedDate,
    P.description AS ProductDescription,
    O.quantity AS OrderQuantity,
    O.totalAmount,
    O.note,
    O.isDelivered
FROM
    orders O
JOIN
    users U ON O.userId = U.userId
JOIN
    products P ON O.productId = P.productId

select * from UserOrderProductView