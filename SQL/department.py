import sqlite3

def insert_department(department_name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    # Check if the department exists
    cursor.execute("SELECT DepartmentName FROM Department WHERE DepartmentName = ?", (department_name,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO Department (DepartmentName) VALUES (?)", (department_name,))
        conn.commit()
    else:
        print(f"Department '{department_name}' already exists.")
    
    conn.close()

def get_department_id(department_name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentID FROM Department WHERE DepartmentName = ?", (department_name,))
    department_id = cursor.fetchone()[0]
    conn.close()
    return department_id
