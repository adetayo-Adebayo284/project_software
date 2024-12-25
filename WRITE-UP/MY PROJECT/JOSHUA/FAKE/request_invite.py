import tkinter as tk

def show_request_invite(container):
    for widget in container.winfo_children():
        widget.destroy()
    label = tk.Label(container, text="Request an Invite Page", bg="#EEEEEE", font=("Helvetica", 16))
    label.pack(pady=20)
