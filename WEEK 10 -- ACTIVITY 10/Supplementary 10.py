import tkinter as tk
from random import choice
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry("600x250")


# label text for title
ttk.Label(window, text="CHOOSE YOUR BIRTH DATE",
          background='light blue', foreground="dark blue",
          font=("Consolas", 15)).place(x=175, y=20)

# Set label
ttk.Label(window, text="Select Month :",
          font=("Consolas", 12)).place(x = 10, y = 135)
ttk.Label(window, text="Select the day :",
          font=("Consolas", 12)).place(x = 10, y = 65)
ttk.Label(window, text="Year :",
          font=("Consolas", 12)).place(x = 10, y = 100)

# Create Combobox for days
m = tk.StringVar()
day = ttk.Combobox(window, width=30, textvariable= m)

# Adding combobox drop down list
day['values'] = tuple(str(i) for i in range (1,32))
day.place(x = 250, y = 67)
day.current()

# Create Combobox for years
n = tk.StringVar()
year = ttk.Combobox(window, width=30, textvariable= n)

# Adding combobox drop down list
year['values'] = tuple(str(i) for i in range(1900, 2025))
year.place(x = 250, y = 100)
year.current()

# Create Combobox for months
o = tk.StringVar()
month = ttk.Combobox(window, width=30, textvariable= o)

# Adding combobox drop down list
month['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     'September',
                     'October',
                     'November',
                     'December')
month.place(x = 250, y = 135)
month.current()

def choice():
    showinfo(
            title = "Selection",
            message = f'You Selected: {o.get()} {m.get()}, {n.get()}')

    day.bind("<<ComboboxSelected>>", choice)
    month.bind("<<ComboboxSelected>>", choice)
    year.bind("<<ComboboxSelected>>", choice)

# Button
ttk.Button(text = "Submit", command = choice).place(x = 250, y = 200)
window.mainloop()