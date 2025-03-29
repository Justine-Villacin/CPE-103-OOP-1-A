from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("500x300")

txtfld1 = Entry(window, justify = "center", bd = 2)
txtfld1.grid(row = 0, column=0)
txtfld1.insert(0, "row 0 column 0")

txtfld2 = Entry(window, justify = "center", bd = 2)
txtfld2.grid(row = 0, column=1)
txtfld2.insert(0, "row 0 column 1")

txtfld3 = Entry(window, justify = "center", bd = 2)
txtfld3.grid(row = 0, column=2)
txtfld3.insert(0, "row 0 column 2")

txtfld4 = Entry(window, justify = "center", bd = 2)
txtfld4.grid(row = 0, column=3)
txtfld4.insert(0, "row 0 column 3")

txtfld5 = Entry(window, justify = "center", bd = 2)
txtfld5.grid(row = 1, column=0)
txtfld5.insert(0, "row 1 column 0")

txtfld6 = Entry(window, justify = "center", bd = 2)
txtfld6.grid(row = 1, column=1)
txtfld6.insert(0, "row 1 column 1")

txtfld7 = Entry(window, justify = "center", bd = 2)
txtfld7.grid(row = 1, column=2)
txtfld7.insert(0, "row 1 column 2")

txtfld8 = Entry(window, justify = "center", bd = 2)
txtfld8.grid(row = 1, column=2)
txtfld8.insert(0, "row 1 column 3")

yscroll = Scrollbar(window)
yscroll.grid(row = 2, column = 2, sticky="nsw")

lstbox = Listbox(window, yscrollcommand=yscroll.set)
lstbox.grid(row = 2, column = 1)

for x in range(51):
    lstbox.insert(0,x)
    yscroll.config(command=lstbox.yview)

window.mainloop()