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