import sqlite3

def create_database():
    with sqlite3.connect('employee_directory.db') as conn:
        cursor = conn.cursor()

        # Create Department table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Department (
            DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT,
            DepartmentName TEXT UNIQUE
        )
        """)

        # Create Employee table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Email TEXT UNIQUE,
            PhoneNumber TEXT,
            DepartmentID INTEGER,
            DateOfJoining TEXT,
            FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
        )
        """)

        conn.commit()

def insert_department(department_name):
    with sqlite3.connect('employee_directory.db') as conn:
        cursor = conn.cursor()

        # Check if the department exists
        cursor.execute("SELECT DepartmentName FROM Department WHERE DepartmentName = ?", (department_name,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO Department (DepartmentName) VALUES (?)", (department_name,))
            conn.commit()
        else:
            print(f"Department '{department_name}' already exists.")

def get_department_id(department_name):
    with sqlite3.connect('employee_directory.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DepartmentID FROM Department WHERE DepartmentName = ?", (department_name,))
        department_id = cursor.fetchone()[0]
        return department_id

def insert_employee(first_name, last_name, phone_number, department_name):
    department_id = get_department_id(department_name)
    email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

    with sqlite3.connect('employee_directory.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Employee (FirstName, LastName, Email, PhoneNumber, DepartmentID, DateOfJoining)
        VALUES (?, ?, ?, ?, ?, date('now'))
        """, (first_name, last_name, email, phone_number, department_id))
        conn.commit()

def retrieve_employee(last_name=""):
    with sqlite3.connect('employee_directory.db') as conn:
        cursor = conn.cursor()
        
        if last_name:
            cursor.execute("""
            SELECT e.EmployeeID, e.FirstName, e.LastName, e.Email, e.PhoneNumber, d.DepartmentName, e.DateOfJoining
            FROM Employee e
            JOIN Department d ON e.DepartmentID = d.DepartmentID
            WHERE e.LastName LIKE ?
            """, (f"%{last_name}%",))
        else:
            cursor.execute("""
            SELECT e.EmployeeID, e.FirstName, e.LastName, e.Email, e.PhoneNumber, d.DepartmentName, e.DateOfJoining
            FROM Employee e
            JOIN Department d ON e.DepartmentID = d.DepartmentID
            """)

        employees = cursor.fetchall()
        return employees

def remove_employee(first_name, last_name):
    with sqlite3.connect('employee_directory.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employee WHERE FirstName = ? AND LastName = ?", (first_name, last_name))
        conn.commit()
