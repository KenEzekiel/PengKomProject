# Program Map and GUI

# Kamus
# peta : array
# i, j : int

# Algoritma
from tkinter import *

peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]]

for i in range(len(peta)):
    for j in range(len(peta[i])):
        print(peta[i][j], end = " ")
    print("")