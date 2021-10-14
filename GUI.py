# Program Map and GUI

# Algoritma
from tkinter import *
from tkinter import font
import tkinter
from PIL import ImageTk, Image

root = Tk()
root.title("Map")
root.iconbitmap("resources/logo_itb.ico")
# root.attributes('-alpha', 0.9)

Font_tuple = ("Product sans", 10, "bold")
# canvas = tkinter.Canvas(root)
# canvas.place(x=0, y=0)

# mapImage = ImageTk.PhotoImage(Image.open("logo_itb_1024.png"))
peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [2, 2, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 2, 1, 1, 0]]

road = ImageTk.PhotoImage(Image.open("resources/bigroad.png"))
grass = ImageTk.PhotoImage(Image.open("resources/biggrass.png"))
car = ImageTk.PhotoImage(Image.open("resources/bigcar.png"))

# Background image
background_image = PhotoImage(file="resources/Wallpaper.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0)

def putBackground(place):
    global frame_background
    frame_background = Label(place, image=background_image)
    frame_background.place(x=0, y=0)

# List Destinasi pre-determined agar mengurangi kekompleksan, 
# kedepannya bisa diganti menjadi suatu koordinat
# dimana x = i, x >= 0, dan y = -j, y >= 0
# y = -j berarti koordinat di kuadran 4, tetapi dianggap di kuadran 1
destination_list = [("Bandung", "Bandung"), 
                    ("Jakarta", "Jakarta"), 
                    ("Bogor", "Bogor"),
                    ("ITB", "ITB")]

def framePeta():
    global labelpeta
    frame_peta = LabelFrame(root, text="Map", padx=10, pady=10, font=Font_tuple, bg="#B6D6EB")
    frame_peta.grid(row=1, column=1)
    # canvas = tkinter.Canvas(frame_peta)
    for i in range(len(peta)):
        for j in range(len(peta[i])):
            labelpeta = Label(frame_peta, text=peta[i][j])
            if peta[i][j] == 0:
                image = Label(frame_peta, image=grass, bg="#B6D6EB")
            elif peta[i][j] == 1:
                image = Label(frame_peta, image=road, bg="#B6D6EB")
            elif peta[i][j] == 2:
                image = Label(frame_peta, image=car, bg="#B6D6EB")
            image.grid(row=i, column=j, ipadx=0, ipady=0)
framePeta()

def destinationList():
    frame_destination = LabelFrame(root, text="Destination list", padx=50, pady=50, font=Font_tuple, bg="#B6D6EB")
    frame_destination.grid(row=1, column=2)
    for text, destination in destination_list:
            destination_label = Label(frame_destination, text=text, font=Font_tuple, bg="#B6D6EB")
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
label_awal = LabelFrame(root, text="Lokasi Awal", padx=50, pady=50, font=Font_tuple, bg="#B6D6EB")
label_awal.grid(row=3, column=1)
entry_lokasi_awal = StringVar()
entry_lokasi_awal.set("Bandung")
for text, destination in destination_list:
    radio_awal = Radiobutton(label_awal, text=text, variable=entry_lokasi_awal, value=destination, font=Font_tuple, bg="#B6D6EB")
    radio_awal.grid()

label_akhir = LabelFrame(root, text="Lokasi Akhir", padx=50, pady=50, font=Font_tuple, bg="#B6D6EB")
label_akhir.grid(row=3, column=2)
entry_lokasi_akhir = StringVar()
entry_lokasi_akhir.set("Jakarta")
for text, destination in destination_list:
    radio_akhir = Radiobutton(label_akhir, text=text, variable=entry_lokasi_akhir, value=destination, font=Font_tuple, bg="#B6D6EB")
    radio_akhir.grid()

# Deklarasi button
myButton = Button(root, text="Click me", command=myClick, bg="#B6D6EB", width=50)
myButton.grid(row=4, column=1, columnspan=2)

def userInput():
    frame_destinasi = LabelFrame(root, text="", bg="#B6D6EB")
    frame_destinasi.grid(row=5, column=1, columnspan=2)

    lokasi_awal = entry_lokasi_awal.get()
    label_awal = Label(frame_destinasi, text="Lokasi awal yang dipilih adalah " + lokasi_awal, font=Font_tuple, bg="#B6D6EB")
    label_awal.grid(row=1, column=1)

    lokasi_akhir = entry_lokasi_akhir.get()
    label_akhir = Label(frame_destinasi, text="Lokasi akhir yang dipilih adalah " + lokasi_akhir, font=Font_tuple, bg="#B6D6EB")
    label_akhir.grid(row=2, column=1)
   
def locationFinder(lokasi):
    coordinate = []
    if lokasi == "Bandung":
        coordinate = [0, 0]
    elif lokasi == "Jakarta":
        coordinate = [5, 5]
    elif lokasi == "Bogor":
        coordinate = [3, 3]
locationFinder(entry_lokasi_awal.get())
locationFinder(entry_lokasi_akhir.get())


root.mainloop()

