import random
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in range(0, len(matrix)):
    for column in range(0, len(matrix[row])):
        i = random.randint(0, len(matrix)-1)
        j = random.randint(0, len(matrix[row])-1)

        matrix[row][column], matrix[i][j] = matrix[i][j], matrix[row][column]

print(matrix)