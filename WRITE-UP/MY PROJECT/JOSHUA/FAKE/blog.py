import tkinter as tk

def show_blog(container):
    for widget in container.winfo_children():
        widget.destroy()
    label = tk.Label(container, text="Blog Page", bg="#EEEEEE", font=("Helvetica", 16))
    label.pack(pady=20)
