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
    def printPath(self, parent, j):
         
        #Base Case : If j is source
        if parent[j] == -1 :
            print (j,end=" "),
            return
        self.printPath(parent , parent[j])
        print(j,end=" "),
         
 
    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
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

<<<<<<< HEAD:dijkstra_algoritm_update.py .py
peta = [[2, 2, 2, 2, 2, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1],
=======
'''
peta = [[1, 2, 2, 2, 2, 0, 0, 0],
        [2, 0, 0, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 2, 1, 1, 1],
        [2, 0, 0, 0, 2, 0, 0, 1],
        [2, 2, 2, 2, 2, 0, 0, 1],
>>>>>>> a3327e16a705149c56a39b2aa7cde1db7cc8c3e4:dijkstra_algoritm_update.py
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
g.dijkstra(graph_ITB,0)
# g.dijkstra(graph,0)
