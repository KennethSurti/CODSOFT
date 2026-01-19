#need to make a password generator
#user input is lenght of password and complexity 
#result needs to be displayed
#promt the input
#use of combination of random characters


import customtkinter as ctk
import random
import string
from tkinter import messagebox

#checking the libraries compatibility
#Theme

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Password Generator")
app.geometry("500x420")
app.resizable(False, False)

# UI Layout
ctk.CTkLabel(
    app,
    text="🔐 Password Generator",
    font=("Segoe UI", 24, "bold")
).pack(pady=15)

length_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter password length"
)
length_entry.pack(pady=10)

# Complexity Options

lowercase_var = ctk.BooleanVar(value=True)
uppercase_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=False)

options_frame = ctk.CTkFrame(app)
options_frame.pack(pady=10)

ctk.CTkCheckBox(options_frame, text="Lowercase (a-z)", variable=lowercase_var).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkCheckBox(options_frame, text="Uppercase (A-Z)", variable=uppercase_var).grid(row=0, column=1, padx=10, pady=5)
ctk.CTkCheckBox(options_frame, text="Digits (0-9)", variable=digits_var).grid(row=1, column=0, padx=10, pady=5)
ctk.CTkCheckBox(options_frame, text="Symbols (!@#$)", variable=symbols_var).grid(row=1, column=1, padx=10, pady=5)