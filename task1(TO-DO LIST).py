import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x550")
        self.root.configure(bg="#f0f0f0")
        
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Entry field for new task
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        # Add task button
        self.add_button = tk.Button(self.button_frame, text="Add Task", width=12, font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Update task button
        self.update_button = tk.Button(self.button_frame, text="Update Task", width=12, font=("Helvetica", 12), bg="#2196F3", fg="white", command=self.update_task)
        self.update_button.grid(row=0, column=1, padx=5)

        # Remove task button
        self.remove_button = tk.Button(self.button_frame, text="Remove Task", width=12, font=("Helvetica", 12), bg="#f44336", fg="white", command=self.remove_task)
        self.remove_button.grid(row=0, column=2, padx=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        # Exit button (fixed with root.destroy)
        self.exit_button = tk.Button(root, text="Exit", width=10, font=("Helvetica", 12), bg="#333333", fg="white", command=root.destroy)
        self.exit_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            current_task = self.task_listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Update Task", "Edit task:", initialvalue=current_task)
            if new_task and new_task.strip():
                self.tasks[selected_task_index[0]] = new_task.strip()
                self.update_tasks()
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_remove = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task_to_remove)
            self.update_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
