
# GUI Conversion of the Calculator:
import tkinter as tk
import math
from tkinter import font

history = []

# Functions for calculation
def update_history():
    history_listbox.delete(0, "end")
    for item in history:
        history_listbox.insert("end", item)

def clear_history():
    history.clear()
    history_listbox.delete(0, "end")

def add():
    results = (float(entry1.get()) + float(entry2.get()))
    result.set(results)
    history.append(f"{entry1.get()} + {entry2.get()} = {results}")
    update_history()

def subtract():
    results = (float(entry1.get()) - float(entry2.get()))
    result.set(results)
    history.append(f"{entry1.get()} - {entry2.get()} = {results}")
    update_history()

def multiply():
    results = (float(entry1.get()) * float(entry2.get()))
    result.set(results)
    history.append(f"{entry1.get()} x {entry2.get()} = {results}")
    update_history()

def divide():
    try:
        results = (float(entry1.get()) / float(entry2.get()))
        result.set(results)
        history.append(f"{entry1.get()} ÷ {entry2.get()} = {results}")
        update_history()
    except ZeroDivisionError:
        results = ("Invalid Input")
        result.set(results)
        history.append(f"{results}")
        update_history()

# CLear Operation
def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, "end")
    entry4.delete(0, "end")
    entry5.delete(0, "end")
    entry6.delete(0, "end")
    result.set("")

# Advance Opearations
def squareroot():
    num = float(entry3.get())
    result_squareroot = math.sqrt(num) if num >= 0 else "Invalid Input"
    result.set(result_squareroot)
    history.append(f"{result_squareroot}")
    update_history()

def power():
    num1 = float(entry4.get())
    num2 = float(entry5.get())
    result_power = num1 ** num2
    result.set(result_power)
    history.append(f"{result_power}")
    update_history()

def sin():
    num = float(entry6.get())
    result_sin = math.sin(num)
    result.set(result_sin)
    history.append(f"{result_sin}")
    update_history()

def cos():
    num = float(entry6.get())
    result_cos = math.cos(num)
    result.set(result_cos)
    history.append(f"{result_cos}")
    update_history()

def tan():
    num = float(entry6.get())
    result_tan = math.tan(num)
    result.set(result_tan)
    history.append(f"{result_tan}")
    update_history()

def arcsin():
    num = float(entry6.get())
    if -1 <= num <= 1:
        result_arcsin = math.asin(num)
        result.set(result_arcsin)
        history.append(f"{result_arcsin}")
        update_history()
    else:
        results = ("Invalid Input")
        result.set(results)
        history.append(f"{results}")
        update_history()

def arccos():
    num = float(entry6.get())
    if -1 <= num <= 1:
        result_arccos = math.acos(num)
        result.set(result_arccos)
        history.append(f"{result_arccos}")
        update_history()
    else:
        results = ("Invalid Input")
        result.set(results)
        history.append(f"{results}")
        update_history()

def arctan():
    num = float(entry6.get())
    result_arctan = math.atan(num)
    result.set(result_arctan)
    history.append(f"{result_arctan}")
    update_history()


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("630x515")
root.configure(bg = "#E9967A")

# Create StringVar to hold the result
result = tk.StringVar()


# Create the layout
tk.Label(root, text="Enter 1st Number:", bg = "#E9967A", font = ("arial", 12)).place(x=30, y = 50)
entry1 = tk.Entry(root, bg = "#E9967A", bd = 3)
entry1.place(x=180, y=50)

tk.Label(root, text="Enter 2nd Number:", bg = "#E9967A", font = ("arial", 12)).place(x=30, y = 80)
entry2 = tk.Entry(root, bg = "#E9967A", bd = 3)
entry2.place(x=180, y=80)

