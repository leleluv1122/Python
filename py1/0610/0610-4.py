matrix = [[1,2,3],[4,5,6],[7,8,9]]
total = 0
total1 = 0


for row in range(0, len(matrix)):
    for column in range(0, len(matrix[row])):
        total1 += matrix[row][column]
print("Total is", total1)

for row in matrix:
    for value in row:
        total += value

print("Total is" , total)

for column in range(0, len(matrix[0])):
    total = 0
    for row in range(0, len(matrix)):
        total += matrix[row][column]
    print("sum for column " + str(column) + " is " + str(total))

maxRow = sum(matrix[0])
indexOfMaxRow = 0
for row in range(1, len(matrix)):
    if sum(matrix[row]) > maxRow:
        maxRow = sum(matrix[row])
        indexOfMaxRow = row

print("Row", indexOfMaxRow, "has the maximum sum of", maxRow)