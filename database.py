import sqlite3
from datetime import datetime

class EmployeeDatabase:
    def __init__(self, db_name="employee_time_tracker.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                hourly_pay REAL NOT NULL,
                tax_deduction REAL NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS time_logs (
                id INTEGER PRIMARY KEY,
                employee_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                clock_in TEXT,
                clock_out TEXT,
                FOREIGN KEY (employee_id) REFERENCES employees (id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS earnings (
                employee_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                hours_worked REAL,
                gross REAL,
                net REAL,
                FOREIGN KEY (employee_id) REFERENCES employees (id)
            )
        """)
        self.conn.commit()

    def add_employee(self, name, hourly_pay, tax_deduction):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO employees (name, hourly_pay, tax_deduction)
            VALUES (?, ?, ?)
        """, (name, hourly_pay, tax_deduction))
        self.conn.commit()
        return cursor.lastrowid

    def log_time(self, employee_id, date, clock_in=None, clock_out=None):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO time_logs (employee_id, date, clock_in, clock_out)
            VALUES (?, ?, ?, ?)
        """, (employee_id, date, clock_in, clock_out))
        self.conn.commit()

    def update_earnings(self, employee_id, date, hours_worked, gross, net):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO earnings (employee_id, date, hours_worked, gross, net)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(employee_id, date) DO UPDATE SET
                hours_worked=excluded.hours_worked,
                gross=excluded.gross,
                net=excluded.net
        """, (employee_id, date, hours_worked, gross, net))
        self.conn.commit()

    def get_employee(self, name):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM employees WHERE name = ?
        """, (name,))
        return cursor.fetchone()

    def get_daily_earnings(self, employee_id, date):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT hours_worked, gross, net FROM earnings
            WHERE employee_id = ? AND date = ?
        """, (employee_id, date))
        return cursor.fetchone()

    def get_weekly_earnings(self, employee_id, start_date, end_date):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT SUM(gross), SUM(net) FROM earnings
            WHERE employee_id = ? AND date BETWEEN ? AND ?
        """, (employee_id, start_date, end_date))
        return cursor.fetchone()

    def get_year_to_date_earnings(self, employee_id, year):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT SUM(gross), SUM(net) FROM earnings
            WHERE employee_id = ? AND strftime('%Y', date) = ?
        """, (employee_id, str(year)))
        return cursor.fetchone()
