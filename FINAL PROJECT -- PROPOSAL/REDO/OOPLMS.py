import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import login

window = tk.Tk()
window.title('Learning Management System')
window.state('zoomed')
window.configure(bg="#9edcff")

imageFrame = tk.Frame(window, bg="#9edcff")
imageFrame.pack(pady=60)

def newWindow(role):
    window.destroy()
    login


def loadImage(imagePath, size):
    try:
        img = Image.open(imagePath)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {imagePath}: {e}")
        return None

photos = [
    (loadImage(imagePath="UCC.png", size=(140, 130)),20),
    (loadImage(imagePath="COE.png", size=(160, 170)),10),
    (loadImage(imagePath="LS.png", size=(200, 215)),10)
    ]

for photo, padx in photos:
    if photo:
        imageLabel = tk.Label(imageFrame, image=photo, bg="#9edcff")
        imageLabel.image = photo
        imageLabel.pack(side=tk.LEFT, padx=padx)

label1 = tk.Label(window, text="UNIVERSITY OF CALOOCAN CITY", font=("Orbitron", 45, "bold"), bg="#9edcff")
label1.pack()
label2 = tk.Label(window, text="COLLEGE OF ENGINEERING", font=("Orbitron", 20), bg="#9edcff")
label2.pack(pady=20)

frame = tk.Frame(window, bg="#9edcff")
frame.pack(pady=20)

buttons = [
    tk.Button(frame, text="STUDENT", font=("Orbitron", 14, "bold"), bg="#FFC19E", fg="black", width=20, height=2, command= lambda: newWindow("STUDENT")),
    tk.Button(frame, text="INSTRUCTOR", font=("Orbitron", 14, "bold"), bg="#FFC19E", fg="black", width=20, height=2, command= lambda: newWindow("INSTRUCTOR"))
    ]


for button in buttons:
    ISbutton = button
    ISbutton.pack(side=tk.LEFT, padx=70, pady=20)

window.mainloop()
