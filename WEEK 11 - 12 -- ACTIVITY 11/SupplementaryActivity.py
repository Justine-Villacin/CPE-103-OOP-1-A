import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro Calculator")
        self.root.geometry("440x525")

        self.expression = ""

        # Entry widget to display expressions
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(root, textvariable=self.input_text, font=('Arial', 20), bd=10, relief='ridge',
                                    justify='right')
        self.input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=10, pady=20)

        # Create the buttons
        self.create_buttons()

        # Keyboard bindings
        self.root.bind("<Return>", self.evaluate)
        self.root.bind("<BackSpace>", self.backspace)

    def create_buttons(self):
        btn_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('C', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in btn_texts:
            action = lambda t=text: self.button_click(t)
            tk.Button(self.root, text=text, width=10, height=3, font=('Arial', 12), command=action) \
                .grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, item):
        if item == 'C':
            self.clear()
        elif item == '=':
            self.evaluate()
        elif item == 'sin':
            try:
                result = math.sin(math.radians(float(self.input_text.get())))
                self.input_text.set(str(result))
                self.expression = str(result)
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif item == 'cos':
            try:
                result = math.cos(math.radians(float(self.input_text.get())))
                self.input_text.set(str(result))
                self.expression = str(result)
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self, event=None):
        try:
            # Replace ^ with ** before evaluation
            expr = self.expression.replace('^', '**')
            result = str(eval(expr))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def backspace(self, event=None):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)


# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
