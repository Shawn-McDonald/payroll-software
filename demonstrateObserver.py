# Create subject (Employee Payroll)
employee = EmployeePayroll("Shawn", hours_worked=40, wage=25)

# Create observers
admin_observer = AdminObserver()
employee_observer = EmployeeObserver()
accounting_observer = AccountingObserver()

# Attach observers to the subject
employee.attach(admin_observer)
employee.attach(employee_observer)
employee.attach(accounting_observer)

# Make changes and notify observers
employee.hours_worked = 45   # This will notify all observers
employee.wage = 27           # This will notify all observers again