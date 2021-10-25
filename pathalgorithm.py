# Algorithm
from GUI_main_program import peta

input_lokasi_awal = int(input("masukan lokasi awal: "))
result = []
def valid():
    global result
    for i in peta:
        for j in peta[i]:
            if peta[i][j] == input_lokasi_awal:
                result = [i, j]
    print(f"x = {int(i)}")
    print(f"y = {int(i)}")
valid()

'''
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (maze[j][i] == "0"):
            return False
    
    return true
'''
