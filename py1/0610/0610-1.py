matrix = []
numberOfRows = eval(input("Enter the number of rows: "))
numberofColumns = eval(input("Enter the number of columns: "))

for row in range(0, numberOfRows):
    matrix.append([])
    for column in range(0, numberofColumns):
        value = eval(input("Enter an element and press Enter: "))
        matrix[row].append(value)

print(matrix)