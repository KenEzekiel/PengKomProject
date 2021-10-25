peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0]]

'''
def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
'''
start_x = int(input("X awal: "))
start_y = int(input("Y awal: "))
end_x = int(input("X akhir: "))
end_y = int(input("Y akhir:"))

def valid(i, j):
        if not(0 <= i < len(peta) and 0 <= j < len(peta[0])):
            return False
        elif (peta[i][j] == 0):
            return False
        else: 
            return True

array_value = []
def findEnd(moves):
    i = start_y
    j = start_x
    value = 0
    for move in moves:
        if move == "U":
            i -= 1
        elif move == "D":
            i += 1
        elif move == "L":
            j -= 1
        elif move == "R":
            j += 1
        value += peta[i][j]
        array_value.append(value)
    if i == end_x and j == end_y:
        print("Found: " + moves)
        return True

    return False


# MAIN ALGORITHM

moves = []
add = moves
while not findEnd(add): 
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = []
        put.append(add)
        put.append(j)
        if valid(peta, put):
            moves.append(j)
print(len(put)-1)