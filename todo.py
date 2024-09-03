import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("TO-DO List App")

        # Create task list frame
        self.task_list_frame = tk.Frame(master)
        self.task_list_frame.pack(fill="both", expand=True)

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame, width=40)
        self.task_list.pack(side="left", fill="both", expand=True)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Create task entry frame
        self.task_entry_frame = tk.Frame(master)
        self.task_entry_frame.pack(fill="x")

        # Create task entry field
        self.task_entry = tk.Entry(self.task_entry_frame, width=40)
        self.task_entry.pack(side="left")

        # Create add task button
        self.add_task_button = tk.Button(self.task_entry_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side="left")

        # Create edit task button
        self.edit_task_button = tk.Button(self.task_entry_frame, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack(side="left")

        # Create delete task button
        self.delete_task_button = tk.Button(self.task_entry_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side="left")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def edit_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task = self.task_list.get(selected_task)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, task)
            self.task_list.delete(selected_task)

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)

root = tk.Tk()
my_todo_list_app = ToDoListApp(root)
root.mainloop()