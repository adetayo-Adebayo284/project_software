import tkinter as tk

def show_agency_solutions(container):
    for widget in container.winfo_children():
        widget.destroy()
    label = tk.Label(container, text="Agency Solutions Page", bg="#EEEEEE", font=("Helvetica", 16))
    label.pack(pady=20)
