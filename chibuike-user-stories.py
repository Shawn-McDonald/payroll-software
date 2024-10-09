import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Employee Time Tracker")
root.geometry("1280x1024")

name = "Chibuike Ijem"
col=("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
time_log=ttk.Treeview(root, columns=col, show="headings")

for day in col:
    time_log.column(day, width=100)
    time_log.heading(day, text=day)

time_log.insert('', 'end', values=("9:00 AM \n 9:05 AM \n 9:10 AM \n 9:15 AM \n 9:20 AM \n 9:25 AM \n 9:30 AM"))

time_log.place(x=10,y=100,width=1024,height=1024)

def clocked_in():
    ciTime=datetime.now().strftime("%b %d, %Y at %I:%M %p")
    logciTime=datetime.now().strftime("%I:%M:%S %p")
    time_log.insert('', 'end', values=(logciTime,))
    messagebox.showinfo("Alert", f"You have clocked in on {ciTime}!")

def clocked_out():
    coTime=datetime.now().strftime("%b %d, %Y at %I:%M %p")
    logcoTime=datetime.now().strftime("%I:%M:%S %p")
    time_log.insert('', 'end', values=(logcoTime,))
    messagebox.showinfo("Alert", f"You have clocked out on {coTime}!")

label = tk.Label(root, text=f"Welcome {name}, to the Employee Time Tracker!", font=("Arial", 24))
label.place(x=0,y=0)

button_1 = tk.Button(root, text="Clock-in", font=("Arial", 12), command=clocked_in)
button_1.place(x=5,y=50)

button_2 = tk.Button(root, text="Clock-out", font=("Arial", 12), command=clocked_out)
button_2.place(x=75,y=50)

root.mainloop()