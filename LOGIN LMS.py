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

        # Right frame (white) for login and signup forms
        self.right_frame = tk.Frame(bg="white", width=200, height=200)
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.role_window.state('zoomed')
        self.role_window.resizable(False, False)

        # Window title label
        lbl_title = ttk.Label(self.role_window, text="Learn\nSync", font=('Impact', 70), foreground="white",
                              background="#2060C4")
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
            command=lambda: self.update_login_signup_form('STUDENT')
        )
        btn_student.place(x=1200, y=900, width=200, height=45)  # Centered button

        # Teacher selection button
        btn_teacher = ttk.Button(
            self.role_window,
            style="Impact.TButton",
            text="TEACHER",
            command=lambda: self.update_login_signup_form('TEACHER')
        )
        btn_teacher.place(x=1500, y=900, width=200, height=45)  # Position below student button

        # Frame Login Signup

        self.role_window.mainloop()

    def update_login_signup_form(self, role):
        # Clear the current contents in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Update the role and add the login/signup widgets
        self.current_role = role

        # Create StringVars for form inputs
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.new_username = tk.StringVar()
        self.new_password = tk.StringVar()

        self.create_login_widgets()


    def create_login_widgets(self):
        # Window title
        lbl_title = ttk.Label(self.right_frame, text=f"{self.current_role.capitalize()} Login", font=('Impact', 35), background="white")
        lbl_title.place(x=340, y=230)

        # Username input
        ttk.Label(self.right_frame, text="Username:",background="white", font=("Arial", 14)).place(x=300, y=350)
        entry_user = ttk.Entry(self.right_frame, textvariable=self.username, background="white", font= ("Arial", 12))
        entry_user.place(x=300, y=390, width=350, height = 35)

        # Password input
        ttk.Label(self.right_frame, text="Password:", background="white", font=("Arial", 14)).place(x=300, y=440)
        entry_pass = ttk.Entry(self.right_frame, textvariable=self.password, show="*", background="white", font= ("Arial", 12))
        entry_pass.place(x=300, y=480, width=350, height=35)

        # Login button
        btn_login = ttk.Button(self.right_frame, text="Login", command=self.authenticate)
        btn_login.place(x=300, y=540, width=350, height=35)

        # Switch to signup button
        btn_switch = ttk.Button(self.right_frame, text="Switch to Sign Up", command=self.create_signup_widgets)
        btn_switch.place(x=300, y=590, width=350, height=35)


    def create_signup_widgets(self):
        # Clear the current contents in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Create Sign Up widgets
        lbl_title = ttk.Label(self.right_frame, text=f"{self.current_role.capitalize()} Sign Up", font=('Impact', 35), background="white")
        lbl_title.place(x=320, y=230)

        # New username input
        ttk.Label(self.right_frame, text="Username:", font=("Arial", 14), background="white").place(x=300, y=350)
        entry_new_user = ttk.Entry(self.right_frame, textvariable=self.new_username, background="white", font= ("Arial", 12))
        entry_new_user.place(x=300, y=390, width=350, height=35)

        # New password input
        ttk.Label(self.right_frame, text="Password:", background="white", font=("Arial", 14)).place(x=300, y=440)
        entry_new_pass = ttk.Entry(self.right_frame, textvariable=self.new_password, show="*", background="white", font= ("Arial", 12))
        entry_new_pass.place(x=300, y=480, width=350, height = 35)

        # Signup button
        btn_signup = ttk.Button(self.right_frame, text="Sign Up", command=self.register_user)
        btn_signup.place(x=300, y=540, width=350, height=35)

        # Switch to login button
        btn_switch = ttk.Button(self.right_frame, text="Switch to Login", command=self.create_login_widgets)
        btn_switch.place(x=300, y=590, width=350, height=35)


    def authenticate(self):
        # Handle login authentication
        username = self.username.get()
        password = self.password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if username in self.credentials[self.current_role] and \
                self.credentials[self.current_role][username] == password:
            messagebox.showinfo("Success", f"Welcome {username}!")
            # Here you would typically open the main application window
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register_user(self):
        # Handle new user registration
        username = self.new_username.get()
        password = self.new_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if username in self.credentials[self.current_role]:
            messagebox.showerror("Error", "Username already exists")
        else:
            self.credentials[self.current_role][username] = password
            messagebox.showinfo("Success", "Registration successful!")


if __name__ == "__main__":
    app = LMSApp()