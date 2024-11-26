import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import json
import os

# Path to the JSON file where tasks will be saved
TASKS_FILE = "tasks.json"

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                tasks_listbox.insert(tk.END, task)

# Function to save tasks to a JSON file
def save_tasks():
    tasks = list(tasks_listbox.get(0, tk.END))  # Get all tasks from the listbox
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task():
    task = task_entry.get()  # Get the task from the input field
    due_date = due_date_entry.get_date()  # Get the selected due date
    due_date_str = due_date.strftime("%d-%m-%Y")  # Format the due date as DD-MM-YYYY
    if task:
        tasks_listbox.insert(tk.END, f"{task} - Due: {due_date_str}")  # Add the task to the listbox
        task_entry.delete(0, tk.END)  # Clear the task input field
        save_tasks()  # Save tasks after adding a new one
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as complete
def mark_complete():
    try:
        selected_task_index = tasks_listbox.curselection()[0]  # Get the selected task index
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)  # Remove the task from the list
        # Add the task back with a strikethrough (marked as complete)
        tasks_listbox.insert(tk.END, f"✓ {task} (Completed)")  
        save_tasks()  # Save tasks after marking a task as complete
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# Function to remove a task
def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]  # Get the selected task index
        tasks_listbox.delete(selected_task_index)  # Remove the selected task
        save_tasks()  # Save tasks after removing a task
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Set up the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry label and input field
task_label = tk.Label(root, text="Task:")
task_label.pack(pady=5)
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Due date label and DateEntry widget
due_date_label = tk.Label(root, text="Due Date:")
due_date_label.pack(pady=5)
due_date_entry = DateEntry(root, width=30, date_pattern="dd-mm-yyyy")  # Calendar format DD-MM-YYYY
due_date_entry.pack(pady=5)

# Button to add task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Button to mark task as complete
mark_button = tk.Button(root, text="Mark as Complete", command=mark_complete)
mark_button.pack(pady=5)

# Button to remove task
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=5)

# Copyright
copyright_label = tk.Label(root, text="By Jeeteendar")
copyright_label.pack(pady=5)

# Load the tasks from the JSON file when the app starts
load_tasks()

# Start the GUI
root.mainloop()
