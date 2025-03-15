from tkinter import *
from tkinter import font

class MyWindow:
    def __init__(self, win):
        bold_font = font.Font(size = 9, weight = "bold")
        #labels and text first line

        self.lbl1 = Label(win, text = 'First number', font = bold_font)
        self.lbl1.place(x = 100, y = 50)
        self.t1 = Entry(bd = 4)
        self.t1.place(x = 200, y = 50)

        # labels and text second line
        self.lbl2 = Label(win, text = 'Second number', font = bold_font)
        self.lbl2.place(x = 100, y = 100)
        self.t2 = Entry(bd = 4 )
        self.t2.place(x = 200, y = 100)

        # labels and text second line
        self.lbl3 = Label(win, text = 'Result', font = bold_font)
        self.lbl3.place(x=100, y=150)
        self.t3 = Entry(bd = 4)
        self.t3.place(x=200, y=150)

        #buttons addition, subtraction, multiplication, divide
        self.btn1 = Button(win, text = 'Addition', command = self.add)
        self.btn1.place(x = 100, y = 200)
        self.btn2 = Button(win, text = 'Subtract', command = self.sub)
        self.btn2.place(x = 200, y = 200)
        self.btn3 = Button(win, text = "Multiplication", command = self.mul)
        self.btn3.place(x = 300, y = 200)
        self.btn4 = Button(win, text = "Division", command = self.div)
        self.btn4.place(x = 425, y = 200)
        self.btn5 = Button(win, text = "Clear", command = self.clear, fg = "red")
        self.btn5.place(x = 525, y = 200)


    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def mul(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("600x250+10+10")
window.mainloop()

