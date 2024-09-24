# payroll-software
Project for CSCI-490

### Design Pattern
MVC (Model, View, Controller)

Model: This will handle the application's data logic, such as employee hours, wages, tax rates, and administrator information. This layer would manage how the data is stored, retrieved, and manipulated, likely interfacing with a SQL database.

View: This is responsible for presenting the data to the user, whether it's the employee entering hours or the admin managing them. This would likely include web pages or API responses since our application is full stack.

Controller: This acts as the intermediary between the model and view, handling user input, manipulating data in the model, and determining which view to display.
