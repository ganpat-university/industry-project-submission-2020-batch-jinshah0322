create database librarymanagement

use librarymanagement

create table authors(
	authorId int primary key identity(1,1),
	firstName nvarchar(100) not null,
	lastName nvarchar(100) not null,
	birthdate date,
	nationality nvarchar(100),
	awarded bit not null,
	awardDate date,
)

create table publisher(
	publisherId int primary key identity(1,1),
	publisherName nvarchar(100) not null,
	publishDate date not null,
	publisherContact varchar(10),
)

create table books(
	bookId int primary key identity(1,1),
	title nvarchar(100) not null,
	author nvarchar(100) not null,
	genre nvarchar(100),
	publishDate date not null,
	copiesAvailable int not null,
	shelfLocation nvarchar(100),
	price decimal(10,2) not null,
	authorId int not null,
	publisherId int not null,
	isEook bit default 0,
	foreign key (authorId) references authors(authorId),
	foreign key (publisherId) references publisher(publisherId),
)

create table members(
	memberId int primary key identity(1,1),
	firstName nvarchar(100) not null,
	lastName nvarchar(100) not null,
	birthDate date,
	contact varchar(10) not null,
	memberType char(1) not null,
)

create table reviews(
	reviewId int primary key identity(1,1),
	memberId int not null,
	bookId int not null,
	rating tinyint not null,
	comment nvarchar(100),
	reviewDate datetime not null,
	reviewSentiment bit,
	foreign key (memberId) references members(memberID),
	foreign key (bookId) references books(bookId)
)



insert into authors(firstName,lastName,birthdate,nationality,awarded,awardDate)
values  ('John', 'Doe', '1980-05-15', 'American', 1, '2005-08-20'),
		('Jane', 'Smith', '1975-02-28', 'British', 0, NULL),
		('Mark', 'Johnson', '1990-12-10', 'Canadian', 1, '2010-03-18'),
		('Alice', 'Williams', '1985-07-03', 'Australian', 0, NULL),
		('Bob', 'Miller', '1982-09-25', 'German', 1, '2007-06-12')

select * from authors


insert into publisher(publisherName,publishDate,publisherContact)
values	('ABC Publishers', '2000-01-15', '1234567890'),
		('XYZ Publications', '1995-08-22', '9876543210'),
		('BookHouse', '2005-03-10', '5678901234')

select * from publisher


insert into books(title, author, genre, publishDate, copiesAvailable, shelfLocation, price, authorId, publisherId, isEook)
values	('The Book of Everything', 'John Doe', 'Fiction', '2000-05-20', 100, 'A1', 25.99, 1, 1, 0),
		('Coding 101', 'Jane Smith', 'Programming', '2015-12-08', 50, 'B2', 35.50, 2, 2, 1),
		('History of Science', 'Mark Johnson', 'Non-Fiction', '2012-07-15', 75, 'C3', 18.75, 3, 3, 0),
		('Nature Exploration', 'Alice Williams', 'Nature', '2008-09-30', 30, 'D4', 12.99, 4, 1, 0),
		('Poetry Collection', 'Bob Miller', 'Poetry', '2019-04-12', 20, 'E5', 8.50, 5, 2, 1)

select * from books


insert into members (firstName, lastName, birthDate, contact, memberType)
values	('Alice', 'Doe', '1995-03-10', '9876543210', 'S'),
		('Bob', 'Smith', '1980-09-18', '1234567890', 'F'),
		('Charlie', 'Johnson', '1992-11-05', '5678901234', 'S'),
		('David', 'White', '1988-06-22', '3456789012', 'F'),
		('Eva', 'Davis', '1997-12-03', '7890123456', 'S')

select * from members


insert into reviews(memberId, bookId, rating, comment, reviewDate, reviewSentiment)
values	(1, 1, 4, 'Great book!', '2022-01-01 08:30:00', 1),
		(2, 2, 5, 'Excellent coding guide.', '2022-01-02 10:45:00', 1),
		(3, 3, 3, 'Interesting history book.', '2022-01-03 12:15:00', 0),
		(4, 4, 4, 'Enjoyed the nature exploration.', '2022-01-04 14:20:00', 1),
		(5, 5, 3, 'Nice collection of poetry.', '2022-01-05 16:45:00', 0)

