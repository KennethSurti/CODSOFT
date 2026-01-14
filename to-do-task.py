#this is the beginning of the task 
#lets go


import customtkinter as ctk
import sqlite3
import os
from tkinter import messagebox

# Database info 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "todo.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL
)
""")
conn.commit()

#Theme of window
 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#window settings
app = ctk.CTk()
app.title("Modern To-Do List")
app.geometry("520x500")
app.resizable(False, False)


#CRUD operations
#keep track of tasks

def load_tasks():
    task_list.delete("1.0", "end")
    cursor.execute("SELECT * FROM tasks")
    for task in cursor.fetchall():
        task_list.insert(
            "end",
            f"{task[0]}. {task[1]}  [{task[2]}]\n"
        )

#add task

def add_task():
    title = task_entry.get().strip()
    if not title:
        messagebox.showwarning("Input Error", "Task cannot be empty")
        return

    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)",
        (title, "Pending")
    )
    conn.commit()
    task_entry.delete(0, "end")
    load_tasks()

# tracking tasks
def get_selected_task_id():
    try:
        selected_line = task_list.get("insert linestart", "insert lineend")
        return selected_line.split(".")[0]
    except:
        return None

def mark_completed():
    task_id = get_selected_task_id()
    if not task_id:
        messagebox.showwarning("Selection Error", "Select a task line")
        return

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        ("Completed", task_id)
    )
    conn.commit()
    load_tasks()

#Priority Levels: Add a dropdown to mark tasks as Low, Medium, or High priority.

#Due Dates: Use a calendar widget to set deadlines.

#Search Bar: Add a filter to find specific tasks in a long list.