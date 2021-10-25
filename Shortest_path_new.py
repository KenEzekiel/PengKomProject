
import queue

peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0]]
 

start_x=int(input("masukkan koordinat x awal : "))
start_y=int(input("masukkan koordinat y awal : "))
end_x=int(input("masukkan koordinat x akhir : "))
end_y=int(input("masukkan koordinat y akhir : "))    


def valid(a,b):
    global peta
    y = int(a)
    x = int(b) 
    if not(0 <= y < len(peta) and 0 <= x < len(peta[0])):
        return False
    elif (peta[b][a] == 0):
        return False
    else :
        return True  
    
    for move in moves: 
        if move == "L" :
            i -= 1
            
        elif move == "R" :
            i += 1
            
        elif move == "U" :
            j -= 1
            
        elif move == "D" :
            j += 1
                
        '''if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1'''

        
    
    return True

array_value = []
def findEnd(peta, moves):
    i = start_x 
    j = start_y 
    value = 0    
    for move in moves: 
        if move == "L" and valid(i-1,j):
            i -= 1
            value += peta[j][i-1]
        elif move == "R" and valid(i+1,j):
            i += 1
            value += peta[j][i+1]
        elif move == "U" and valid(i,j-1):
            j -= 1
            value += peta[j-1][i]
        elif move == "D" and valid(i,j+1):
            j += 1
            value += peta[j+1][i]
        
        array_value.append(value)    
        
    if j == end_x and i==end_y and min(array_value):
        print("Found: " + moves)
        return True


    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""


while not findEnd(peta, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(peta,put):
            nums.put(put)