import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')  # Added missing colon between M and S
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')  # Fixed tk.Label
label.pack(anchor='center')

time()

root.mainloop()
