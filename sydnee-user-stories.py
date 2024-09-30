#Sydnee Young
#User Stories

class Payroll:
    def __init__(self, hourly_wage, tax_rate):
        self.hourly_wage = hourly_wage
        self.tax_rate = tax_rate
        self.daily_hours = []
        self.daily_earnings = []
    
    def clock_in(self):
        #user input of hours worked today
        #place holder for future clock in and clock out calculations
        #you will not have to enter the hours worked, you will just
        #have to clock in and clock out, the program wil then calculate
        #your hours that day
        hours = float(input("Enter hours worked today: "))
        self.daily_hours.append(hours)
        self.calculate_daily_earnings(hours)
    
    def calculate_daily_earnings(self, hours):
        earnings = hours * self.hourly_wage
        self.daily_earnings.append(earnings)
        print(f"Today's earnings: ${earnings:.2f}")
    
    def calculate_weekly_earnings(self):
        weekly_earnings = sum(self.daily_earnings)
        return weekly_earnings
    
    def calculate_tax(self, earnings):
        taxes = earnings * self.tax_rate
        return taxes
    
    def calculate_net_earnings(self):
        weekly_earnings = self.calculate_weekly_earnings()
        taxes = self.calculate_tax(weekly_earnings)
        net_earnings = weekly_earnings - taxes
        return weekly_earnings, taxes, net_earnings


#tax deduction user story
#Computer will also know what tax percentage is being deducted
#due to time restraints on this class, we will just have Myrtle Beach, SC
#but for right now you will enter the tax deduction percentage manually
hourly_wage = float(input("Enter hourly wage: "))
tax_rate = float(input("Enter tax rate (as a decimal, e.g., 0.15 for 15%): "))

payroll = Payroll(hourly_wage, tax_rate)

# Simulate clocking in and calculating for 5 days
#I will use other group memebers programs to write this section 
#for now this is a place holder of what the program will do
for day in range(5):
    print(f"Day {day + 1}:")
    payroll.clock_in()

weekly_earnings, taxes, net_earnings = payroll.calculate_net_earnings()

print(f"Total weekly earnings: ${weekly_earnings:.2f}")
print(f"Taxes deducted: ${taxes:.2f}")
print(f"Net earnings after taxes: ${net_earnings:.2f}")
