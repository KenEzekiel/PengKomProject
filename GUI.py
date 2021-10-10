# Program Map and GUI

# Algoritma
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Map")

# mapImage = ImageTk.PhotoImage(Image.open("logo_itb_1024.png"))
peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [2, 2, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 2, 1, 1, 0]]

# List Destinasi pre-determined agar mengurangi kekompleksan, 
# kedepannya bisa diganti menjadi suatu koordinat
# dimana x = i, x >= 0, dan y = -j, y >= 0
# y = -j berarti koordinat di kuadran 4, tetapi dianggap di kuadran 1
destination_list = [("Bandung", "Bandung"), 
                    ("Jakarta", "Jakarta"), 
                    ("Bogor", "Bogor"),
                    ("ITB", "ITB")]

def framePeta():
    frame = LabelFrame(root, text="Map", padx=50, pady=50)
    frame.grid(row=1, column=1)
    for i in range(len(peta)):
        for j in range(len(peta[i])):
            labelpeta = Label(frame, text=peta[i][j])
            labelpeta.grid(row=i, column=j)
framePeta()

def destinationList():
    frame_destination = LabelFrame(root, text="Destination list", padx=10, pady=10)
    frame_destination.grid(row=1, column=2)
    for text, destination in destination_list:
            destination_label = Label(frame_destination, text=text)
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
label_awal = LabelFrame(root, text="Lokasi Awal")
label_awal.grid(row=3, column=1)
entry_lokasi_awal = StringVar()
entry_lokasi_awal.set("Bandung")
for text, destination in destination_list:
    radio_awal = Radiobutton(label_awal, text=text, variable=entry_lokasi_awal, value=destination)
    radio_awal.grid()

label_akhir = LabelFrame(root, text="Lokasi Akhir")
label_akhir.grid(row=3, column=2)
entry_lokasi_akhir = StringVar()
entry_lokasi_akhir.set("Jakarta")
for text, destination in destination_list:
    radio_akhir = Radiobutton(label_akhir, text=text, variable=entry_lokasi_akhir, value=destination)
    radio_akhir.grid()

# Deklarasi button
myButton = Button(root, text="Click me", command=myClick)
myButton.grid(row=4, column=1, columnspan=2)

def userInput():
    frame_destinasi = LabelFrame(root, text="")
    frame_destinasi.grid(row=5, column=1, columnspan=2)

    lokasi_awal = entry_lokasi_awal.get()
    label_awal = Label(frame_destinasi, text="Lokasi awal yang dipilih adalah " + lokasi_awal)
    label_awal.grid(row=1, column=1)

    lokasi_akhir = entry_lokasi_akhir.get()
    label_akhir = Label(frame_destinasi, text="Lokasi akhir yang dipilih adalah " + lokasi_akhir)
    label_akhir.grid(row=2, column=1)
   

root.mainloop()

