import tkinter as tk
from PIL import Image, ImageTk

# Create main window
window = tk.Tk()
window.state("zoomed")
window.resizable(False, True)

# Disable minimize
def disable_minimize():
    return

window.iconify = disable_minimize

# Load and resize the background image
image_path = "bg5.png"  # Replace with your image path
img = Image.open(image_path)
img = img.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

# Create a canvas
canvas = tk.Canvas(window, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Add background image to canvas
canvas.create_image(0, 0, image=photo, anchor="nw")

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Define text elements
text_elements = [
    {"text": "Dashboard", "x": 0.26, "y": 0.095, "font": ("Open Sans", 35), "tag": "dashboard", "hover": False},
    {"text": "Home", "x": 0.138, "y": 0.326, "font": ("Poppins", 30, "bold"), "tag": "home", "hover": True},
    {"text": "Assignment", "x": 0.11, "y": 0.6, "font": ("Poppins", 30, "bold"), "tag": "assignment", "hover": True},
    {"text": "Courses", "x": 0.125, "y": 0.465, "font": ("Poppins", 30, "bold"), "tag": "courses", "hover": True},
    {"text": "Quiz", "x": 0.145, "y": 0.74, "font": ("Poppins", 30, "bold"), "tag": "quiz", "hover": True},
]

# Add text elements to canvas
for element in text_elements:
    x_pos = element["x"] * screen_width
    y_pos = element["y"] * screen_height

    text_id = canvas.create_text(
        x_pos,
        y_pos,
        text=element["text"],
        font=element["font"],
        fill="black",
        anchor="w",
        tags=element["tag"]
    )

    if element["hover"]:
        canvas.tag_bind(element["tag"], "<Enter>", lambda e, t=element["tag"]: canvas.itemconfig(t, fill="white"))
        canvas.tag_bind(element["tag"], "<Leave>", lambda e, t=element["tag"]: canvas.itemconfig(t, fill="black"))

# Function to reset the home screen
def reset_home_screen():
    # Remove all dynamically created widgets and text objects
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

# Function to display the "Assignments" UI
def show_assignment_section(event):
    reset_home_screen()  # Clear any previous dynamic content

    # Create a frame for "Assignments" UI on the right side
    assignment_frame = tk.Frame(window, bg="#f0f0f0", width=screen_width // 3, height=screen_height, relief="raised")
    assignment_frame.place(x=2 * screen_width // 3, y=0)  # Positioned on the right side

    # Add title to the "Assignments" frame
    title = tk.Label(assignment_frame, text="Assignments", font=("Arial", 25, "bold"), bg="#f0f0f0", fg="black")
    title.pack(pady=20)

    # Add some placeholder labels for assignments
    placeholder_1 = tk.Label(assignment_frame, text="• Assignment 1: Math Homework", font=("Arial", 15), bg="#f0f0f0")
    placeholder_1.pack(pady=10, anchor="w", padx=20)

    placeholder_2 = tk.Label(assignment_frame, text="• Assignment 2: Physics Lab", font=("Arial", 15), bg="#f0f0f0")
    placeholder_2.pack(pady=10, anchor="w", padx=20)

    placeholder_3 = tk.Label(assignment_frame, text="• Assignment 3: Programming Project", font=("Arial", 15), bg="#f0f0f0")
    placeholder_3.pack(pady=10, anchor="w", padx=20)

# Function to display "Courses" UI
def show_courses_section():
    reset_home_screen()  # Clear any previous dynamic content

    # Create a frame for "Courses" UI on the right side
    courses_frame = tk.Frame(window, bg="#f0f0f0", width=screen_width // 3, height=screen_height, relief="raised")
    courses_frame.place(x=2 * screen_width // 3, y=0)  # Positioned on the right side

    # Add title to the "Courses" frame
    title = tk.Label(courses_frame, text="Courses", font=("Arial", 25, "bold"), bg="#f0f0f0", fg="black")
    title.pack(pady=20)

    # Add some placeholder labels for courses
    placeholder_1 = tk.Label(courses_frame, text="• Course 1: Math 101", font=("Arial", 15), bg="#f0f0f0")
    placeholder_1.pack(pady=10, anchor="w", padx=20)

    placeholder_2 = tk.Label(courses_frame, text="• Course 2: Physics 101", font=("Arial", 15), bg="#f0f0f0")
    placeholder_2.pack(pady=10, anchor="w", padx=20)

    placeholder_3 = tk.Label(courses_frame, text="• Course 3: Programming 101", font=("Arial", 15), bg="#f0f0f0")
    placeholder_3.pack(pady=10, anchor="w", padx=20)

# Bind click events to "Home", "Courses", and "Assignment"
canvas.tag_bind("home", "<Button-1>", lambda e: reset_home_screen())
canvas.tag_bind("courses", "<Button-1>", lambda e: show_courses_section(e))
canvas.tag_bind("assignment", "<Button-1>", lambda e: show_assignment_section(e))

# Keep a reference to the background image
canvas.image = photo

# Start the Tkinter event loop
window.mainloop()
