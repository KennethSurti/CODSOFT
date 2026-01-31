# Inital start to the 3rd task 
#  Going wiht making a calculator 

import customtkinter as ctk
from tkinter import messagebox

# Theme of UI (using same as other tasks)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Simple Calculator")
app.geometry("420x420")
app.resizable(False, False)



# UI layout using the same customtikinter as before


ctk.CTkLabel(
    app,
    text="Simple Calculator",
    font=("Segoe UI", 24, "bold")
).pack(pady=15)

#Input system 

num1_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter first number"
)
num1_entry.pack(pady=8)

num2_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter second number"
)
num2_entry.pack(pady=8)


# Operation System

operation_var = ctk.StringVar(value="Select Operation")
operation_menu = ctk.CTkOptionMenu(
    app,
    variable=operation_var,
    values=[
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    ]
)
operation_menu.pack(pady=12)


# The buttons (a little complex)

ctk.CTkButton(
    app,
    text="Calculate",
    command=calculate
).pack(pady=15)

result_entry = ctk.CTkEntry(
    app,
    width=300,
    state="readonly",
    placeholder_text="Result"
)
result_entry.pack(pady=10)

app.mainloop()
