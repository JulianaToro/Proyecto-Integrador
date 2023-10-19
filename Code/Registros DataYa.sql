CREATE DATABASE accounts_db;
USE accounts_db;

CREATE TABLE Usuarios (
ID INT auto_increment,
Name VARCHAR(50),
Last_Name VARCHAR(50),
Email VARCHAR(100) UNIQUE,
Company_name VARCHAR(100),
Role VARCHAR(100),
Password VARCHAR(100),
primary key (ID)
);