import tkinter as tk

# Function to handle button press
def add_to_input(value):
    current_text = input_var.get()
    input_var.set(current_text + str(value))

# Function to evaluate expression
def evaluate_expression():
    try:
        result = str(eval(input_var.get()))
        input_var.set(result)
    except:
        input_var.set("Error")

# Function to clear input
def clear_input():
    input_var.set("")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("360x520")
window.configure(bg='#D3D3D3')

# Display frame for input box
input_frame = tk.Frame(window, bg='#D3D3D3', bd=10, relief="ridge")
input_frame.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")

# Input field (Entry widget)
input_var = tk.StringVar()
input_entry = tk.Entry(
    input_frame,
    textvariable=input_var,
    font=("Arial", 20),
    bg='#D3D3D3',
    justify="right",
)
input_entry.pack(fill="x", ipadx=8, ipady=8)

# Button layout
button_labels = [
    ["C"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+"],
    ["="]
]

# Frame to hold buttons
buttons_frame = tk.Frame(window, bg='#D3D3D3')
buttons_frame.grid(row=1, column=0, columnspan=4)

# Create buttons
for row_index, row_values in enumerate(button_labels):
    for col_index, label in enumerate(row_values):
        if label == "C":
            button = tk.Button(buttons_frame, text=label, font=("Arial", 16, "bold"), height=2,
                               bg="white", command=clear_input)
            button.grid(row=row_index, column=0, columnspan=4, sticky="we", padx=2, pady=2)
        elif label == "0":
            button = tk.Button(buttons_frame, text=label, font=("Arial", 16, "bold"), height=2,
                               bg="white", command=lambda v=label: add_to_input(v))
            button.grid(row=row_index, column=0, columnspan=2, sticky="we", padx=2, pady=2)
        elif label == ".":
            button = tk.Button(buttons_frame, text=label, font=("Arial", 16, "bold"), height=2,
                               bg="white", command=lambda v=label: add_to_input(v))
            button.grid(row=row_index, column=2, sticky="we", padx=2, pady=2)
        elif label == "+":
            button = tk.Button(buttons_frame, text=label, font=("Arial", 16, "bold"), height=2,
                               bg="white", command=lambda v=label: add_to_input(v))
            button.grid(row=row_index, column=3, sticky="we", padx=2, pady=2)
        elif label == "=":
            button = tk.Button(buttons_frame, text=label, font=("Arial", 16, "bold"), height=2,
                               bg="white", command=evaluate_expression)
            button.grid(row=row_index, column=0, columnspan=4, sticky="we", padx=2, pady=2)
        else:
            button = tk.Button(buttons_frame, text=label, font=("Arial", 16, "bold"), width=5, height=2,
                               bg="white", command=lambda v=label: add_to_input(v))
            button.grid(row=row_index, column=col_index, padx=2, pady=2)

# Run the app
window.mainloop()
