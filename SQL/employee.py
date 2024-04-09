import sqlite3
from database import insert_department, get_department_id

def insert_employee(first_name, last_name, email, phone_number, department_name, date_of_joining):
    conn = sqlite3.connect("employee_directory.db")
    cursor = conn.cursor()

    try:
        # Insert department if not exists
        insert_department(department_name)

        # Retrieve DepartmentID
        department_id = get_department_id(department_name)

        cursor.execute("""
        INSERT INTO Employee (FirstName, LastName, Email, PhoneNumber, DepartmentID, DateOfJoining)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone_number, department_id, date_of_joining))
        
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Employee with email '{email}' already exists.")
    except Exception as e:
        print(e)

    conn.close()

def retrieve_employee():
    conn = sqlite3.connect("employee_directory.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT e.EmployeeID, e.FirstName, e.LastName, e.Email, e.PhoneNumber, d.DepartmentName, e.DateOfJoining
    FROM Employee e
    JOIN Department d ON e.DepartmentID = d.DepartmentID
    """)

    employees = cursor.fetchall()
    
    conn.close()
    return employees
