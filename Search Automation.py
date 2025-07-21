import tkinter as tk
from tkinter import messagebox
import csv
import os

# CSV filename
FILENAME = "students.csv"

# Dictionary to store student data
students = {}

# Convert marks to grade
def get_grade(marks):
    marks = int(marks)
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Load from file
def load_students():
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    students[row[0]] = row[1]

# Save to file
def save_students():
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for name, grade in students.items():
            writer.writerow([name, grade])

# Add or update a student
def add_student():
    name = name_entry.get().title()
    marks = marks_entry.get()
    if not name or not marks.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid name and numeric marks.")
        return
    grade = get_grade(marks)
    students[name] = grade
    save_students()
    messagebox.showinfo("Success", f"Student '{name}' added/updated with grade {grade}.")
    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

# View all student records
def view_students():
    if not students:
        messagebox.showinfo("Student Records", "No students found.")
        return
    record = "\n".join([f"{name} ➤ Grade: {grade}" for name, grade in students.items()])
    messagebox.showinfo("Student Records", record)

# Delete student
def delete_student():
    name = name_entry.get().title()
    if name in students:
        del students[name]
        save_students()
        messagebox.showinfo("Deleted", f"Record for {name} deleted.")
    else:
        messagebox.showerror("Not Found", f"No record found for {name}.")
    name_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Student Grade Management System")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Student Grade Manager", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Student Name:", bg="#f0f0f0").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Marks (0-100):", bg="#f0f0f0").pack()
marks_entry = tk.Entry(root, width=30)
marks_entry.pack(pady=5)

tk.Button(root, text="Add/Update Student", command=add_student, width=25, bg="lightgreen").pack(pady=8)
tk.Button(root, text="View All Students", command=view_students, width=25, bg="lightblue").pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student, width=25, bg="salmon").pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=25, bg="gray").pack(pady=15)

# Load records when app starts
load_students()

root.mainloop()
