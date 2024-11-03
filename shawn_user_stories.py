# Shawn McDonald
# CSCI 490

'''
Log in and log out (2):
As an employee, I want to log in using my username and password, as well as have the ability to log out, so that I can securely access and protect my information from unauthorized access.

Track yearly earnings (3):
As a manager, I want to be able to generate yearly earnings reports for all employees to ensure the payroll records are accurate and up-to-date.

Hourly pay rate (1):
As an employee, I want to check my hourly pay rate, so that I know what I am earning for each hour I work.
'''

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

import tkinter as tk
from tkinter import messagebox

# Dummy user database for demonstration
user_db = {'shawn': 'password123', 'employee2': 'password456'}

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Login System")
        
        # Login screen widgets
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=10)
        
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)
        
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=10)
        
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)
        
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        
        # Logout button (hidden at first)
        self.logout_button = tk.Button(root, text="Logout", command=self.logout)
        
        # Status label
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        # Check if the credentials are valid
        if username in user_db and user_db[username] == password:
            messagebox.showinfo("Login", "Login successful!")
            self.status_label.config(text=f"Logged in as {username}")
            
            # Hide login widgets
            self.entry_username.pack_forget()
            self.entry_password.pack_forget()
            self.login_button.pack_forget()
            
            # Show logout button
            self.logout_button.pack(pady=10)
        else:
            messagebox.showerror("Login", "Invalid username or password.")
    
    def logout(self):
        # Reset fields and status
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.status_label.config(text="")
        
        # Hide logout button
        self.logout_button.pack_forget()
        
        # Show login widgets again
        self.entry_username.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.login_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.geometry("300x250")
    root.mainloop()
