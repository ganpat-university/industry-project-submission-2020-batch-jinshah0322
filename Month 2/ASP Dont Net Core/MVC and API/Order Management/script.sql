USE [master]
GO
/****** Object:  Database [OrderManagement]    Script Date: 29-02-2024 19:52:49 ******/
CREATE DATABASE [OrderManagement]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'OrderManagement', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\OrderManagement.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'OrderManagement_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\OrderManagement_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [OrderManagement] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [OrderManagement].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [OrderManagement] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [OrderManagement] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [OrderManagement] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [OrderManagement] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [OrderManagement] SET ARITHABORT OFF 
GO
ALTER DATABASE [OrderManagement] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [OrderManagement] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [OrderManagement] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [OrderManagement] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [OrderManagement] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [OrderManagement] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [OrderManagement] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [OrderManagement] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [OrderManagement] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [OrderManagement] SET  DISABLE_BROKER 
GO
ALTER DATABASE [OrderManagement] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [OrderManagement] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [OrderManagement] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [OrderManagement] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [OrderManagement] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [OrderManagement] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [OrderManagement] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [OrderManagement] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [OrderManagement] SET  MULTI_USER 
GO
ALTER DATABASE [OrderManagement] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [OrderManagement] SET DB_CHAINING OFF 
GO
ALTER DATABASE [OrderManagement] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [OrderManagement] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [OrderManagement] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [OrderManagement] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [OrderManagement] SET QUERY_STORE = OFF
GO
USE [OrderManagement]
GO
/****** Object:  Table [dbo].[Customer]    Script Date: 29-02-2024 19:52:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Customer](
	[CustomerId] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](100) NULL,
	[Email] [nvarchar](100) NULL,
	[Address] [nvarchar](255) NULL,
	[isDeleted] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[CustomerId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Order]    Script Date: 29-02-2024 19:52:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Order](
	[OrderId] [int] IDENTITY(1,1) NOT NULL,
	[CustomerId] [int] NULL,
	[OrderDate] [datetime] NULL,
	[TotalAmount] [decimal](10, 2) NULL,
	[Status] [nvarchar](50) NULL,
	[isDeleted] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[OrderId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrderItem]    Script Date: 29-02-2024 19:52:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrderItem](
	[OrderItemId] [int] IDENTITY(1,1) NOT NULL,
	[OrderId] [int] NULL,
	[ProductId] [int] NULL,
	[Quantity] [int] NULL,
	[UnitPrice] [decimal](10, 2) NULL,
	[isDeleted] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[OrderItemId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Product]    Script Date: 29-02-2024 19:52:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Product](
	[ProductId] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](100) NULL,
	[Description] [nvarchar](max) NULL,
	[Price] [decimal](10, 2) NULL,
	[StockQuantity] [int] NULL,
	[isDeleted] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[ProductId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Customer] ON 

INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (1, N'Himanshu', N'himanshu@example.com', N'SilverTouch', 1)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (2, N'Jinay', N'jinay@example.com', N'Sabarmati', 0)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (3, N'supan', N'supan@example.com', N'Gujarat', 0)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (4, N'Naitik', N'naitik@gmail.com', N'Nadiad', 0)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (5, N'Surya', N'surya@gmail.com', N'', 1)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (6, N'Surya', N'surya@gmail.com', N'Nadiad', 1)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (7, N'Naitik', N'naitik@gmail.com', N'Nadiad', 0)
INSERT [dbo].[Customer] ([CustomerId], [Name], [Email], [Address], [isDeleted]) VALUES (8, N'Narsinh', N'user@example.com', N'Ahmedabad', 1)
SET IDENTITY_INSERT [dbo].[Customer] OFF
GO
SET IDENTITY_INSERT [dbo].[Order] ON 

INSERT [dbo].[Order] ([OrderId], [CustomerId], [OrderDate], [TotalAmount], [Status], [isDeleted]) VALUES (24, 2, CAST(N'2024-02-29T00:00:00.000' AS DateTime), CAST(400.00 AS Decimal(10, 2)), N'pending', 0)
SET IDENTITY_INSERT [dbo].[Order] OFF
GO
SET IDENTITY_INSERT [dbo].[OrderItem] ON 

INSERT [dbo].[OrderItem] ([OrderItemId], [OrderId], [ProductId], [Quantity], [UnitPrice], [isDeleted]) VALUES (17, 24, 1, 20, CAST(10.00 AS Decimal(10, 2)), 0)
SET IDENTITY_INSERT [dbo].[OrderItem] OFF
GO
SET IDENTITY_INSERT [dbo].[Product] ON 

INSERT [dbo].[Product] ([ProductId], [Name], [Description], [Price], [StockQuantity], [isDeleted]) VALUES (1, N'Mobile', N'Must need product', CAST(35000.00 AS Decimal(10, 2)), 80, 0)
INSERT [dbo].[Product] ([ProductId], [Name], [Description], [Price], [StockQuantity], [isDeleted]) VALUES (2, N'HP Laptop', N'Good for Programmers', CAST(75000.00 AS Decimal(10, 2)), 100, 0)
SET IDENTITY_INSERT [dbo].[Product] OFF
GO
ALTER TABLE [dbo].[Customer] ADD  DEFAULT ((0)) FOR [isDeleted]
GO
ALTER TABLE [dbo].[Order] ADD  DEFAULT ((0)) FOR [isDeleted]
GO
ALTER TABLE [dbo].[OrderItem] ADD  DEFAULT ((0)) FOR [isDeleted]
GO
ALTER TABLE [dbo].[Product] ADD  DEFAULT ((0)) FOR [isDeleted]
GO
ALTER TABLE [dbo].[Order]  WITH CHECK ADD FOREIGN KEY([CustomerId])
REFERENCES [dbo].[Customer] ([CustomerId])
GO
ALTER TABLE [dbo].[OrderItem]  WITH CHECK ADD FOREIGN KEY([OrderId])
REFERENCES [dbo].[Order] ([OrderId])
GO
ALTER TABLE [dbo].[OrderItem]  WITH CHECK ADD FOREIGN KEY([ProductId])
REFERENCES [dbo].[Product] ([ProductId])
GO
USE [master]
GO
ALTER DATABASE [OrderManagement] SET  READ_WRITE 
GO
