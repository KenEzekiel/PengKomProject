# Program Map and GUI

# Algoritma
from tkinter import *
from tkinter import font
import tkinter
from PIL import ImageTk, Image
import random as rd
from queue import PriorityQueue
# --------------------------------------------------------------
root = Tk()
root.title("Map") 
root.iconbitmap("resources/logo_itb.ico")

Font_tuple = ("Colibri", 10)

# Initial map
peta = [[1, 1, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

# Set images
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

# List Destinasi pre-determined agar mengurangi kekompleksan
# dimana x = i, x >= 0, dan y = -j, y >= 0
# y = -j berarti koordinat di kuadran 4, tetapi dianggap di kuadran 1
destination_list = [("Bandung", "Bandung"), 
                    ("Jakarta", "Jakarta"),
                    ("ITB", "ITB"),
                    ("Bogor", "Bogor")]

def positionVehicle():
    # Generates the number of cars that will add traffic
    number_of_cars = rd.randint(3, 12)  # randomize the number of cars
    for x in range(number_of_cars):
        not_found = True                # loops to position the cars
        while not_found:                # uses while to make sure every car is placed
            # randomize the coordinate
            i = rd.randint(0, len(peta)-1)
            j = rd.randint(0, len(peta[i])-1)
            if peta[i][j] == 1:         # checks whether the coordinate is a road or not
                peta[i][j] += 1
                not_found = False
positionVehicle()

# Clears or delete the item
def clear_frame(item):
   for widgets in item.winfo_children():
      widgets.destroy()
    
# Making a frame to put the map in
frame_peta = LabelFrame(root, 
                        text="Map", 
                        padx=10, 
                        pady=10, 
                        font=Font_tuple, 
                        bg="#B6D6EB")
frame_peta.grid(row=1, column=1, columnspan=2)

# Function to print the map inside the frame coordinate by coordinate
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
            elif peta[i][j] == 5:
                image = Label(frame_peta, image=highlight, bg="#B6D6EB")
            elif (i == final_location_coordinate[0]) and (j == final_location_coordinate[1]):
                image = Label(frame_peta, image=pin, bg="#B6D6EB")
            elif peta[i][j] == 1:
                image = Label(frame_peta, image=road, bg="#B6D6EB")
            elif peta[i][j] == 2:
                image = Label(frame_peta, image=car, bg="#B6D6EB")
            image.grid(row=i, column=j, ipadx=0, ipady=0)
# framePeta()

# Function to print the destinations inside the destination frame
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
# commented out because the feature is not used

# Function to disable a button
def switch(button):
    if button["state"] == NORMAL:
        button["state"] = DISABLED
    else:
        button["state"] = NORMAL

# Function to update the map when a different location is picked
def myClick():
    global first_location_coordinate
    global final_location_coordinate
    clear_frame(frame_lokasi)
    userInput()
    clear_frame(frame_peta)

    first_location_coordinate = locationFinder(entry_lokasi_awal.get())
    final_location_coordinate = locationFinder(entry_lokasi_akhir.get())
    switch(startButton)
    framePeta()

# Function to print radio buttons inside a frame to get user input
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

# Declare location frame
frame_lokasi = LabelFrame(root, text="", bg="#B6D6EB", width=50)
frame_lokasi.grid(row=5, column=1, columnspan=2)

# Function to get user input and prints it into a frame
def userInput():
    lokasi_awal = entry_lokasi_awal.get()
    label_awal = Label(frame_lokasi, text="Lokasi awal yang dipilih adalah " + lokasi_awal, font=Font_tuple, bg="#B6D6EB")
    label_awal.grid(row=1, column=1)

    lokasi_akhir = entry_lokasi_akhir.get()
    label_akhir = Label(frame_lokasi, text="Lokasi akhir yang dipilih adalah " + lokasi_akhir, font=Font_tuple, bg="#B6D6EB")
    label_akhir.grid(row=2, column=1)

# Function to map user input's location into coordinates
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

def getLocation():
    global asal
    global akhir
    asal = entry_lokasi_awal.get()
    akhir = entry_lokasi_akhir.get()
getLocation()

# ------------------------------------------------------------------
# ---------------------Dijkstra's Algorithm-------------------------
# ------------------------------------------------------------------
import sys

# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph
 
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self,dist,queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1
         
        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
 
    # Function to print shortest path
    # from source to j
    # using parent array
    global z
    z =[0]
    def printPath(self, parent, j):
        #Base Case : If j is source
        if parent[j] == -1  :
            #print (j)#end=" "),
            return
        self.printPath(parent , parent[j]),
        z.append(j)
        print(z)
        
        
    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent):
        if asal == "Bandung" or asal == "bandung":
            if akhir == "ITB" or akhir == "itb" :
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 1 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
                        a = dist[i]
                        
                        
            if akhir == "Jakarta" or akhir == "jakarta" :
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 8 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
            
            if akhir == "Bogor" or akhir == "bogor" :
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 9 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
            
        if asal == "ITB" or asal == "itb" :
            if akhir == "Bandung" or akhir == "bandung" :
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 1 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)  
                        
            if akhir == "Bogor" or akhir == "bogor":
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 3 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
                        
            if akhir == "Jakarta" or akhir == "jakarta": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 6 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
                        
        if asal == "Jakarta" or asal == "jakarta" :
            if akhir == "Bandung" or akhir == "bandung": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 5 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i) 
            
            if akhir == "ITB" or akhir == "itb": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 6 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
            
            if akhir == "Bogor" or akhir == "bogor": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 3 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i) 
        
        if asal == "Bogor" or asal == "bogor" :
            if akhir == "Bandung" or akhir == "bandung": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 2 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i) 
            
            if akhir == "ITB" or akhir == "itb": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 3 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)
            
            if akhir == "Jakarta" or akhir == "jakarta": 
                src = 0
                print("Vertex \t\tDistance from Source\tPath")
                for i in range(1, len(dist)):
                    if i == 9 :
                        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])) 
                        self.printPath(parent,i)   
                
 
    
    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''
    def dijkstra(self, graph, src):
 
        row = len(graph)
        col = len(graph[0])
 
        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row
 
        #Parent array to store
        # shortest path tree
        parent = [-1] * row
 
        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0
     
        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
             
        #Find shortest path for all vertices
        while queue:
 
            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)
        
            # remove min element    
            queue.remove(u)
            
            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
                        
 
        # print the constructed distance array
        self.printSolution(dist,parent)
