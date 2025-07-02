import tkinter as tk
from tkinter import messagebox

# Functions
def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(float(entry1.get()) / float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

# GUI setup
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x300")
root.configure(bg="#f0f0f0")

# Inputs
tk.Label(root, text="First Number:", bg="#f0f0f0").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:", bg="#f0f0f0").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Result
result = tk.StringVar()
tk.Label(root, text="Result:", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=result, state='readonly').pack()

# Buttons
tk.Button(root, text="Add (+)", command=add).pack(pady=5)
tk.Button(root, text="Subtract (-)", command=subtract).pack(pady=5)
tk.Button(root, text="Multiply (*)", command=multiply).pack(pady=5)
tk.Button(root, text="Divide (/)", command=divide).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
