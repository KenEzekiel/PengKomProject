# Program Map and GUI

# Algoritma
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Map")

# mapImage = ImageTk.PhotoImage(Image.open("logo_itb_1024.png"))
peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]]

def framePeta():
    frame = LabelFrame(root, text="Map", padx=50, pady=50)
    frame.pack(padx=10, pady=10)
    for i in range(len(peta)):
        for j in range(len(peta[i])):
            labelpeta = Label(frame, text=peta[i][j])
            labelpeta.grid(row=i, column=j)
framePeta()

def destinationList():
    # List Destinasi pre-determined agar mengurangi kekompleksan, 
    # kedepannya bisa diganti menjadi suatu koordinat
    # dimana x = i, x >= 0, dan y = -j, y >= 0
    # y = -j berarti koordinat di kuadran 4, tetapi dianggap di kuadran 1
    destination_list = ["Bandung", "Jakarta"]
    frame_destination = LabelFrame(root, text="Destination list", padx=10, pady=10)
    frame_destination.pack()
    for i in range(len(destination_list)):
        destination_label = Label(frame_destination, text=destination_list[i])
        destination_label.pack()
destinationList()

def switch():
    global myButton
    if myButton["state"] == NORMAL:
        myButton["state"] = DISABLED
    else:
        myButton["state"] = NORMAL

def myClick():
    switch()
    userInput()

# Deklarasi lokasi
entry_lokasi_awal = Entry(root, width=50)
entry_lokasi_awal.pack()
entry_lokasi_awal.insert(0, "Enter your position")

entry_lokasi_akhir = Entry(root, width=50)
entry_lokasi_akhir.pack()
entry_lokasi_akhir.insert(0, "Enter your destination")    

# Deklarasi button
myButton = Button(root, text="Click me", command=myClick)
myButton.pack()

def userInput():
    lokasi_awal = entry_lokasi_awal.get()
    label_awal = Label(root, text="Lokasi awal yang dipilih adalah " + lokasi_awal)
    label_awal.pack()

    lokasi_akhir = entry_lokasi_akhir.get()
    label_akhir = Label(root, text="Lokasi akhir yang dipilih adalah " + lokasi_akhir)
    label_akhir.pack()
   

root.mainloop()