'''
peta = [[2, 2, 2, 2, 2, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]
'''

def node_ae():
        value_ae = 4
        for i in range (1,5):
            for j in range (1):
                if peta[i][j]==2 : 
                    value_ae+=1
                else :
                    value_ae+=0 
        return value_ae  
    
def node_ea(): 
    value_ea = 4
    for i in range (3,-1,-1):
        for j in range (0,1):
            if peta[i][j]==2 : 
                value_ea+=1
            else :
                value_ea+=0 
    return value_ea
           
def node_ab(): 
    value_ab = 4
    for i in range (1):
        for j in range (1,5):
            if peta[i][j]==2 : 
                value_ab+=1
            else :
                value_ab+=0
    return value_ab
     
def node_ba(): 
    value_ba = 4
    for i in range (1):
        for j in range (3,-1,-1):
            if peta[i][j]==2 : 
                value_ba+=1
            else :
                value_ba+=0 
    return value_ba              

def node_bc(): 
    value_bc = 2
    for i in range (1,3):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_bc+=1
            else :
                value_bc+=0   
    return value_bc
    
def node_cb(): 
    value_cb = 2
    for i in range (1,-1,-1):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_cb+=1
            else :
                value_cb+=0
    return value_cb
                               
def node_cd(): 
    value_cd = 3
    for i in range (2,3):
        for j in range (4,8):
            if peta[i][j]==2 : 
                value_cd+=1
            else :
                value_cd+=0  
    return value_cd
                
def node_dc(): 
    value_dc = 3
    for i in range (2,3):
        for j in range (6,3,-1):
            if peta[i][j]==2 : 
                value_dc+=1
            else :
                value_dc+=0 
        return value_dc
                        
def node_cf(): 
    value_cf = 2
    for i in range (3,5):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_cf+=1
            else :
                value_cf+=0 
    return value_cf
    
def node_fc(): 
    value_fc = 2
    for i in range (3,1,-1):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_fc+=1
            else :
                value_fc+=0
    return value_fc
                 
def node_fg(): 
    value_fg = 1
    for i in range (5,6):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_fg+=1
            else :
                value_fg+=0
    return value_fg 
    
def node_gf(): 
    value_gf = 1
    for i in range (4,3,-1):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_gf+=1
            else :
                value_gf+=0   
    return value_gf
    
