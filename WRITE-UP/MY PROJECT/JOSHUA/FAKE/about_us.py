import tkinter as tk

def show_about_us(container):
    for widget in container.winfo_children():
        widget.destroy()
    
    # Main label for the About Us page
    label = tk.Label(container, text="About Abdulakeem Sukurat", bg="#EEEEEE", font=("Helvetica", 32))
    label.pack(pady=20)
    
    # Information about Abdulakeem Sukurat
    about_text = (
        "Welcome to my About Me page! I am Abdulakeem Sukurat, currently studying at Gateway ICT Polytechnic. "
        "I have a strong passion for artificial intelligence and its applications in solving real-world problems. "
        "With a background in computer science, I enjoy delving into complex algorithms and creating innovative software solutions."
    )
    
    about_label = tk.Label(container, text=about_text, justify='left', padx=20)
    about_label.pack(padx=20, pady=10)
    
    # Subheading label with increased font size
    subheading_text = "More about me..."
    subheading_label = tk.Label(
        container, 
        text=subheading_text, 
        bg="#EEEEEE", 
        font=("Helvetica", 18),  # Increased font size to 18 pixels
        justify='left',
        padx=20
    )
    subheading_label.pack(padx=20, pady=10)
