import tkinter as tk
from tkinter import messagebox, ttk

class LMSApp:
    def __init__(self):
        # Initialize credentials storage with sample data
        self.credentials = {
            'student': {'user1': 'pass1', 'user2': 'pass2'},
            'teacher': {'teacher1': 'tpass1', 'teacher2': 'tpass2'}
        }
        self.current_role = None
        self.create_role_selection_window()

    def create_role_selection_window(self):
        # Create the initial role selection window
        self.role_window = tk.Tk()
        self.role_window.title("Learning Management System")
        self.role_window.geometry("700x500")

        # Left frame (blue)
        left_frame = tk.Frame(bg="#2060C4", width=200, height=200)
        left_frame.pack(side="left", fill="both", expand=True)

        # Right frame (blue)
        right_frame = tk.Frame(bg="white", width=200, height=200)
        right_frame.pack(side="right", fill="both", expand=True)
        self.role_window.state('zoomed')
        self.role_window.resizable(False,False)

        # Window title label
        lbl_title = ttk.Label(self.role_window,text="Learn\nSync", font=('Impact', 70),foreground="white", background="#2060C4")
        lbl_title.place(x=70, y=30)  # Position title at (50,20)

        style = ttk.Style()
        style.configure("Impact.TButton",
                        font=('Impact', 20),  # Font and size
                        foreground="black",  # Text color
                        background="black")  # Button background color

        # Student selection button
        btn_student = ttk.Button(
            self.role_window,
            style="Impact.TButton",
            text="STUDENT",
            command=lambda: self.open_login_window('STUDENT')
        )
        btn_student.place(x=1200, y=900, width=200, height= 45)  # Centered button



        # Teacher selection button
        btn_teacher = ttk.Button(
            self.role_window,
            style="Impact.TButton",
            text="TEACHER",
            command=lambda: self.open_login_window('TEACHER')
        )
        btn_teacher.place(x=1500, y=900, width=200, height = 45)  # Position below student button

        #Frame Login Signup



        self.role_window.mainloop()

    def open_login_window(self, role):
        # Handle role selection and transition to login window
        self.current_role = role
        self.role_window.destroy()
        LoginWindow(self, role)

class LoginWindow:
    def __init__(self, app, role):
        self.app = app
        self.role = role
        self.window = tk.Tk()
        self.window.title(f"LMS - {role.capitalize()} Login")
        self.window.geometry("300x250")

        # Create StringVars for form inputs
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Window title
        lbl_title = ttk.Label(
            self.window,
            text=f"{self.role.capitalize()} Login",
            font=('Arial', 12)
        )
        lbl_title.place(x=100, y=20)

        # Username input
        ttk.Label(self.window, text="Username:").place(x=50, y=60)
        entry_user = ttk.Entry(self.window, textvariable=self.username)
        entry_user.place(x=50, y=85, width=200)

        # Password input
        ttk.Label(self.window, text="Password:").place(x=50, y=120)
        entry_pass = ttk.Entry(self.window, textvariable=self.password, show="*")
        entry_pass.place(x=50, y=145, width=200)

        # Login button
        btn_login = ttk.Button(
            self.window,
            text="Login",
            command=self.authenticate
        )
        btn_login.place(x=50, y=180, width=200)

        # Switch to signup button
        btn_switch = ttk.Button(
            self.window,
            text="Switch to Sign Up",
            command=self.open_signup_window
        )
        btn_switch.place(x=50, y=210, width=200)

        # Back to role selection button
        btn_back = ttk.Button(
            self.window,
            text="Back to Role Selection",
            command=self.back_to_role_selection
        )
        btn_back.place(x=50, y=240, width=200)

    def authenticate(self):
        # Handle login authentication
        username = self.username.get()
        password = self.password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if username in self.app.credentials[self.role] and \
           self.app.credentials[self.role][username] == password:
            messagebox.showinfo("Success", f"Welcome {username}!")
            self.window.destroy()
            # Here you would typically open the main application window
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def open_signup_window(self):
        # Transition to signup window
        self.window.destroy()
        SignupWindow(self.app, self.role)

    def back_to_role_selection(self):
        # Return to role selection screen
        self.window.destroy()
        self.app.create_role_selection_window()

class SignupWindow:
    def __init__(self, app, role):
        self.app = app
        self.role = role
        self.window = tk.Tk()
        self.window.title(f"LMS - {role.capitalize()} Sign Up")
        self.window.geometry("300x250")
        self.window.resizable(False, False)

        # Create StringVars for form inputs
        self.new_username = tk.StringVar()
        self.new_password = tk.StringVar()

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Window title
        lbl_title = ttk.Label(
            self.window,
            text=f"{self.role.capitalize()} Sign Up",
            font=('Arial', 12)
        )
        lbl_title.place(x=100, y=20)

        # New username input
        ttk.Label(self.window, text="New Username:").place(x=50, y=60)
        entry_new_user = ttk.Entry(self.window, textvariable=self.new_username)
        entry_new_user.place(x=50, y=85, width=200)

        # New password input
        ttk.Label(self.window, text="New Password:").place(x=50, y=120)
        entry_new_pass = ttk.Entry(self.window, textvariable=self.new_password, show="*")
        entry_new_pass.place(x=50, y=145, width=200)

        # Signup button
        btn_signup = ttk.Button(
            self.window,
            text="Sign Up",
            command=self.register_user
        )
        btn_signup.place(x=50, y=180, width=200)

        # Switch to login button
        btn_switch = ttk.Button(
            self.window,
            text="Switch to Login",
            command=self.open_login_window
        )
        btn_switch.place(x=50, y=210, width=200)

        # Back to role selection button
        btn_back = ttk.Button(
            self.window,
            text="Back to Role Selection",
            command=self.back_to_role_selection
        )
        btn_back.place(x=50, y=240, width=200)

    def register_user(self):
        # Handle new user registration
        username = self.new_username.get()
        password = self.new_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if username in self.app.credentials[self.role]:
            messagebox.showerror("Error", "Username already exists")
        else:
            self.app.credentials[self.role][username] = password
            messagebox.showinfo("Success", "Registration successful!")
            self.window.destroy()
            LoginWindow(self.app, self.role)

    def open_login_window(self):
        # Return to login window
        self.window.destroy()
        LoginWindow(self.app, self.role)

    def back_to_role_selection(self):
        # Return to role selection screen
        self.window.destroy()
        self.app.create_role_selection_window()

if __name__ == "__main__":
    app = LMSApp()