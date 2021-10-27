# Program Map and GUI

# Algoritma
from tkinter import *
from tkinter import font
import tkinter
from PIL import ImageTk, Image
import random as rd
from queue import PriorityQueue

root = Tk()
root.title("Map") 
root.iconbitmap("resources/logo_itb.ico")
# root.attributes('-alpha', 0.9)

Font_tuple = ("Colibri", 10)
# canvas = tkinter.Canvas(root)
# canvas.place(x=0, y=0)

peta = [[1, 1, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

road = ImageTk.PhotoImage(Image.open("resources/road.png"))
grass = ImageTk.PhotoImage(Image.open("resources/grass.png"))
car = ImageTk.PhotoImage(Image.open("resources/car.png"))
dot = ImageTk.PhotoImage(Image.open("resources/dot.png"))
pin = ImageTk.PhotoImage(Image.open("resources/pin.png"))
highlight = ImageTk.PhotoImage(Image.open("resources/highlight.png"))

# Background image
background_image = PhotoImage(file="resources/Wallpaper.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0)

# List Destinasi pre-determined agar mengurangi kekompleksan, 
# kedepannya bisa diganti menjadi suatu koordinat
# dimana x = i, x >= 0, dan y = -j, y >= 0
# y = -j berarti koordinat di kuadran 4, tetapi dianggap di kuadran 1
destination_list = [("Bandung", "Bandung"), 
                    ("Jakarta", "Jakarta"),
                    ("ITB", "ITB"),
                    ("Bogor", "Bogor")]

def positionVehicle():
    # Generates the number of cars that will add traffic
    number_of_cars = rd.randint(1, 10)
    for x in range(number_of_cars):
        not_found = True
        while not_found:
            i = rd.randint(0, len(peta)-1)
            j = rd.randint(0, len(peta[i])-1)
            if peta[i][j] == 1:
                peta[i][j] += 1
                not_found = False
positionVehicle()

def clear_frame(item):
   for widgets in item.winfo_children():
      widgets.destroy()
    
frame_peta = LabelFrame(root, 
                        text="Map", 
                        padx=10, 
                        pady=10, 
                        font=Font_tuple, 
                        bg="#B6D6EB")
frame_peta.grid(row=1, column=1, columnspan=2)

def framePeta():
    global labelpeta
    global frame_peta
    for i in range(len(peta)):
        for j in range(len(peta[i])):
            labelpeta = Label(frame_peta, text=peta[i][j])
            if peta[i][j] == 0:
                image = Label(frame_peta, image=grass, bg="#B6D6EB")
            elif (i == first_location_coordinate[0]) and (j == first_location_coordinate[1]):
                image = Label(frame_peta, image=dot, bg="#B6D6EB")
            elif (i == final_location_coordinate[0]) and (j == final_location_coordinate[1]):
                image = Label(frame_peta, image=pin, bg="#B6D6EB")
            elif peta[i][j] == 1:
                image = Label(frame_peta, image=road, bg="#B6D6EB")
            elif peta[i][j] == 2:
                image = Label(frame_peta, image=car, bg="#B6D6EB")
            image.grid(row=i, column=j, ipadx=0, ipady=0)
# framePeta()

def destinationList():
    frame_destination = LabelFrame(root, 
                                text="Destination list", 
                                padx=50, 
                                pady=50, 
                                font=Font_tuple, 
                                bg="#B6D6EB")
    frame_destination.grid(row=1, column=2)
    for text, destination in destination_list:
            destination_label = Label(frame_destination, 
                                    text=text, 
                                    font=Font_tuple, 
                                    bg="#B6D6EB")
            destination_label.pack()
# destinationList()

def switch():
    global myButton
    if myButton["state"] == NORMAL:
        myButton["state"] = DISABLED
    else:
        myButton["state"] = NORMAL

def myClick():
    global first_location_coordinate
    global final_location_coordinate
    clear_frame(frame_lokasi)
    userInput()
    clear_frame(frame_peta)

    first_location_coordinate = locationFinder(entry_lokasi_awal.get())
    final_location_coordinate = locationFinder(entry_lokasi_akhir.get())
    framePeta()

def startClick():
    switch()
    Algorithm()

def declareLocation():
    global label_awal
    global entry_lokasi_awal
    global destination_list
    global label_akhir
    global entry_lokasi_akhir
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
declareLocation()

# Deklarasi button
myButton = Button(root, 
                text="Konfirmasi Destinasi", 
                command=myClick, bg="#B6D6EB", 
                width=50, 
                font=Font_tuple)
myButton.grid(row=4, column=1, columnspan=2)

startButton = Button(root, 
                    text="Start Program",
                    command=startClick, bg="#B6D6EB", 
                    width=50, 
                    font=Font_tuple)
startButton.grid(row=6, column=1, columnspan=2)

# Deklarasi frame lokasi
frame_lokasi = LabelFrame(root, text="", bg="#B6D6EB", width=50)
frame_lokasi.grid(row=5, column=1, columnspan=2)

def userInput():
    lokasi_awal = entry_lokasi_awal.get()
    label_awal = Label(frame_lokasi, text="Lokasi awal yang dipilih adalah " + lokasi_awal, font=Font_tuple, bg="#B6D6EB")
    label_awal.grid(row=1, column=1)

    lokasi_akhir = entry_lokasi_akhir.get()
    label_akhir = Label(frame_lokasi, text="Lokasi akhir yang dipilih adalah " + lokasi_akhir, font=Font_tuple, bg="#B6D6EB")
    label_akhir.grid(row=2, column=1)
   
def locationFinder(lokasi):
    if lokasi == "Bandung":
        return([0, 0])
    elif lokasi == "Jakarta":
        return([6, 7])
    elif lokasi == "Bogor":
        return([7, 0])
    elif lokasi == "ITB":
        return([0, 4])
first_location_coordinate = locationFinder(entry_lokasi_awal.get())
final_location_coordinate = locationFinder(entry_lokasi_akhir.get())
framePeta()

root.mainloop()