def node_dh(): 
    value_dh = 3
    for i in range (3,6):
        for j in range (7,8):
            if peta[i][j]==2 : 
                value_dh+=1
            else :
                value_dh+=0
    return value_dh
    
def node_hd(): 
    value_hd = 3
    for i in range (4,1,-1):
        for j in range (7,8):
            if peta[i][j]==2 : 
                value_hd+=1
            else :
                value_hd+=0   
    return value_hd 
               
def node_gh(): 
    value_gh = 3
    for i in range (5,6):
        for j in range (5,8):
            if peta[i][j]==2 : 
                value_gh+=1
            else :
                value_gh+=0   
    return value_gh
                
def node_hg(): 
    value_hg = 3
    for i in range (5,6):
        for j in range (6,3,-1):
            if peta[i][j]==2 : 
                value_hg+=1
            else :
                value_hg+=0
    return value_hg 
                
def node_gk(): 
    value_gk = 2
    for i in range (6,8):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_gk+=1
            else :
                value_gk+=0   
    return value_gk
    
def node_kg(): 
    value_kg = 2
    for i in range (6,4,-1):
        for j in range (4,5):
            if peta[i][j]==2 : 
                value_kg+=1
            else :
                value_kg+=0
    return value_kg           
                    
def node_hi(): 
    value_hi = 1
    for i in range (6,7):
        for j in range (7,8):
            if peta[i][j]==2 : 
                value_hi+=1
            else :
                value_hi+=0   
    return value_hi
                
def node_ih(): 
    value_ih = 1
    for i in range (5,4,-1):
        for j in range (7,8):
            if peta[i][j]==2 : 
                value_ih+=1
            else :
                value_ih+=0                
    return value_ih 
                
def node_il(): 
    value_il = 1
    for i in range (7,8):
        for j in range (7,8):
            if peta[i][j]==2 : 
                value_il+=1
            else :
                value_il+=0
    return value_il 
    
def node_li(): 
    value_li = 1
    for i in range (6,5,-1):
        for j in range (7,8):
            if peta[i][j]==2 : 
                value_li+=1
            else :
                value_li+=0 
    return value_li 
    
def node_kl(): 
    value_kl = 3
    for i in range (7,8):
        for j in range (5,8):
            if peta[i][j]==2 : 
                value_kl+=1
            else :
                value_kl+=0
    return value_kl 
                
def node_lk(): 
    value_lk = 3
    for i in range (7,8):
        for j in range (6,3,-1):
            if peta[i][j]==2 : 
                value_lk+=1
            else :
                value_lk+=0
    return value_lk 
    
                    
def node_kj(): 
    value_kj = 4
    for i in range (7,8):
        for j in range (3,-1,-1):
            if peta[i][j]==2 : 
                value_kj+=1
            else :
                value_kj+=0
    return value_kj
    
def node_jk(): 
    value_jk = 4
    for i in range (7,8):
        for j in range (1,5):
            if peta[i][j]==2 : 
                value_jk+=1
            else :
                value_jk+=0
    return value_jk 
                
def node_ef(): 
    value_ef = 4
    for i in range (4,5):
        for j in range (1,5):
            if peta[i][j]==2 : 
                value_ef+=1
            else :
                value_ef+=0
    return value_ef 
    
def node_fe(): 
    value_fe = 4
    for i in range (4,5):
        for j in range (3,-1,-1):
            if peta[i][j]==2 : 
                value_fe+=1
            else :
                value_fe+=0
    return value_fe
    
def node_ej(): 
    value_ej = 3
    for i in range (5,8):
        for j in range (0,1):
            if peta[i][j]==2 : 
                value_ej+=1
            else :
                value_ej+=0
    return value_ej 
    
def node_je(): 
    value_je = 3
    for i in range (6,3,-1):
        for j in range (0,1):
            if peta[i][j]==2 : 
                value_je+=1
            else :
                value_je+=0
    return value_je
 
g= Graph()
          
graph_Bandung = [[0,node_ab(),0,0,node_ae(),0,0,0,0,0,0,0],
        [node_ba(),0,node_bc(),0,0,0,0,0,0,0,0,0],
        [0,node_cb(),0,node_cd(),0,node_cf(),0,0,0,0,0,0],
        [0,0,node_dc(),0,0,0,0,node_dh(),0,0,0,0],
        [node_ea(),0,0,0,0,node_ef(),0,0,0,node_ej(),0,0],
        [0,0,node_fc(),0,node_fe(),0,node_fg(),0,0,0,0,0],
        [0,0,0,0,0,node_gf(),0,node_gh(),0,0,node_gk(),0],
        [0,0,0,node_hd(),0,0,node_hg(),0,node_hi(),0,0,0],
        [0,0,0,0,0,0,0,node_ih(),0,0,0,node_il()],
        [0,0,0,0,node_je(),0,0,0,0,0,node_jk(),0],
        [0,0,0,0,0,0,node_kg(),0,0,node_kj(),0,node_kl()],
        [0,0,0,0,0,0,0,0,node_li(),0,node_lk(),0]
        ]

