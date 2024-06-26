USE [master]
GO
/****** Object:  Database [CoreMVC]    Script Date: 22-02-2024 13:19:11 ******/
CREATE DATABASE [CoreMVC]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'CoreMVC', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\CoreMVC.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'CoreMVC_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\CoreMVC_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [CoreMVC] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [CoreMVC].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [CoreMVC] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [CoreMVC] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [CoreMVC] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [CoreMVC] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [CoreMVC] SET ARITHABORT OFF 
GO
ALTER DATABASE [CoreMVC] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [CoreMVC] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [CoreMVC] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [CoreMVC] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [CoreMVC] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [CoreMVC] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [CoreMVC] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [CoreMVC] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [CoreMVC] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [CoreMVC] SET  DISABLE_BROKER 
GO
ALTER DATABASE [CoreMVC] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [CoreMVC] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [CoreMVC] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [CoreMVC] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [CoreMVC] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [CoreMVC] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [CoreMVC] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [CoreMVC] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [CoreMVC] SET  MULTI_USER 
GO
ALTER DATABASE [CoreMVC] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [CoreMVC] SET DB_CHAINING OFF 
GO
ALTER DATABASE [CoreMVC] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [CoreMVC] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [CoreMVC] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [CoreMVC] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [CoreMVC] SET QUERY_STORE = OFF
GO
USE [CoreMVC]
GO
/****** Object:  Table [dbo].[Department]    Script Date: 22-02-2024 13:19:11 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Department](
	[DepartmentID] [int] IDENTITY(1,1) NOT NULL,
	[DepartmentName] [varchar](100) NOT NULL,
	[DepartmentHead] [varchar](100) NOT NULL,
	[Budget] [decimal](18, 2) NOT NULL,
	[CreationDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[DepartmentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Employee]    Script Date: 22-02-2024 13:19:11 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Employee](
	[EmployeeID] [int] IDENTITY(1,1) NOT NULL,
	[FirstName] [varchar](50) NOT NULL,
	[LastName] [varchar](50) NOT NULL,
	[Email] [varchar](100) NOT NULL,
	[Salary] [decimal](10, 2) NOT NULL,
	[HireDate] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[EmployeeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Department] ON 

INSERT [dbo].[Department] ([DepartmentID], [DepartmentName], [DepartmentHead], [Budget], [CreationDate], [IsActive]) VALUES (1, N'Marketing', N'John Doe', CAST(10000.00 AS Decimal(18, 2)), CAST(N'2024-02-22' AS Date), 1)
INSERT [dbo].[Department] ([DepartmentID], [DepartmentName], [DepartmentHead], [Budget], [CreationDate], [IsActive]) VALUES (2, N'Finance', N'Jane Smith', CAST(15000.00 AS Decimal(18, 2)), CAST(N'2024-02-22' AS Date), 1)
INSERT [dbo].[Department] ([DepartmentID], [DepartmentName], [DepartmentHead], [Budget], [CreationDate], [IsActive]) VALUES (3, N'HR', N'Michael Johnson', CAST(12000.00 AS Decimal(18, 2)), CAST(N'2024-02-22' AS Date), 1)
INSERT [dbo].[Department] ([DepartmentID], [DepartmentName], [DepartmentHead], [Budget], [CreationDate], [IsActive]) VALUES (4, N'IT', N'Emily Brown', CAST(20000.00 AS Decimal(18, 2)), CAST(N'2024-02-22' AS Date), 1)
INSERT [dbo].[Department] ([DepartmentID], [DepartmentName], [DepartmentHead], [Budget], [CreationDate], [IsActive]) VALUES (5, N'Operations', N'David Wilson', CAST(18000.00 AS Decimal(18, 2)), CAST(N'2024-02-22' AS Date), 1)
SET IDENTITY_INSERT [dbo].[Department] OFF
GO
SET IDENTITY_INSERT [dbo].[Employee] ON 

INSERT [dbo].[Employee] ([EmployeeID], [FirstName], [LastName], [Email], [Salary], [HireDate]) VALUES (3, N'Michael', N'Johnson', N'michael.johnson@example.com', CAST(55000.00 AS Decimal(10, 2)), CAST(N'2023-03-10' AS Date))
INSERT [dbo].[Employee] ([EmployeeID], [FirstName], [LastName], [Email], [Salary], [HireDate]) VALUES (4, N'Emily', N'Brown', N'emily.brown@example.com', CAST(62000.00 AS Decimal(10, 2)), CAST(N'2021-11-05' AS Date))
INSERT [dbo].[Employee] ([EmployeeID], [FirstName], [LastName], [Email], [Salary], [HireDate]) VALUES (5, N'David', N'Wilson', N'david.wilson@example.com', CAST(58000.00 AS Decimal(10, 2)), CAST(N'2022-09-25' AS Date))
INSERT [dbo].[Employee] ([EmployeeID], [FirstName], [LastName], [Email], [Salary], [HireDate]) VALUES (6, N'Jinay', N'Shah', N'jinshah0322@gmail.com', CAST(5000.00 AS Decimal(10, 2)), CAST(N'2024-01-08' AS Date))
SET IDENTITY_INSERT [dbo].[Employee] OFF
GO
USE [master]
GO
ALTER DATABASE [CoreMVC] SET  READ_WRITE 
GO
