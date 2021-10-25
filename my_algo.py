peta = [[1, 10, 10, 10, 1, 10],
        [1, 10, 10, 10, 1, 10],
        [1, 1, 1, 1, 1, 10],
        [1, 10, 10, 10, 1, 10],
        [1, 1, 1, 1, 1, 10]]

start_x = 0
start_y = 0
end_x = 4
end_y = 4
distance_x = end_x - start_x
distance_y = end_y - start_y

# Translate the moves into coordinate
def moveList(moves):
    i = start_y
    j = start_x
    for move in moves:
        if move == "L":
            j -= 1
        elif move == "R":
            j += 1
        elif move == "U":
            i -= 1
        elif move == "D":
            i += 1
        total_move = [i, j]
    return total_move

# m, n coordinate of end point
'''
def findMinimumEnd(matrix, m, n):
    minimum = [[0 for x in range(n + 1)] for y in range(m + 1)]
    minimum[0][0] = matrix[0][0]
    for i in range(1, m + 1):
        above_cost = minimum[i-1][0]
        minimum[i][0] = above_cost + matrix[i][0]
    for j in range(1, n + 1):
        left_cost = minimum[0][j-1]
        minimum[0][j] = left_cost + matrix[0][j]
    for i in range(1, m +1):
        for j in range(1, n + 1):
            left_cost = minimum[i-1][j]
            above_cost = minimum[i][j-1]
            minimum[i][j] = matrix[i][j] + min(left_cost, above_cost)
    print(minimum)
    return minimum
findMinimumEnd(peta, end_x, end_y)
'''
