from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("500x300")

yscroll = Scrollbar(window)
yscroll.pack(side=RIGHT, fill = BOTH)

lstbox = Listbox(window)
lstbox.pack(side=RIGHT, fill=BOTH, expand=True)

for x in range(51):
    lstbox.insert(0,x)
    yscroll.config(command=lstbox.yview)

window.mainloop()