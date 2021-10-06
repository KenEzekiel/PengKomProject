# Program Map and GUI

# Kamus
# peta : array
# i, j : int

# Algoritma
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Map")

mapImage = ImageTk.PhotoImage(Image.open("logo_itb_1024.png"))

frame = LabelFrame(root, text="Map", padx=50, pady=50)
frame.pack(padx=10, pady=10)

peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]]

labelpeta = Label(frame, text=peta[0][0])

def myClick():
    for i in range(len(peta)):
        for j in range(len(peta[i])):
            labelpeta = Label(frame, text=peta[i][j])
            labelpeta.grid(row=i, column=j)


myButton = Button(root, text="Click me", command=myClick)
myButton.pack()


root.mainloop()

