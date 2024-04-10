import tkinter as tk
from tkinter import ttk, font, messagebox
from database import create_database, insert_employee, retrieve_employee, remove_employee

class EmployeeDirectoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Directory Management System")

        # Set custom font
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Set background color
        self.root.configure(background='#f0f0f0')

        self.labels_dict = {}  # Initialize labels_dict here
        
        self.create_gui()

    def create_gui(self):
        # Create search bar
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_employee_list)
        
        self.search_entry = ttk.Entry(self.root, textvariable=self.search_var, width=20, font=self.custom_font)
        self.search_entry.grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)
        self.search_entry.insert(0, "Last Name")

        # Create navigation buttons
        self.prev_button = ttk.Button(self.root, text="◀ Previous", command=self.prev_employee)
        self.prev_button.grid(row=0, column=1, padx=10, pady=20)

        self.next_button = ttk.Button(self.root, text="Next ▶", command=self.next_employee)
        self.next_button.grid(row=0, column=2, padx=10, pady=20)

        # Create employee details frame
        self.details_frame = ttk.LabelFrame(self.root, text="Employee Details", padding="20")
        self.details_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky=(tk.W, tk.E))

        # Labels for employee details
        labels = ["Employee ID:", "First Name:", "Last Name:", "Email:", "Phone Number:", "Department:", "Date of Joining:"]
        self.labels_dict = {}
        for i, label in enumerate(labels):
            ttk.Label(self.details_frame, text=label, font=self.custom_font).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            self.labels_dict[label] = ttk.Label(self.details_frame, text="", font=self.custom_font)
            self.labels_dict[label].grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

        # Remove employee button
        self.remove_button = ttk.Button(self.details_frame, text="Remove Employee", command=self.remove_selected_employee, state=tk.DISABLED)
        self.remove_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Create employee frame
        self.create_employee_frame = ttk.LabelFrame(self.root, text="Create Employee", padding="20")
        self.create_employee_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky=(tk.W, tk.E))

        self.first_name_label = ttk.Label(self.create_employee_frame, text="First Name:", font=self.custom_font)
        self.first_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.first_name_entry = ttk.Entry(self.create_employee_frame, font=self.custom_font)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.last_name_label = ttk.Label(self.create_employee_frame, text="Last Name:", font=self.custom_font)
        self.last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.last_name_entry = ttk.Entry(self.create_employee_frame, font=self.custom_font)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.phone_label = ttk.Label(self.create_employee_frame, text="Phone Number:", font=self.custom_font)
        self.phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.phone_entry = ttk.Entry(self.create_employee_frame, font=self.custom_font)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.department_label = ttk.Label(self.create_employee_frame, text="Department:", font=self.custom_font)
        self.department_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.department_combobox = ttk.Combobox(self.create_employee_frame, values=["HR", "Finance", "IT"], font=self.custom_font)
        self.department_combobox.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.create_button = ttk.Button(self.create_employee_frame, text="Create", command=self.create_employee)
        self.create_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        # Retrieve all employees
        self.employees = retrieve_employee()

        # Initialize current employee index
        self.current_employee_index = 0
        self.display_employee(self.current_employee_index)

    def update_employee_list(self, *args):
        search_term = self.search_var.get()
        if search_term == "Last Name":
            search_term = ""
        self.employees = retrieve_employee(search_term)
        self.current_employee_index = 0
        self.display_employee(self.current_employee_index)

    def display_employee(self, index):
        if index < len(self.employees):
            employee = self.employees[index]
            dept_prefix = employee[5][:3].upper()
            emp_id = f"{dept_prefix}-{employee[0]:03}"
            
            if "Employee ID:" in self.labels_dict:
                self.labels_dict["Employee ID:"].config(text=emp_id)
            if "First Name:" in self.labels_dict:
                self.labels_dict["First Name:"].config(text=employee[1])
            if "Last Name:" in self.labels_dict:
                self.labels_dict["Last Name:"].config(text= employee[2])
            if "Email:" in self.labels_dict:
                self.labels_dict["Email:"].config(text= employee[3])
            if "Phone Number:" in self.labels_dict:
                self.labels_dict["Phone Number:"].config(text= employee[4])
            if "Department:" in self.labels_dict:
                self.labels_dict["Department:"].config(text= employee[5])
            if "Date of Joining:" in self.labels_dict:
                self.labels_dict["Date of Joining:"].config(text= employee[6])
            
            self.remove_button.config(state=tk.NORMAL)
        else:
            self.labels_dict["Employee ID:"].config(text="")
            self.labels_dict["First Name:"].config(text="")
            self.labels_dict["Last Name:"].config(text="")
            self.labels_dict["Email:"].config(text="")
            self.labels_dict["Phone Number:"].config(text="")
            self.labels_dict["Department:"].config(text="")
            self.labels_dict["Date of Joining:"].config(text="")
            self.remove_button.config(state=tk.DISABLED)

    def next_employee(self):
        if self.current_employee_index < len(self.employees) - 1:
            self.current_employee_index += 1
            self.display_employee(self.current_employee_index)

    def prev_employee(self):
        if self.current_employee_index > 0:
            self.current_employee_index -= 1
            self.display_employee(self.current_employee_index)

    def remove_selected_employee(self):
        first_name_label_text = self.labels_dict["First Name:"].cget("text").split(": ")[1]
        last_name_label_text = self.labels_dict["Last Name:"].cget("text").split(": ")[1]
        
        try:
            remove_employee(first_name_label_text, last_name_label_text)
            messagebox.showinfo("Success", f"Employee {first_name_label_text} {last_name_label_text} removed successfully!")
            self.update_employee_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_entry.get()
        department = self.department_combobox.get()

        try:
            insert_employee(first_name, last_name, phone_number, department)
            messagebox.showinfo("Success", f"Employee {first_name} {last_name} added successfully!")
            self.update_employee_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    # Create database and tables
    create_database()

    root = tk.Tk()
    app = EmployeeDirectoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
