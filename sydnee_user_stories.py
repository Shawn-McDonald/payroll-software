import os
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime, timedelta

root = tk.Tk()
root.title("Employee Time Tracker")
root.geometry("1360x800")

# Set up column headers and times for Treeview
name = "Chibuike Ijem"
cols = ["", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
rows = ["7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM",
        "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM"]

time_log_matrix = [["" for _ in range(len(cols))] for _ in range(len(rows))]
time_log = ttk.Treeview(root, columns=cols, show="headings", height=13)
for i, day in enumerate(cols):
    time_log.column(day, width=120, anchor="center")
    time_log.heading(day, text=day)
for i, time in enumerate(rows):
    time_log.insert('', 'end', values=[time] + [""] * (len(cols) - 1))

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12))
style.configure("Treeview", rowheight=50, font=("Arial", 12))

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=10)
root.grid_columnconfigure(0, weight=1)

label = tk.Label(root, text=f"Welcome {name}, to the Employee Time Tracker!", font=("Arial", 24))
label.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")
time_log.grid(row=1, column=0, rowspan=2, columnspan=4, sticky="nsew", padx=20, pady=5)

# Variables for hourly pay, tax, and logs
hourly_pay = 0.0
tax_deduction = 0.0
daily_log = {}
earnings_log = {}

# Function to set hourly pay and tax, required before clocking in
def set_pay_and_tax():
    global hourly_pay, tax_deduction
    while True:
        try:
            hourly_pay = float(simpledialog.askstring("Hourly Pay", "Enter your hourly pay:"))
            tax_deduction = float(simpledialog.askstring("Tax Deduction", "Enter your tax deduction percentage in decimal form:")) / 100
            if hourly_pay > 0 and 0 <= tax_deduction <= 1:
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter valid positive values for hourly pay and tax deduction.")
        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

    messagebox.showinfo("Settings Saved", "Your hourly pay and tax deduction have been set.")

# Update Treeview with current time log
def update_treeview():
    for i, row in enumerate(time_log_matrix):
        time_log.item(time_log.get_children()[i], values=[rows[i]] + row[1:])

# Clock-in and clock-out functions
def clocked_in():
    if hourly_pay == 0 or tax_deduction == 0:
        messagebox.showerror("Error", "Please set your hourly pay and tax deduction before clocking in.")
        return

    now = datetime.now()
    day_key = now.strftime("%Y-%m-%d")
    if day_key not in daily_log:
        daily_log[day_key] = {"clock_in": [], "clock_out": []}
    daily_log[day_key]["clock_in"].append(now)
    messagebox.showinfo("Clocked In", f"Clocked in at {now.strftime('%I:%M:%S %p')} on {day_key}")

def clocked_out():
    if hourly_pay == 0 or tax_deduction == 0:
        messagebox.showerror("Error", "Please set your hourly pay and tax deduction before clocking out.")
        return

    now = datetime.now()
    day_key = now.strftime("%Y-%m-%d")
    if day_key in daily_log and daily_log[day_key]["clock_in"]:
        daily_log[day_key]["clock_out"].append(now)
        calculate_daily_earnings(day_key)
        messagebox.showinfo("Clocked Out", f"Clocked out at {now.strftime('%I:%M:%S %p')} on {day_key}")
    else:
        messagebox.showerror("Error", "Please clock in first before clocking out.")

# Calculate total hours worked in a day and save earnings
def calculate_daily_earnings(day_key):
    total_minutes = 0
    if day_key in daily_log:
        logs = daily_log[day_key]
        for clock_in, clock_out in zip(logs["clock_in"], logs["clock_out"]):
            total_minutes += (clock_out - clock_in).total_seconds() / 60

    hours_worked = total_minutes / 60
    daily_gross = hourly_pay * hours_worked
    daily_net = daily_gross * (1 - tax_deduction)

    earnings_log[day_key] = {"hours_worked": hours_worked, "gross": daily_gross, "net": daily_net}
    update_treeview()

# Function to check daily earnings for a specific date
def check_daily_earnings():
    date_str = tk.simpledialog.askstring("Daily Earnings", "Enter the date (YYYY-MM-DD):")
    
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        
        if date in earnings_log:
            earnings = earnings_log[date]
            daily_gross = earnings["gross"]
            daily_net = earnings["net"]
            messagebox.showinfo("Daily Earnings",
                                f"Earnings for {date}:\n"
                                f"Gross: ${daily_gross:.2f}\n"
                                f"Net: ${daily_net:.2f}")
        else:
            messagebox.showinfo("No Earnings", f"No earnings recorded for {date}.")
    
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in the format YYYY-MM-DD.")

# Button to check daily earnings
button_5 = tk.Button(root, text="Check Daily Earnings", font=("Arial", 12), command=check_daily_earnings)
button_5.grid(row=2, column=5, padx=30, pady=15, sticky="ew")

# Function to check weekly earnings
def check_weekly_earnings():
    date_str = simpledialog.askstring("Weekly Earnings", "Enter the date (YYYY-MM-DD):")
    
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        start_of_week = date - timedelta(days=date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        weekly_gross = 0.0
        weekly_net = 0.0
        
        for i in range(7):
            current_day = start_of_week + timedelta(days=i)
            current_day_str = current_day.strftime("%Y-%m-%d")
            if current_day_str in earnings_log:
                weekly_gross += earnings_log[current_day_str]["gross"]
                weekly_net += earnings_log[current_day_str]["net"]
        
        messagebox.showinfo("Weekly Earnings",
                            f"Weekly Earnings from {start_of_week.strftime('%Y-%m-%d')} to {end_of_week.strftime('%Y-%m-%d')}:\n"
                            f"Gross: ${weekly_gross:.2f}\n"
                            f"Net: ${weekly_net:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in the format YYYY-MM-DD.")

# Function to calculate year-to-date earnings
def calculate_year_to_date_earnings():
    current_year = datetime.now().year
    year_to_date_gross = 0.0
    year_to_date_net = 0.0

    for date_str, earnings in earnings_log.items():
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date.year == current_year:
            year_to_date_gross += earnings["gross"]
            year_to_date_net += earnings["net"]

    messagebox.showinfo("Year-to-Date Earnings",
                        f"Year-to-Date Earnings for {current_year}:\n"
                        f"Gross: ${year_to_date_gross:.2f}\n"
                        f"Net: ${year_to_date_net:.2f}")

# Buttons on the right side
button_1 = tk.Button(root, text="Clock In", font=("Arial", 12), command=clocked_in)
button_2 = tk.Button(root, text="Clock Out", font=("Arial", 12), command=clocked_out)
button_4 = tk.Button(root, text="Check Weekly Earnings", font=("Arial", 12), command=check_weekly_earnings)
button_6 = tk.Button(root, text="Year-to-Date Earnings", font=("Arial", 12), command=calculate_year_to_date_earnings)

button_1.grid(row=1, column=5, padx=30, pady=15, sticky="ew")
button_2.grid(row=1, column=6, padx=30, pady=15, sticky="ew")
button_4.grid(row=2, column=6, padx=30, pady=15, sticky="ew")
button_6.grid(row=3, column=5, padx=30, pady=15, sticky="ew")

# Prompt user for pay and tax settings before main interface opens
set_pay_and_tax()

root.mainloop() 