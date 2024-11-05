import sqlite3

def view_database():
    conn = sqlite3.connect("employee_time_tracker.db")
    cursor = conn.cursor()

    # Display employees
    print("Employees Table:")
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

    # Display time logs
    print("\nTime Logs Table:")
    cursor.execute("SELECT * FROM time_logs")
    for row in cursor.fetchall():
        print(row)

    # Display earnings
    print("\nEarnings Table:")
    cursor.execute("SELECT * FROM earnings")
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    view_database()

