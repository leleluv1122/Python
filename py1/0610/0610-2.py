import random
matrix = []

numberOfRows = eval(input("rows: "))
numberOfColumns = eval(input("column: "))
for row in range(0, numberOfRows):
    matrix.append([])
    for column in range(0, numberOfColumns):
        matrix[row].append(random.randint(0, 99))

print(matrix)