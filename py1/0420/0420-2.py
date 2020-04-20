def max(a, b):
    if a > b:
        result = a
    else:
        result = b
    return result

def main():
    i = 5
    j = 2
    k = max(i, j)

    print("The maximum between", i, "and", j, "is", k)

main()

def sum(n1, n2):
    total = n1 + n2
    return total
print(sum(1, 2))