graph_ITB = [
        [0,node_ba(),0,0,0,0,0,0,0,node_bc(),0,0],
        [0,0,node_ae(),0,0,0,0,0,0,0,0,0],
        [0,node_ea(),0,node_ej(),0,0,0,0,0,0,0,0],
        [0,0,node_je(),0,node_jk(),0,0,0,0,0,0,0],
        [0,0,0,node_kj(),0,node_kl(),0,0,0,0,0,node_kg()],
        [0,0,0,0,node_lk(),0,node_li(),0,0,0,0,0],
        [0,0,0,0,0,node_il(),0,node_ih(),0,0,0,0],
        [0,0,0,0,0,0,node_hi(),0,node_hd(),0,0,node_hg()],
        [0,0,0,0,0,0,0,node_dh(),0,node_dc(),0,0],
        [node_cb(),0,0,0,0,0,0,0,node_cd(),0,node_cf(),0],
        [0,0,0,0,0,0,0,0,0,node_fc(),0,node_fg()],
        [0,0,0,0,node_gk(),0,0,node_gh(),0,0,node_gf(),0],
        ]

graph_Jakarta = [
        [0,node_il(),0,0,0,0,0,0,0,0,node_ih(),0],
        [node_li(),0,node_lk(),0,0,0,0,0,0,0,0,0],
        [0,node_kl(),0,node_kj(),0,0,0,0,0,node_kg(),0,0],
        [0,0,node_jk(),0,node_je(),0,0,0,0,0,0,0],
        [0,0,0,node_ej(),0,node_ea(),0,0,node_ef(),0,0,0],
        [0,0,0,0,node_ae(),0,node_ab(),0,0,0,0,0],
        [0,0,0,0,0,node_ba(),0,node_bc(),0,0,0,0],
        [0,0,0,0,0,0,node_cb(),0,node_cf(),0,0,node_cd()],
        [0,0,0,0,node_fe(),0,0,node_fc(),0,node_fg(),0,0],
        [0,0,node_gk(),0,0,0,0,0,node_gf(),0,node_gh(),0],
        [node_hi(),0,0,0,0,0,0,0,0,node_hg(),0,node_hd()],
        [0,0,0,0,0,0,0,node_dc(),0,0,node_dh(),0],
        ]

graph_Bogor = [
        [0,node_je(),0,0,0,0,0,node_jk(),0,0,0,0],
        [node_ej(),0,node_ea(),0,0,node_ef(),0,0,0,0,0,0],
        [0,node_ae(),0,node_ab(),0,0,0,0,0,0,0,0],
        [0,0,node_ba(),0,node_bc(),0,0,0,0,0,0,0],
        [0,0,0,node_cb(),0,node_cf(),0,0,0,0,0,node_cd()],
        [0,node_fe(),0,0,node_fc(),0,node_fg(),0,0,0,0,0],
        [0,0,0,0,0,node_gf(),0,node_gk(),0,0,node_gh(),0],
        [node_kj(),0,0,0,0,0,node_kg(),0,node_kl(),0,0,0],
        [0,0,0,0,0,0,0,node_lk(),0,node_li(),0,0],
        [0,0,0,0,0,0,0,0,node_il(),0,node_ih(),0],
        [0,0,0,0,0,0,node_hg(),0,0,node_hi(),0,node_hd()],
        [0,0,0,0,node_dc(),0,0,0,0,0,node_dh(),0],
        ]
# Print the solution

def run(a):
    if a == "Bandung" or a == "bandung":
        g.dijkstra(graph_Bandung,0)
    elif a == "ITB" or a == "itb":
        g.dijkstra(graph_ITB,0)
    elif a == "Jakarta" or a == "jakarta":
        g.dijkstra(graph_Jakarta,0)
    elif a == "Bogor" or a == "bogor":  
        g.dijkstra(graph_Bogor,0)

