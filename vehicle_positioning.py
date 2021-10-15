import random as rd

peta = [[1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0]]

print(peta)
# Generates the number of cars that will add traffic
number_of_cars = rd.randint(0, 10)

for x in range(number_of_cars):
    not_found = True
    while not_found:
        i = rd.randint(0, len(peta)-1)
        j = rd.randint(0, len(peta[i])-1)
        if peta[i][j] == 1:
            peta[i][j] += 1
            not_found = False
print(peta)