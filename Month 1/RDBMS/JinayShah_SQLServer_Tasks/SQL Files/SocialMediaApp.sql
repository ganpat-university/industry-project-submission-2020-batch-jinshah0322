create database socialmediaapp

use socialmediaapp

CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    UserName NVARCHAR(50) NOT NULL,
    FullName NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Birthdate DATE NULL,
    ProfileImage VARBINARY(MAX) NULL,
    IsActive BIT NOT NULL DEFAULT 1
)

CREATE TABLE Posts (
    PostID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT NOT NULL,
    Caption NVARCHAR(255) NULL,
    Image VARBINARY(MAX) NULL,
    PostedDate DATETIME NOT NULL,
    Likes INT DEFAULT 0,
    IsPublic BIT NOT NULL DEFAULT 1,
	foreign key(UserId) references Users(UserID)
)

CREATE TABLE Comments (
    CommentID INT PRIMARY KEY IDENTITY(1,1),
    PostID INT NOT NULL,
    UserID INT NOT NULL,
    CommentText NVARCHAR(MAX) NOT NULL,
    CommentDate DATETIME NOT NULL,
    FOREIGN KEY (PostID) REFERENCES Posts(PostID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)

CREATE TABLE Friendships (
    FriendshipID INT PRIMARY KEY IDENTITY(1,1),
    UserID1 INT NOT NULL,
    UserID2 INT NOT NULL,
    Status NVARCHAR(20) NOT NULL,
    SinceDate DATETIME NOT NULL,
    FOREIGN KEY (UserID1) REFERENCES Users(UserID),
    FOREIGN KEY (UserID2) REFERENCES Users(UserID)
)

CREATE TABLE Messages (
    MessageID INT PRIMARY KEY IDENTITY(1,1),
    SenderID INT NOT NULL,
    ReceiverID INT NOT NULL,
    MessageText NVARCHAR(MAX) NOT NULL,
    SentDate DATETIME NOT NULL,
    IsRead BIT NOT NULL DEFAULT 0,
    FOREIGN KEY (SenderID) REFERENCES Users(UserID),
    FOREIGN KEY (ReceiverID) REFERENCES Users(UserID)
)



insert into Users(UserName, FullName, Email, Birthdate, ProfileImage, IsActive)
values	('john_doe', 'John Doe', 'john.doe@example.com', '1990-05-15', NULL, 1),
		('jane_smith', 'Jane Smith', 'jane.smith@example.com', '1985-02-28', NULL, 1),
		('mark_johnson', 'Mark Johnson', 'mark.johnson@example.com', '1992-12-10', NULL, 1),
		('alice_williams', 'Alice Williams', 'alice.williams@example.com', '1987-07-03', NULL, 1),
		('bob_miller', 'Bob Miller', 'bob.miller@example.com', '1984-09-25', NULL, 1)

select * from Users


insert into Posts(UserID, Caption, Image, PostedDate, Likes, IsPublic)
values	(1, 'Enjoying a sunny day!', NULL, '2022-01-10 08:30:00', 15, 1),
		(2, 'Coding all day!', NULL, '2022-01-11 10:45:00', 20, 1),
		(3, 'Exploring new places.', NULL, '2022-01-12 12:15:00', 25, 1),
		(4, 'Nature hike with friends.', NULL, '2022-01-13 14:20:00', 18, 1),
		(5, 'Poetry reading night.', NULL, '2022-01-14 16:45:00', 30, 1)

select * from Posts


insert into Comments(PostID, UserID, CommentText, CommentDate)
values	(1, 2, 'Looks amazing!', '2022-01-10 09:00:00'),
		(2, 3, 'Great code!', '2022-01-11 11:00:00'),
		(3, 4, 'Beautiful places!', '2022-01-12 13:00:00'),
		(4, 5, 'Nature is the best!', '2022-01-13 15:00:00'),
		(5, 1, 'Love poetry!', '2022-01-14 17:00:00')

select * from Comments


insert into Friendships(UserID1, UserID2, Status, SinceDate)
values	(1, 2, 'Friends', '2022-01-01'),
		(2, 3, 'Friends', '2022-01-02'),
		(3, 4, 'Friends', '2022-01-03'),
		(4, 5, 'Friends', '2022-01-04'),
		(5, 1, 'Friends', '2022-01-05')

select * from Friendships


insert into Messages(SenderID, ReceiverID, MessageText, SentDate, IsRead)
values	(1, 2, 'Hi Jane! How are you?', '2022-01-01 09:30:00', 0),
		(2, 3, 'Hey Mark! Working on any projects?', '2022-01-02 11:00:00', 1),
		(3, 4, 'Hello Alice! Lets plan a trip.', '2022-01-03 13:30:00', 0),
		(4, 5, 'Hi Bob! Nature hike this weekend?', '2022-01-04 15:45:00', 1),
		(5, 1, 'Hey John! Poetry night on Friday!', '2022-01-05 18:00:00', 0);

select * from Messages

/*Display the post of john_doe user using subquery*/
select * from Posts where UserID=(select UserID from users where UserName='john_doe')

/*Display all the friends of john_doe using subquery*/
select * from Friendships where UserID1 in (select userId from Users where UserName='john_doe') or UserID2 in (select userId from Users where UserName='john_doe')

/*Display all the unread messages by the john_doe using subquery*/
select * from Messages where ReceiverID=(select userId from Users where UserName='john_doe') and IsRead=0

/*Count of post of each user using inline query*/
select userName,(select count(*) from Posts where userId=Users.UserID) PostCount from users

/*Display latest post of each user using inline query*/
select UserName,(select top 1 Caption from Posts where UserID=Users.UserID order by PostedDate desc) LatestPost from Users

/*Display latest comment of each user using inline query*/
select UserName,(select top 1 CommentText from Comments where UserID=Users.UserID) latestMessage from Users


/*String functions*/
SELECT U.UserName, P.Caption,CONCAT(U.UserName, ' - ', P.Caption) AS UserNameAndCaption FROM Users U INNER JOIN Posts P ON U.UserID = P.UserID

select FriendshipID,(select UserName from Users where UserID=Friendships.UserID1) user1,(select UserName from Users where UserID=Friendships.UserID2)user2,status,REPLACE(Status, 'friends', 'notFriend') AS UpdatedStatus  from Friendships

select c.CommentID,u.UserName,QUOTENAME(CONCAT(u.UserName,'-',c.CommentText)) from Users u inner join Comments c on u.UserID=c.UserID

/*Math functions*/
SELECT U.UserID, U.UserName, SUM(P.Likes) AS TotalLikes FROM Users U INNER JOIN Posts P ON U.UserID = P.UserID GROUP BY U.UserID, U.UserName

SELECT C.CommentText, P.Caption,AVG(P.Likes) AS AverageLikesPerComment FROM Comments C INNER JOIN Posts P ON C.PostID = P.PostID GROUP BY C.CommentID, C.CommentText, P.PostID, P.Caption

SELECT U.UserID, U.UserName, COUNT(*) AS NumberOfPosts FROM Users U INNER JOIN Posts P ON U.UserID = P.UserID GROUP BY U.UserID, U.UserName

/*Date functions*/
SELECT C.CommentText, U.UserName, DATEDIFF(YEAR, U.Birthdate, GETDATE()) AS UserAge FROM Comments C INNER JOIN Users U ON C.UserID = U.UserID

SELECT YEAR(U.Birthdate) AS BirthYear, COUNT(P.PostID) AS TotalPosts FROM Users U INNER JOIN Posts P ON U.UserID = P.UserID GROUP BY YEAR(U.Birthdate)

select FriendshipID,(select UserName from Users where UserID=Friendships.UserID1) user1,(select UserName from Users where UserID=Friendships.UserID2)user2,datediff(year,SinceDate,GETDATE()) AS friendSince  from Friendships

/*Advanced functions*/
SELECT U.UserID, U.UserName, F.FriendshipID, CAST(F.SinceDate AS DATETIME) AS FriendSinceDate FROM Users U INNER JOIN Friendships F ON U.UserID = F.UserID1

SELECT P.PostID, P.Caption, P.Likes, U.UserName, IIF(P.Likes >= 20, 'High Likes', 'Low Likes') AS LikeCategory FROM Posts P INNER JOIN Users U ON P.UserID = U.UserID;

SELECT P.PostID, P.Caption, P.Likes, U.UserName, NULLIF(25,P.Likes) AS LikesEqual25 FROM Posts P INNER JOIN Users U ON P.UserID = U.UserID;