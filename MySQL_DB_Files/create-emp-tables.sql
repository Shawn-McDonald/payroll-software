-- Creates the EmployeeTimeTracker database if it already doesn't exist
create database if not exists EmployeeTimeTracker;

-- Switches to the EmployeeTimeTracker database
use EmployeeTimeTracker;

-- Creates the Users table to store employee and admin details
create table Users (
	UserID int auto_increment primary key,
    Username varchar(50) unique not null,
    PasswordHash varchar(255) not null,
    FullName varchar(100) not null,
    Role enum('Employee', 'Admin') default 'Employee',
    CreatedAt timestamp default current_timestamp
);

-- Creates the ClockLogs table to store clock-in/clock-out data
create table ClockLogs (
	LogID int auto_increment primary key,
    UserID int not null,
    WeekLabel varchar(50) not null,
    DayOfWeek enum('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat') not null,
    TimeLog varchar(500) default null,
	LogDate date not null,
    foreign key (UserID) references Users(UserID) on delete cascade
);

-- Inserts sample data into the Users table for testing
insert into Users (Username, PasswordHash, FullName, Role)
values
('johndoe', SHA2('password123', 256), 'John Doe', 'Employee'),
('janedoe', SHA2('adminpass', 256), 'Jane Doe', 'Admin');

-- Inserts sample clock-in/out data into the ClockLogs table for testing
insert into ClockLogs (UserID, WeekLabel, DayOfWeek, TimeLog, LogDate)
values
(1, 'Week of Nov. 20, 2024', 'Mon', 'In: 08:00 AM, Out: 05:00 PM', '2024-11-20'),
(1, 'Week of Nov. 20, 2024', 'Tue', 'In: 08:10 AM, Out: 04:50 PM', '2024-11-21'),
(2, 'Week of Nov. 20, 2024', 'Wed', 'In: 09:00 AM, Out: 05:30 PM', '2024-11-22');

-- Select all data from the Users and ClockLogs tables to verify contents
SELECT * FROM Users;
SELECT * FROM ClockLogs;

-- Create an index on the WeekLabel and UserID columns in the ClockLogs table to optimize weekly and user-specific queries
create index WeekLabelidx on ClockLogs (WeekLabel);
create index UserIDidx on ClockLogs (UserID);