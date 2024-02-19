-- Create the "emp" database
CREATE DATABASE IF NOT EXISTS emp;
USE emp;

-- Create a new table to store department information
CREATE TABLE Department (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    DepartmentName VARCHAR(100),
    ManagerID INT,
    Location VARCHAR(100)
);

-- Insert sample data into the Department table
INSERT INTO Department (DepartmentName, ManagerID, Location)
VALUES ('IT', 1, 'New York'),
       ('HR', 2, 'Los Angeles');

-- Create a new table to store employee information
CREATE TABLE Employee (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10, 2),
    HireDate DATE,
    CONSTRAINT FK_Department_Employee FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

-- Insert sample data into the Employee table
INSERT INTO Employee (FirstName, LastName, DepartmentID, Salary, HireDate)
VALUES ('John', 'Doe', 1, 50000.00, '2022-01-15'),
       ('Jane', 'Smith', 2, 60000.00, '2021-03-20'),
       ('David', 'Johnson', 1, 55000.00, '2022-05-10');

-- Retrieve employee information along with department details
SELECT e.FirstName, e.LastName, d.DepartmentName, e.Salary
FROM Employee e
JOIN Department d ON e.DepartmentID = d.DepartmentID;

-- Update the salary of all employees in the IT department
UPDATE Employee AS e
JOIN Department AS d ON e.DepartmentID = d.DepartmentID
SET e.Salary = e.Salary * 1.1
WHERE d.DepartmentName = 'IT';

-- Delete employees who were hired before 2021-01-01
DELETE FROM Employee
WHERE HireDate < '2021-01-01';

-- Perform data migration from the Employee table to a new table Employee_Backup
CREATE TABLE Employee_Backup AS
SELECT *
FROM Employee;

-- Drop the original Employee table
DROP TABLE Employee;