# Dictionary nodes to coordinate
nodes_bandung = {
    # node : [y, x]
    0 : [0, 0],
    1 : [0, 4],
    2 : [2, 4],
    3 : [2, 7],
    4 : [4, 0],
    5 : [4, 4],
    6 : [5, 4],
    7 : [5, 7],
    8 : [6, 7],
    9 : [7, 0],
    10 : [7, 4],
    11 : [7, 7]
}

nodes_jakarta = {
    # node : [y, x]
    0 : nodes_bandung[8],
    1 : nodes_bandung[11],
    2 : nodes_bandung[10],
    3 : nodes_bandung[9],
    4 : nodes_bandung[4],
    5 : nodes_bandung[0],
    6 : nodes_bandung[1],
    7 : nodes_bandung[2],
    8 : nodes_bandung[5],
    9 : nodes_bandung[6],
    10 : nodes_bandung[7],
    11 : nodes_bandung[3]
}

nodes_ITB = {
    0 : nodes_bandung[1],
    1 : nodes_bandung[0],
    2 : nodes_bandung[4],
    3 : nodes_bandung[9],
    4 : nodes_bandung[10],
    5 : nodes_bandung[11],
    6 : nodes_bandung[8],
    7 : nodes_bandung[7],
    8 : nodes_bandung[3],
    9 : nodes_bandung[2],
    10 : nodes_bandung[5],
    11 : nodes_bandung[6]
}

nodes_bogor = {
    0 : nodes_bandung[9],
    1 : nodes_bandung[4],
    2 : nodes_bandung[0],
    3 : nodes_bandung[1],
    4 : nodes_bandung[2],
    5 : nodes_bandung[5],
    6 : nodes_bandung[6],
    7 : nodes_bandung[10],
    8 : nodes_bandung[11],
    9 : nodes_bandung[8],
    10 : nodes_bandung[7],
    11 : nodes_bandung[3]
}

def highlightMove(point_a, point_b):
    # node = [Y, X]
    # The node can only be separated either horizontally or vertically, not both 
    # Check the Y and X whether it is the same or not
    if point_a[0] == point_b[0]:                        # Jika Y sama, X pasti berbeda
        if point_a[1] < point_b[1]:                     # Jika Xa < Xb, gerak ke kanan
            for i in range(point_a[1], point_b[1]+1, 1):  # Untuk update X nya
                peta[point_a[0]][i] = 5
        elif point_a[1] > point_b[1]:
            for i in range(point_b[1], point_a[1]+1, 1):  # Untuk update X nya
                peta[point_a[0]][i] = 5
    elif point_a[1] == point_b[1]:                      # Jika X sama, Y pasti berbeda
        if point_a[0] < point_b[0]:                     # Jika Ya < Yb, gerak ke kanan
            for i in range(point_a[0], point_b[0]+1, 1):  # Untuk update X nya
                peta[i][point_a[1]] = 5
        elif point_a[0] > point_b[0]:                   # Jika Ya > Yb, gerak ke kiri (ke kanan dari b)
            for i in range(point_b[0], point_a[0]+1, 1):  # Untuk update X nya
                peta[i][point_a[1]] = 5

def updateMap(tipe):
    clear_frame(frame_peta)
    if tipe == "Bandung":
        # Uses nodes_bandung
        for i in range(len(z)-1):
            a = int(z[i])
            b = int(z[i+1])
            highlightMove(nodes_bandung[a], nodes_bandung[b])
    elif tipe == "Bogor":
        # Uses nodes_bogor
        for i in range(len(z)-1):
            a = int(z[i])
            b = int(z[i+1])
            highlightMove(nodes_bogor[a], nodes_bogor[b])
    elif tipe == "Jakarta":
        # Uses nodes_jakarta
        for i in range(len(z)-1):
            a = int(z[i])
            b = int(z[i+1])
            highlightMove(nodes_jakarta[a], nodes_jakarta[b])
    elif tipe == "ITB":
        # Uses nodes_ITB
        for i in range(len(z)-1):
            a = int(z[i])
            b = int(z[i+1])
            highlightMove(nodes_ITB[a], nodes_ITB[b])
    framePeta()

def startClick():
    getLocation()               # Update location
    switch(myButton)            # Disable myButton
    run(asal)                   # Running the algorithm
    switch(startButton)         # Disable startButton
    updateMap(asal)             # Update Map

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
                    font=Font_tuple,
                    state=DISABLED)
startButton.grid(row=6, column=1, columnspan=2)

root.mainloop()
