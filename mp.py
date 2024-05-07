import mysql.connector
import tkinter as tk
from tkinter import messagebox

class EmployeeDBGUI:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cur = self.conn.cursor()
        self.create_table()

        self.root = tk.Tk()
        self.root.title("Employee Database")
        self.root.geometry("500x400")
        
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_age = tk.Label(self.root, text="Age:")
        self.label_age.grid(row=1, column=0)
        self.entry_age = tk.Entry(self.root)
        self.entry_age.grid(row=1, column=1)

        self.label_department = tk.Label(self.root, text="Department:")
        self.label_department.grid(row=2, column=0)
        self.entry_department = tk.Entry(self.root)
        self.entry_department.grid(row=2, column=1)

        self.button_add = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.button_add.grid(row=3, column=0, columnspan=2)

        self.button_view = tk.Button(self.root, text="View Employees", command=self.view_employees)
        self.button_view.grid(row=4, column=0, columnspan=2)

        self.label_update_id = tk.Label(self.root, text="Employee ID to Update:")
        self.label_update_id.grid(row=5, column=0)
        self.entry_update_id = tk.Entry(self.root)
        self.entry_update_id.grid(row=5, column=1)

        self.button_update = tk.Button(self.root, text="Update Employee", command=self.update_employee)
        self.button_update.grid(row=6, column=0, columnspan=2)

        self.label_delete_id = tk.Label(self.root, text="Employee ID to Delete:")
        self.label_delete_id.grid(row=7, column=0)
        self.entry_delete_id = tk.Entry(self.root)
        self.entry_delete_id.grid(row=7, column=1)

        self.button_delete = tk.Button(self.root, text="Delete Employee", command=self.delete_employee)
        self.button_delete.grid(row=8, column=0, columnspan=2)

        self.root.mainloop()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            age INT,
                            department VARCHAR(255))''')
        self.conn.commit()

    def add_employee(self):
        name = self.entry_name.get()
        age = int(self.entry_age.get())
        department = self.entry_department.get()
        sql = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
        values = (name, age, department)
        self.cur.execute(sql, values)
        self.conn.commit()
        messagebox.showinfo("Success", "Employee added successfully!")

    def view_employees(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        if not rows:
            messagebox.showinfo("Info", "No employees found.")
        else:
            for row in rows:
                print(row)
        self.conn.commit()

    def update_employee(self):
        id = int(self.entry_update_id.get())
        name = self.entry_name.get()
        age = int(self.entry_age.get())
        department = self.entry_department.get()
        sql = "UPDATE employees SET name=%s, age=%s, department=%s WHERE id=%s"
        values = (name, age, department, id)
        self.cur.execute(sql, values)
        self.conn.commit()
        messagebox.showinfo("Success", "Employee updated successfully!")

    def delete_employee(self):
        id = int(self.entry_delete_id.get())
        sql = "DELETE FROM employees WHERE id=%s"
        values = (id,)
        self.cur.execute(sql, values)
        self.conn.commit()
        messagebox.showinfo("Success", "Employee deleted successfully!")

    def __del__(self):
        self.conn.close()

# Example Usage
if __name__ == "__main__":
    db = EmployeeDBGUI(host='localhost', user='root', password='Shrivathsan007', database='dbp')
