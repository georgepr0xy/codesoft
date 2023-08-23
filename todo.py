import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List App")

tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
tasks_listbox.pack(padx=10, pady=10)

task_entry = tk.Entry(root)
task_entry.pack(padx=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)

add_button.pack(padx=10, pady=5)
remove_button.pack(padx=10, pady=5)
clear_button.pack(padx=10, pady=5)

root.mainloop()