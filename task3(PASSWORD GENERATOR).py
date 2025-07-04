# Password Generate Application

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x500")
        master.configure(bg='#f0f0f0')
        master.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(
            master, 
            text="Password Generator", 
            font=("Arial", 16, "bold"),
            bg='#f0f0f0'
        )
        self.title_label.pack(pady=20)

        # Length Frame
        self.length_frame = tk.Frame(master, bg='#f0f0f0')
        self.length_frame.pack(pady=10)

        self.length_label = tk.Label(
            self.length_frame, 
            text="Password Length:", 
            font=("Arial", 12),
            bg='#f0f0f0'
        )
        self.length_label.pack(side=tk.LEFT, padx=5)

        self.length_entry = tk.Entry(
            self.length_frame, 
            font=("Arial", 12), 
            width=10
        )
        self.length_entry.pack(side=tk.LEFT)
        self.length_entry.insert(0, "12")  # Default length

        # Complexity Checkboxes
        self.complexity_frame = tk.Frame(master, bg='#f0f0f0')
        self.complexity_frame.pack(pady=10)

        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(
            self.complexity_frame, 
            text="Uppercase", 
            variable=self.use_uppercase,
            bg='#f0f0f0'
        )
        self.uppercase_check.pack(anchor='w')

        self.lowercase_check = tk.Checkbutton(
            self.complexity_frame, 
            text="Lowercase", 
            variable=self.use_lowercase,
            bg='#f0f0f0'
        )
        self.lowercase_check.pack(anchor='w')

        self.numbers_check = tk.Checkbutton(
            self.complexity_frame, 
            text="Numbers", 
            variable=self.use_numbers,
            bg='#f0f0f0'
        )
        self.numbers_check.pack(anchor='w')

        self.symbols_check = tk.Checkbutton(
            self.complexity_frame, 
            text="Symbols", 
            variable=self.use_symbols,
            bg='#f0f0f0'
        )
        self.symbols_check.pack(anchor='w')

        # Generate Button
        self.generate_button = tk.Button(
            master, 
            text="Generate Password", 
            command=self.generate_password,
            font=("Arial", 12),
            bg='#4CAF50',
            fg='white',
            width=20
        )
        self.generate_button.pack(pady=20)

        # Result Frame
        self.result_frame = tk.Frame(master, bg='#f0f0f0')
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(
            self.result_frame, 
            text="Generated Password:", 
            font=("Arial", 12),
            bg='#f0f0f0'
        )
        self.result_label.pack()

        self.password_display = tk.Entry(
            self.result_frame, 
            font=("Arial", 12), 
            width=30,
            state='readonly',
            justify='center'
        )
        self.password_display.pack()

        # Copy Button
        self.copy_button = tk.Button(
            master, 
            text="Copy Password", 
            command=self.copy_password,
            font=("Arial", 12),
            bg='#2196F3',
            fg='white',
            width=20
        )
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            length_text = self.length_entry.get()
            if not length_text.strip().isdigit():
                messagebox.showerror("Error", "Please enter a valid number for password length")
                return

            length = int(length_text)

            # Validate length
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters")
                return

            # Determine character sets based on checkboxes
            character_set = ""
            if self.use_uppercase.get():
                character_set += string.ascii_uppercase
            if self.use_lowercase.get():
                character_set += string.ascii_lowercase
            if self.use_numbers.get():
                character_set += string.digits
            if self.use_symbols.get():
                character_set += string.punctuation

            # Check if at least one character set is selected
            if not character_set:
                messagebox.showerror("Error", "Select at least one character type")
                return

            # Generate password
            password = ''.join(random.choice(character_set) for _ in range(length))

            # Display password
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def copy_password(self):
        # Copy generated password to clipboard
        password = self.password_display.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
