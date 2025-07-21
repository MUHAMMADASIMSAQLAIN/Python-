import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Create the main window
root = tk.Tk()
root.title("🗂️ File Manager")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# === Core Functions ===
def create_file():
    filename = simpledialog.askstring("Create File", "Enter filename:")
    if filename:
        try:
            with open(filename, 'x') as f:
                messagebox.showinfo("Success", f"✅ File '{filename}' created successfully.")
        except FileExistsError:
            messagebox.showwarning("Already Exists", f"⚠️ File '{filename}' already exists.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {e}")

def view_files():
    files = os.listdir()
    if files:
        file_list = "\n".join(files)
        messagebox.showinfo("Files in Directory", file_list)
    else:
        messagebox.showinfo("No Files", "📁 No files found in this directory.")

def read_file():
    filename = simpledialog.askstring("Read File", "Enter filename to read:")
    if filename:
        try:
            with open(filename, 'r') as f:
                content = f.read()
                messagebox.showinfo(f"📖 {filename}", content if content else "📄 (Empty file)")
        except FileNotFoundError:
            messagebox.showerror("Not Found", f"❌ File '{filename}' not found.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {e}")

def delete_file():
    filename = simpledialog.askstring("Delete File", "Enter filename to delete:")
    if filename:
        try:
            os.remove(filename)
            messagebox.showinfo("Deleted", f"🗑️ File '{filename}' deleted successfully.")
        except FileNotFoundError:
            messagebox.showerror("Not Found", f"❌ File '{filename}' not found.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {e}")

# === GUI Widgets ===
tk.Label(root, text="File Management System", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)

tk.Button(root, text="➕ Create File", width=25, bg="lightgreen", command=create_file).pack(pady=10)
tk.Button(root, text="📂 View All Files", width=25, bg="lightblue", command=view_files).pack(pady=10)
tk.Button(root, text="📖 Read File", width=25, bg="khaki", command=read_file).pack(pady=10)
tk.Button(root, text="🗑️ Delete File", width=25, bg="salmon", command=delete_file).pack(pady=10)
tk.Button(root, text="❌ Exit", width=25, bg="gray", fg="white", command=root.quit).pack(pady=20)

# Run the GUI loop
root.mainloop()