# Buttons for operations
tk.Button(root, text="+", command=add, bg = "#E9967A", bd = 3, font = ("arial", 14, "bold")).place(x = 70, y = 135)
tk.Button(root, text="-", command=subtract, bg = "#E9967A", bd = 3, font = ("arial", 14, "bold")).place(x = 123, y = 135)
tk.Button(root, text="x", command=multiply, bg = "#E9967A", bd = 3, font = ("arial", 14, "bold")).place(x = 170, y = 135)
tk.Button(root, text="÷", command=divide, bg = "#E9967A", bd = 3, font = ("arial", 14, "bold")).place(x = 220, y = 135)


# Label to show result
tk.Label(root, text="Result:", bg = "#E9967A", font = ("arial", 12, "bold")).place(x = 350, y = 65)
result_label = tk.Label(root, textvariable=result, bg = "#E9967A", font = ("arial", 14))
result_label.place(x = 410, y = 63)

#Clear Button
tk.Button(root, text = "Clear", command = clear, bg = "#E9967A", bd = 3, font = ("arial", 14, "bold")).place(x = 530, y = 450)

# Advance Calculation Button
tk.Button(root, text = "√", command = squareroot, bg = "#E9967A", bd = 3, font = ("arial", 10, "bold")).place(x = 320, y = 205)
tk.Button(root, text = "^", command = power, bg = "#E9967A", bd = 3, font = ("arial", 10, "bold")).place(x = 320, y = 276)
tk.Button(root, text = "sin", command = sin, bg = "#E9967A", bd = 3, font = ("arial", 12, "bold")).place(x = 70, y = 370)
tk.Button(root, text = "cos", command = cos, bg = "#E9967A", bd = 3, font = ("arial", 12, "bold") ).place(x = 140, y = 370)
tk.Button(root, text = "tan", command = tan, bg = "#E9967A", bd = 3, font = ("arial", 12, "bold") ).place(x = 210, y = 370)
tk.Button(root, text = "sin⁻¹", command = arcsin, bg = "#E9967A", bd = 3, font = ("arial", 12, "bold")).place(x = 70, y = 425)
tk.Button(root, text = "cos⁻¹", command = arccos, bg = "#E9967A", bd = 3, font = ("arial", 12, "bold")).place(x = 140, y = 425)
tk.Button(root, text = "tan⁻¹", command = arctan, bg = "#E9967A", bd = 3, font = ("arial", 12, "bold")).place(x = 210, y = 425)

# Advance Calculation Label
tk.Label(root, text = "√Square root:", bg = "#E9967A", font = ("arial", 12)).place(x = 30, y = 210)
entry3 = tk.Entry(root, bg = "#E9967A", bd = 3)
entry3.place(x = 180, y = 210)

tk.Label(root, text = "Power:", bg = "#E9967A", font = ("arial", 12)).place(x = 30, y = 280)
tk.Label(root, text = "BASE", bg = "#E9967A").place(x = 120, y = 250)
tk.Label(root, text = "EXPONENT", bg = "#E9967A").place(x = 225, y = 250)
entry4 = tk.Entry(root, bg = "#E9967A", bd = 3, width = 15)
entry4.place(x = 90, y = 280)
entry5 = tk.Entry(root, bg = "#E9967A", bd = 3, width = 15)
entry5.place(x = 209, y = 280)

tk.Label(root, text = "Trigonometry:", bg = "#E9967A", font = ("arial", 12)).place(x = 30, y = 320)
entry6 = tk.Entry(root, bg = "#E9967A", bd = 3)
entry6.place(x = 180, y = 320)


# Store History
tk.Label(root, text = "MY HISTORY", bg = "#E9967A", font = ("arial", 12)).place(x = 440, y = 120)
history_listbox = tk.Listbox(root, height=15, width=38, bg="#E9967A", font = ("arial", 10))
history_listbox.place(x=350, y=160)
tk.Button(root, text = "Clear History", command = clear_history, bd = 3,  bg = "#E9967A", font = ("arial", 12, "bold")).place(x = 400, y = 455)


# Start the main loop
root.mainloop()
