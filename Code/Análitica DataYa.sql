CREATE DATABASE analytics_db;
USE analytics_db;

CREATE TABLE AnalysisReport (
    id INT AUTO_INCREMENT PRIMARY KEY,
    excel_file VARCHAR(900) NOT NULL,
    mae FLOAT NOT NULL
);