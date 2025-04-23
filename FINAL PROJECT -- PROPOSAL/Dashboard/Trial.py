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

# Define course codes
course_codes = {
    "Math 101": "12345",
    "Physics 101": "qwerty",
    "Programming 101": "abcde",
}

# Variables to track enrolled courses
enrolled_courses = []  # Stores the names of enrolled courses

# Function to display the "Courses" section
def show_courses_section():
    # Remove all dynamically created UI elements
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

    # Create a new frame for the enrollment UI
    courses_frame = tk.Frame(window, name="courses_frame", width=screen_width // 3, height=screen_height, bg="#f0f0f0")
    courses_frame.place(x=screen_width // 2.74, y=210)

    # Add widgets for enrollment
    tk.Label(courses_frame, text="Enroll in a Course", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)
    tk.Label(courses_frame, text="Course Name:", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w", padx=20, pady=10)
    course_entry = tk.Entry(courses_frame, font=("Arial", 14))
    course_entry.pack(padx=20, pady=10)

    tk.Label(courses_frame, text="Course Code:", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w", padx=20, pady=10)
    code_entry = tk.Entry(courses_frame, font=("Arial", 14))
    code_entry.pack(padx=20, pady=10)

    # Frame for success/error messages
    message_frame = tk.Frame(courses_frame, bg="#f0f0f0")
    message_frame.pack(fill="x", pady=10)

    # Function to recreate enrolled course frames
    def recreate_enrolled_course_frames():
        for idx, course_name in enumerate(enrolled_courses):
            y_position = 210 + idx * 170  # Offset between frames
            x_position = 3.5 * screen_width // 6  # Fixed horizontal position

            # Create a frame for the course
            course_frame = tk.Frame(
                window,
                width=300,
                height=150,
                bg="#e0e0e0",
                relief="raised",
                borderwidth=2
            )
            course_frame.place(x=x_position, y=y_position)

            # Add label inside the frame
            tk.Label(course_frame, text=course_name, font=("Arial", 14, "bold"), bg="#e0e0e0").pack(pady=55)
            course_frame.pack_propagate(False)

            # Add a click event to the frame with the course name as an argument
            course_frame.bind("<Button-1>", lambda event, name=course_name: show_lessons(event, name))

    # Recreate frames for previously enrolled courses
    recreate_enrolled_course_frames()

    # Enrollment button functionality
    def enroll_course():
        # Clear previous messages
        for widget in message_frame.winfo_children():
            widget.destroy()

        course_name = course_entry.get().strip()
        course_code = code_entry.get().strip()

        if course_name in course_codes and course_codes[course_name] == course_code:
            if course_name not in enrolled_courses:  # Avoid duplicates
                # Add to enrolled courses list
                enrolled_courses.append(course_name)

                # Recreate enrolled course frames
                recreate_enrolled_course_frames()

                # Display success message in the enrollment UI
                tk.Label(message_frame, text=f"Successfully enrolled in {course_name}!", font=("Arial", 14),
                         bg="#f0f0f0").pack(anchor="w")
            else:
                tk.Label(message_frame, text=f"Already enrolled in {course_name}!", font=("Arial", 14), fg="orange",
                         bg="#f0f0f0").pack(anchor="w")
        else:
            tk.Label(message_frame, text="Invalid course name or code!", font=("Arial", 14), fg="red",
                     bg="#f0f0f0").pack(anchor="w")

    tk.Button(courses_frame, text="Enroll", font=("Arial", 14), command=enroll_course).pack(pady=20)

# Function to reset to the home screen
def reset_home_screen():
    # Remove all frames or widgets added dynamically
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

# Function to display "Lessons" UI for a specific course
def show_lessons(event, name):
    # Remove all existing UI elements
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

    # Create a "Lessons" UI positioned to the right
    lessons_frame = tk.Frame(window, bg="#f0f0f0", width=screen_width, height=screen_height)
    lessons_frame.place(x=1000,y=200)  # Right-aligned

    # Add title
    tk.Label(lessons_frame, text=f"Lessons for {name}", font=("Arial", 35, "bold"), bg="#f0f0f0").pack(pady=20)

# Bind click events to "Home" and "Courses"
canvas.tag_bind("home", "<Button-1>", lambda e: reset_home_screen())
canvas.tag_bind("courses", "<Button-1>", lambda e: show_courses_section())

# Keep a reference to the background image
canvas.image = photo

# Start the Tkinter event loop
window.mainloop()
