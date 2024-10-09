# main.py 

import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import sydnee_user_stories  # Your software
import chibuike_user_stories  # Partner's software

def main():
    root = tk.Tk()
    root.title("Payroll System")
    root.geometry("600x400")

    # Get hourly wage and tax rate
    hourly_wage = simpledialog.askfloat("Input", "Enter hourly wage:")
    tax_rate = simpledialog.askfloat("Input", "Enter tax rate (as a decimal, e.g., 0.15 for 15%):")

    # Initialize Payroll instances for both users
    sydnee_payroll = sydnee_user_stories.Payroll(hourly_wage, tax_rate)
    chibuike_payroll = chibuike_user_stories.Payroll(hourly_wage, tax_rate)

    # Frame for Sydnee's functions
    sydnee_frame = tk.Frame(root)
    sydnee_frame.pack(side="left", padx=20, pady=20)

    sydnee_label = tk.Label(sydnee_frame, text="Sydnee's Payroll Section", font=("Arial", 16))
    sydnee_label.pack(pady=10)

    # Button to check earnings for Sydnee
    check_earnings_button = tk.Button(sydnee_frame, text="Check Earnings", command=lambda: sydnee_user_stories.view_earnings(datetime.now().strftime("%A, %B %d, %Y"), sydnee_payroll))
    check_earnings_button.pack(pady=10)

    # Frame for Chibuike's functions
    chibuike_frame = tk.Frame(root)
    chibuike_frame.pack(side="right", padx=20, pady=20)

    chibuike_label = tk.Label(chibuike_frame, text="Chibuike's Time Tracker", font=("Arial", 16))
    chibuike_label.pack(pady=10)

    # Clock-in button for Chibuike
    clock_in_button = tk.Button(chibuike_frame, text="Clock In", command=lambda: chibuike_user_stories.clock_in(chibuike_payroll))
    clock_in_button.pack(pady=10)

    # Clock-out button for Chibuike
    clock_out_button = tk.Button(chibuike_frame, text="Clock Out", command=lambda: chibuike_user_stories.clock_out(chibuike_payroll))
    clock_out_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
