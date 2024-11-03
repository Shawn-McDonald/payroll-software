import os
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
# import shawn_user_stories

# Initialize main window
root=tk.Tk()
root.title("Employee Time Tracker")
root.geometry("1360x800")

# User-specific name and column headers for the schedule
name="Chibuike Ijem"
cols=["", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Time rows for each hour of a workday
rows=["7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", 
              "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM"]

# Initialize a matrix for storing clock-in/clock-out times
time_log_matrix=[["" for _ in range(len(cols))] for _ in range(len(rows))]
# Create Treeview widget for time log display
time_log=ttk.Treeview(root, columns=cols, show="headings", height=13)

# Setup column width and headers for Treeview
for i, day in enumerate(cols):
    time_log.column(day, width=120, anchor="center")
    time_log.heading(day, text=day)

# Add rows to the Treeview (first column is time, other columns are for logging)
for i, time in enumerate(rows):
    time_log.insert('', 'end', values=[time] + [""] * (len(cols) - 1))

# Configure styles for headings and row height
style=ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12))
style.configure("Treeview", rowheight=50, font=("Arial", 12))

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=10)
root.grid_columnconfigure(0, weight=1)

# Create a welcome label with the user's name
label=tk.Label(root, text=f"Welcome {name}, to the Employee Time Tracker!", font=("Arial", 24))
label.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

# Place the Treeview in the window
time_log.grid(row=1, column=0, rowspan=2, columnspan=4, sticky="nsew", padx=20, pady=5)

# Function to update the Treeview with new data from the matrix
def update_treeview():
    for i, row in enumerate(time_log_matrix):
        time_log.item(time_log.get_children()[i], values=[rows[i]] + row[1:])

# Function to log the user's clock-in time
def clocked_in():
    nowDay=datetime.now().strftime("%a")  # Get current day abbreviation
    nowTime=datetime.now().strftime("%I:00 %p").lstrip('0')  # Get the current time in "hour:00 AM/PM" format
    ciTime=datetime.now().strftime("%b %d, %Y at %I:%M %p")  # Clock-in time as string
    logciTime=datetime.now().strftime("%I:%M:%S %p")  # Clock-in time with seconds

    # Find the correct row and column in the matrix to store the clock-in time
    rindex=rows.index(nowTime) 
    cindex=cols.index(nowDay)

    time_log_matrix[rindex][cindex]=f"In: {logciTime}"  # Save clock-in time
    update_treeview()  # Update Treeview display
    
    messagebox.showinfo("Alert", f"You have clocked in on {ciTime}!")  # Notify user of clock-in

# Function to log the user's clock-out time
def clocked_out():
    nowDay=datetime.now().strftime("%a")  # Get current day abbreviation
    nowTime=datetime.now().strftime("%I:00 %p").lstrip('0')  # Get the current time in "hour:00 AM/PM" format
    coTime=datetime.now().strftime("%b %d, %Y at %I:%M %p")  # Clock-out time as string
    logcoTime=datetime.now().strftime("%I:%M:%S %p")  # Clock-out time with seconds

    # Find the correct row and column in the matrix to store the clock-out time
    rindex=rows.index(nowTime)
    cindex=cols.index(nowDay)

    # Check if a clock-in time already exists for this hour
    if "In:" in time_log_matrix[rindex][cindex]:
        messagebox.showerror("Alert", f"You must work up to atleast one hour before clocking out!")
    else:
        # Log clock-out time if no clock-in entry exists
        time_log_matrix[rindex][cindex] = f"Out: {logcoTime}"
        update_treeview()
        messagebox.showinfo("Alert", f"You have clocked out on {coTime}!")  # Notify user of clock-out

# Function to generate a unique filename to avoid overwriting existing files
def uniquefname(dir, fn):
    base, ext=os.path.splitext(fn)
    counter=1
    uniquefn=fn

    # Append a number to the filename if it already exists
    while os.path.exists(os.path.join(dir, uniquefn)):
        uniquefn=f"{base}({counter}){ext}"
        counter+=1

    return uniquefn

# Function to export the time log as a PDF
def export():
    docupath=os.path.expanduser("~/Documents")  # System's Documents folder
    subfolder=os.path.join(docupath, "DataFiles")  # Subfolder to save the file

    # Create the folder if it doesn't exist
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)
    
    # Initial filename for the exported PDF
    initfname=f"EmployeeTimeLog_{name}.pdf"
    uniquefile=uniquefname(subfolder, initfname)

    # Open file dialog for the user to save the file
    fn=filedialog.asksaveasfilename(
        defaultext=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile=uniquefile,
        initialdir=subfolder)
    
    # If the user selected a file, generate the PDF
    if fn:
        c=canvas.Canvas(fn, pagesize=landscape(letter))  # Create a landscape PDF
        c.setFont("Helvetica", 12)

        # Title of the PDF
        c.drawString(320, 575, f"{name}'s Employee Time Log")

        y=525  # Starting position for table headers
        for index, header in enumerate(cols):
            c.drawString(0 + cols.index(header)*100, y, header)

        y-=30  # Move down for table rows
        for i, margin in enumerate(rows):
            c.drawString(10, y - (i * 40), margin)

        # Fill the table with clock-in/out data
        for i, row in enumerate(time_log_matrix):
            y-=25
            for j, value in enumerate(row):
                c.drawString(75 + j * 100, y, str(value))

        c.save()  # Save the PDF file
        messagebox.showinfo("Exported Successfully", f"Time log exported to {fn}!")

# Creates Clock-in button
button_1=tk.Button(root, text="Clock-in", font=("Arial", 12), command=clocked_in)
button_1.grid(row=2, column=1, padx=0, pady=15, sticky="ew")

# Creates Clock-out button
button_2=tk.Button(root, text="Clock-out", font=("Arial", 12), command=clocked_out)
button_2.grid(row=2, column=2, padx=30, pady=15, sticky="ew")

# Creates Export button
button_3=tk.Button(root, text="Export", font=("Arial", 12), command=export)
button_3.grid(row=2, column=3, padx=30, pady=15, sticky="ew")

# Start the application loop
root.mainloop()