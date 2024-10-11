# sydnee_user_stories.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import chibuike_user_stories  # Import the partner module

class Payroll:
    def __init__(self, hourly_wage, tax_rate):
        self.hourly_wage = hourly_wage
        self.tax_rate = tax_rate
        self.work_log = {}  # Store clock-in and clock-out times

    def add_work_hours(self, day, clock_in, clock_out=None):
        if day not in self.work_log:
            self.work_log[day] = {}
        
        self.work_log[day]['clock_in'] = clock_in
        
        if clock_out:
            self.work_log[day]['clock_out'] = clock_out
            ci_time = datetime.strptime(clock_in, "%I:%M:%S %p")
            co_time = datetime.strptime(clock_out, "%I:%M:%S %p")
            hours_worked = (co_time - ci_time).seconds / 3600  # Convert seconds to hours
            self.work_log[day]['hours_worked'] = hours_worked
        else:
            self.work_log[day]['clock_out'] = None
            self.work_log[day]['hours_worked'] = 0

    def calculate_daily_earnings(self, day):
        hours = self.work_log.get(day, {}).get('hours_worked', 0)
        return hours * self.hourly_wage

    def calculate_tax(self, earnings):
        return earnings * self.tax_rate

    def calculate_net_earnings(self, day):
        earnings = self.calculate_daily_earnings(day)
        taxes = self.calculate_tax(earnings)
        net_earnings = earnings - taxes
        return earnings, taxes, net_earnings

# Function to view earnings for a specific day
def view_earnings(day, payroll):
    if day in payroll.work_log:
        clock_in = payroll.work_log[day].get('clock_in', 'No clock-in')
        clock_out = payroll.work_log[day].get('clock_out', 'No clock-out')
        earnings, taxes, net = payroll.calculate_net_earnings(day)
        messagebox.showinfo("Earnings Info", f"On {day}:\nClock In: {clock_in}\nClock Out: {clock_out}\nEarnings: ${earnings:.2f}\nTaxes: ${taxes:.2f}\nNet Earnings: ${net:.2f}")
    else:
        messagebox.showinfo("No Work", f"You didn't work on {day}.")

# Main Application
def main():
    root = tk.Tk()
    root.title("Payroll Information")
    root.geometry("600x400")

    # Get hourly wage and tax rate
    hourly_wage = simpledialog.askfloat("Input", "Enter hourly wage:")
    tax_rate = simpledialog.askfloat("Input", "Enter tax rate (as a decimal, e.g., 0.15 for 15%):")

    payroll = Payroll(hourly_wage, tax_rate)

    # Function to select a day
    def select_day():
        today = datetime.now().strftime("%A, %B %d, %Y")
        selected_day = simpledialog.askstring("Input", "Enter day (e.g., 'Monday, October 09, 2024'):", initialvalue=today)
        view_earnings(selected_day, payroll)

    # Button to check earnings for a selected day
    check_earnings_button = tk.Button(root, text="Check Earnings", command=select_day)
    check_earnings_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
