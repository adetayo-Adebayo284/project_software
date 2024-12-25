import tkinter as tk
from tkinter import font

# Import the navigation page modules
import request_invite
import agency_solutions
import about_us
import ai_detector
import blog

# Create the main window
root = tk.Tk()
root.title("Content Detector")

# Set the window size
root.geometry("800x300")

# Create a canvas for the navigation bar
nav_canvas = tk.Canvas(root, height=120, bg="#FFFFFF")
nav_canvas.pack(fill=tk.X)

# Create custom fonts for the navigation bar items
logo_font = font.Font(family="Helvetica", size=20, weight="bold")
nav_font = font.Font(family="Helvetica", size=12, weight="normal")

# Add the logo to the center of the navigation bar
logo_label = tk.Label(root, text="DEEPFAKE", fg="#007BFF", bg="#FFFFFF", font=logo_font)
logo_label.place(x=40, y=40)

# Create menu items on the right side
menu_items = ["AI Detector", "Request an Invite", "Agency Solutions", "About Us", "Blog"]
menu_actions = [
    ai_detector.show_ai_detector,
    request_invite.show_request_invite,
    agency_solutions.show_agency_solutions,
    about_us.show_about_us,
    blog.show_blog
]

# Create a container with padding and background color
container = tk.Frame(root, bg="#EEEEEE", width=760, height=260, padx=20, pady=20)
container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
container.pack_propagate(False)

# Function to create menu buttons and assign actions
for i, (item, action) in enumerate(zip(menu_items, menu_actions)):
    menu_label = tk.Label(root, text=item, fg="#000000", bg="#FFFFFF", font=nav_font, cursor="hand2")
    menu_label.place(x=700 + i*140, y=45)
    menu_label.bind("<Button-1>", lambda e, act=action: act(container))

# Run the main loop
root.mainloop()