select * from reviews



/* find the books published by 'ABC Publishers' write sub query*/
select title from books where publisherId=(select publisherId from publisher where publisherName='ABC Publishers')

/*find members who have more than or equal to 4 ratings write sub query*/
select * from members where memberId in (select memberId from reviews where rating>=4)

/* find book with highest number of reviews write sub query*/
select * from books where bookId in (select top 1 bookId from reviews group by bookId order by count(reviewId) desc)

/*find the books published by 'ABC Publishers' write inline query*/
select publisherName,(select count(*) nbooks from books where publisherId=publisher.publisherId) 'Number of books' from publisher where publisherName='ABC Publishers'

/*Find rating of The Book of Everything book write inline query*/
select title,(select rating from reviews where bookId=books.bookId) from books where title='The Book of Everything'

/*Find the books written by John write inline query*/
select firstName ,(select title from books where authorId=authors.authorId) Book from authors where firstName='John'


/*String Functions*/
SELECT B.title, A.firstName + ' ' + A.lastName AS AuthorFullName, M.firstName + ' ' + M.lastName AS MemberFullName, R.rating FROM books B INNER JOIN authors A ON B.authorId = A.authorId INNER JOIN reviews R ON B.bookId = R.bookId INNER JOIN members M ON R.memberId = M.memberId

SELECT B.title, CONCAT(A.firstName, ' ', A.lastName, ' - ', A.nationality) AS AuthorFullNameNationality FROM books B INNER JOIN authors A ON B.authorId = A.authorId

SELECT B.title, P.publisherName,REPLACE(P.publisherName, 'Publication', 'Company') AS UpdatedPublisherName FROM books B INNER JOIN publisher P ON B.publisherId = P.publisherId

/*Math Functions*/
SELECT A.authorId, A.firstName, A.lastName, B.title, B.price AS OriginalPrice, B.price * 0.9 AS DiscountedPrice FROM Authors A INNER JOIN Books B ON A.authorId = B.authorId

SELECT B.bookId, B.title, B.price, R.rating,B.price * R.rating AS TotalValue FROM Books B INNER JOIN Reviews R ON B.bookId = R.bookId

SELECT B.bookId, B.title, B.price,AVG(CAST(R.rating AS INT)) AS AverageRating FROM Books B LEFT JOIN Reviews R ON B.bookId = R.bookId GROUP BY B.bookId, B.title, B.price

/*Date functions*/
SELECT M.firstName, M.lastName, R.reviewDate, FORMAT(R.reviewDate, 'MM/dd/yyyy') AS FormattedReviewDate FROM Members M INNER JOIN Reviews R ON M.memberId = R.memberId

SELECT B.title, A.firstName, A.lastName, A.birthdate FROM Books B INNER JOIN Authors A ON B.authorId = A.authorId WHERE YEAR(A.birthdate) < 2000

SELECT B.title, R.rating, R.comment, R.reviewDate FROM Books B INNER JOIN Reviews R ON B.bookId = R.bookId WHERE R.reviewDate >= DATEADD(year, -5, GETDATE())

/*Advanced functions*/
SELECT B.title, COALESCE(A.firstName + ' ' + A.lastName, 'Unknown') AS AuthorFullName FROM Books B LEFT JOIN Authors A ON B.authorId = A.authorId

SELECT M.firstName, M.lastName, ISNULL(CONVERT(VARCHAR, R.reviewDate), 'Not Reviewed') AS ReviewDate FROM Members M LEFT JOIN Reviews R ON M.memberId = R.memberId

SELECT B.title,IIF(R.reviewId IS NOT NULL, 'Has Review', 'No Review') AS ReviewStatus FROM Books B LEFT JOIN Reviews R ON B.bookId = R.bookId