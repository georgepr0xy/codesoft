import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def view_tasks(self):
        return "\n".join([f"[{'✓' if task_info['completed'] else ' '}] {task_info['task']}" for task_info in self.tasks])

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = ToDoList()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_text = tk.Text(self.root, height=10, width=40)
        self.tasks_text.pack()

        self.view_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack()

        self.mark_button = tk.Button(self.root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.todo_list.add_task(task)
            self.entry.delete(0, tk.END)

    def view_tasks(self):
        tasks = self.todo_list.view_tasks()
        self.tasks_text.delete(1.0, tk.END)
        self.tasks_text.insert(tk.END, tasks)

    def mark_completed(self):
        index = self.tasks_text.index(tk.SEL_FIRST)
        if index:
            index = int(index.split('.')[0]) - 1
            self.todo_list.mark_completed(index)
            self.view_tasks()
        else:
            messagebox.showinfo("Message", "Select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()