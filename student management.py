import tkinter as tk
from tkinter import messagebox

students = []


def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    grade = grade_entry.get()

    if name and roll and grade:
        students.append({"Name": name, "Roll": roll, "Grade": grade})
        messagebox.showinfo("Success", "Student added successfully!")
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        update_display()
    else:
        messagebox.showwarning("Error", "Please fill all fields.")


def update_display():
    output_box.delete("1.0", tk.END)
    for i, student in enumerate(students, start=1):
        output_box.insert(tk.END, f"{i}. {student['Name']} - {student['Roll']} - {student['Grade']}\n")


# GUI window
root = tk.Tk()
root.title("Student Management System")

# Labels & Entry fields
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Roll No").grid(row=1, column=0)
roll_entry = tk.Entry(root)
roll_entry.grid(row=1, column=1)

tk.Label(root, text="Grade").grid(row=2, column=0)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1)

# Add button
add_btn = tk.Button(root, text="Add Student", command=add_student)
add_btn.grid(row=3, columnspan=2, pady=10)

# Output Box
output_box = tk.Text(root, height=10, width=40)
output_box.grid(row=4, columnspan=2)

root.mainloop()