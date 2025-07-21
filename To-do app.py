import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Define the main window
root = tk.Tk()
root.title("Mini Search Assistant")
root.geometry("400x300")
root.configure(bg='steelblue')

# Define the functions
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_instagram():
    username = entry.get().replace('@', '')  # clean '@'
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

# Create widgets
Label(root, text="Enter your command:", bg='steelblue', fg='white', font=('Arial', 12, 'bold')).pack(pady=10)

entry = Entry(root, width=50)
entry.pack(pady=10)

Button(root, text="Search on YouTube", command=search_youtube).pack(pady=5)
Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)

# Run the GUI event loop
root.mainloop()
