def getMatrix():
    matrix = []

    numberOfRows = eval(input("rows: "))
    numberOfColumns = eval(input("columns: "))

    for row in range(numberOfRows):
        matrix.append([])
        for column in range(numberOfColumns):
            value = eval(input("Enter a value: "))
            matrix[row].append(value)

    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)

    return total

def main():
    m = getMatrix()
    print(m)

    print("accumulate~~ ", accumulate(m))

main()